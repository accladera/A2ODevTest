class QueenPiece:
    def queensAttack(self, n, k, rq, cq, obstacles):
        if 10 ** 5 >= n < 0 or 10 ** 5 >= k < 0:
            raise ValueError('Invalid value for n or k.')
        if len(obstacles) > 0:
            return self.get_cant_movements(n,rq,cq) - self.get_cant_movements_blocked(n,rq,cq,obstacles)
        return self.get_cant_movements(n,rq,cq)

    def get_cant_movements(self, n, queen_x, queen_y):
        vertical_horizontal = 2 * n - 2
        diagonals = 2 * n - 2 - abs(queen_x - queen_y) - abs(queen_x + queen_y - n - 1)
        return vertical_horizontal + diagonals

    def get_cant_movements_blocked(self, n, queen_y, queen_x, obstacles):
        blockedCells = set()
        for obstacle in obstacles:
            y=obstacle[0]
            x=obstacle[1]
            dir = self.getDirection(queen_x, queen_y, x, y)
            if dir == 'U':
                for i in range(y, n + 1):
                    blockedCells.add((i, x))
            if dir == 'D':
                for i in range(y, 0, -1):
                    blockedCells.add((i, x))
            if dir == 'L':
                for i in range(x, 0, -1):
                    blockedCells.add((y, i))
            if dir == 'R':
                for i in range(x, n + 1):
                    blockedCells.add((y, i))
            if dir == 'UL':
                while y <= n and x > 0:
                    blockedCells.add((y, x))
                    x -= 1
                    y += 1
            if dir == 'UR':
                while y <= n and x <= n:
                    blockedCells.add((y, x))
                    x += 1
                    y += 1
            if dir == 'DR':
                while y > 0 and x <= n:
                    blockedCells.add((y, x))
                    x += 1
                    y -= 1
            if dir == 'DL':
                while y > 0 and x > 0:
                    blockedCells.add((y, x))
                    x -= 1
                    y -= 1
        return len(blockedCells)

    def getDirection(self, queen_x, queen_y, obstacle_x, obstable_y):
        if obstable_y == queen_y and obstacle_x < queen_x:
            return 'L'
        if obstable_y == queen_y and obstacle_x > queen_x:
            return 'R'
        if queen_x == obstacle_x and obstable_y > queen_y:
            return 'U'
        if queen_x == obstacle_x and obstable_y < queen_y:
            return 'D'
        if abs(queen_x - obstacle_x)== abs(queen_x-queen_y):
            if obstable_y > queen_y and obstacle_x < queen_x:
                return 'UL'
            if obstable_y > queen_y and obstacle_x > queen_x:
                return 'UR'
            if obstable_y < queen_y and obstacle_x > queen_x:
                return 'DR'
            if obstable_y < queen_y and obstacle_x < queen_x:
                return 'DL'