import random
import sys
from cgitb import handler
from typing import Dict, Union, List

from config.user_config import main_is_manual_params
from src.enrollment.body.enrollment_body import Enrollment
from src.generated_data.bdvo.payement_bdvo import PaymentBDVO
from src.generated_data.header.bdvo_header import BDVOHeader
from config import config, user_config
import json
import datetime
import re
import os
import shutil
import copy
import logging


def validation_and_prepare_input_data(
        logger: logging.Logger,
        direction: str,
        customer: str = 'рандом',
        is_transit_customer_account: str = 'рандом',
        counter: str = 'рандом',
        operation_currency: str = 'рандом',
        customer_currency: str = 'рандом',
        currency_operation_code: str = 'рандом',
        is_registry: str = 'рандом',
        document_date: str = 'сегодня',
        operation_date: str = 'рандом',
        amount_payment: str = 'рандом',
        amount_in_customer_account_currency: str = 'рандом',
        epk_id: str = 'рандом',
        is_correspondence_account: str = 'рандом',
        terbank: str = 'рандом',
        department_code: str = 'рандом',
        sender_system: str = 'выписка+зачисления',
        only_bdvo_params: str = 'рандом'
):
    direction = direction.lower()
    customer = customer.lower()
    is_transit_customer_account = is_transit_customer_account.lower()
    counter = counter.lower()
    operation_currency = operation_currency.lower()
    customer_currency = customer_currency.lower()
    currency_operation_code = currency_operation_code.lower()
    is_registry = is_registry.lower()
    document_date = document_date.lower()
    operation_date = operation_date.lower()
    amount_payment = amount_payment.lower()
    amount_in_customer_account_currency = amount_in_customer_account_currency.lower()
    epk_id = epk_id.lower()
    is_correspondence_account = is_correspondence_account.lower()
    terbank = terbank.lower()
    department_code = department_code.lower()
    sender_system = sender_system.lower()
    only_bdvo_params = only_bdvo_params.lower()
    try:
        assert (
                direction in ('зачисление', 'списание', 'рандом')
        ), ('Направление операции(direction) передано не корректно, получено - %s, '
            'ожидалось - зачисление, списание или рандом.') % direction

        assert (
                customer in ('резидент', 'не резидент', 'рандом')
        ), ('Тип клиента(customer) передан не корректно, получено - %s, '
            'ожидалось - резидент, не резидент или рандом.') % customer

        assert (
                is_transit_customer_account in ('да', 'нет', 'рандом')
        ), ('Транзитивность счета клиента(is_transit_customer_account) передана не корректно, получено - %s, '
            'ожидалось - да, нет или рандом.') % is_transit_customer_account

        assert (
                counter in ('резидент', 'не резидент', 'рандом')
        ), ('Тип контрагента(counter) передан не корректно, получено - %s, ожидалось - резидент, '
            'не резидент или рандом.') % counter

        assert (
                operation_currency == 'рандом' or
                (
                        len(operation_currency) == 3 or
                        operation_currency in config.dict_currency.keys() or
                        operation_currency in config.dict_currency.values()
                )
        ), ('Валюта операции(operation_currency) передана не корректно, получено - %s, о'
            'жидалось - буквенный или цифровой код валюты согласно ОКВ, либо значение - рандом') % operation_currency

        assert (
                customer_currency == 'рандом' or
                (
                        len(customer_currency) == 3 or
                        customer_currency in config.dict_currency.keys() or
                        customer_currency in config.dict_currency.values()
                )
        ), ('Валюта счета клиента(customer_currency) передана не корректно, получено - %s, '
            'ожидалось - буквенный или цифровой код валюты согласно ОКВ, либо значение - рандом') % customer_currency

        assert (
                is_registry in ('да', 'нет', 'рандом')
        ), ('Принадлежность к реестру(is_registry) передана не корректно, получено - %s, '
            'ожидалось - да, нет или рандом.') % is_registry

        if document_date != 'сегодня':
            try:
                datetime.date.fromisoformat(document_date)
            except Exception:
                raise ValueError(
                    'Дата документа(document_date) передана не корректно, получено - %s, '
                    'ожидалось - YYYY-MM-DD или сегодня.' % document_date)

        if operation_date != 'рандом':
            try:
                datetime.date.fromisoformat(operation_date)
            except Exception:
                raise ValueError(
                    'Дата операции(operation_date) передана не корректно, получено - %s, '
                    'ожидалось - YYYY-MM-DD или рандом.' % operation_date)

        assert (
                amount_payment.isdigit() or
                amount_payment == 'рандом'
        ), ('Сумма операции(amount_payment) передана не корректно, получено - %s, '
            'ожидалось - сумма состоящая из цифр или рандом') % amount_payment

        assert (
                amount_in_customer_account_currency.isdigit() == True or
                amount_in_customer_account_currency == 'рандом'
        ), ('Сумма в валюте счета клиента(amount_in_customer_account_currency) передана не корректно, получено - %s, '
            'ожидалось - сумма состоящая из цифр или рандом') % amount_in_customer_account_currency

        assert (
                epk_id.isdigit() or
                epk_id == 'рандом'
        ), ('Идентификатор ЕПК(epk_id) передан не корректно, получено - %s, '
            'ожидалось - идентификатор состоящий из цифр или рандом') % epk_id

        assert (
                is_correspondence_account in ('да', 'нет', 'рандом')
        ), ('Наличие корреспондентского счета(is_correspondence_account) передано не корректно, получено - %s, '
            'ожидалось - да, нет или рандом.') % is_correspondence_account

        assert (
                terbank == 'рандом' or
                (
                        terbank.isdigit() and
                        (
                                len(terbank) == 3 or
                                len(terbank) == 2
                        )
                )

        ), ('Тер. банк(terbank) передан не корректно, получено - %s, '
            'ожидалось - двух значный или трёхзначный цифровой код.') % terbank

        assert (
                (
                        len(department_code) == 11 and
                        department_code.isdigit()
                ) or
                re.match(r'\d{4}-\d{4}-\d{5}', department_code) or
                department_code == 'рандом'
        ), ('Код подразделения(department_code) передан не корректно, получено - %s, '
            'ожидалось - код подразделения состоящий из одиннадцати цифр или соответсвующий формату'
            ' 9999-9999-99999 или рандом.') % department_code

        assert (
                sender_system in ('зачисления', 'выписка', 'выписка+зачисления')
        ), ('Система поставщик(sender_system) передана не корректно, получено - %s, '
            'ожидалось - зачисления, выписка или выписка+зачисления.') % sender_system

        assert (
                only_bdvo_params in ('да', 'нет', 'рандом')
        ), ('Наличие неиспользуемых в БДВО параметров(only_bdvo_params) передано не корректно, получено - %s, '
            'ожидалось - да, нет или рандом.') % only_bdvo_params
    except ValueError as error:
        logger.exception(error)

    return {
        'direction': direction,
        'customer': customer,
        'is_transit_customer_account': is_transit_customer_account,
        'counter': counter,
        'operation_currency': operation_currency,
        'customer_currency': customer_currency,
        'currency_operation_code': currency_operation_code,
        'is_registry': is_registry,
        'document_date': document_date,
        'operation_date': operation_date,
        'amount_payment': amount_payment,
        'amount_in_customer_account_currency': amount_in_customer_account_currency,
        'epk_id': epk_id,
        'is_correspondence_account': is_correspondence_account,
        'terbank': terbank,
        'department_code': department_code,
        'sender_system': sender_system,
        'only_bdvo_params': only_bdvo_params
    }


