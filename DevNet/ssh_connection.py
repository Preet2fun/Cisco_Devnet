from netmiko import ConnectHandler


Router34 =  cisco = {
      'device_type': 'cisco_ios',
      'host': '172.16.9.211',
      'username': 'Router1',
      'password': 'Router1',
      'secret': 'Router1'
      }


net_connect = ConnectHandler(**Router34)

print(net_connect.find_prompt())

output = net_connect.send_command('show ip int brief')
print(output)