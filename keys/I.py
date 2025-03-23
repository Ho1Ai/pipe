#functions for key -I
import requests
from installer import install


print('test')

class Install:
    def __init__(self, pkg_name):
        self.pkg_name = pkg_name
        #self.dependencies_list = [] # installation list used instead
        self.installation_list = []
        self.INSTALLATION_PATH = './downloads/' # Named in CAPS because it is const

    def areThereAPackage(self):
        checkbox = requests.get('http://localhost:8000/api/package-info', params={'name': self.pkg_name})
        checkbox_in_json = checkbox.json()
        if checkbox_in_json.get('detail'):
            print('An error occured: ', checkbox_in_json.get('detail')) #don't wanna use it as a variable, because there is no places where it is used once more
            return (False)
        else:
            return(True)

    def fetchPkgData(self, package_name: str):
        res = requests.get("http://localhost:8000/api/package-info", params={"name": package_name})
        if res.status_code == 200:
            print('resolving dependencies for:', package_name)
            if(package_name in self.installation_list) == False: #the best cork ever. I guess it is not me unworthy of Oxford University, it is just Oxford University unworthy of me
                self.installation_list.append(package_name)
            if res.json().get("dependencies"): #in case it is empty it will just ignore this stuff, because empty array, false (boolean), 0 (int), "" (empty string), etc. are same to 0. IDK will it work in Python, but I wonder why can't it work
                for index in res.json().get("dependencies"):                    
                    if (index in self.installation_list) == False:
                        #print('resolving subdependencies for:', index) #thought it could be a great idea. Never mind, I'm just sleepy at the moment
                        self.installation_list.append(index)
                        self.fetchPkgData(index)
            # well, I guess, there can be no cases, when one lib requires second lib, second lib requires first lib... It sound dumb, lmao
        else:
            return ("An error occured while fetching data for: "+package_name)

    def showData(self):
        print('\nReceived packages list:')
        print('package:', self.pkg_name)
        print('full list of installation (package and dependencies for this package):', self.installation_list)
    
    def installationConfirmation(self):
        if self.installation_list:
            checkbox = input("Download and install packages? [Y/n] ")
            if checkbox == 'y' or checkbox =='Y' or checkbox =='':
                self.download()
            elif checkbox == 'n' or checkbox == 'N':
                print('Installation canceled')
            else:
                print('Couldn\'t recognize entered flag. Installation canceled')
        
        else:
            print('Nothing to install.')

    def download(self):
        if(self.installation_list == []):
            print("nothing to download") #checking if there is nothing to download (in case there is a bug)
        for index in self.installation_list: #index is just a child of self.installation_list (I mean it is 
            response = requests.get('http://localhost:8000/api/download', params={'name':index})
            
            name = self.INSTALLATION_PATH+"tmp/"+index #INSTALLATION_PATH is just a path to download dir. Downloaded files should be placed here. Then it will be placed by status in "downloads/installed" (in "downloads/installed/lib" or "downloads/installed/app"). It is using "./downloads/..." because it starts from main.py so I have to call it like I.py is in core of this package manager. Then goes name of package (index = name, because we run through the array with packages)
            with open(name, "wb") as archieved:
                archieved.write(response.content)
            
            print(index,'- succesful')
