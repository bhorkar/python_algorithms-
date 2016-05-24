
def reverse(stringInput):
    lower = 0;
    string = list(stringInput);
    higher = len(string) -1;
    while (lower < higher):
        string[lower], string[higher] = string[higher], string[lower];
        lower +=1;
        higher -= 1;
    return (string);



if __name__ == "__main__":
    line = ("my name is abhijeet")
    string = reverse(line);
    currIdx = 0;
    startIdx = 0;
    print string
    for char in string:
        if char == ' ' or currIdx == len(string)-1:
            print (startIdx,currIdx)
            print string[startIdx:currIdx]
            string[startIdx:currIdx] = reverse(string[startIdx:currIdx]);
            startIdx = currIdx+1;
        currIdx +=1
        
    print ''.join(string);

           
     
   
