MOVESET = {
    "f": {
        "front.1": "front.3",
        "front.3": "front.9",
        "front.7": "front.1",
        "front.9": "front.7",
        "front.2": "front.6",
        "front.6": "front.8",
        "front.8": "front.4",
        "front.4": "front.2",
        
        "top.7": "right.1",
        "top.8": "right.4",
        "top.9": "right.7",
        
        "right.1": "bottom.3",
        "right.4": "bottom.2",
        "right.7": "bottom.1",
        
        "bottom.1": "left.3",
        "bottom.2": "left.6",
        "bottom.3": "left.9",
        
        "left.9": "top.7",
        "left.6": "top.8",
        "left.3": "top.9"
    },
    
    "r": {
        "right.1": "right.3",
        "right.3": "right.9",
        "right.7": "right.1",
        "right.9": "right.7",
        "right.2": "right.6",
        "right.6": "right.8",
        "right.8": "right.4",
        "right.4": "right.2",
        
        "front.3": "top.3",
        "front.6": "top.6",
        "front.9": "top.9",
        
        "top.3": "back.7",
        "top.6": "back.4",
        "top.9": "back.1",
        
        "back.7": "bottom.3",
        "back.4": "bottom.6",
        "back.1": "bottom.9",
        
        "bottom.3": "front.3",
        "bottom.6": "front.6",
        "bottom.9": "front.9"
    },
    
    "u": {
        "top.1": "top.3",
        "top.3": "top.9",
        "top.7": "top.1",
        "top.9": "top.7",
        "top.2": "top.6",
        "top.6": "top.8",
        "top.8": "top.4",
        "top.4": "top.2",
        
        "front.1": "left.1",
        "front.2": "left.2",
        "front.3": "left.3",
        
        "left.1": "back.1",
        "left.2": "back.2",
        "left.3": "back.3",
        
        "back.1": "right.1",
        "back.2": "right.2",
        "back.3": "right.3",
        
        "right.1": "front.1",
        "right.2": "front.2",
        "right.3": "front.3"
    },
    
    "l": {
        "left.1": "left.3",
        "left.3": "left.9",
        "left.7": "left.1",
        "left.9": "left.7",
        "left.2": "left.6",
        "left.6": "left.8",
        "left.8": "left.4",
        "left.4": "left.2",
        
        "front.1": "bottom.1",
        "front.4": "bottom.4",
        "front.7": "bottom.7",
        
        "bottom.1": "back.9",
        "bottom.4": "back.6",
        "bottom.7": "back.3",
        
        "back.9": "top.1",
        "back.6": "top.4",
        "back.3": "top.7",
        
        "top.1": "front.1",
        "top.4": "front.4",
        "top.7": "front.7"
    },
    
    "b": {
        "back.1": "back.3",
        "back.3": "back.9",
        "back.7": "back.1",
        "back.9": "back.7",
        "back.2": "back.6",
        "back.6": "back.8",
        "back.8": "back.4",
        "back.4": "back.2",
        
        "top.1": "left.7",
        "top.2": "left.4",
        "top.3": "left.1",
        
        "left.7": "bottom.9",
        "left.4": "bottom.8",
        "left.1": "bottom.7",
        
        "bottom.9": "right.3",
        "bottom.8": "right.6",
        "bottom.7": "right.9",
        
        "right.3": "top.1",
        "right.6": "top.2",
        "right.9": "top.3"
    },
    
    "d": {
        "bottom.1": "bottom.3",
        "bottom.3": "bottom.9",
        "bottom.7": "bottom.1",
        "bottom.9": "bottom.7",
        "bottom.2": "bottom.6",
        "bottom.6": "bottom.8",
        "bottom.8": "bottom.4",
        "bottom.4": "bottom.2",
        
        "front.7": "right.7",
        "front.8": "right.8",
        "front.9": "right.9",
        
        "right.7": "back.7",
        "right.8": "back.8",
        "right.9": "back.9",
        
        "back.7": "left.7",
        "back.8": "left.8",
        "back.9": "left.9",
        
        "left.7": "front.7",
        "left.8": "front.8",
        "left.9": "front.9"
    }
}

