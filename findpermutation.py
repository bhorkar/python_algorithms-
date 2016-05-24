def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]

def recurse(string):
    strlength = len(string);
    if(strlength <=1):
        return set([string]);
    permuted_string_except_1 =  recurse(string[1:]);
    store_string = set();
    print permuted_string_except_1
    for s in permuted_string_except_1:
       for position in range(0,len(s)+1):
         permuted_string = s[0:position] + string[0] + s[position:];
         store_string.add(permuted_string);
    return store_string;



#    print recurse("abc")
   
def permutations(string, step = 0):
#    print "aaa" + str(string);

    # if we've gotten to the end, print the permutation
    if step == len(string):
        print "".join(string)

    # everything to the right of step has not been swapped yet
    for i in range(step, len(string)):

        # copy the string (store as array)
        string_copy = [character for character in string]

        # swap the current index with the step
        print string_copy
        string_copy[step], string_copy[i] = string_copy[i], string_copy[step]
        print string_copy

        # recurse on the portion of the string that has not been swapped yet (now it's index will begin with step + 1)
        permutations(string_copy, step + 1)

        
if __name__ == "__main__":
    A = all_perms("aac");
    for s in A:
        print s;
