from ncclient import manager


if __name__ == '__main__':
    with manager.connect(host='sbx-nxos-mgmt.cisco.com', port='10000', username='admin', password='Admin_1234!',
                         hostkey_verify=False) as m:
        print("here is netconf cpability ")
        for capability in m.server_capabilities:
            print(capability)