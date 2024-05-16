class Matrix :
    def __init__(self, mat, n, m) :
        self.mat = mat
        self.n = n
        self.m = m
    def checkValidity(self, pos) :
        if pos[0] < 0 or pos[0] >= self.n or pos[1] < 0 or pos[1] >= self.m :
            return False
        return True
    def cost(self, p1, p2) :
        ret = abs(self.mat[p1[0]][p1[1]] - self.mat[p2[0]][p2[1]])
        return ret
    def fromTopLeftToDownRight(self) :
        INF = 10000
        dp = list(self.n*[self.m*[INF]])
        dp = []
        for i in range(self.n) :
            tmp = self.m * [INF]
            dp.append(tmp)
        dp[0][0] = 0
        for i in range (1,self.n) :
            dp[i][0] = dp[i-1][0] + self.cost([i, 0], [i-1, 0])
        for i in range(1, self.m) :
            dp[0][i] = dp[0][i-1] + self.cost([0, i], [0, i-1])
        for i in range(1, self.n) :
            for j in range(1, self.m):
                dp[i][j] = min(dp[i-1][j] + self.cost([i, j], [i-1, j]), dp[i][j-1] + self.cost([i, j], [i, j-1]))
        return dp