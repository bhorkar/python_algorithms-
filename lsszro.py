store_result = [];
def lszero( A):

    global store_result;
 #   Alcs = lssum(A,0)
#    print store_resultd
    print Method2(A)

def lssum(A,sum):
        global store_result;
        if(len(A) == 0):
            return sum == 0;
        if lssum(A[1:],sum-A[0]):
            store_result.append(A[0])
            return True;
        if lssum(A[1:],sum):

           return True;


def Method2(arr):
        hM = {};
        maxLength  = -1;
        start = -1;
        end = -1;
        sumi = 0;        
        hM[0] = 0;
         
        for i in xrange(len(arr)):
            sumi += arr[i];
            print sumi
          
            if (arr[i] == 0):
                maxLength = max(maxLength,1);
                if(maxLength)==1:
                   start = i;
                   end = i;
            if (sumi in hM):
                print "here"
                print hM
                print (i,sumi,hM[sumi])
                if(maxLength < (i- hM[sumi])):
                    maxLength = i- hM[sumi];
                    start = hM[sumi] + 1;
                    print start
                    if(hM[sumi]==0 and sum(arr[0:i+1]) == 0):
                        start = 0;
                    print "s"
                    print start
                    print (start, i, sum(arr[0:i]));
                    end = i;
            else: 
               hM[sumi] = i;

            print hM
        if(start >=0):
            return arr[start:end+1];

lszero( [ -8, 8, -1, -14, 14, ])



