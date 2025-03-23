import requests
from keys import I, R, U 

todo = input("write a key (-I, -R, -U): ")
if todo:
    package = input("write package name: ")
else:
    print('couldn\'t receive a key. Application has been stopped')

final_response = None

getting_final_list = None

#def fetch(pkg: str):
#    response = requests.get("http://localhost:8000/api/package-info", params={"name": pkg})
#    if response.status_code == 200:
#        return response.json()
#    else:
#        print('Error:', response.text)
#        return 'An error occured. Couldn\'t receive package or dependency'

if todo == '-I':
    work_instance = I.Install(package)
    can_proceed = work_instance.areThereAPackage()
    if(can_proceed):
        
        work_instance.fetchPkgData(work_instance.pkg_name) # start package is this package. I am using "package_name" variable in this function. If I didn't add this stuff then it's gonna scream that it needs more params. I don't need it, no one needs it, lol
        work_instance.showData()
        work_instance.installationConfirmation()
    
#    final_response = fetch(package)
#    print(final_response.get('dependencies'))
#    if (final_response.get('dependencies')): # looking if there are any dependencies. Still not ready. Gonna write it tomorrow (on 2025/03/21)
#        nextStep = final_response.get('dependencies')
#        for index in nextStep:
#            print(fetch(index))
