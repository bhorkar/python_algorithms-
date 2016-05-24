def solvemaze(arrayinput,visited,x,y,xmax,ymax):
    if(x == xmax and y == ymax):
        return True;

    if(isvalid(arrayinput, visited,x+1,y,xmax,ymax)):
        return solvemaze(arrayinput,visited,x+1,y,xmax,ymax);
    if(isvalid(arrayinput, visited,x,y+1,xmax,ymax)):
        return solvemaze(arrayinput,visited,x,y+1,xmax,ymax);
    if(isvalid(arrayinput, visited,x+1,y+1,xmax,ymax)):
        return solvemaze(arrayinput,visited,x+1,y+1,xmax,ymax);
      


def isvalid(arrayinput,visited,x,y,xmax,ymax):
    if((x<=xmax and y<=ymax and visited[x][y] !=0) and \
            ((x<xmax and not visited[x+1][y]) or \
            (y<xmax and not visited[x][y+1]) or \
            (x<xmax and y < ymax and not visited[x+1][y+1])):
                return True;
    return False;
           


arrayinput = [[1,0,0],[0,1,0],[0,0,1]];
visited = [[[0]*len(arrayInput)]*len(arrayinput[0])];
solvemaze(arrayinput, visited,0,0,2,2);

