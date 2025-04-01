#functions for -U key
#imports
import os
import shutil
import requests
from installer import update


#code
class Update:
    def __init__(self):
        self.update_list = []

    def checkPackages(self):
        print('Checking packages...')
        current_pkg_version = ''

        with open('./downloads/list_of_installations.totmb') as list_file:
            reader = list_file.readlines()
            for index in reader:
                pkg_name = index.replace('\n', '') # yeah, I forgot, that I keep these lines with \n in the end...
                
                #app
                if os.path.isdir('./downloads/installed/app/'+pkg_name):
                    # print('app') # debug line
                    current_pkg_version = open('./downloads/installed/app/'+pkg_name+'/info.st').readlines()[0].replace('\n', '')
                    latest_version = self.fetchPkgData(pkg_name)
                    if (latest_version == current_pkg_version) == False:
                        self.update_list.append(pkg_name)
                        # print('application "'+pkg_name+'" is up to date')
            
                #lib
                if os.path.isdir('./downloads/installed/lib/'+pkg_name):
                    # print('lib') # debug line
                    current_pkg_version = open('./downloads/installed/lib/'+pkg_name+'/info.st').readlines()[0].replace('\n', '') # here I get package version and remove \n from the end of the line. It can't keep '\n' in the version
                    latest_version = self.fetchPkgData(pkg_name)
                    if (latest_version == current_pkg_version) == False:
                        self.update_list.append(pkg_name)
                        # print('library "'+pkg_name+'" is up to date')
           #it still has no more pkg_types, so I can use these two ifs. Not if...else construction, because I can add some more pkg_types so it can be used not only with these types
       
    def areThereAnyUpdates(self):
        if(self.update_list):
            return True # then it just returns True and it shows full list of updates in self.updateConfirmation
        else:
            print('Everything is up to date')
            return False

    def fetchPkgData(self, pkg_name: str):
        # print(pkg_name) # debug line
        response = requests.get('http://localhost:8000/api/package-info', params={'name': pkg_name})
        res_json = response.json()
        return(res_json.get('version'))
    
    def updateConfirmation(self):
        print('Updates for next packages have been found:', self.update_list) 
        checkbox = input('Download and install updates for these packages? [Y/n] ')
        if checkbox == '' or checkbox == 'Y' or checkbox == 'y':
            self.download()
        elif checkbox == 'N' or checkbox == 'n':
            print('Updating has been canceled')
        else:
            print('Couldn\'t recognise entered flag. Updating has been canceled')

    def download(self):
        for index in self.update_list:
            response = requests.get('http://localhost:8000/api/download', params={'name':index})

            os.makedirs('./downloads/tmp/'+index, exist_ok = True)
            name = './downloads/tmp/'+index+'/'+index
            cfg = './downloads/tmp/'+index+'/install_cfg.totmb'
            with open(name, 'wb') as archieved:
                archieved.write(response.content)

            with open(cfg,'w') as cfg:
                cfg.write(response.headers.get('X-Pkg-Type') + '\n' + response.headers.get('X-Pkg-Version'))

                print(index, '- succesful')
        
        print('Everything has been downloaded succesfully.')
        
        self.startInstallation()
        # here it runs through "update_list" and downloads every

    def startInstallation(self):
        print('Starting installation...')
        for index in self.update_list:
            update.updatePackage(index)
