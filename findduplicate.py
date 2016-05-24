import math
def duplicate(arrayInput,lower,higher):
    if((higher-lower) <= 1):
        return arrayInput[lower];
    checkNumber = lower + int((higher-lower)/2);
    counter = 0;
    for i in arrayInput:
        if(i<=checkNumber and i>=lower):
            counter +=1;
    if(counter == checkNumber):
        return duplicate(arrayInput,checkNumber+1,higher)
    else:
        return duplicate(arrayInput,lower,checkNumber)



if __name__ == "__main__":
    print duplicate([1,4,3,2,5],1,5);
