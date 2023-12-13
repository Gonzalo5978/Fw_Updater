class Calls:
    def __init__(self, call):
        self.call = call

    def api_list(self):
        api_calls = {
            "info": "/ISAPI/System/deviceInfo",
            "reboot": "/ISAPI/System/reboot",
            "update": "/ISAPI/System/updateFirmware"
        }       
        return(api_calls[self.call])