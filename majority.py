import random
    # @param A : tuple of integers
    # @return an integer
def majorityElement( a):
        count = 1;
        majority = 0; 
        for i in range(1,len(a)):
             if a[majority] == a[i]:
                 count +=1;
             else:
                 count -=1;
             if count == 0:
                 majority = i;
                 count = 1;
        return a[majority];
print majorityElement([1,2,2])
