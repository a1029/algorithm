
class Solution:

    # X
    direction = 0
    def solution(self,n,m,pos,arr):

        d = [[0] * m for _ in range(n)]
        x,y,self.direction = pos[0],pos[1],pos[2]
        dx = [-1,0,1,0]
        dy = [0,1,0,-1]
        d[x][y]=1

        def turn_left():
            self.direction -= 1
            if self.direction == -1:
                self.direction = 3

        count = 1
        turn_time = 0
        while True:
            turn_left()
            nx = x + dx[self.direction]
            ny = y + dy[self.direction]
            if d[nx][ny] == 0 and arr[nx][ny]==0:
                d[nx][ny] = 1
                x = nx
                y = ny
                count += 1
                turn_time = 0
                continue
            else:
                turn_time += 1
            if turn_time==4:
                nx = x - dx[self.direction]
                ny = y - dy[self.direction]
                if arr[nx][ny]==0:
                    x = nx
                    y = ny
                else:
                    break
                turn_time=0

        print(count)

p = Solution()
p.solution(4,4,[1,1,0],[[1,1,1,1],[1,0,0,1],[1,1,0,1],[1,1,1,1]])
p.solution(11,10,[7,4,0],[[1,1,1,1,1,1,1,1,1,1],
                          [1,0,0,0,0,0,0,0,0,1],
                          [1,0,0,0,1,1,1,1,0,1],
                          [1,0,0,1,1,0,0,0,0,1],
                          [1,0,1,1,0,0,0,0,0,1],
                          [1,0,0,0,0,0,0,0,0,1],
                          [1,0,0,0,0,0,0,1,0,1],
                          [1,0,0,0,0,0,1,1,0,1],
                          [1,0,0,0,0,0,1,1,0,1],
                          [1,0,0,0,0,0,0,0,0,1],
                          [1,1,1,1,1,1,1,1,1,1]])