#functions for key -I
import requests

class Install:
    def __init__(self, pkg_name):
        self.pkg_name = pkg_name
        #self.dependencies_list = [] # installation list used instead
        self.installation_list = []

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
        print('package:', self.pkg_name)
        print('full list of installation (package and dependencies for this package):', self.installation_list)
    
    def download(self):
        #download script is going here
        print("nothing to download")
