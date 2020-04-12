import requests
import auth_token
import json


def get_device_list():
       api_path = "https://sandboxdnac.cisco.com/dna"
       auth = auth_token.get_token()
       headers = {"Content-Type": "application/json", "X-Auth-Token": auth}
   

       auth_resp = requests.get(f"{api_path}/intent/api/v1/network-device/", headers= headers)
       
       auth_resp.raise_for_status() 
       print(auth_resp.json())
       print("##########################################")
       device_list = json.dumps(auth_resp.json(), indent=2)
       if auth_resp.ok:
          for device in auth_resp.json()["response"]:
              print(f"ID: {device['id']}   IP: {device['managementIpAddress']}")
       else:
          print ("operation is not successful")


       return device_list

def main():
    list = get_device_list()
    print(list)



if __name__ == "__main__":
    main()