class Edges:
    TOP = [
        ["top.2", "back.2"],
        ["top.4", "left.2"],
        ["top.6", "right.2"],
        ["top.8", "front.2"],
        ["back.2", "top.2"],
        ["left.2", "top.4"],
        ["right.2", "top.6"],
        ["front.2", "top.8"]
    ]
    
    MIDDLE = [
        ["front.6", "right.4"],
        ["front.4", "left.6"],
        ["back.4", "right.6"],
        ["back.6", "left.4"],
        ["right.4", "front.6"],
        ["left.6", "front.4"],
        ["right.6", "back.4"],
        ["left.4", "back.6"]
    ]
    
    BOTTOM = [
        ["bottom.2", "front.8"],
        ["bottom.4", "left.8"],
        ["bottom.6", "right.8"],
        ["bottom.8", "back.8"],
        ["front.8", "bottom.2"],
        ["left.8", "bottom.4"],
        ["right.8", "bottom.6"],
        ["back.8", "bottom.8"]
    ]
    
    ALL = TOP + MIDDLE + BOTTOM
    
class EdgeFaces:
    FRONT = [
        ["front.2", "top.8"],
        ["front.6", "right.4"],
        ["front.4", "left.6"],
        ["front.8", "bottom.2"],
        ["top.8", "front.2"],
        ["right.4", "front.6"],
        ["left.6", "front.4"],
        ["bottom.2", "front.8"]
    ]
    
    RIGHT = [
        ["right.4", "front.6"],
        ["right.6", "back.4"],
        ["right.4", "front.6"],
        ["right.8", "bottom.6"],
        ["front.6", "right.4"],
        ["back.4", "right.6"],
        ["front.6", "right.4"],
        ["bottom.6", "right.8"]
    ]
    
    LEFT = [
        ["left.2", "top.4"],
        ["left.4", "back.6"],
        ["left.6", "front.4"],
        ["left.8", "bottom.4"],
        ["top.4", "left.2"],
        ["back.6", "left.4"],
        ["front.4", "left.6"],
        ["bottom.4", "left.8"],
    ]
    
    BACK = [
        ["back.2", "top.2"],
        ["back.4", "right.6"],
        ["back.6", "left.4"],
        ["back.8", "bottom.8"],
        ["top.2", "back.2"],
        ["right.6", "back.4"],
        ["left.4", "back.6"],
        ["bottom.8", "back.8"]
    ]
    
class Corners:
    TOP = [
        ["top.1", "left.1", "back.3"],
        ["top.1", "back.3", "left.1"],
        ["left.1", "top.1", "back.3"],
        ["left.1", "back.3", "top.1"],
        ["back.3", "top.1", "left.1"],
        ["back.3", "left.1", "top.1"],
        
        ["top.3", "right.3", "back.1"],
        ["top.3", "back.1", "right.3"],
        ["right.3", "back.1", "top.3"],
        ["right.3", "top.3", "back.1"],
        ["back.1", "top.3", "right.3"],
        ["back.1", "right.3", "top.3"],
        
        ["top.7", "left.3", "front.1"],
        ["top.7", "front.1", "left.3"],
        ["left.3", "front.1", "top.7"],
        ["left.3", "top.7", "front.1"],
        ["front.1", "top.7", "left.3"],
        ["front.1", "left.3", "top.7"],
        
        ["top.9", "front.3", "right.1"],
        ["top.9", "right.1", "front.3"],
        ["front.3", "right.1", "top.9"],
        ["front.3", "top.9", "right.1"],
        ["right.1", "top.9", "front.3"],
        ["right.1", "front.3", "top.9"]
    ]
    
    BOTTOM = [
        ["bottom.1", "front.7", "left.9"],
        ["bottom.1", "left.9", "front.7"],
        ["front.7", "bottom.1", "left.9"],
        ["front.7", "left.9", "bottom.1"],
        ["left.9", "bottom.1", "front.7"],
        ["left.9", "front.7", "bottom.1"],
        
        ["bottom.3", "front.9", "right.7"],
        ["bottom.3", "right.7", "front.9"],
        ["front.9", "bottom.3", "right.7"],
        ["front.9", "right.7", "bottom.3"],
        ["right.7", "bottom.3", "front.9"],
        ["right.7", "front.9", "bottom.3"],
        
        ["bottom.7", "left.7", "back.9"],
        ["bottom.7", "back.9", "left.7"],
        ["left.7", "bottom.7", "back.9"],
        ["left.7", "back.9", "bottom.7"],
        ["back.9", "bottom.7", "left.7"],
        ["back.9", "left.7", "bottom.7"],
        
        ["bottom.9", "right.9", "back.7"],
        ["bottom.9", "back.7", "right.9"],
        ["right.9", "bottom.9", "back.7"],
        ["right.9", "back.7", "bottom.9"],
        ["back.7", "bottom.9", "right.9"],
        ["back.7", "right.9", "bottom.9"]
    ]
    
    ALL = TOP + BOTTOM

