from aiohttp_jinja2 import template


# Декоратор шаблонизатора
@template('index.html')
async def index(request):
    """
    Создание странички с подгрузкой шаблона
    :param request:
    :return:
    """

    site_name = request.app['config'].get('site_name')
    return {'site_name': site_name}
