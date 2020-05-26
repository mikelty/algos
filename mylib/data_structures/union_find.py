class UnionFind():
    """
    optimized union find with path compression and better union
    based on algorithms, etc. online book
    """
    def __init__(self,length=0):
        self.length=length
        self.parent=[i for i in range(self.length)]
        self.rank=[0]*length

    def find(self,a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self,a,b):
        a, b = self.find(a), self.find(b)
        if self.rank[a]>self.rank[b]:
            self.parent[b]=a
        else:
            self.parent[a]=b
            if self.rank[a]==self.rank[b]:
                self.rank[b]+=1
