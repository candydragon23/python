from abc import ABC, abstractmethod
class ChessPiece(ABC):
    def __init__(self, horizontal, vertical):
        self.x = horizontal
        self.y = vertical

    @abstractmethod
    def can_move(self, endx, endy):
        pass

class King(ChessPiece):
        def can_move(self, endx, endy):
            if abs(ord(endx) - ord(self.x)) == 1 and abs(endy - self.y) == 1:
                return True
            else:
                return False

