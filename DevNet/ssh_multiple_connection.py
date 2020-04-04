from netmiko import ConnectHandler


Router_9_211 =  cisco = {
      'device_type': 'cisco_ios',
      'host': '172.16.9.211',
      'username': 'Router1',
      'password': 'Router1',
      'secret': 'Router1'
      }

Router_8_34 =  cisco = {
      'device_type': 'cisco_ios',
      'host': '172.16.8.34',
      'username': 'ospf1',
      'password': 'ospf1',
      'secret': 'ospf1'
      }

DEVICE_LIST = [Router_9_211, Router_8_34]
for DEVICE in DEVICE_LIST:

    print('Connecting to the Device ' + DEVICE['host'])
    net_connect = ConnectHandler(**DEVICE)
    print(net_connect.find_prompt())
    output = net_connect.send_command('show ip int brief')
    print(output)