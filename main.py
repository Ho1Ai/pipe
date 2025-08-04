import requests
import argparse
from keys import I, R, U, C 

parser = argparse.ArgumentParser(prog="pipe",
                               description="pipe package manager",
                               epilog="Pipe package manager. WaxusBS operating system package manager. Test versions")

parser.add_argument('--key', type=str, help='package manager key', required=False)
parser.add_argument('--pkg', type=str, help='package name', required = False)


#parser.add_argument('--update-all', type=bool, help='if you wanna update all packages, which have been installed using pipe package manager, on your computer', required = False)
#parser.add_argument('--install', type=bool, help='if you wanna install a package', required = False)
#parser.add_argument('--remove', type=bool, help='if you wanna remove a package', required=False)
#parser.add_argument('--install-single', type=bool, help='if you wanna install only package, with no dependencies', required=False)
#parser.add_argument('--no-ask', type=bool, help='removes "install? [Y/n]" message on installation. For remove and some others it won\'t disable anything')


args = parser.parse_args()

#print(args.pkg)
#print(args.key)

#print(args)

keys_arr = ['-I', '-R', '-U', '-C']

#todo = input("write a key (-I, -R, -U): ")

can_proceed = False

package = ''

if args.key==None:
    todo = input("Write a key (-I, -R, -U): ")
    if todo in keys_arr:
        if todo != '-U':
            package = input('Write a package name: ')
        can_proceed = True
    else:
        print('Couldn\'t receive or recognise entered key. Pipe has been stopped.')
else:
    todo = '-'+args.key

#can_proceed = False

#todo = '-'+args.key
if todo in keys_arr and args.key:
    #if todo != '-U':
        #package = input("write package name: ")
    if todo !='-U' and args.pkg:
        package=args.pkg
        can_proceed=True
    elif todo == '-U':
        can_proceed=True
    elif todo !='-U' and args.pkg==None:
        print('Couldn\'t recieve package name. Please restart pipe and try again.')
        can_proceed = False # well, it is false by default btw
#else:
#   print('Couldn\'t receive a key or couldn\'t recognise entered key. Pipe has been stopped.')

final_response = None

getting_final_list = None

#def fetch(pkg: str):
#    response = requests.get("http://localhost:8000/api/package-info", params={"name": pkg})
#    if response.status_code == 200:
#        return response.json()
#    else:
#        print('Error:', response.text)
#        return 'An error occured. Couldn\'t receive package or dependency'

if can_proceed==True:
    if todo == '-I':
        work_instance = I.Install(package)
        can_proceed = work_instance.areThereAPackage()
        if(can_proceed):
        
            work_instance.fetchPkgData(work_instance.pkg_name) # start package is this package. I am using "package_name" variable in this function. If I didn't add this stuff then it's gonna scream that it needs more params. I don't need it, no one needs it, lol
            work_instance.showData()
            work_instance.installationConfirmation()
    
    #legacy code, btw
#    final_response = fetch(package)
#    print(final_response.get('dependencies'))
#    if (final_response.get('dependencies')): # looking if there are any dependencies. Still not ready. Gonna write it tomorrow (on 2025/03/21)
#        nextStep = final_response.get('dependencies')
#        for index in nextStep:
#            print(fetch(index))

    if todo == '-R':
        work_instance = R.Remove(package)
        if work_instance.checkPkgType():
            work_instance.removeConfirmation()
        else:
            print('An error occured. Pipe has been stopped')

    if todo == '-U':
        work_instance = U.Update()
        work_instance.checkPackages()
        if work_instance.areThereAnyUpdates(): #checking if updating is needed (if not it won't start)
            work_instance.updateConfirmation() # add installation script!
        else:
            print('Package manager has been stopped')

    if todo == '-C':
        work_instance = C.Check(args.pkg)
        work_instance.getInfo()
