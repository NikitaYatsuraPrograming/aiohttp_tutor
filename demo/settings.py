from pathlib import Path

import yaml

__all__ = 'load_config'


def loader_config(config_file=None):
    """
    Создание загрузки конфига
    :param config_file:
    :return:
    """

    # Файл по умолчанию
    default_file = Path(__file__).parent / 'config.yaml'

    # Чтение файла
    with open(default_file, 'r') as f:
        config = yaml.safe_load(f)

    # Запись в словарь для дальнейшего использования
    cf_dict = {}
    if config_file:
        cf_dict = yaml.safe_load(config_file)

    config.update(**cf_dict)

    return config
