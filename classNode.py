class Node:
    def __init__(self):
        self.isWall = True
        self.isPartOfPath = False
        self.coordinates = (-1, -1)
    def __init__(self, coords: tuple):
        self.isWall = True
        self.isPartOfPath = False
        self.coordinates = coords
