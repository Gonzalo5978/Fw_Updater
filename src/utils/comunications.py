import requests
from requests.auth import HTTPDigestAuth

class ISAPI:
    def __init__(self, url, key):
        self.url = url
        self.key = key

    def getapi(self): #Operaciones GET para API Hikvision
        try:
            req = requests.get(self.url, auth=HTTPDigestAuth('admin', self.key))

            if req.status_code == 200:
                return(req.text)
            else:
                return(req)
        
        #EXCEPCIONES
        except ConnectionError:
            return('[-] Error de Conexión')
        except KeyboardInterrupt:
            return('\n[-] Interrumpiendo Programa...')
        except Exception as e:
            return(f'Error: [{e}]')

    def putapi(self, c_data): #Operaciones GET para API Hikvision
        try:
            req = requests.put(self.url, data = c_data, headers = {'Content-Type': 'application/xml'}, auth=HTTPDigestAuth('admin', self.key))

            if req.status_code == 200:
                return(req.status_code)
            else:
                return(req.text)
            
        #EXCEPCIOENS
        except Exception as e:
            return(f'Error: [{e}]')
