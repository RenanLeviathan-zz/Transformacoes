class Matrix:
    def __init__(self,n,m):
        self._mt=[]
        self._mt=[[0 for _ in range(m)] for _ in range(n)]
        self._dim=(n, m)

    def getdim(self):
        return self._dim

    def get_el(self,i,j):
        return self._mt[i][j]

    def set_el(self,i,j,v):
        self._mt[i][j]=v

    #soma de matrizes
    def __add__(self, m2):
        res=Matrix(m2.getdim()[0],m2.getdim()[1])
        for i in range(len(res.getdim()[0])):
            for j in range(len(res.getdim()[1])):
                res.set_el(i,j,self.get_el(i,j)+m2.get_el(i,j))
        return res