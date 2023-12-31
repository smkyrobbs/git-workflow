from scrapli.driver.core import IOSXEDriver
from rich import print as rprint
import logging
import getpass

logging.basicConfig(filename="log.txt", level=logging.DEBUG)

DEVICE = {"hostname" : "CSR_Practice",
          "host" : "192.168.78.134"}
username = input("USERNAME: ")
password = getpass.getpass("PASSWORD:")

def test_func():
    with IOSXEDriver(host=DEVICE["host"], auth_username=username, auth_password=password, auth_strict_key=False) as conn:
        response = conn.send_command("show version")
        structured_data = response.textfsm_parse_output()[0]
        host_name = structured_data["hostname"]
        #print(host_name)
        if host_name.startswith("CSR"):
            send_new_cmd = conn.send_config("hostname "+host_name.lower())
            print(send_new_cmd)
        else:
            print("It starts with lowercase")
        #rprint(structured_data)

if __name__ == "__main__":
    test_func()