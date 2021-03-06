from aiohttp import web
import aiohttp_jinja2
import jinja2

from demo.routes import setup_routes


async def create_app(config: dict):
    """
    Метод создания приложения
    :return:
    """
    app = web.Application()

    # Добавление конфига в словарь
    app['config'] = config

    # Подгрузка шаблонизатора
    aiohttp_jinja2.setup(app,
                         loader=jinja2.PackageLoader('demo', 'templates'))
    # Загрузка роутов(путей)
    setup_routes(app)

    return app
