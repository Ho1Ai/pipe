#package manager updater will be here. It will just change info.st file
import os
import shutil

def updatePackage(pkg_name:str):
    config_list = open('./downloads/tmp/'+pkg_name+'/install_cfg.totmb').readlines()
    if ('lib' in config_list[0]):
        final_path='./downloads/installed/lib/'+pkg_name+'/'
        src_path='./downloads/tmp/'+pkg_name+'/'
        #file = open(src_path+'/'+pkg_name, 'rb')
        shutil.copy(src_path+pkg_name, final_path)
        os.chmod(final_path+pkg_name, 0o755)
        os.remove(final_path+'info.st') # removing file just because it is way easier to overwrite it after deleting
        writePackageVersion(pkg_name, 'lib', config_list[1].replace('\n', ''))
        shutil.rmtree(src_path)

    if ('app' in config_list[0]):
        final_path='./downloads/installed/app/'+pkg_name+'/'
        src_path = './downloads/tmp/'+pkg_name+'/'
        shutil.copy(src_path+pkg_name, final_path)
        os.chmod(final_path+pkg_name, 0o755)
        os.remove(final_path+'info.st')
        writePackageVersion(pkg_name, 'app', config_list[1].replace('\n', ''))
        shutil.rmtree(src_path)

        

def writePackageVersion(pkg_name:str, pkg_type:str, pkg_ver: str):
    with open('./downloads/installed/'+pkg_type+'/'+pkg_name+'/info.st', 'w') as statusFileWriter:
        statusFileWriter.write(pkg_ver+'\n')
