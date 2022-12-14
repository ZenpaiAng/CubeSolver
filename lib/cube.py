from . import consts
from . import funcs
import colorama
import copy

colorama.init()

class Side:
    def __init__(self, base: str) -> None:
        self.state = [base for _ in range(9)]
        
class Sides:
    def __init__(self) -> None:
        self.top = Side("w")
        self.bottom = Side("y")
        self.front = Side("b")
        self.back = Side("g")
        self.right = Side("o")
        self.left = Side("r")
        
class Piece:
    EDGE = 1
    CORNER = 2

class Cube:
    def __init__(self):
        self.sides = Sides()
        self.moveset = consts.MOVESET
        self.moves = []
        
    def get_side(self, obj: object, side: str) -> Side:
        if side in ["top", "bottom", "front", "back", "right", "left"]:
            return getattr(obj, side)
        else:
            raise ValueError("Invalid Side.")
        
    def compile(self, obj: object, location: str):
        ls = location.split(".")
        
        if len(ls) == 2 and ls[0] in ["top", "bottom", "front", "back", "right", "left"] and funcs.intable(ls[1]) and int(ls[1]) in [i for i in range(1, 10)]:
            return self.get_side(obj, ls[0]).state[int(ls[1]) - 1]
        else:
            raise ValueError("Invalid value.")
        
    def run_moves(self, moves: list[str]):
        for move in moves:
            if move in self.moveset:
                new = copy.deepcopy(self.sides)
            
                for key in self.moveset[move]:
                    self.get_side(new, self.moveset[move][key].split(".")[0]).state[int(self.moveset[move][key].split(".")[1]) - 1] = self.compile(self.sides, key)
                
                self.sides = new
                self.moves.append(move)
            else:
                raise ValueError("Invalid Value")
            
        return moves
    
    def verify(self):
        for edge in consts.ALL_EDGES:
            if not self.locate(Piece.EDGE, edge):
                raise ValueError(f"Piece {edge} was not found in cubestate.")
        
        for corner in consts.ALL_CORNERS:
            if not self.locate(Piece.CORNER, corner):
                raise ValueError(f"Piece {corner} was not found in cubestate.")
                    
    def move(self, move: str):
        if move in self.moveset:
            new = copy.deepcopy(self.sides)
            
            for key in self.moveset[move]:
                self.get_side(new, self.moveset[move][key].split(".")[0]).state[int(self.moveset[move][key].split(".")[1]) - 1] = self.compile(self.sides, key)
            
            self.sides = new
            self.moves.append(move)
            
            return move
        else:
            raise ValueError("Invalid value.")
        
    def load(self, state: str):
        if len(state) == 54:
            sides = [state[i:i+9] for i in range(0, len(state), 9)]
            
            self.sides.top.state = [i for i in sides[0]]
            self.sides.left.state = [i for i in sides[1]]
            self.sides.front.state = [i for i in sides[2]]
            self.sides.right.state = [i for i in sides[3]]
            self.sides.back.state = [i for i in sides[4]]
            self.sides.bottom.state = [i for i in sides[5]]
        else:
            raise ValueError(f"State is an invalid length | {len(state)} instead of 54")
        
    def locate(self, type: int, value: list):
        if type == Piece.EDGE:
            locs = consts.Edges.ALL
            
            for loc in locs:
                compiled = [self.compile(self.sides, i) for i in loc]

                if compiled == value:
                    return loc
                elif list(reversed(compiled)) == value:
                    return loc
            else:
                return None
        elif type == Piece.CORNER:
            locs = consts.Corners.ALL
            
            for loc in locs:
                compiled = [self.compile(self.sides, i) for i in loc]
                
                if compiled == value:
                    return loc
            else:
                return None
        else:
            raise ValueError("Invalid piece type.")
        
    def simplify(self):
        moves = "".join(self.moves)
        
        for format in consts.FORMATS:
            moves = moves.replace(format, consts.FORMATS[format])
        
        new = []
        
        for item in [i for i in moves]:
            if item in consts.TICKS:
                new.append(consts.TICKS[item])
            else:
                new.append(item)
            
        self.moves = new
        
    def visualize(self):
        t = self.sides.top.state
        bo = self.sides.bottom.state
        l = self.sides.left.state
        r = self.sides.right.state
        f = self.sides.front.state
        b = self.sides.back.state
        
        def c(r: str):
            f = colorama.Fore
            
            co = ""
            
            if r == "w":
                co = f.LIGHTWHITE_EX
            elif r == "y":
                co = f.YELLOW
            elif r == "r":
                co = f.RED
            elif r == "o":
                co = f.LIGHTRED_EX
            elif r == "b":
                co = f.LIGHTBLUE_EX
            elif r == "g":
                co = f.LIGHTGREEN_EX
                
            return f"{co}{r}{f.RESET}"
        
        print(f"      {c(t[0])} {c(t[1])} {c(t[2])}")
        print(f"      {c(t[3])} {c(t[4])} {c(t[5])}")
        print(f"      {c(t[6])} {c(t[7])} {c(t[8])}")
        print(f"{c(l[0])} {c(l[1])} {c(l[2])} {c(f[0])} {c(f[1])} {c(f[2])} {c(r[0])} {c(r[1])} {c(r[2])} {c(b[0])} {c(b[1])} {c(b[2])}")
        print(f"{c(l[3])} {c(l[4])} {c(l[5])} {c(f[3])} {c(f[4])} {c(f[5])} {c(r[3])} {c(r[4])} {c(r[5])} {c(b[3])} {c(b[4])} {c(b[5])}")
        print(f"{c(l[6])} {c(l[7])} {c(l[8])} {c(f[6])} {c(f[7])} {c(f[8])} {c(r[6])} {c(r[7])} {c(r[8])} {c(b[6])} {c(b[7])} {c(b[8])}")
        print(f"      {c(bo[0])} {c(bo[1])} {c(bo[2])}")
        print(f"      {c(bo[3])} {c(bo[4])} {c(bo[5])}")
        print(f"      {c(bo[6])} {c(bo[7])} {c(bo[8])}")
        print()
        
    def moveify(self, move: str):
        c = colorama.Fore.LIGHTWHITE_EX
        r = colorama.Fore.RESET
        
        if move in consts.MOVES:
            print(f"{c}{consts.MOVES[move]}{r}")
                
    def solved(self) -> bool:
        return self.to_str() == "wwwwwwwwwrrrrrrrrrbbbbbbbbbooooooooogggggggggyyyyyyyyy"
                
    def to_str(self) -> str:
        top = "".join(self.sides.top.state)
        bottom = "".join(self.sides.bottom.state)
        left = "".join(self.sides.left.state)
        right = "".join(self.sides.right.state)
        front = "".join(self.sides.front.state)
        back = "".join(self.sides.back.state)
        return f"{top}{left}{front}{right}{back}{bottom}"

