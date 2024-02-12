def reverse(st):
    l=len(st)
    s=st.lower()
    for i in range(20):
        if s[i]!=s[l-(i+1)]:
            return 'False'
    return st
lst=['Malayalam','Drawing','madamlamadam','1234321']
print(list(filter(lambda y:y!='False',map(reverse,lst))))