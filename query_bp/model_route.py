from dataclasses import dataclass
from database.select import select_list


@dataclass
class ProductInfoResponse:
    result: list
    error_message: str
    status: bool


def model_route(user_dict, sql_provider):
    error_message = ''
    status = True
    category = user_dict.get('prod_category', '').strip()
    if not category:
        return ProductInfoResponse(
            result=[], error_message='Введите категорию продуктов', status=False
        )

    _sql = sql_provider.get('product.sql')
    print('sql=', _sql)
    user_list = [category]
    result = select_list(_sql, user_list)
    if not result:
        error_message = 'Нет товаров заданной категории'
        status = False
    return ProductInfoResponse(result=result, error_message=error_message, status=status)