class CubeDemo(Cube):
    def __init__(self):
        super().__init__()
        self.cc = colorama.Fore.LIGHTGREEN_EX
    
    def visualize(self, move):
        t = self.sides.top.state
        bo = self.sides.bottom.state
        l = self.sides.left.state
        r = self.sides.right.state
        f = self.sides.front.state
        b = self.sides.back.state
        
        def c(r: str):
            f = colorama.Fore
            
            co = ""
            
            if r == "w":
                co = f.LIGHTWHITE_EX
            elif r == "y":
                co = f.YELLOW
            elif r == "r":
                co = f.RED
            elif r == "o":
                co = f.LIGHTRED_EX
            elif r == "b":
                co = f.LIGHTBLUE_EX
            elif r == "g":
                co = f.LIGHTGREEN_EX
                
            return f"{co}{r}{f.RESET}"
        
        if self.cc == colorama.Fore.LIGHTGREEN_EX:
            d = colorama.Fore.LIGHTGREEN_EX
            self.cc = colorama.Fore.LIGHTCYAN_EX
        else:
            d = colorama.Fore.LIGHTCYAN_EX
            self.cc = colorama.Fore.LIGHTGREEN_EX
                
        re = colorama.Fore.RESET
        
        cm = consts.MOVES[move]
        
        print(f"      {c(t[0])} {c(t[1])} {c(t[2])}             │ {d}{cm[0]}{re}")
        print(f"      {c(t[3])} {c(t[4])} {c(t[5])}             │ {d}{cm[1]}{re}")
        print(f"      {c(t[6])} {c(t[7])} {c(t[8])}             │ {d}{cm[2]}{re}")
        print(f"{c(l[0])} {c(l[1])} {c(l[2])} {c(f[0])} {c(f[1])} {c(f[2])} {c(r[0])} {c(r[1])} {c(r[2])} {c(b[0])} {c(b[1])} {c(b[2])} │ {d}{cm[3]}{re}")
        print(f"{c(l[3])} {c(l[4])} {c(l[5])} {c(f[3])} {c(f[4])} {c(f[5])} {c(r[3])} {c(r[4])} {c(r[5])} {c(b[3])} {c(b[4])} {c(b[5])} │ {d}{cm[4]}{re}")
        print(f"{c(l[6])} {c(l[7])} {c(l[8])} {c(f[6])} {c(f[7])} {c(f[8])} {c(r[6])} {c(r[7])} {c(r[8])} {c(b[6])} {c(b[7])} {c(b[8])} │ {d}{cm[5]}{re}")
        print(f"      {c(bo[0])} {c(bo[1])} {c(bo[2])}             │ {d}{cm[6]}{re}")
        print(f"      {c(bo[3])} {c(bo[4])} {c(bo[5])}             │ {d}{cm[7]}{re}")
        print(f"      {c(bo[6])} {c(bo[7])} {c(bo[8])}             │ {d}{cm[8]}{re}")
        print()