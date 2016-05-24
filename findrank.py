


import math


def factorialMod(n, modulus):
        ans=1
        if n == 0:
            return 1;
        for i in range(1,n+1):
            ans = ans * i % modulus    
        return ans % modulus

def inverseNumber(num, MOD):
            ans = 1;
            base =  num;
            power = MOD - 2;
            while (power > 0):
                if (power == 1):
                    return (ans * base) % MOD;
                if (power % 2 == 0) :
                    base = (base * base) % MOD;
                    power /= 2;
                else:
                    ans = (ans * base) % MOD;
                    power-=1;
            return ans;
def findRank(A):
         strlen = len(A);
         B = list(sorted(A));
         count = 0;
         for i in xrange(len(A)):
             char  = A[i];
             countrep = {};
             for x in xrange(len(B)):
              if A[x] in countrep:
               countrep[A[x]] +=1;
              else:
                countrep[A[x]] =1;
              div = 1;
             for key in countrep:
                div = div*factorialMod(countrep[key],1000003);
             try:
              idxchar = B.index(char);
             except ValueError:
                 continue;
             fact = (factorialMod(len(A)-i-1,1000003)*inverseNumber(div,1000003))%1000003;
             count = (count + ((idxchar)*fact))%1000003;
             print char
             B = filter(lambda a: a != char, B);

         return count+1;



if __name__ == "__main__":
    print findRank("bac")
