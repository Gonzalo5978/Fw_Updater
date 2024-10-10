from .comunications import ISAPI
from xml.etree import ElementTree as ET
from pathlib import Path

class Hikvision:
    def __init__(self, ip, password, port):
            self.ip = ip
            self.password = password
            self.port = port
            self.namespace = {'ns': 'http://www.hikvision.com/ver20/XMLSchema'}
            self.model = self.getmodel()
            self.gateway = self.defgateway()
            self.api = ISAPI(self.ip, self.password)
            self.parent_dir = Path(__file__).parent.parent
            self.directory = f'{self.parent_dir}/firmwares/{self.model}/digicap.dav'

    #CLASS DATA
    def defgateway(self): #Default gateway for the Hikvision camera API
        ip = self.ip.split('.')
        gateway = str(ip[0] + '.' + ip[1] + '.' + ip[2] + '.' + '1')
        return(gateway)

    def getmodel(self): #Check deviceInfo endpoint and filter <model> tag to get the camera model
        req = ISAPI(f'http://{self.ip}:{self.port}/ISAPI/System/deviceInfo', self.password)
        response = str(req.getapi())
        root = ET.ElementTree(ET.fromstring(response))
        model_text = None
        model_tag = root.find('ns:model', self.namespace)
        if model_tag is not None:
            model_text = model_tag.text
        return(model_text)

    #UPDATE ENDPOINT
    def fw_update(self): #Update device Firmware
        with open(self.directory, 'rb') as f:
            firmware = f.read()
            f.close()
        req = ISAPI(f'http://{self.ip}:{self.port}/ISAPI/System/updateFirmware', self.password)
        update = req.putapi(firmware)
        return(update)

    #REBOOT ENDPOINT
    def reboot(self): #Reboot device
        req = ISAPI(f'http://{self.ip}:{self.port}/ISAPI/System/reboot', self.password)
        operation = req.putapi('')
        return(operation)
