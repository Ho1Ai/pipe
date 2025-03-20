import requests
from keys import I, R, U 

todo = input("write a key (-I, -R, -U): ")
package = input("write a package name: ")

final_response = None

getting_final_list = None

def fetch(pkg: str):
    response = requests.get("http://localhost:8000/api/package-info", params={"name": pkg})
    if response.status_code == 200:
        return response.json()
    else:
        print('Error:', response.text)
        return 'An error occured. Couldn\'t receive package or dependency'

if todo == '-I':
    
    
    final_response = fetch(package)
    print(final_response.get('dependencies'))
    if (final_response.get('dependencies')): # looking if there are any dependencies. Still not ready. Gonna write it tomorrow (on 2025/03/21)
        nextStep = final_response.get('dependencies')
        for index in nextStep:
            print(fetch(index))
