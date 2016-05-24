def convertToBase(stringInput, base):
    stringList = list(stringInput)
    if (base < 2) || (base > 16):
        print "Not supported"
        return;
    #convert to integer
    for i in reversed(xrange(len(stringList))):
        char = stringList[i];



        
