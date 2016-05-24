
def checkAnagram(str1,str2):
    if len(str1)<len(str2):
            str1, str2 = str2,str1;
    #method 1
    #sorting nlogn
    #method 2
    #hash char 
    hash1 = [0]*256;
    hash2 = [0]*256;
    for i in str2:
        hash2[ord(i)]+=1;
    for i in str1:
        hash1[ord(i)]+=1;

    anagram = 0;
    for i in str2:
        if (hash2[ord(i)] is not  hash1[ord(i)]):
             return False

    return True;


print checkAnagram('dcab','cbm');
