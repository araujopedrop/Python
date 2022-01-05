import sys
import json
import websockets
import asyncio

IP = "localhost"
PORT = 8766

my_dict = {"id":"1",
           "qty":"2",
           "place":"warehouse_2"}

json_obj = json.dumps(my_dict, indent=4, sort_keys=False)

async def send_message():
	uri = "ws://" + str(IP) + ":" + str(PORT)
	print("Connecting to the socket " + str(IP) + ":" + str(PORT) + "\n")
	async with websockets.connect(uri) as websocket:
		print("Sending json_obj: ")
		print(my_dict)
		await websocket.send(json_obj)


def start_client_service():
	print("Starting client\n")
	asyncio.get_event_loop().run_until_complete(send_message())

start_client_service()
