from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import NetMikoAuthenticationException
from paramiko.ssh_exception import SSHException
import textfsm
import json


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

    output = net_connect.send_command('show ip int brief')
    print(output)

    # open the template file
    with open('cisco_ios_show_ip_interface_brief.textfsm', 'r') as f:
        template = textfsm.TextFSM(f)

    # run the interface data through the template parser
    int_output = template.ParseText(output)
    print(int_output)

    print(json.dumps(int_output, indent=2))

    device_up_list = []
    device_down_list = []

    length = len(int_output)
    print('Total interfaces are :' + str(length))

    print("List of all up interfaces as below ##################################")
    for i in range(0, length):
        if int_output[i][2] == 'up':
            device_up_list.append(int_output[i][0])

    print(device_up_list)
    print("List of all down interfaces as below ##################################")
    for i in range(0, length):
        if int_output[i][2] != 'up':
            device_down_list.append(int_output[i][0])
    print(device_down_list)

    #for i in int_output:
    #    print(i[2])
    print([i[0] for i in int_output if i[2] == 'up'])
