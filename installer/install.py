#package manager installer will be here
import os
import shutil
import tarfile



AVAILABLE_PKG_TYPES = ['app', 'lib', 'osn', 'kernel', 'etc'] # osn = needed by OS (OS needed). Used for these packages: drivers, shell, init, etc.


#cfgl = open('../downloads/tmp/one/install_cfg.totmb').readlines()
#print(cfgl)

# Updating legacy code. Renamed function

def installPrebuiltPackage(pkg_name: str):
    config_list = open('./downloads/tmp/'+pkg_name+'/install_cfg.totmb').readlines()
    npkg_name = config_list[3]
    #print(npkg_name, pkg_name)
    if ('lib' in config_list[0]):
        final_path = './downloads/installed/lib/'+pkg_name+'/'
        src_path='./downloads/tmp/'+pkg_name+'/'
        os.makedirs(final_path, exist_ok = True)# creating dirs for each package in app or lib
        print('\nCreated directory for next library:', pkg_name+';')
        shutil.copy(src_path + npkg_name, final_path)
        print('Copied library "'+npkg_name+'" into '+final_path)
        os.chmod(final_path+npkg_name, 0o755)
        print('Execution permission has been given to application "' + pkg_name + '"')
        shutil.rmtree(src_path)
        print('Tree, which contained library "' + pkg_name + '", has been removed (from tmp)')
        writePackageVersion(pkg_name, 'lib', config_list[1])
        

    if ('app' in config_list[0]):
        final_path = './downloads/installed/app/'+pkg_name+'/'
        src_path = './downloads/tmp/'+pkg_name+'/'
        os.makedirs(final_path, exist_ok = True) # I don't use elif just not to catch bug in case it is an application and lib in the same moment
        print('\nCreated directory for next application:',pkg_name+';')
        shutil.copy(src_path + npkg_name, final_path)
        print('Copied application "'+pkg_name+'" into '+final_path)
        os.chmod(final_path + npkg_name,0o755)
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
    list_path = './cache/loi.sst'
    reader = open(list_path).read()
    if pkg_name in reader:
        pass
    else:
        with open(list_path, 'a') as writter:
            writter.write(pkg_name+'\n')





def extractPackage(pkg_name: str, path: str, arc_pkg_name:str):
    with tarfile.open(path+arc_pkg_name) as archieve: # arc means ARChieve (chars, from which goes abbreviation, are in CAPS)
        archieve.extractall(path)
        print("Package \""+pkg_name+"\" has been extracted")
        return True





def compileApplication(pkg_name: str, path: str):
    builder_dir_path = path+pkg_name+"/"
    try:
        os.system("cd "+builder_dir_path+"&& make")
        print("Application has been compiled succesfully")
        os.makedirs("./downloads/cache/"+pkg_name, exist_ok = True)
        shutil.copy(builder_dir_path+pkg_name, "./downloads/cache/"+pkg_name+"/"+pkg_name)
        shutil.copy(path+"install_cfg.totmb", "./downloads/cache/"+pkg_name+"/")
        print("Copying compiled application and installation config to cache directory")
        
        shutil.rmtree(path)
        print("Removed downloaded files")

        return True
    except Exception as e:
        print("Exception: ", e)
        return False



def compileTemporaryClean(final_path: str):
    shutil.rmtree(final_path)



def finalCompiledInstall(pkg_name:str, src_path:str, pkg_type:str, pkg_ver:str): #function is needed because installCompiledApplication() will just check pkg_type, pkg_version, etc. Variable src_path is needed just to take variable name instead of "./Downloads/cache/"+pkg_name+"/"+pkg_name
    installation_path = "./downloads/installed/"+pkg_type+"/"+pkg_name+"/"

    os.makedirs(installation_path, exist_ok=True)
    print("Making directory for package " + pkg_name)

    shutil.copy(src_path+pkg_name, installation_path)
    print("Package built file has been copied to final directory")
    #print(installation_path+"info.st")

    with open(installation_path+"info.st",'w') as status_file_writer:
        status_file_writer.writelines(pkg_ver+'\n')
        print("info.st status file has been written into compiled package directory.\nInstallation has been completed succesfully")

    compileTemporaryClean(src_path)

    




def installCompiledApplication(pkg_name: str, path: str):
    cfg_reader = open(path+"install_cfg.totmb").readlines()

    cfg__pkg_type = cfg_reader[0].replace('\n', '')
    cfg__pkg_version = cfg_reader[1].replace('\n', '')
    if(cfg__pkg_type in AVAILABLE_PKG_TYPES):
        finalCompiledInstall(pkg_name, path, cfg__pkg_type, cfg__pkg_version)
    else:
        print("Couldn't recognize package type: "+cfg__pkg_type+" is not in AVAILABLE_PKG_TYPES array. You can remove everything that has been downloaded and compiled: check out next path: ./Downloads/cache/"+pkg_name)





def checkPackageBuildType(pkg_name:str):
    tmp_path = "./downloads/tmp/"+pkg_name+"/"
    cfg_reader = open(tmp_path+"install_cfg.totmb","r").readlines()
    pkg_file = pkg_name+".tar.gz"
    cfg_reader[2] = cfg_reader[2].replace('\n', '')
    #pkg_type = cfg_reader[0].replace('\n', '')# now it's gonna travel in install_cfg.totmb
    if(cfg_reader[2] == "compile"):
        is_ext_ok = extractPackage(pkg_name, tmp_path, pkg_file)
        if is_ext_ok == True:
            is_compile_ok = compileApplication(pkg_name, tmp_path)
            if is_compile_ok == True:
                print("\nStarting installation....")
                cache_path = "./downloads/cache/"+pkg_name+"/"
                installCompiledApplication(pkg_name, cache_path) 
    else:
       installPrebuiltPackage(pkg_name) 
