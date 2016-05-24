
def reserveString(strInput):
   strLength = len(strInput);
   strLi = [];
   strLi.extend(strInput);
   for i in range(0,strLength/2):
       temp = strLi[i];
       strLi[i] = strLi[strLength-i-1];       
       strLi[strLength-i-1] = temp;
   return ''.join(strLi);

def reverseInteger(intInput):




print reserveString("abcde")


