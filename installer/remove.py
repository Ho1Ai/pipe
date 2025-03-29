#package manager remover will be here
#imports
import shutil


#code
def removePackage(pkg_name:str, pkg_type: str):
    shutil.rmtree('./downloads/installed/'+pkg_type+'/'+pkg_name)

def removePackageFromTheList(pkg_name:str):
    reader = open('./downloads/list_of_installations.totmb').readlines()
    writer = open('./downloads/list_of_installations.totmb', 'w')
    
    final_list=""

    for index in reader:
        if (pkg_name in index) == False:
            final_list+=index
    

    writer.write(final_list)
