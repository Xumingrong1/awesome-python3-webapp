import logging; logging.basicConfig(level=logging.INFO)
import asyncio, os, json, time, pdb
from datetime import datetime

from aiohttp import web

def index(request):
	return web.Response(body=b'<h1>Awesome</h1>')

@asyncio.coroutine
async def init(loop):
	app = web.Application()
	app.router.add_route('GET','/',index)
	pdb.set_trace()
	app_runner = web.AppRunner(app)
	await app_runner.setup()
	srv = await loop.create_server(app_runner.server,'127.0.0.1',9000)
	logging.info('server started at http://127.0.0.1:9000...')
	return srv
loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()