from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import NetMikoAuthenticationException
from paramiko.ssh_exception import SSHException
import time
import datetime

TNOW = datetime.datetime.now().replace(microsecond=0)

IP_Address = open('IP_Address')
for IP_Pass in IP_Address:
    fields = IP_Pass.split(',')
    IP = fields[0]
    Password = fields[1]

    Router = cisco = {
          'device_type': 'cisco_ios',
          'host': IP,
          'username': Password,
          'password': Password,
          'secret': Password
          }

    print('\n ######## Connecting to the Device ' + IP.strip() + '####### \n')
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

    print('Initiating cofig backup')
    output = net_connect.send_command('show run')

    #SAVE_FILE = open("RTR_" + IP + '_' + str(TNOW), 'w')
    
    SAVE_FILE = open('Router', 'w')
    SAVE_FILE
    SAVE_FILE.write(output)
    SAVE_FILE.close
    print('Finished config backup')






