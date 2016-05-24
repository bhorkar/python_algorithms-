

den = [1,2,3,4,5];
sumcoin = 10;

def findNum(den,sumcoin):
    maxcount = [0]*(sumcoin+1);
    maxcount[0] = 1; 
    #DP count[j,c]= count[j-s,c] + count[j,c-1]
    for coin in den:
        for highamount in xrange(coin,sumcoin+1):
            high_amount_rem =  highamount - coin;
            maxcount[highamount] = maxcount[high_amount_rem] + maxcount[highamount] 
   
    return maxcount[sumcoin];


def minNum(den,sumcoin):
    mincount = [0]*(sumcoin+1);
    mincount[0] = 0;
#mincount[j] = 1+min_c(mincount[j-c]), c>=j
    for sumneed in xrange(1,sumcoin+1):
      minsumcoin = 10000;
      for coin in [c for c in den if c <=sumneed]:         
          if(mincount[sumneed-coin] < minsumcoin):
              minsumcoin = mincount[sumneed-coin];
      mincount[sumneed] = 1+minsumcoin;
    return mincount[sumcoin];

print findNum(den,sumcoin)
print minNum(den,sumcoin)