def create_direction(direction: str, sender_system: str):
    if sender_system == 'выписка+зачисления':
        return '1'
    if direction == 'рандом':
        return '1' if random.randint(1, 2) == 1 else '2'
    elif direction == 'зачисление':
        return '1'
    else:
        return '2'


def convert_message_for_direction(header: BDVOHeader, body: PaymentBDVO, is_correspondence_account: str):
    # print('*'*30)
    # print('INPUT HEADER = ', header.to_JSON())
    # print('*'*30)
    # print('INPYT BODY = ', body.to_JSON())
    # print('*'*30)
    header_enrollment = json.loads(header.to_JSON())
    header_extract = json.loads(header.to_JSON())
    body_enrollment = json.loads(body.to_JSON())
    body_extract = json.loads(body.to_JSON())

    # Header enrollment
    header_enrollment['sourceData'] = 'CREDITING-PAYMENT'

    # Header extract
    header_extract.pop('srcModule')
    header_extract.pop('evtId')
    header_extract.pop('sndDate')
    header_extract.pop('kindDoc')
    header_extract.pop('accountType')
    header_extract['sourceData'] = 'STATEMENT-LEGAL-ENTITY'

    # Body enrollment
    body_enrollment['operation']['status'] = random.choice(['EXECUTED', 'REJECTED', 'SENT_EKS'])
    body_enrollment['operation']['documentCurrency'] = None
    body_enrollment['operation']['departmentCode'] = None
    body_enrollment['payer']['kpp'] = None
    body_enrollment['payee']['inn'] = None
    body_enrollment['payee']['kpp'] = None
    body_enrollment['payee']['bankBic'] = None
    body_enrollment['payee']['bankName'] = None
    body_enrollment['objectVersions'] = None
    body_enrollment['swiftTransfer']['orderingInstitutionOption'] = None
    if is_correspondence_account == 'рандом':
        if random.randint(0, 1) == 0:
            body_enrollment['correspondence'] = None
    elif is_correspondence_account == 'нет':
        body_enrollment['correspondence'] = None

    # Body extract
    body_extract['operation']['status'] = body_extract['objectVersions']['docData']['action']
    body_extract['operation']['documentCurrencyCode'] = None
    body_extract['payee']['accountDigitalCurrencyCode'] = None
    body_extract['payee']['accountCurrencyCode'] = None
    body_extract['payee']['bankBic'] = None
    body_extract['payee']['bankName'] = None
    body_extract['correspondence'] = None
    body_extract['swiftTransfer']['orderingCustomerINN'] = None
    body_extract['swiftTransfer']['orderingInstitutionBIC'] = None
    body_extract['swiftTransfer']['docNumber'] = None
    body_extract['swiftTransfer']['docDate'] = None

    # print('ENROLMENT HEADER = ', json.dumps(header_enrollment, indent=4, sort_keys=True, ensure_ascii=False))
    # print('*'*30)
    # print('EXTRACT HEADER = ', json.dumps(header_extract, indent=4, sort_keys=True, ensure_ascii=False))
    # print('*'*30)
    # print('ENROLMENT BODY = ', json.dumps(body_enrollment, indent=4, sort_keys=True, ensure_ascii=False))
    # print('*'*30)
    # print('EXTRACT BODY = ', json.dumps(body_extract, indent=4, sort_keys=True, ensure_ascii=False))
    return header_enrollment, header_extract, body_enrollment, body_extract


