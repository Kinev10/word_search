import sys

class WordSearch:
    _words = []
    _puzzle = []


    def __init__(self, file=None) -> None:
        if file: self.file_parser(file)
    
    
    def file_parser(self, file_name):
        try:
            with open(file_name) as fp:
                Lines = fp.readlines()
                breaker = Lines.index('\n')
                first_half = Lines[:breaker]
                second_half = Lines[breaker + 1:]
                self._puzzle = [list(line.strip()) for line in first_half]
                self._words = [line.strip() for line in second_half]
        except FileNotFoundError:
            print(f'{file_name} not found.')
            sys.exit(1)

    def puzzle_explorer(self, word):
        ROWS, COLS = len(self._puzzle), len(self._puzzle[0])
        coor = []
        def dfs(r, c, i, d):
            if i == len(word):
                return True
            if (r < 0 or
                c < 0 or
                r >= ROWS or
                c >= COLS or
                    word[i] != self._puzzle[r][c]):
                return False
            coor.append(f'({r + 1}, {c + 1})')
            # traverse
            if d == 0:
                # downward
                return dfs(r + 1, c, i + 1, d)
            elif d == 1:
                # upward
                return dfs(r-1, c, i + 1, d)
            elif d == 2:
                # forward
                return dfs(r, c + 1, i + 1, d)
            else:
                # backward
                return dfs(r, c - 1, i + 1, d)
        
        for r in range(ROWS):
            for c in range(COLS):
                # search to all directions
                for d in range(4):
                    if dfs(r, c, 0, d):
                        return f'{coor[0]}, {coor[-1]}'
        return f'not found'

    @property
    def result(self):
        result = []
        for word in self._words:
            result.append([word, self.puzzle_explorer(word)])
        return result

    def file_outputter(self):
        build = [f'{" ".join(i)}\n' for i in self.result]
        file = open('puzzle1.out', 'w')
        file.writelines((build))
        file.close()

    def screen_outputter(self):
        for word in self.result:
            print(word)

if __name__ == '__main__':
    a = WordSearch(sys.argv[1])
    a.screen_outputter()
    a.file_outputter()