from netmiko import ConnectHandler
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

    print('Connecting to the Device ' + IP)
    '''we will be in user(>) mode using below command'''
    try:
        net_connect = ConnectHandler(**Router)
        print(net_connect.find_prompt())
        net_connect.enable()
        steps = net_connect.send_command('Show ip int brief')
        print(json.dumps(steps, indent=2))
    except Exception as e:
        print(e)



