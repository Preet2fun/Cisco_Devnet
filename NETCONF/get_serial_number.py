#!/usr/bin/env python

"""
Purpose: Using NETCONF with Openconfig YANG models to collect switchport
configs on a Cisco NX-OS switch via the always-on Cisco DevNet sandbox.
"""


import xmltodict
from ncclient import manager
import sys

def main():
    """
    Execution begins here.
    """
    

    serial_number = """
     <System xmlns="http://cisco.com/ns/yang/cisco-nx-os-device">
     <serial/>
     </System>
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

        # Collect the NETCONF response
        netconf_response = conn.get(('subtree', serial_number))
         # Parse the XML and print the data
        print(netconf_response.xml)
        print(xmltodict.parse(netconf_response.xml)['rpc-reply']['data']['System']['serial'])


    print("NETCONF session disconnected")


if __name__ == "__main__":
    main()
