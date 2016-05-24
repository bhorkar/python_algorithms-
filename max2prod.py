def maxp3(A):
        minval = 0;
        maxval = 0;
        prod2min = 0;
        prod2max = 0;
        prod3max = 0;
        first = 0;
        if len(A)<3:
            return 0;
        if len(A) == 3:
            return A[0]*A[1]*A[2];
        for i in xrange(len(A)):
            val = A[i];
            if(i == 1):
                first = 0;
                minval = val;
                maxval = val;
                continue;
            if (i == 2):
                prod2min = A[0]*A[1];
                prod2max = A[0]*A[1];
            if (i == 3):
                prod3max = A[0]*A[1]*A[2];

                
          
           
            prod3max  = max(prod3max, prod2min*A[i], prod2max*A[i]);
            print (i,minval, maxval,prod2min, prod2max, prod3max);
            prod2min = min(prod2min,A[i]*minval, A[i]*maxval);
            prod2max = max(prod2max,A[i]*minval, A[i]*maxval);
            minval = min(minval,A[i]);
            maxval = max(maxval,A[i]);
        return prod3max


maxp3([1, 3, 5, 2, 8, 0, -1, -3]);
