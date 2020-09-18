from aiohttp_jinja2 import template


# Декоратор шаблонизатора
@template('index.html')
async def index(request):
    """
    Создание странички с подгрузкой шаблона
    :param request:
    :return:
    """
    return {}
