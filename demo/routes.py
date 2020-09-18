from demo.views import frontend


def setup_routes(app):
    """
    Создание путей
    :param app:
    :return:
    """
    app.router.add_route('GET', '/', frontend.index)
