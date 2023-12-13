from rich.console import Console
from api_handler import API, APIClean
from api_calls import Calls

#Definición de consola para modulo "rich"
console = Console()

#Conseguir llamadas de API
info = Calls("info")
info_call = info.api_list()

reboot = Calls("reboot")
reboot_call = reboot.api_list()

update = Calls("update")
update_call = update.api_list()

#Inputs del usuario para los datos necesarios
def inputs():
    ip = console.input("[bold][cyan][+][/cyan] Introduce la IP: [/bold]")
    password = console.input("[bold][cyan][+][/cyan] Introduce la Password: [/bold]")
    port = console.input("[bold][cyan][+][/cyan] Introduce el Puerto: [/bold]")
    input_data = ip, password, port
    return(input_data)

def version(data):
    data_send = API(data[0], data[1], data[2], info_call)
    fw_ver_xml = data_send.fw_version()
    clean_xml = APIClean(fw_ver_xml)
    fw_ver = clean_xml.clean_info()
    return(fw_ver)

def update_fw(data):
    data_send = API(data[0], data[1], data[2], update_call)
    update_send = data_send.fw_update()
    return(update_send)

def api_reboot(data):
    data_send = API(data[0], data[1], data[2], reboot_call)
    reboot_send = data_send.reboot()
    return(reboot_send)

#Cambiar la forma de conseguir los inputs
data = inputs()
print('')
prt_version = version(data)
prt_update = update_fw(data)
prt_reboot = api_reboot(data)

print("Versión Actual: " + str(prt_version))
print(prt_update)
print(prt_reboot)
