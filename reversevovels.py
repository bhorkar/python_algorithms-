def reverse_vowels(s):
    if not s:
        return s
    vowels = ['a', 'e', 'i', 'o', 'u']
    a = [c for c in s]
    i = 0
    j = len(a)-1
    while i < j:
        while i < j and a[i] not in vowels:
            i += 1
        while i < j and a[j] not in vowels:
            j -= 1
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return "".join(a)

print reverse_vowels("united states")