class CornerFaces:
    FRONT = [
        ["top.7", "left.3", "front.1"],
        ["top.7", "front.1", "left.3"],
        ["left.3", "front.1", "top.7"],
        ["left.3", "top.7", "front.1"],
        ["front.1", "top.7", "left.3"],
        ["front.1", "left.3", "top.7"],
        
        ["top.9", "front.3", "right.1"],
        ["top.9", "right.1", "front.3"],
        ["front.3", "right.1", "top.9"],
        ["front.3", "top.9", "right.1"],
        ["right.1", "top.9", "front.3"],
        ["right.1", "front.3", "top.9"],
        
        ["bottom.1", "front.7", "left.9"],
        ["bottom.1", "left.9", "front.7"],
        ["front.7", "bottom.1", "left.9"],
        ["front.7", "left.9", "bottom.1"],
        ["left.9", "bottom.1", "front.7"],
        ["left.9", "front.7", "bottom.1"],
        
        ["bottom.3", "front.9", "right.7"],
        ["bottom.3", "right.7", "front.9"],
        ["front.9", "bottom.3", "right.7"],
        ["front.9", "right.7", "bottom.3"],
        ["right.7", "bottom.3", "front.9"],
        ["right.7", "front.9", "bottom.3"]
    ]
    
    RIGHT = [
        ["top.3", "right.3", "back.1"],
        ["top.3", "back.1", "right.3"],
        ["right.3", "back.1", "top.3"],
        ["right.3", "top.3", "back.1"],
        ["back.1", "top.3", "right.3"],
        ["back.1", "right.3", "top.3"],
        
        ["top.9", "front.3", "right.1"],
        ["top.9", "right.1", "front.3"],
        ["front.3", "right.1", "top.9"],
        ["front.3", "top.9", "right.1"],
        ["right.1", "top.9", "front.3"],
        ["right.1", "front.3", "top.9"],
        
        ["bottom.3", "front.9", "right.7"],
        ["bottom.3", "right.7", "front.9"],
        ["front.9", "bottom.3", "right.7"],
        ["front.9", "right.7", "bottom.3"],
        ["right.7", "bottom.3", "front.9"],
        ["right.7", "front.9", "bottom.3"],
        
        ["bottom.9", "right.9", "back.7"],
        ["bottom.9", "back.7", "right.9"],
        ["right.9", "bottom.9", "back.7"],
        ["right.9", "back.7", "bottom.9"],
        ["back.7", "bottom.9", "right.9"],
        ["back.7", "right.9", "bottom.9"]
    ]
    
    LEFT = [
        ["top.1", "left.1", "back.3"],
        ["top.1", "back.3", "left.1"],
        ["left.1", "top.1", "back.3"],
        ["left.1", "back.3", "top.1"],
        ["back.3", "top.1", "left.1"],
        ["back.3", "left.1", "top.1"],
        
        ["top.7", "left.3", "front.1"],
        ["top.7", "front.1", "left.3"],
        ["left.3", "front.1", "top.7"],
        ["left.3", "top.7", "front.1"],
        ["front.1", "top.7", "left.3"],
        ["front.1", "left.3", "top.7"],
        
        ["bottom.1", "front.7", "left.9"],
        ["bottom.1", "left.9", "front.7"],
        ["front.7", "bottom.1", "left.9"],
        ["front.7", "left.9", "bottom.1"],
        ["left.9", "bottom.1", "front.7"],
        ["left.9", "front.7", "bottom.1"],
        
        ["bottom.7", "left.7", "back.9"],
        ["bottom.7", "back.9", "left.7"],
        ["left.7", "bottom.7", "back.9"],
        ["left.7", "back.9", "bottom.7"],
        ["back.9", "bottom.7", "left.7"],
        ["back.9", "left.7", "bottom.7"],
    ]
    
    BACK = [
        ["top.1", "left.1", "back.3"],
        ["top.1", "back.3", "left.1"],
        ["left.1", "top.1", "back.3"],
        ["left.1", "back.3", "top.1"],
        ["back.3", "top.1", "left.1"],
        ["back.3", "left.1", "top.1"],
        
        ["top.3", "right.3", "back.1"],
        ["top.3", "back.1", "right.3"],
        ["right.3", "back.1", "top.3"],
        ["right.3", "top.3", "back.1"],
        ["back.1", "top.3", "right.3"],
        ["back.1", "right.3", "top.3"],
        
        ["bottom.7", "left.7", "back.9"],
        ["bottom.7", "back.9", "left.7"],
        ["left.7", "bottom.7", "back.9"],
        ["left.7", "back.9", "bottom.7"],
        ["back.9", "bottom.7", "left.7"],
        ["back.9", "left.7", "bottom.7"],
        
        ["bottom.9", "right.9", "back.7"],
        ["bottom.9", "back.7", "right.9"],
        ["right.9", "bottom.9", "back.7"],
        ["right.9", "back.7", "bottom.9"],
        ["back.7", "bottom.9", "right.9"],
        ["back.7", "right.9", "bottom.9"]
    ]

