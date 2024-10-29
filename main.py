import random
from src.enrollment.body.enrollment_body import Enrollment
from src.generated_data.bdvo.payement_bdvo import PaymentBDVO
from src.generated_data.header.bdvo_header import BDVOHeader
from config import config
import json
import datetime
import re
import itertools


def validation_and_prepare_input_data(
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
        is_swift: str = 'рандом',
        terbank: str = 'рандом',
        department_code: str = 'рандом',
        sender_system: str = 'выписка+зачисления',
        only_bdvo_params: str = 'рандом',
        generate_count: int = 1
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
    is_swift = is_swift.lower()
    terbank = terbank.lower()
    department_code = department_code.lower()
    sender_system = sender_system.lower()
    only_bdvo_params = only_bdvo_params.lower()

    assert (
            direction in ('зачисление', 'списание', 'рандом')
    ), 'Напрвление операции(direction) переданно не корректно, получено - %s, ожидалось - зачисление, списание или рандом.' % direction

    assert (
            customer in ('резидент', 'не резидент', 'рандом')
    ), 'Тип клиента(customer) передан не корректно, получено - %s, ожидалось - резидент, не резидент или рандом.' % customer

    assert (
            is_transit_customer_account in ('да', 'нет', 'рандом')
    ), 'Транзитность счета клиента(is_transit_customer_account) переданна не корректно, получено - %s, ожидалось - да, нет или рандом.' % is_transit_customer_account

    assert (
            counter in ('резидент', 'не резидент', 'рандом')
    ), 'Тип контрагента(counter) передан не корректно, получено - %s, ожидалось - резидент, не резидент или рандом.' % counter

    assert (
            operation_currency == 'рандом' or
            (
                    len(operation_currency) == 3 or
                    operation_currency in config.dict_currency.keys() or
                    operation_currency in config.dict_currency.values()
            )
    ), 'Валюта операции(operation_currency) переданна не корректно, получено - %s, ожидалось - буквенный или цифровой код валюты согласно ОКВ, либо знчение - рандом' % operation_currency

    assert (
            customer_currency == 'рандом' or
            (
                    len(customer_currency) == 3 or
                    customer_currency in config.dict_currency.keys() or
                    customer_currency in config.dict_currency.values()
            )
    ), 'Валюта счета клиента(customer_currency) переданна не корректно, получено - %s, ожидалось - буквенный или цифровой код валюты согласно ОКВ, либо знчение - рандом' % customer_currency

    assert (
            is_registry in ('да', 'нет', 'рандом')
    ), 'Принадлежность к реестру(is_registry) переданна не корректно, получено - %s, ожидалось - да, нет или рандом.' % is_registry

    if document_date != 'сегодня':
        try:
            datetime.date.fromisoformat(document_date)
        except Exception:
            raise ValueError(
                'Дата документа(document_date) переданна не корректно, получено - %s, ожидалось - YYYY-MM-DD или сегодня.' % document_date)

    if operation_date != 'рандом':
        try:
            datetime.date.fromisoformat(operation_date)
        except Exception:
            raise ValueError(
                'Дата операции(operation_date) переданна не корректно, получено - %s, ожидалось - YYYY-MM-DD или рандом.' % operation_date)

    assert (
            amount_payment.isdigit() or
            amount_payment == 'рандом'
    ), 'Сумма операции(amount_payment) переданна не корректно, получено - %s, ожидалось - сумма состоящая из цифр или рандом' % amount_payment

    assert (
            amount_in_customer_account_currency.isdigit() == True or
            amount_in_customer_account_currency == 'рандом'
    ), 'Сумма в валюте счета клиента(amount_in_customer_account_currency) переданна не корректно, получено - %s, ожидалось - сумма состоящая из цифр или рандом' % amount_in_customer_account_currency

    assert (
            epk_id.isdigit() or
            epk_id == 'рандом'
    ), 'Идентификатор ЕПК(epk_id) передан не корректно, получено - %s, ожидалось - идентификтор состоящий из цифр или рандом' % epk_id

    assert (
            is_correspondence_account in ('да', 'нет', 'рандом')
    ), 'Наличие корреспонденского счета(is_correspondence_account) передано не корректно, получено - %s, ожидалось - да, нет или рандом.' % is_correspondence_account

    assert (
            is_swift in ('да', 'нет', 'рандом')
    ), 'Наличие блока по свифту(is_swift) передано не корректно, получено - %s, ожидалось - да, нет или рандом.' % is_swift

    assert (
            terbank == 'рандом' or
            (
                    terbank.isdigit() and
                    (
                            len(terbank) == 3 or
                            len(terbank) == 2
                    )
            )

    ), 'Тер. банк(terbank) передан не корректно, получено - %s, ожидалось - двух значный или трёзначный цифровой код.' % terbank

    assert (
            (
                    len(department_code) == 11 and
                    department_code.isdigit()
            ) or
            re.match(r'\d{4}-\d{4}-\d{5}', department_code) or
            department_code == 'рандом'
    ), 'Код подразделения(department_code) передан не корректно, получено - %s, ожидалось - код подразделения состоящий из одиннадцати цифр или соответсвующий формату 9999-9999-99999 или рандом.' % department_code

    assert (
            sender_system in ('зачисления', 'выписка', 'выписка+зачисления')
    ), 'Система поставщик(sender_system) переданна не корректно, получено - %s, ожидалось - зачисления, выписка или выписка+зачисления.' % sender_system

    assert (
            only_bdvo_params in ('да', 'нет', 'рандом')
    ), 'Наличие неиспользуемых в БДВО параметров(only_bdvo_params) переданно не корректно, получено - %s, ожидалось - да, нет или рандом.' % only_bdvo_params

    assert (
            generate_count > 0
    ), 'Количество примеров(generate_count) переданно не корректно, получено - %s, ожидалось - значение больше 0.' % generate_count

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
        'is_swift': is_swift,
        'terbank': terbank,
        'department_code': department_code,
        'sender_system': sender_system,
        'only_bdvo_params': only_bdvo_params
    }

