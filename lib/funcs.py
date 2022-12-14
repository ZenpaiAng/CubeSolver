def intable(inp) -> bool:
    try:
        e = int(inp)
        return True
    except:
        return False

class DirectionalMoveset:
    def __init__(self, side: str):
        if side not in ["front", "right", "left", "back", "bottom"]:
            raise ValueError(f"Invalid Side. {side}")
             
        self.front = {"f": "f", "r": "r", "u": "u", "l": "l", "b": "b", "d": "d"}
        self.right = {"f": "r", "r": "b", "u": "u", "l": "f", "b": "l", "d": "d"}
        self.left = {"f": "l", "r": "f", "u": "u", "l": "b", "b": "r", "d": "d"}
        self.back = {"f": "b", "r": "l", "u": "u", "l": "r", "b": "f", "d": "d"}
        self.bottom = {"u": "d", "d": "u", "r": "l", "l": "r", "b": "b", "f": "f"}
        
        self.moveset = getattr(self, side)
        
    def c(self, inp: str):
        r = ""
        
        for c in inp:
            r += self.moveset[c]
            
        return r