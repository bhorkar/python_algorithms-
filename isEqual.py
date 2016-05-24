def equal(A):
    hash = {};
    storelist = [];
    for i in xrange(len(A)):
        for j in xrange(len(A)):
            if (i == j):
                continue;
            sumij = A[i]+A[j];           
            if(sumij in hash):                
                key = hash[sumij];
                if( key[0] < i and key[1] < j and (key[1] is not i) and i < j):
                   if(len(storelist) == 0):
                     storelist.append([key[0],key[1],i,j]);
                   else:
                     num = storelist.pop();
                     if(num[0]<key[0]) or \
                      ((num[0]==key[0]) and num[1] < key[1]) or \
                      ((num[0]==key[0]) and num[1] == key[1] and num[2] < i) or \
                      ((num[0]==key[0]) and num[1] == key[1] and num[2] ==  i and num[3] < j): 
                         storelist.append([key[0],key[1],i,j]);
                         storelist.append(num);
                     else:
                         storelist.append(num);
                         storelist.append([key[0],key[1],i,j]);



            else: 
               hash[sumij] = [i,j];
           #    print (sumij,i,j)
    


    print storelist;
if __name__ == "__main__":
    equal([1, 3, 3, 3, 3, 2, 2 ]);