class LastLayerPatterns:
    def single(self, layer: list) -> tuple[bool, tuple[bool, str | None]]:
        if layer[1] != "y" and \
           layer[3] != "y" and \
           layer[4] == "y" and \
           layer[5] != "y" and \
           layer[7] != "y":
                
            return True, (True, None)
        else:
            return False, (False, None)
    
    def straight(self, layer: list) -> tuple[bool, tuple[bool, str | None]]:
        if layer[1] == "y" and \
           layer[3] != "y" and \
           layer[4] == "y" and \
           layer[5] != "y" and \
           layer[7] == "y":
                   
            return True, (False, "d")
        elif layer[1] != "y" and \
             layer[3] == "y" and \
             layer[4] == "y" and \
             layer[5] == "y" and \
             layer[7] != "y":
                
            return True, (True, None)
        else:
            return False, (False, None)
        
    def l_shape(self, layer: list) -> tuple[bool, tuple[bool, str | None]]:
        if layer[1] == "y" and \
           layer[3] == "y" and \
           layer[4] == "y" and \
           layer[5] != "y" and \
           layer[7] != "y":
            return True, (False, "dd")
        elif layer[1] == "y" and \
           layer[3] != "y" and \
           layer[4] == "y" and \
           layer[5] == "y" and \
           layer[7] != "y":
            return True, (False, "d")
        elif layer[1] != "y" and \
           layer[3] != "y" and \
           layer[4] == "y" and \
           layer[5] == "y" and \
           layer[7] == "y":
            return True, (True, None)
        elif layer[1] != "y" and \
           layer[3] == "y" and \
           layer[4] == "y" and \
           layer[5] != "y" and \
           layer[7] == "y":
            return True, (False, "ddd")
        else:
            return False, (False, None)
        
    def fish(self, layer: list) -> tuple[bool, tuple[bool, str | None]]:
        # x y x
        # y y y
        # y y x
        
        if layer[0] != "y" and \
           layer[1] == "y" and \
           layer[2] != "y" and \
           layer[3] == "y" and \
           layer[4] == "y" and \
           layer[5] == "y" and \
           layer[6] == "y" and \
           layer[7] == "y" and \
           layer[8] != "y":
            return True, (False, "dd")
        
        # x y x
        # y y y
        # x y y
        
        elif layer[0] != "y" and \
           layer[1] == "y" and \
           layer[2] != "y" and \
           layer[3] == "y" and \
           layer[4] == "y" and \
           layer[5] == "y" and \
           layer[6] != "y" and \
           layer[7] == "y" and \
           layer[8] == "y":
            return True, (False, "ddd")
        
        # x y y
        # y y y
        # x y x
        
        elif layer[0] != "y" and \
           layer[1] == "y" and \
           layer[2] == "y" and \
           layer[3] == "y" and \
           layer[4] == "y" and \
           layer[5] == "y" and \
           layer[6] != "y" and \
           layer[7] == "y" and \
           layer[8] != "y":
            return True, (True, None)
        
        # y y x
        # y y y
        # x y x
        
        elif layer[0] == "y" and \
           layer[1] == "y" and \
           layer[2] != "y" and \
           layer[3] == "y" and \
           layer[4] == "y" and \
           layer[5] == "y" and \
           layer[6] != "y" and \
           layer[7] == "y" and \
           layer[8] != "y":
            return True, (False, "d")
        
        else:
            return False, (False, None)
    
    def no_corners(self, layer: list) -> tuple[bool, tuple[bool, str | None]]:
        if layer[0] != "y" and \
           layer[1] == "y" and \
           layer[2] != "y" and \
           layer[3] == "y" and \
           layer[4] == "y" and \
           layer[5] == "y" and \
           layer[6] != "y" and \
           layer[7] == "y" and \
           layer[8] != "y":
            return True, (True, None)
        else:
            return False, (False, None)
        
    def two_corners(self, layer: list) -> tuple[bool, tuple[bool, str | None]]:
        if layer.count("y") == 7:
            return True, (False, None)
        else:
            return False, (False, None)
        
    def headlights(self, sides) -> list:
        front = sides.front.state
        back = sides.back.state
        right = sides.right.state
        left = sides.left.state
        
        locs = []
        
        pl = {
            "g": "back",
            "b": "front",
            "r": "left",
            "o": "right"
        }
        
        moves = {
            "front-back": "dd",
            "front-right": "d",
            "front-left": "ddd",
            "front-front": "",
            
            "left-front": "ddd",
            "left-back": "d",
            "left-right": "dd",
            "left-left": "",
            
            "back-front": "dd",
            "back-right": "ddd",
            "back-left": "d",
            "back-back": "",
            
            "right-front": "ddd",
            "right-right": "",
            "right-back": "d",
            "right-left": "dd"
        }
        
        valid = [
            "g",
            "b",
            "r",
            "o"
        ]
        
        if front[6] == front[8] and front[6] in valid and front[8] in valid:
            locs.append({"locs": ["front.7", "front.9"], "color": front[6], "orient": [i for i in moves[f"front-{pl[front[6]]}"]]})
            
        if back[6] == back[8] and back[6] in valid and back[8] in valid:
            locs.append({"locs": ["back.7", "back.9"], "color": back[6], "orient": [i for i in moves[f"back-{pl[back[6]]}"]]})
            
        if right[6] == right[8] and back[6] in valid and back[8] in valid:
            locs.append({"locs": ["right.7", "right.9"], "color": right[6], "orient": [i for i in moves[f"right-{pl[right[6]]}"]]})
            
        if left[6] == left[8] and left[6] in valid and left[8] in valid:
            locs.append({"locs": ["left.7", "left.9"], "color": left[6], "orient": [i for i in moves[f"left-{pl[left[6]]}"]]})
            
        return locs

