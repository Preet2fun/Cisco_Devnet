from device_info import ios_xe1
from ncclient import manager
import xmltodict
from pprint import pprint

# NETCONF filter to use
netconf_filter = open("filter-ietf-interfaces.xml").read()

if __name__ == '__main__':
    with manager.connect(host=ios_xe1["address"], port=ios_xe1["port"],
                         username=ios_xe1["username"],
                         password=ios_xe1["password"],
                         hostkey_verify=False) as m:

        # Get Configuration and State Info for Interface, out will be in xml format
        netconf_reply = m.get(netconf_filter)
        pprint(netconf_reply)

        # now convert this xml out put into directory to play around
        int_details = xmltodict.parse(netconf_reply.xml)
        pprint(int_details)

        # now we will print only all important data from rpc-reply directory
        data = int_details["rpc-reply"]["data"]
        pprint(data)

        # now we will print only all interface from rpc-reply directory
        int_data = data["interfaces"]["interface"]
        pprint(int_data)

        # now we will print only all interface status from rpc-reply directory
        int_status = data["interfaces-state"]["interface"]
        pprint(int_status)

        # now we will display diffrent statistics of interfaces
        print("")
        print("Interface Details:")
        print("  Name: {}".format(int_data["name"]["#text"]))
        print("  Description: {}".format(int_data["description"]))
        print("  Type: {}".format(int_data["type"]["#text"]))
        print("  MAC Address: {}".format(int_status["phys-address"]))
        print("  Packets Input: {}".format(int_status["statistics"]["in-unicast-pkts"]))
        print("  Packets Output: {}".format(int_status["statistics"]["out-unicast-pkts"]))

