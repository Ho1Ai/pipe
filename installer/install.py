#package manager installer will be here
import os
import shutil

#cfgl = open('../downloads/tmp/one/install_cfg.totmb').readlines()
#print(cfgl)

def installPackage(pkg_name: str):
    config_list = open('./downloads/tmp/'+pkg_name+'/install_cfg.totmb').readlines()
    if ('lib' in config_list[0]):
        final_path = './downloads/installed/lib/'+pkg_name+'/'
        src_path='./downloads/tmp/'+pkg_name+'/'
        os.makedirs(final_path, exist_ok = True)# creating dirs for each package in app or lib
        print('\nCreated directory for next library:', pkg_name+';')
        shutil.copy(src_path + pkg_name, final_path)
        print('Copied library "'+pkg_name+'" into '+final_path)
        os.chmod(final_path+pkg_name, 0o755)
        print('Execution permission has been given to application "' + pkg_name + '"')
        shutil.rmtree(src_path)
        print('Tree, which contained library "' + pkg_name + '", has been removed (from tmp)')
        writePackageVersion(pkg_name, 'lib', config_list[1])
        

    if ('app' in config_list[0]):
        final_path = './downloads/installed/app/'+pkg_name+'/'
        src_path = './downloads/tmp/'+pkg_name+'/'
        os.makedirs(final_path, exist_ok = True) # I don't use elif just not to catch bug in case it is an application and lib in the same moment
        print('\nCreated directory for next application:',pkg_name+';')
        shutil.copy(src_path + pkg_name, final_path)
        print('Copied application "'+pkg_name+'" into '+final_path)
        os.chmod(final_path + pkg_name,0o755)
        print('Execution permission has been given to application "' + pkg_name + '"') #yeah, 'print(f"... to application {pkg_name}")' is not for me.
        shutil.rmtree(src_path)
        print('Tree, which contained application "' + pkg_name + '", has been removed (from tmp)')
        writePackageVersion(pkg_name, 'app', config_list[1])
    # Now you can see legacy comment, btw
    # This stuff will be started after Install.download(). It will just place downloaded files in dirs "lib" and "app". I've divided these files (I.py and install.py) because I.py is already very big and it is a lil bit hard to read this file. I don't use VSCode or smth like that, I use Vim instead 

def writePackageVersion(pkg_name:str, pkg_type:str, pkg_ver: str):
    print('Writting package version into info.st file') # info.st is a file, which keeps status of package (at least version). '.st' means 'STatus file'
    with open('./downloads/installed/'+pkg_type+'/'+pkg_name+'/info.st','w') as statusFileWriter:
        statusFileWriter.write(pkg_ver+'\n')


def writePackageInTheList(pkg_name: str):
    #reader reads logs, writter writes if it is necessary
    list_path = './downloads/list_of_installations.totmb'
    reader = open(list_path).read()
    if pkg_name in reader:
        pass
    else:
        with open(list_path, 'a') as writter:
            writter.write(pkg_name+'\n')
