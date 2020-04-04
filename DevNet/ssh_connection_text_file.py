from netmiko import ConnectHandler

with open('IP_Address') as IP_Address:
    for IP_Pass in IP_Address:
        fields = IP_Pass.split(',')
        IP = fields[0]
        Password = fields[1]
        print(IP)
        print(Password)
        Router = cisco = {
              'device_type': 'cisco_ios',
              'host': IP,
              'username': Password,
              'password': Password,
              'secret': Password
              }
        print(cisco['username'])
        print(cisco['password'])
        print(cisco['secret'])
        with open('Command_list') as Command:
            for cmd in Command:
                print('Connecting to the Device ' + IP)
                net_connect = ConnectHandler(**Router)
                print(net_connect.find_prompt())
                output = net_connect.send_command(cmd)
                print(output)