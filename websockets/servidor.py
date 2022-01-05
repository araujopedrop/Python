import sys
import json
import websockets
import asyncio

IP = "localhost"
PORT = 8766

async def receive_message(websocket,message):
	message = await websocket.recv()
	print("Message received: ")
	print(message)

def start_server_service():
	print("Starting server\n")
	print("Listening socket: " + str(IP) + ":" + str(PORT) + "\n")
	start_server = websockets.serve(receive_message,IP,PORT)
	asyncio.get_event_loop().run_until_complete(start_server)
	asyncio.get_event_loop().run_forever()

start_server_service()
