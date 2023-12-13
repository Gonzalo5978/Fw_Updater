import requests
from requests.auth import HTTPDigestAuth as digest
import xml.etree.ElementTree as ET

class API:
    def __init__(self, ip, password, port, call):
        self.ip = ip
        self.password = password
        self.port = port
        self.call = call
    
    def fw_update(self):
        with open('digicap.dav', 'rb') as f:
            firmware = f.read()
            f.close()
        req = requests.put("http://" + self.ip + self.call, auth=digest('admin', self.password), data=firmware)
        return(req)

    def fw_version(self):
        req = requests.get("http://" + self.ip + self.call, auth=digest('admin', self.password))
        with open("info" + ".xml", "wb") as f:
            f.write(req.content)
            f.close()
        with open("info" + ".xml", "r") as f:
            fw_data = f.read()
            f.close()
        return(fw_data)

    def reboot(self):
        req = requests.put("http://" + self.ip + self.call, auth=digest('admin', self.password))
        return(req)

class APIClean:
    def __init__(self, data):
        self.data = data
    
    def clean_info(self):
        tree = ET.parse('info.xml')
        root = tree.getroot()
        return(root[8].text, root[9].text)