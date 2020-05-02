#!/usr/bin/env python

"""
Purpose: Using NETCONF with Openconfig YANG models to collect switchport
configs on a Cisco NX-OS switch via the always-on Cisco DevNet sandbox.
"""


import xmltodict
from ncclient import manager


def main():
    """
    Execution begins here.
    """

    # Dictionary containing keyword arguments (kwargs) for connecting
    # via NETCONF. Because SSH is the underlying transport, there are
    # several minor options to set up.
    connect_params = {
        "host": "sbx-nxos-mgmt.cisco.com",
        "port": 10000,
        "username": "admin",
        "password": "Admin_1234!",
        "hostkey_verify": False,
        "allow_agent": False,
        "look_for_keys": False,
        "device_params": {"name": "nexus"},
    }

    # Unpack the connect_params dict and use them to connect inside
    # of a "with" context manager. The variable "conn" represents the
    # NETCONF connection to the device.
    with manager.connect(**connect_params) as conn:
        print("NETCONF session connected")

        # To save time, only capture 3 switchports. Less specific filters
        # will return more information, but take longer to process/transport.
        # Note: In this sandbox, it can take ~30 seconds to get all interfaces
        # and several minutes to get the whole config, so be aware!
        nc_filter = """
            <interfaces xmlns="http://openconfig.net/yang/interfaces">
                <interface>
                   <name>eth1/24</name>
                </interface>
                <interface>
                   <name>eth1/23</name>
                </interface>
            </interfaces>
        """

        # Execute a "get-config" RPC using the filter defined above
        resp = conn.get_config(source="running", filter=("subtree", nc_filter))

        # Uncomment line below to see raw RPC XML reply; great for learning
        #print(resp.xml)

        resp_dict = xmltodict.parse(resp.xml)
    
        for int in resp_dict['rpc-reply']['data']['interfaces']['interface']:
            #print(int)
            status = int['config']['enabled']
            if status:
                print("Status of interface {0} is {1}".format(int['name'],status))
            else:
                print("Status of interface {0} is {1}".format(int['name'],status)) 

    print("NETCONF session disconnected")


if __name__ == "__main__":
    main()