def remove_result_dir(logger: logging.Logger):
    """
    Function for remove directory where last result was saved.
    :param logging.Logger: Logger
    """
    if os.path.isdir(os.path.join(os.getcwd(), config.directory_to_save)):
        shutil.rmtree(os.path.join(os.getcwd(), config.directory_to_save))
        logger.info("Direction %s was removed." % os.path.join(os.getcwd(), config.directory_to_save))


def write_to_file(message: dict, name: str):
    with open('%s.json' % name, 'w') as file:
        file.write(json.dumps(message, indent=4, ensure_ascii=False))


def save_result(messages: tuple, sender_system: str):
    os.makedirs(os.path.join(os.getcwd(), config.directory_to_save, messages[0]['sendServiceId']))

    if sender_system == 'выписка+зачисления':
        enrollment_path = os.path.join(
            os.getcwd(),
            config.directory_to_save,
            messages[0]['sendServiceId'],
            'enrollment'
        )
        extract_path = os.path.join(
            os.getcwd(),
            config.directory_to_save,
            messages[0]['sendServiceId'],
            'extract'
        )
        os.makedirs(enrollment_path)
        os.makedirs(extract_path)
        write_to_file(
            message=messages[0],
            name=os.path.join(enrollment_path, 'header')
        )
        write_to_file(
            message=messages[1],
            name=os.path.join(extract_path, 'header')
        )
        write_to_file(
            message=messages[2],
            name=os.path.join(enrollment_path, 'body')
        )
        write_to_file(
            message=messages[3],
            name=os.path.join(extract_path, 'body')
        )


