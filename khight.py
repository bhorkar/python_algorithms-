def knight(N, M, x1, y1, x2, y2):
	    status, count = knightUtil(N, M, x1, y1, x2, y2,0);
	    if(status == True):
	       return count; 
	    return -1;
def isSafe(x,y,N,M):
	    if(x>=0 and x<N and y >=0 and y < M):
	        return True;
	    return False;
	
def knightUtil( N, M, x, y, x2, y2,count):
	    if(x == x2 and y == y2):
	        return (True, count);
            print (x,y)
	    if(isSafe(x,y,N,M)):
	        count = count + 1;
	        check, ncount = knightUtil(N, M, x+2, y+1, x2, y2,count);
	        if(check == True):
	            return (True,ncount);
	        check, ncount = knightUtil(N, M, x-2, y+1, x2, y2,count);
	        if(check == True):
	            return (True,ncount);
	        check, ncount = knightUtil(N, M, x+2, y-1, x2, y2,count);
	        if(check == True):
	            return (True,ncount);
	        check, ncount = knightUtil(N, M, x-2, y-1, x2, y2,count);
	        if(check == True):
	            return (True,ncount);
	        count = count -1;
	        return (False,count);
	    return False,count;

knight(8,8,1,1,8,8)	    
