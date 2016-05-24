class Binarytree:
    def __init__(self,val):
        self.left = None;
        self.right = None;
        self.val = val;
    def __addLeft__(self,val):
        self.left = Binarytree(val);
        return self.left;



def checkIsSubTreeUtil(tree1, tree2):
    if tree1 == None:
        return Null;
    if tree2 == None:
        return True;
    if (checkIdentical (tree1,tree2)):
        return True;
    return (checkIsSubftee(tree1.left, tree2) or \ 
    checkIsSubftee(tree1.right, tree2)) 
def checkIdentical(tree1,tree2) :
    if tree1 == None and tree2 == None:
        return True;
    if tree1 == None or tree2 == None:
        return False;
    return tree1.val == tree2.val and checkIdentical(tree1.left,tree2.left) and checkIdentical(tree1.left,tree2.left)