def check_user_params(logger: logging.Logger) -> dict:
    """
    Function for validate user configure file
    :return: dict - additional params
    """
    for key, value in user_config.__dict__.items():
        if key.__contains__('main_') and value is None:
            logger.exception('Некорректное заполнение основных параметров: '
                             'параметр %s имеет значение %s, пожалуйста поправьте!' % (key, value))

    dict_manual_params = {}
    if user_config.main_is_manual_params:
        for key, value in user_config.__dict__.items():
            if not key.__contains__('main_') and not key.startswith('__') and value not in [None, '', 0.00]:
                dict_manual_params[key] = value
    if not dict_manual_params and user_config.main_is_manual_params:
        logger.exception('Некорректное заполнение дополнительных параметров: '
                         'флаг включения дополнительных параметров main_is_manual_params = True, '
                         'но не один из параметров не заполнен. '
                         'Пожалуйста поправьте!')
    else:
        logger.info("MAIN_IS_MANUAL_PARAMS = %s, DICT_MANUAL_PARAMS = %s" % (
            user_config.main_is_manual_params, dict_manual_params))
        return dict_manual_params


def create_update_messages(body: dict, list_update_objects: list, count_object: int):
    count = 0
    list_update_objects_index = 0
    for item in range(len(list_update_objects) * count_object):
        if count == count_object:
            list_update_objects_index += 1
            count = 0
        field_to_update = random.choice(list_update_objects[list_update_objects_index]).split('.')
        count += 1

        print('#%s Field in list %s = %s' % (item, list_update_objects_index, field_to_update))


def convert_message_to_update_delete(header: dict, body: dict):
    messages = []

    create_update_messages(
        body=copy.deepcopy(body),
        list_update_objects=[
            config.list_doc_data_keys,
            config.list_turn_keys,
            config.list_mt_currency_keys
        ],
        count_object=5
    )
    messages.append(
        {
            'insert': {
                'header': copy.deepcopy(header),
                'body': copy.deepcopy(body)
            }
        }
    )

    for num in range(2):
        object_to_update = random.choice([config.list_doc_data_keys, config.list_turn_keys, config.list_mt_currency_keys])

        if object_to_update == config.list_doc_data_keys:
            body['objectVersions']['docData']['action'] = 'U'
            body['objectVersions']['docData']['version'] += 1
            body['operation']['status'] = 'U'
        elif object_to_update == config.list_turn_keys:
            body['objectVersions']['turn']['action'] = 'U'
            body['objectVersions']['turn']['version'] += 1
        else:
            body['objectVersions']['mtCurrency']['action'] = 'U'
            body['objectVersions']['mtCurrency']['version'] += 1

        field_to_update = random.choice(object_to_update).split('.')
        print('UPDATE FIELD %s = %s' % (num, field_to_update))
        if field_to_update[1].__contains__('date') or field_to_update[1].__contains__('Date'):
            body[field_to_update[0]][field_to_update[1]] = '2099-12-12'
        elif field_to_update[1].__contains__('amount') or field_to_update[1].__contains__('Amount'):
            body[field_to_update[0]][field_to_update[1]] = body[field_to_update[0]][field_to_update[1]] + 100
            if field_to_update[0] in ('payer', 'payee') and field_to_update[1] == 'amount':
                if field_to_update[0] == 'payer':
                    body['payee'][field_to_update[1]] = body['payee'][field_to_update[1]] + 100
                else:
                    body['payer'][field_to_update[1]] = body['payer'][field_to_update[1]] + 100
        elif field_to_update[1].__contains__('voCode'):
            body[field_to_update[0]][field_to_update[1]] = 12345
        elif type(body[field_to_update[0]][field_to_update[1]]) == int:
            body[field_to_update[0]][field_to_update[1]] += 10
        elif body[field_to_update[0]][field_to_update[1]].isdigit():
            body[field_to_update[0]][field_to_update[1]] = body[field_to_update[0]][field_to_update[1]][::-1]
        else:
            body[field_to_update[0]][field_to_update[1]] += '_update_%s' % num

        messages.append(
            {
                'update': {
                    'header': copy.deepcopy(header),
                    'body': copy.deepcopy(body)
                }
            }
        )
    body['operation']['status'] = 'D'
    body['objectVersions']['docData']['action'] = 'D'
    body['objectVersions']['docData']['version'] += 1
    messages.append(
        {
            'delete': {
                'header': copy.deepcopy(header),
                'body': copy.deepcopy(body)
            }
        }
    )
    # print('MESSAGES = ', json.dumps(messages, indent=4, ensure_ascii=False))
    return messages


