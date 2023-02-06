class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle
        self.history = []   

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.history.append([row1, row2, col1, col2, newValue])

    def getValue(self, row: int, col: int) -> int:
        for h in reversed(self.history):
            if h[0] <= row <= h[1] and h[2] <= col <= h[3]:
                return h[4]
        return self.rectangle[row][col]