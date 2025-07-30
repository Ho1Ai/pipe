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
            print("\nObject with this name does not exist")
