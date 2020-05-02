import requests
import yaml
import json


def main():
     
    # The IOS-XE sandbox uses a self-signed cert at present, so let's
    # ignore any obvious security warnings for now.
    requests.packages.urllib3.disable_warnings()

    # The API path below is what the sandbox uses for API testing,
    api_path = "https://ios-xe-mgmt-latest.cisco.com:9443/restconf"

    # Create 2-tuple for "basic" authentication using Cisco credentials.
    auth = ('root', 'D_Vay!_10&')

    # Read YAML declarative state with list of DHCP pools to add
    with open('config_state.yml', 'r') as handle:
         config_state = yaml.safe_load(handle)
    print(config_state)
    print("#################################################")
    # Create JSON structure to add a new pool along with the HTTP POST
    # headers needed to add it.
    add_pool = {"Cisco-IOS-XE-dhcp:pool": config_state["add_pools"]}

    print(add_pool)
    print("###################################################")
    add_headers = {"Content-Type": "application/yang-data+json",
        "Accept": "application/yang-data+json, application/yang-data.errors+json",}
    
    # Can double-check our HTTP body using this debug; great for learning
    print(json.dumps(add_pool, indent=2))
    
    add_pool_resp = requests.post(
                    f"{api_path}/data/Cisco-IOS-XE-native:native/ip/dhcp",
                    headers=add_headers,
                    auth=auth,
                    json=add_pool,
                    verify=False,
                    )

     
    print(add_pool_resp)
    # HTTP 201 means "created", implying a new resource was added. The
    # response will tell us the URL of the newly-created resource, simplifying
    # future removal.
    if add_pool_resp.status_code == 201:
        print(f"Added DHCP pool at: {add_pool_resp.headers['Location']}")

        # Save configuration whenever the DHCP pool is added. This ensures
        # the configuration will persist across reboots.
        save_config_resp = requests.post(
            f"{api_path}/operations/cisco-ia:save-config",
            headers=add_headers,
            auth=auth,
            verify=False,
        )

        # Optionally print the JSON response, along with success message
        # import json; print(json.dumps(save_config_resp.json(), indent=2))
        if save_config_resp.ok:
            print("Saved configuration")





if __name__=='__main__':
   main()
