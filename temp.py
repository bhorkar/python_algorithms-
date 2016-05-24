def generate(A):
        if A == 1:
            return [1];
     
        outl=[];
        outl.append([1]);
        for n in xrange(2,A+1):
            line = [];
            line.append(1);
            for i in xrange(1,n-1):
                line.append(lineprev[i]+lineprev[i-1]);
            line.append(1);
            outl.append(line);
            lineprev = line;
        return outl;
print generate(1);
