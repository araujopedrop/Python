import os
import sys
import json
import asyncio
import websockets

from dotenv          import load_dotenv
from os.path         import join, dirname
from PyQt5           import uic
from PyQt5.QtWidgets import QMainWindow,QApplication



class WMS(QMainWindow):

    IP       = "localhost"
    PORT     = 8766
    SKU      = ""
    QUANTITY = ""
    SHELF    = ""
    
    request = {"sku":"",
               "quantity":"",
               "shelf":""}

    json_request = None

    def __init__(self):
        super().__init__()

        dotenv_path = join(dirname(__file__), 'EnvFile.env')
        load_dotenv(dotenv_path)
        UI_FILE = os.environ.get("UI")
         
        uic.loadUi(UI_FILE,self)
        self.pb_send_request.clicked.connect(self.fn_send_Request)

    def fn_send_Request(self):
        try:
            #Retrieve data from GUI
            self.SKU      = str(self.le_sku.text())
            self.QUANTITY = str(self.le_quantity.text())
            self.SHELF    = str(self.le_shelf.text())

            #Build message
            self.request  = {"sku":self.SKU,
                             "quantity":self.QUANTITY,
                             "shelf":self.SHELF}
            self.json_request = json.dumps(self.request, indent=4, sort_keys=False)

            #Send message
            self.send_request()
            self.l_Envio.setText("Envie datos")

        except:
            pass
        

    def send_request(self):
        self.l_Envio.setText("Envio de datos2")
        asyncio.get_event_loop().run_until_complete(self.send_message())

    async def send_message(self):
        uri = "ws://" + str(self.IP) + ":" + str(self.PORT)
        async with websockets.connect(uri) as websocket:
            await websocket.send(self.json_request)

    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = WMS()
    GUI.show()
    sys.exit(app.exec_())