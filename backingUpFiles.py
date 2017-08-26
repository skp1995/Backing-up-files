import zipfile, os

def backup(folder):
    folder = os.path.abspath(folder)
    n = 1
    while True:
        zip1 = os.path.basename(folder) + '_' + str(n) + '.zip' #Name of the zip file = nameOfThebackedUpFolder_<backupcount>.zip
        if not os.path.exists(zip1):
                break
        n = n + 1

    print('Creating %s...' % (zip1))
 
    backupZip = zipfile.ZipFile(zip1, 'w') 

    for f, subf, filen in os.walk(folder):
        print('Adding files in %s...' % (f))
           # Add the current folder to the ZIP file.
        backupZip.write(f)
           # Add all the files in this folder to the ZIP file.
        for filename in filen:
            if filename.endswith('.mp3'):
                print(filename)
                newBase = os.path.basename(folder) + '_'
                # Remember:  Do not back up the zip files
                if filename.startswith(newBase) and filename.endswith('.zip'):
                    continue   
                backupZip.write(os.path.join(f, filename))
    backupZip.close()    

    print('Done.')

backup('C:\\Test') #Enter the path of the directory which you want to back up



