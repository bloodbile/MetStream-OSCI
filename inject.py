import requests
import sys

url = f"{sys.argv[1]}/cgi-bin/CGI_SetTimezone.cgi"

try:
    r = requests.post(url, 
                      headers={"User-Agent": "Mozilla/5.0", 
                               "Content-Type": "application/x-www-form-urlencoded", 
                               "Connection": "close"}, 
                      data=f"zone=Europe/Stockholm|{sys.argv[2]}||a #'")
    print(r.text if r.status_code == 200 else r.status_code)
except Exception as e:
    print(f"error: {e}")