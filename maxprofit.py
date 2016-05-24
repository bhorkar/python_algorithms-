def maxProfit(prices):
        if (len(prices) <= 1):
            return 0;
        K = 2;  
        maxProf = 0;
        f = [[0 for x in range(len(prices))] for x in range(K+1)]

        for kk in range(1,K+1):
             tmpMax = f[kk-1][0] - prices[0];
             for ii in range(1,len(prices)):
                print ii
                f[kk][ii] = max(f[kk][ii-1], prices[ii] + tmpMax);
                tmpMax = max(tmpMax, f[kk-1][ii] - prices[ii]);
                maxProf = max(f[kk][ii], maxProf);
        
         
        return maxProf;

print maxProfit([1,2])
