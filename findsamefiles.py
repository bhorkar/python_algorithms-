import os
import hashlib

def searchallfiles(baseDir):
    stackdict = ([baseDir]);
    filelist = {};
    while len(stackdict) > 0:
     currentDir = stackdict.pop();
     for file in os.listdir(currentDir):
        filename =  os.path.join(currentDir,file)
        if (os.path.isdir(filename)):
            stackdict.append(file);
        else:
            with open(filename) as f:
             m = hashlib.sha224();
             f.seek(0);
             string = f.read(100);
             m.update(string);            
             hashkey = m.hexdigest();

             #print (string, filename, hashkey);
             #print filename
             if hashkey in filelist:
                 None
                 print (filename, filelist[hashkey]);
             else:
               filelist[hashkey] = filename;





if __name__ == "__main__":
    searchallfiles('.')
