#functions for key -R
#imports
import os
from installer import remove


#code
class Remove:
    def __init__(self, pkg_name):
        self.pkg_name = pkg_name
        self.pkg_type = ''

    def checkPkgType(self): # returns True or False. If there is no package on this PC with this name it will just return False
        with open('./downloads/list_of_installations.totmb') as installation_list:
            if self.pkg_name in installation_list.read():
                if os.path.isdir('./downloads/installed/app/' + self.pkg_name):
                    self.pkg_type = 'app'
                    return True
                if os.path.isdir('./downloads/installed/lib/' + self.pkg_name): # not else: just remember that I am making this stuff because I wanna use it in WaxusBS. There may be way more package types
                    self.pkg_type = 'lib'
                    return True
            else:
                print ('An error occured: couldn\'t find package with this name on your computer')
                return False

    def startRemoving(self):
        print('Removing package "' + self.pkg_name + '"...')
        remove.removePackage(self.pkg_name, self.pkg_type)
        print('Removing package ' + self.pkg_name + ' from journal')
        remove.removePackageFromTheList(self.pkg_name)
