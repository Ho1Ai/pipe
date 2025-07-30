import requests
import os
import enum

class Check:
    def __init__(self, pkg_name):
        self.pkg_name = pkg_name
    

    def getInfo(self):
        self.ex = requests.get('http://localhost:8000/api/package-existence', params={'name': self.pkg_name}).json()
        #print(self.ex.get('exist'))
        if self.ex.get('exist'):
            info = requests.get('http://localhost:8000/api/package-info', params={'name': self.pkg_name}).json()
            installation_list = open('./downloads/list_of_installations.totmb').readlines()
            index = 0
            installed = False
            for index in installation_list:
                index = index.replace('\n', '')
                #print(index)
                if(info.get('name') == index):
                    #print('yes')
                    installed = True
            #print(installation_list)
            print('') # adding an empty line
            print("name:", info.get('name'), "\ncurrent version:", info.get('version'), "\npackage type (prebuilt/compile):", info.get('build_type'), "\ninstalled:", installed)
        else:
            print("\nObject with this name does not exist on server... \nLooking for it locally...")
            installation_list = open('./downloads/list_of_installations.totmb').readlines() #yeah, DRY, don't ask me, why did I add this stuff again...
            installed = False
            for index in installation_list:
                index = index.replace('\n', '')
                if (index == self.pkg_name):
                    installed = True
            if(installed):
                print("There is a package on your computer with this name.")
                if(os.path.isdir('./downloads/installed/app/'+self.pkg_name) or os.path.isdir('./downloads/installed/lib/'+self.pkg_name)):
                    pass
                else:
                    print("Unfortunately, couldn't find this package on your computer... Maybe, you have moved it somewhere else.")
            else:
                print("There is no packages with this name on your computer. Maybe, you did a mistake in pkg name")