def save_result_update_delete(messages: dict):
    os.makedirs(
        os.path.join(
            os.getcwd(),
            config.directory_to_save,
            messages[0]['insert']['header']['sendServiceId'],
            'insert'
        )
    )
    os.makedirs(os.path.join(os.getcwd(), config.directory_to_save, messages[0]['insert']['header']['sendServiceId'],
                             'update_1'))
    os.makedirs(os.path.join(os.getcwd(), config.directory_to_save, messages[0]['insert']['header']['sendServiceId'],
                             'update_2'))
    os.makedirs(
        os.path.join(os.getcwd(), config.directory_to_save, messages[0]['insert']['header']['sendServiceId'], 'delete'))

    write_to_file(
        message=messages[0]['insert']['header'],
        name=os.path.join(
            os.path.join(
                os.getcwd(),
                config.directory_to_save,
                messages[0]['insert']['header']['sendServiceId'],
                'insert',
                'header'
            )
        )
    )
    write_to_file(
        message=messages[0]['insert']['body'],
        name=os.path.join(
            os.path.join(
                os.getcwd(),
                config.directory_to_save,
                messages[0]['insert']['header']['sendServiceId'],
                'insert',
                'body'
            )
        )
    )

    write_to_file(
        message=messages[1]['update']['header'],
        name=os.path.join(
            os.path.join(
                os.getcwd(),
                config.directory_to_save,
                messages[0]['insert']['header']['sendServiceId'],
                'update_1',
                'header'
            )
        )
    )
    write_to_file(
        message=messages[1]['update']['body'],
        name=os.path.join(
            os.path.join(
                os.getcwd(),
                config.directory_to_save,
                messages[0]['insert']['header']['sendServiceId'],
                'update_1',
                'body'
            )
        )
    )

    write_to_file(
        message=messages[2]['update']['header'],
        name=os.path.join(
            os.path.join(
                os.getcwd(),
                config.directory_to_save,
                messages[0]['insert']['header']['sendServiceId'],
                'update_2',
                'header'
            )
        )
    )
    write_to_file(
        message=messages[2]['update']['body'],
        name=os.path.join(
            os.path.join(
                os.getcwd(),
                config.directory_to_save,
                messages[0]['insert']['header']['sendServiceId'],
                'update_2',
                'body'
            )
        )
    )

    write_to_file(
        message=messages[3]['delete']['header'],
        name=os.path.join(
            os.path.join(
                os.getcwd(),
                config.directory_to_save,
                messages[0]['insert']['header']['sendServiceId'],
                'delete',
                'header'
            )
        )
    )
    write_to_file(
        message=messages[3]['delete']['body'],
        name=os.path.join(
            os.path.join(
                os.getcwd(),
                config.directory_to_save,
                messages[0]['insert']['header']['sendServiceId'],
                'delete',
                'body'
            )
        )
    )


