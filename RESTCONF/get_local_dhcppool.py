import requests


def main():
    
    # The IOS-XE sandbox uses a self-signed cert at present, so let's
    # ignore any obvious security warnings for now.
    requests.packages.urllib3.disable_warnings()

    # The API path below is what the sandbox uses for API testing,
    #api_path = "https://172.16.8.237:443/restconf"
    api_path = "https://172.16.8.237:443/restconf/data/Cisco-IOS-XE-native:native/logging/monitor/severity"

    # Create 2-tuple for "basic" authentication using Cisco credentials.
    auth = ('admin', 'Mind@123')
    
    # Define headers for issuing HTTP GET requests to receive YANG data as JSON.
    #headers = {"Accept": "application/yang-data+json"}
    headers = {'Accept-Encoding': 'gzip, deflate',  'Accept': 'application/yang-data+json, application/yang-data.errors+json'}
     
    # Issue a GET request to collect the DHCP pool information only. This will
    get_pool_respo = requests.get(
                     api_path,
                     headers=headers,
                     auth=auth,
                     verify=False,
                     )


    print(get_pool_respo)
                     








if __name__=='__main__':
  main()

