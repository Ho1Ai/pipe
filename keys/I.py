#functions for key -I
import requests

class Install:
    def __init__(self, pkg_name):
        self.pkg_name = pkg_name
        #self.dependencies_list = [] # installation list used instead
        self.installation_list = []

    def fetchPkgData(self, package_name: str):
        res = requests.get("http://localhost:8000/api/package-info", params={"name": name})
        if res.status_code == 200:
            if res.json().get("dependencies"): #in case it is empty it will just ignore this stuff, because empty array, false (boolean), 0 (int), "" (empty string), etc. are same to 0. IDK will it work in Python, but I wonder why can't it work
                for index in res.json().get("dependencies"):
                    fetchPkgData(index)
            else:
                self.installation_list.append(package_name)# well, I guess, there can be no cases, when one lib requires second lib, second lib requires first lib... It sound dumb, lmao
        else:
            return ("An error occured while fetching data for: "+package_name)

    def showData(self):
        print('package:', self.pkg_name)
        print('full list of installation (package and dependencies for this package):', installation_list)

