from device_info import ios_xe1
from ncclient import manager
import xmltodict
from pprint import pprint

# NETCONF filter to use
netconf_filter = open("config-temp-ietf-interfaces.xml").read()

if __name__ == '__main__':

    netconf_payload = netconf_filter.format(int_name="GigabitEthernet3", int_desc="configured by netconf 555",
                                            ip_address="5.5.5.5", subnet_mask="255.255.255.0")

    print(netconf_payload)

    with manager.connect(host=ios_xe1["address"], port=ios_xe1["port"],
                         username=ios_xe1["username"],
                         password=ios_xe1["password"],
                         hostkey_verify=False) as m:

        # Get Configuration and State Info for Interface, out will be in xml format
        netconf_reply = m.edit_config(netconf_payload,target="running")
        pprint(netconf_reply)
