from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import NetMikoAuthenticationException
from paramiko.ssh_exception import SSHException
import schedule
import time
import datetime


def fixed_time():
    tnow = datetime.datetime.now().replace(microsecond=0)
    ip_address = open('IP_Address')
    for IP_Pass in ip_address:
        fields = IP_Pass.split(',')
        ip = fields[0]
        password = fields[1]

        Router = cisco = {
            'device_type': 'cisco_ios',
            'host': ip,
            'username': password,
            'password': password,
            'secret': password
        }

        print('\n ######## Connecting to the Device ' + ip.strip() + '####### \n')
        '''we will be in user(>) mode using below command'''
        try:
            net_connect = ConnectHandler(**Router)
        except NetMikoTimeoutException:
            print("connection time out")
            continue
        except NetMikoAuthenticationException:
            print("Authentication failure")
            continue
        except SSHException:
            print("SSH is not enabled in device")
            continue

        print(net_connect.find_prompt())

        '''below command will put enable on cisco user mode(>) and use password 
        from above secret field to move in to privilege mode(#).'''
        net_connect.enable()

        print('Initiating cofig backup at : ' + str(tnow))
        output = net_connect.send_command('show run')

        # SAVE_FILE = open("RTR_" + IP + '_' + str(TNOW), 'w')

        SAVE_FILE = open('Router1', 'w')
        SAVE_FILE
        SAVE_FILE.write(output)
        SAVE_FILE.close
        print('Finished config backup at :' + str(tnow))


schedule.every().day.at("17:03").do(fixed_time)

while True:
    schedule.run_pending()
    time.sleep(1)