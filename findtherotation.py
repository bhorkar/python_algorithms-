def findrotation(array, startIdx, endIdx):
    if (startIdx > endIdx):
        return -1;
    if (startIdx == endIdx):
        return startIdx;
    mid = (endIdx+startIdx)/2;
    if(array[startIdx] > array[mid]):
        return findrotation(array,startIdx,mid);
    else:
        return findrotation(array,mid+1,endIdx);





if __name__ == "__main__":
    x =  findrotation([3,4,5,1,2],0,4)
    print x;
