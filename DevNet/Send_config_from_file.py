from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import NetMikoAuthenticationException
from paramiko.ssh_exception import SSHException

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

    '''belwo command will get use to move in to config mode(Confi#)'''
    # net_connect.config_mode()

    '''When we use send_config_from_file then we directly moving to config mode and we don't need to execute 
    above config_mode command'''
    output = net_connect.send_config_from_file(config_file='C:\\Users\\Dhurvi\\PycharmProjects\\DevNet\\Command_list')
    print(output)

    '''Belwo save_config() used for saving(wr) configuration once we make all changes'''
    print('\n Saving the Router configuration \n')
    output = net_connect.save_config(confirm=True)
    print(output)

    output = net_connect.send_command('show ip int brief')
    print(output)




