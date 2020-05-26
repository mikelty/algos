def lcs_length(s1, s2):
    """
    O(nm) time
    O(min(n,m)) space
    """
    s1, s2=sorted([s1,s2],key=len)
    l1, l2 = len(s1), len(s2)
    cur, nxt = [0] * (l2 + 1), [0] * (l2 + 1)
    for _,x in enumerate(s1):
        for j,y in enumerate(s2):
            if x==y:
                nxt[j+1]=cur[j]+1
            else:
                nxt[j+1]=max(nxt[j],cur[j+1])
        cur, nxt = nxt, [0] * (l2 + 1)
    return cur[-1]

print(lcs_length('abcde', 'ace'))