def create_input_params(param: dict, logger: logging.Logger) -> object:
    """
    Function to convert user params for program params
    :rtype: object
    :return: dict[str, Union[list[str], str]]
    """
    input_params_dict: dict[str, Union[list[str], str]] = {}

    if user_config.main_is_manual_params:
        input_params_dict = param
    #     TODO: Ручная настройка параметров
    else:
        input_params_dict['direction'] = config.dict_direction_by_main_action[user_config.main_action]
        input_params_dict['customer'] = user_config.main_resident_customer
        input_params_dict['is_transit_customer_account'] = user_config.main_transit_customer_account
        input_params_dict['counter'] = user_config.main_resident_counter
        input_params_dict['operation_currency'] = 'рандом'
        input_params_dict['customer_currency'] = 'рандом'
        input_params_dict['currency_operation_code'] = user_config.main_currency_operation_code
        input_params_dict['is_registry'] = user_config.main_is_registry
        input_params_dict['document_date'] = 'сегодня'
        input_params_dict['operation_date'] = 'рандом'
        input_params_dict['amount_payment'] = 'рандом'
        input_params_dict['amount_in_customer_account_currency'] = 'рандом'
        input_params_dict['epk_id'] = user_config.main_epk_id
        input_params_dict['is_correspondence_account'] = user_config.main_is_correspondence_account
        input_params_dict['terbank'] = user_config.main_ter_bank
        input_params_dict['department_code'] = user_config.main_department_code
        input_params_dict['sender_system'] = config.dict_sender_system[user_config.main_sender_system]
        input_params_dict['count_examples'] = user_config.main_count_examples
        input_params_dict['unnecessary_params'] = user_config.main_unnecessary_params.split(',')
        input_params_dict['message_format'] = user_config.main_message_format
        logger.info("INPUT PARAMETERS = %s" % json.dumps(input_params_dict, indent=4, ensure_ascii=False))
    return input_params_dict


def create_logger() -> logging.Logger:
    """
    Function for create and configure logger
    :rtype: object
    :return: - Logger object
    """
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(stream=sys.stdout)
    handler.setFormatter(logging.Formatter(fmt='[%(asctime)s]: %(levelname)8s: %(filename)20s:'
                                               ' %(funcName)30s: %(message)s'))
    logger.addHandler(handler)
    return logger