def create_direction(direction: str, sender_system: str):
    if sender_system == 'выпиcка':
        if direction == 'рандом':
            return str(random.randint(0,1))
        elif direction == 'зачисление':
            return '0' 
        else: 
            return '1'
    elif sender_system == 'зачисления':
        if direction == 'рандом':
            return random.randint(1,2)
        elif direction == 'зачисление':
            return '1' 
        else: 
            return '2'   
    


if __name__ == '__main__':
    

    # Validation and prepare data
    item = validation_and_prepare_input_data(direction='ЗАЧИСЛЕНИе')
    payment_header_enrollment = None
    payment_header_extract = None
    payment_body_enrollment = None
    payment_body_extract = None
    
    # Create Headers
    if item['sender_system'] == 'выписка+зачисления':
        payment_header_enrollment = BDVOHeader(sender_system=item['sender_system'].replace('выписка+', ''),
                                               direction=item['direction'],
                                               is_transit_customer_account=item['is_transit_customer_account'],
                                               is_registry=item['is_registry'])
        payment_header_extract = BDVOHeader(sender_system=item['sender_system'].replace('+зачисления', ''),
                                            direction=item['direction'],
                                            is_transit_customer_account=item['is_transit_customer_account'],
                                            is_registry=item['is_registry'])
        item['sender_system'] = 'зачисления'
        item['direction'] = create_direction(direction=item['direction'], sender_system=item['sender_system'])
        item['division_id'] = payment_header_enrollment.get_divisionId()
        item['payment_code'] = payment_header_enrollment.get_kindDoc()
        payment_body_enrollment = PaymentBDVO(kwargs=item)
        item['sender_system'] = 'выписка'
        payment_body_extract = PaymentBDVO(kwargs=item)
    elif item['sender_system'] == 'выписка':
        payment_header_extract = BDVOHeader(sender_system=item['sender_system'],
                                            direction=item['direction'],
                                            is_transit_customer_account=item['is_transit_customer_account'],
                                            is_registry=item['is_registry'])
        
        payment_body_extract = PaymentBDVO(kwargs=item)
    elif item['sender_system'] == 'зачисления':
        payment_header_enrollment = BDVOHeader(sender_system=item['sender_system'],
                                               direction=item['direction'],
                                               is_transit_customer_account=item['is_transit_customer_account'],
                                               is_registry=item['is_registry'])
        
        payment_body_enrollment = PaymentBDVO(kwargs=item)
        
    if payment_header_extract is not None:
        print(payment_header_extract.to_JSON())
    if payment_header_enrollment is not None:
        print(payment_header_enrollment.to_JSON())
    
    if payment_body_enrollment is not None:
        print(payment_body_enrollment.to_JSON())
    if payment_body_extract is not None:
        print(payment_body_extract.to_JSON())


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


    