class Headlights:
    def rotation(self, sides):
        front = sides.front.state
        back = sides.back.state
        right = sides.right.state
        left = sides.left.state
        
        fc = front.count("b")
        bc = back.count("g")
        rc = right.count("o")
        lc = left.count("r")
        
        count = fc + bc + rc + lc
        
        pl = {
            "g": "front",
            "b": "back",
            "r": "right",
            "o": "left"
        }
        
        if fc == 9:
            e = "b"
        elif bc == 9:
            e = "g"
        elif rc == 9:
            e = "o"
        elif lc == 9:
            e = "r"
        
        if count == 33:
            return True, (pl[e]) # type: ignore
        else:
            return False, None
        
    def no_full_face(self, sides):
        front = sides.front.state
        back = sides.back.state
        right = sides.right.state
        left = sides.left.state
        
        count = front.count("b") + back.count("g") + right.count("o") + left.count("r")
        
        if count == 32:
            return True, ()
        else:
            return False, (None)
        
TICKS = {
    "F": "f'",
    "R": "r'",
    "D": "d'",
    "L": "l'",
    "U": "u'",
    "B": "b'"
}

FORMATS = {
    "ffff": "",
    "rrrr": "",
    "dddd": "",
    "llll": "",
    "uuuu": "",
    "bbbb": "",
    
    "fff": "F",
    "rrr": "R",
    "ddd": "D",
    "lll": "L",
    "uuu": "U",
    "bbb": "B"
}

