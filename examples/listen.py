"""Connects to an RCON server and listens for messages indefinitely."""
import asyncio
import logging
import math

import berconpy as rcon

IP_ADDR = 'XXX.XXX.XXX.XXX'
PORT = 9999
PASSWORD = 'ASCII_PASSWORD'

log = logging.getLogger('berconpy')
log.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
log.addHandler(handler)

client = rcon.AsyncRCONClient('listen.py')


@client.listen()
async def on_login():
    print('on_login')


@client.listen()
async def on_message(message: str):
    print('on_message:', message)


@client.listen('on_command')
async def server_response_to_command(command: str):
    print('on_command:', command)


async def main():
    async with client.connect(IP_ADDR, PORT, PASSWORD):
        await asyncio.sleep(math.inf)


if __name__ == '__main__':
    asyncio.run(main())