if __name__ == '__main__':
    logger = create_logger()

    # Remove previous results
    remove_result_dir(logger=logger)

    # analysis user params
    manual_params = check_user_params(logger=logger)
    input_params = create_input_params(param=manual_params, logger=logger)

    list_for_generation = []

    for _ in range(input_params['count_examples']):
        if type(input_params['direction']) == list:
            for direction in range(len(input_params['direction'])):
                list_for_generation.append(
                    validation_and_prepare_input_data(
                        logger=logger,
                        direction=input_params['direction'][direction],
                        customer=input_params['customer'],
                        is_transit_customer_account=input_params['is_transit_customer_account'],
                        counter=input_params['counter'],
                        operation_currency=input_params['operation_currency'],
                        customer_currency=input_params['customer_currency'],
                        currency_operation_code=input_params['currency_operation_code'],
                        is_registry=input_params['is_registry'],
                        document_date=input_params['document_date'],
                        amount_payment=input_params['amount_payment'],
                        amount_in_customer_account_currency=input_params['amount_in_customer_account_currency'],
                        epk_id=input_params['epk_id'],
                        is_correspondence_account=input_params['is_correspondence_account'],
                        terbank=input_params['terbank'],
                        department_code=input_params['department_code'],
                        sender_system=input_params['sender_system']
                    )
                )
        else:
            list_for_generation.append(
                validation_and_prepare_input_data(
                    logger=logger,
                    direction=input_params['direction'],
                    customer=input_params['customer'],
                    is_transit_customer_account=input_params['is_transit_customer_account'],
                    counter=input_params['counter'],
                    operation_currency=input_params['operation_currency'],
                    customer_currency=input_params['customer_currency'],
                    currency_operation_code=input_params['currency_operation_code'],
                    is_registry=input_params['is_registry'],
                    document_date=input_params['document_date'],
                    amount_payment=input_params['amount_payment'],
                    amount_in_customer_account_currency=input_params['amount_in_customer_account_currency'],
                    epk_id=input_params['epk_id'],
                    is_correspondence_account=input_params['is_correspondence_account'],
                    terbank=input_params['terbank'],
                    department_code=input_params['department_code'],
                    sender_system=input_params['sender_system']
                )
            )
    logger.info("LIST FOR GENERATION = %s" % json.dumps(list_for_generation, indent=4, ensure_ascii=False))

    for item in list_for_generation:
        payment_header_raw = None
        payment_body_raw = None

        # Create Headers
        payment_header_raw = BDVOHeader(direction=item['direction'],
                                        is_transit_customer_account=item['is_transit_customer_account'],
                                        is_registry=item['is_registry']
                                        )
        item['direction'] = create_direction(direction=item['direction'], sender_system=item['sender_system'])
        item['division_id'] = payment_header_raw.get_divisionId()
        item['payment_code'] = payment_header_raw.get_kindDoc()

        # Create body
        payment_body_raw = PaymentBDVO(kwargs=item)

        # Convert to format for sender system
        result_enrollment_header, result_extract_header, result_enrollment_body, result_extract_body = convert_message_for_direction(
            header=payment_header_raw,
            body=payment_body_raw,
            is_correspondence_account=item['is_correspondence_account']
        )

        if user_config.main_action == 1:
            result = convert_message_to_update_delete(
                header=result_extract_header,
                body=result_extract_body
            )
            save_result_update_delete(messages=result)
        else:
            # save to result
            save_result(
                messages=(result_enrollment_header, result_extract_header, result_enrollment_body, result_extract_body),
                sender_system=item['sender_system']
            )
    """

    


    


    

    # enrollment_body = Enrollment(request_id = '123', operation_date='2024-10-10', customer_account='91827364658128102297')
    # print(enrollment_body)д
    # for new_payment in range(0, 100):
    #     payment_body = PaymentBDVO(direction='Зачисления')

    # attrs = vars(payment_header)
    # print('#', new_payment)
    # print(payment_header.toJSON())
    # # print(', '.join("%s: %s" % item for item in attrs.items()))
    # print('*'*100)

    # (
    # direction = 'Зачисление\Списание', обязательное
    # customer = 'Резидент\Не резидент', необязательное
    # is_transit_customer_account = 'Да\Нет', необязательное
    # counter = 'Резидент\Не резидент', необязательное
    # operation_currency = 'Валюта\Рубли', необязательное
    # customer_currency = 'Валюта\Рубли', необязательное
    # currency_operation_code = 12345, необязательное
    # is_registry = 'Да\Нет', необязательное
    # document_date = 'yyyy-mm-dd', необязательное
    # operation_date = 'yyyy-mm-dd', необязательное
    # amount_payment = 12345.99, необязательное
    # amount_in_customer_account_currency = 12345.99, необязательное
    # epk_id = 9981818828, необязательное
    # is_correspondence_account = 'Да\Нет', необязательное
    # is_swift = 'Да\Нет', необязательное
    # terbank = '038', необязательное
    # department_code = '00dd-dddd-ddddd\ddddddddddd' необязательное
    # sender_system = 'Выписка\Зачисления', необязательное
    # only_bdvo_params = 'Да\Нет', необязательное
    # generate_count = 5 необязательное
    # )

    # CSV to JSON
    # lines = []
    # with open("temp.txt", 'r', encoding='utf-8') as my_file:
    #     lines = [line.replace('\n', '').split(',') for line in my_file.readlines()]
    #
    # result = []
    # for num, item in enumerate(lines):
    #     result.append(
    #         {
    #             'currency': item[0],
    #             'wholePart': {
    #                 'singularNominativeCase': item[1],
    #                 'singularGenitiveCase': item[2],
    #                 'pluralGenitiveCase': item[3],
    #                 'wordGender': item[4]
    #             },
    #             'fractionalPart': {
    #                 'singularNominativeCase': item[5],
    #                 'singularGenitiveCase': item[6] if item[6] else '',
    #                 'pluralGenitiveCase': item[7] if item[7] else '',
    #                 'wordGender': item[8] if len(item) > 8 and item[8] else 'мужской'
    #             }
    #         }
    #     )
    #
    # with open("temp_res.json", 'w', encoding='utf-8') as my_file:
    #     my_file.write(json.dumps(result, ensure_ascii=False))

"""
