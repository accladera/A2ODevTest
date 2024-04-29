
from app.models import ExerciseProcessorStrategy
from app.models.chess import QueenPiece


class ExersiceChess(ExerciseProcessorStrategy):
    def process_exercise(self, input_data):
        n, k, rq, cq, obstacles = self.read_input_data(input_data)
        queen = QueenPiece()
        return queen.queensAttack(n, k, rq, cq, obstacles)

    def read_input_data(self, input_data):
        lines = str(input_data).strip().split("\n")
        if len(lines) < 2:
            raise ValueError('Not enough lines to process')
        for line in lines:
            if not all(char.isdigit() or char.isspace() for char in line):
                raise ValueError('Data must contain only numbers, spaces, or newlines')
            if len(line) == 0 or (' ' not in line):
                raise ValueError('Not enough values to process')
        n, k = lines[0].strip().split(' ')
        rq, cq = lines[1].strip().split(' ')
        n=int(n)
        k=int(k)
        rq=int(rq)
        cq=int(cq)
        obstacles = []
        if k >= 1:
            for line in lines[2:2 + k]:
                obstacle_r, obstacle_c = map(int, line.strip().split(' '))
                obstacles.append((obstacle_r, obstacle_c))
        return n, k, rq, cq, obstacles
