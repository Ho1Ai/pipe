import requests
from keys import I, R, U 

todo = input("write a key (-I, -R, -U): ")
package = input("write a package name: ")

final_response = None

def fetch(pkg: str):
    response = requests.get("http://localhost:8000/api/package-info", params={"name": pkg})
    if response.status_code == 200:
        return response.json()
    else:
        print('An error occured while fetching package:', response.text)
        return None

if todo == '-I':
    final_response = fetch(package)
    print(final_response)
