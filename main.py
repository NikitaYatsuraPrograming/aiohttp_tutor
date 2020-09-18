import argparse

import aioreloader
import asyncio
from aiohttp import web

import uvloop

from demo.app import create_app

# Быстрее работает async
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

# Добавление аргументов при запуске
parser = argparse.ArgumentParser(description='Demo')
parser.add_argument('--host', help='Host')
parser.add_argument('--port', help='Port')
parser.add_argument('--reload',
                    help='AutoReload',
                    action='store_true')

# Парсинг аргументов
args = parser.parse_args()

# Вызов конструктора создания приложения
app = create_app()

# Авторелоад
if args.reload:
    print('Start with code reload')
    aioreloader.start()

if __name__ == '__main__':
    # Запуск приложения
    web.run_app(app, host=args.host, port=args.port)
