    # @param A : list of integers
    # @return a list of list of integers
totalSize  = 0;
res = [];
dp = [];
original = [];
def avgset( A):
        SumArray = sum(A);
        global totalSize ;
        global dp
        global original
        global res;
        A = sorted(A);
        original = A;
        totalSum  = sum(A);
        result = [];
        totalSize = len(A);
        
        if(len(A) == 0): 
            return result;
        dp = [[[True for x in range(len(A))] for x in range(totalSum+1)] for x in range(totalSize)];
        for i in xrange(1,totalSize): 
            if((totalSum * i) % totalSize != 0):
                continue;
            sumOfSet1 = (totalSum * i) / totalSize;
            if(isPossible(0, sumOfSet1, i) == True): 
                print (i,sumOfSet1)
                ptr1 = 0;
                ptr2 = 0;
                res1 = res;
                res2 = [];
                
                while(ptr1 < totalSize or ptr2 < len(res)):
                    if(ptr2 < len(res) and res[ptr2] == A[ptr1]): 
                        ptr1+=1;
                        ptr2+=1;
                        continue;
                    
                    res2.append(A[ptr1]);
                    ptr1+=1;
                
                result.append(res1);
                result.append(res2);
                return result;
            
        
        
        
        return result;


def isPossible(index, sum, sz):
        global totalSize ;
        global dp
        global original
        global res;


        if(sz == 0): 
            return sum == 0;
        if(index >= totalSize): 
            return False;
        if(dp[index][sum][sz] == False): 
            return False;
        if(sum >= original[index]): 
            print "here"
            print (index, sum, sz);
            res.append(original[index]);
            if(isPossible(index + 1, sum - original[index], sz - 1) == True): 
                return True;
            res.pop();            
        
        print "herei1"
        print (index, sum, sz);
        if(isPossible(index + 1, sum, sz)): 
            return True;
        print "herei2"
        print (index, sum, sz);
        dp[index][sum][sz] = False;
        return dp[index][sum][sz];
    

print avgset([1, 7, 15, 29, 11, 9]);
