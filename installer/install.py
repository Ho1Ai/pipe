#package manager installer will be here
import os
import shutil

def installPackage(pkg_name: str):
    with open('./downloads/tmp/'+pkg_name+'/install_cfg.totmb') as config_list:
        print (config_list)
        if 'lib' in config_list:
            os.makedirs('./downloads/installed/lib/'+pkg_name+'/', exist_ok = True) # creating dirs for each package in app or lib 
        if 'app' in config_list:
            os.makedirs('./downloads/installed/app/'+pkg_name+'/', exist_ok = True) # I don't use elif just not to catch bug in case it is an application and lib in the same moment
    # Now you can see legacy comment, btw
    # This stuff will be started after Install.download(). It will just place downloaded files in dirs "lib" and "app". I've divided these files (I.py and install.py) because I.py is already very big and it is a lil bit hard to read this file. I don't use VSCode or smth like that, I use Vim instead 

def writePackageInTheList(pkg_name: str):
    pass
