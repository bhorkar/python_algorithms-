
def mergesort(ArrayA, ArrayB):
    iterA = 0;
    iterB = 0;
    ArrayC = [];

    while(iterA < len(ArrayA) and iterB < len(ArrayB)):
        if(ArrayA[iterA] < ArrayB[iterB]):
            ArrayC.append(ArrayA[iterA]);
            iterA +=1;
        else:
            ArrayC.append(ArrayB[iterB]);
            iterB +=1;
    while(iterA < len(ArrayA)):
            ArrayC.append(ArrayA[iterA]);
            iterA +=1;

    while(iterB < len(ArrayB)):
            ArrayC.append(ArrayB[iterB]);
            iterB +=1;
    return ArrayC;

if __name__ == '__main__':
   C = mergesort([3, 4, 6, 10, 11, 15], [1, 5, 8, 12, 14, 19]);
   print C;

