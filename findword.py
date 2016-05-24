class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
   def ladderLength1(self, start, end, dict):
        distance, cur, visited = 0, [start], set([start])
        dict.add(end)
        
        while cur:
            print cur
            next = []
            for word in cur:
                if word == end:
                    return distance + 1
                for i in xrange(len(word)):
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        candidate = word[:i] + j + word[i + 1:]
                        if candidate not in visited and candidate in dict:
                            next.append(candidate)
                            visited.add(candidate)
            distance += 1
            cur = next
        
        return 0
    
   def ladderLength(self, start, end, dictV):
        dictV.add(end)
        q = []
        q.append((start, 1))
        while q:
            curr = q.pop(0)
            currword = curr[0]; currlen = curr[1]
            print curr
            if currword == end: return currlen
            for i in range(len(start)):
                part1 = currword[:i]; part2 = currword[i+1:]
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    if currword[i] != j:
                        nextword = part1 + j + part2
                        if nextword in dictV:
                            q.append((nextword, currlen+1)); 
                            dictV.remove(nextword)
        return 0


if __name__ == "__main__":
    print Solution().ladderLength("hit", "cog", set(["hot","dot","dog","lot","log"]))
