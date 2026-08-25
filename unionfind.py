class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, i):
        # actually finding root of this set
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])

        return self.parent[i]  

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)

        if rootx == rooty:
            return

        self.parent[rooty] = rootx
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)