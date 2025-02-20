import subprocess
import json

profile_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profile']).decode('utf-8').split("\n")

profiles = [cred.split(":")[1].strip()  for cred in profile_data if "All User Profile" in cred]

creds = {}

for profile in profiles:
    try:
    
        result_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8').split('\n')

        result = [res.split(":")[1].strip() for res in result_data if "Key Content" in res]

        creds[profile] = result[0] if result else "Not Available"
    
    except Exception :
        continue


print(json.dumps(creds,indent=2))
input("Press Any Key to Exit")
