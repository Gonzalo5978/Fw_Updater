from utils.operations import Hikvision as Hik
from rich.console import Console
import argparse

console = Console()

parser = argparse.ArgumentParser(description="API Firmware Updater")

parser.add_argument('--ip', type=str, help='Device IP', required=True)
parser.add_argument('--password', type=str, help='Device password', required=True)
parser.add_argument('--port', type=str, help='Device HTTP Port (Default: 80)', required=False, default='80')

args = parser.parse_args()

config = Hik(args.ip, args.password, args.port)

console.print('[[cyan][bold]+[/bold][/cyan]] Actualizando Firmware...')

update = config.fw_update()

if update == 200:
    console.print('[[green][bold]![/bold][/green]] Firmware actualizado correctamente')
    print('')
else:
    console.print('[[green][red]![/bold][/red]] Error al actualizar Firmware')
    print(update)

console.print('[[cyan][bold]+[/bold][/cyan]] Reiniciando Dispositivo...')

reboot = config.reboot()

if reboot == 200:
    console.print('[[green][bold]![/bold][/green]] Dispositivo reiniciado corectamente')
    print('')
else:
    console.print('[[green][red]![/bold][/red]] Error en el reinicio del dispositivo')
    print(reboot)