UNDO_TICK = {
    "f'": "fff",
    "r'": "rrr",
    "d'": "ddd",
    "l'": "lll",
    "u'": "uuu",
    "b'": "bbb"
}

ALL_EDGES = [
    ["w", "b"],
    ["w", "o"],
    ["w", "g"],
    ["w", "r"],
    
    ["y", "b"],
    ["y", "o"],
    ["y", "g"],
    ["y", "r"],
    
    ["b", "o"],
    ["o", "g"],
    ["g", "r"],
    ["r", "b"]
]

ALL_CORNERS = [
    ["w", "b", "o"],
    ["w", "o", "g"],
    ["w", "g", "r"],
    ["w", "r", "b"],
    
    ["y", "b", "o"],
    ["y", "o", "g"],
    ["y", "g", "r"],
    ["y", "r", "b"],
]

F_MOVE = """



      ▢ ▢ ▢ ┌───┐
      ▢ ▢ ▢ │ f ↓
      ▢ ▢ ▢ └─── 



"""

R_MOVE = """



      ▢ ▢ ▢
      ▢ ▢ ▢
      ▢ ▢ ▢
          ^
          |
          |
"""

U_MOVE = """



      ▢ ▢ ▢ <----
      ▢ ▢ ▢
      ▢ ▢ ▢



"""

L_MOVE = """
      |
      |
      ↓
      ▢ ▢ ▢
      ▢ ▢ ▢
      ▢ ▢ ▢



"""

B_MOVE = """



      ▢ ▢ ▢ ┌───┐
      ▢ ▢ ▢ ↓ b │
      ▢ ▢ ▢  ───┘



"""

D_MOVE = """



      ▢ ▢ ▢
      ▢ ▢ ▢
----> ▢ ▢ ▢



"""

FD_MOVE = """



      ▢ ▢ ▢ ┌───┐
      ▢ ▢ ▢ ↓ f'│
      ▢ ▢ ▢  ───┘



"""

RD_MOVE = """
          |
          |
          ↓
      ▢ ▢ ▢
      ▢ ▢ ▢
      ▢ ▢ ▢



"""

UD_MOVE = """



----> ▢ ▢ ▢
      ▢ ▢ ▢
      ▢ ▢ ▢



"""

LD_MOVE = """



      ▢ ▢ ▢
      ▢ ▢ ▢
      ▢ ▢ ▢
      ^
      |
      |
"""

BD_MOVE = """



      ▢ ▢ ▢ ┌───┐
      ▢ ▢ ▢ │ b'↓
      ▢ ▢ ▢ └─── 



"""

DD_MOVE = """



      ▢ ▢ ▢
      ▢ ▢ ▢      
      ▢ ▢ ▢ <----
      
      
      
"""

MOVES = {
    "f": F_MOVE.splitlines(keepends=False),
    "r": R_MOVE.splitlines(keepends=False),
    "u": U_MOVE.splitlines(keepends=False),
    "l": L_MOVE.splitlines(keepends=False),
    "b": B_MOVE.splitlines(keepends=False),
    "d": D_MOVE.splitlines(keepends=False),
    
    "f'": FD_MOVE.splitlines(keepends=False),
    "r'": RD_MOVE.splitlines(keepends=False),
    "u'": UD_MOVE.splitlines(keepends=False),
    "l'": LD_MOVE.splitlines(keepends=False),
    "b'": BD_MOVE.splitlines(keepends=False),
    "d'": DD_MOVE.splitlines(keepends=False),
}