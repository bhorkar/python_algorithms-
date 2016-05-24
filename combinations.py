def combination(strlist, length, currIdx):
    if(currIdx == length-1):
        print ''.join(strlist);
    for i in xrange(currIdx,length):
        if(strlist[i] == '?'):
            strlist[i] = '0';
            combination(strlist,length,i+1)
            strlist[i] = '1';
            combination(strlist,length,i+1)

strlist = list('ab?c')
combination(strlist,len(strlist),0);

