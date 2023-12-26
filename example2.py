from scrapli.driver.core import IOSXEDriver
from rich import print as rprint
import getpass

username = input("Type Username here:")
password =getpass.getpass("Type Password here:")
ip = input("IP Address:")
MY_DEVICES = [
    {
        "host": ip,
        "auth_username": username,
        "auth_password": password,
        "auth_strict_key": False,
    }
    
]

for device in MY_DEVICES:
    with IOSXEDriver(**device) as conn:
        response = conn.send_command("sho ip int brief")
        structured =response.textfsm_parse_output()
        rprint(structured)