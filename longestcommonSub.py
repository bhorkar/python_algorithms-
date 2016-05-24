def lcs(string1,string2,m,n):
#edge cases, len  =0
#L(string1[0:m],string[0:m]) = LCS(string1[0:m-1], string1[0:n-1])+1 if str1[m] = str2[n]; 
    if m == 0 or n == 0:
        return 0;
    elif string1[m-1] == string2[n-1]:
        return 1+lcs(string1,string2,m-1,n-1);
    else:
        return max(lcs(string1,string2,m,n-1), lcs(string1,string2,m-1,n));



print lcs('abcd','abd',4,3)
