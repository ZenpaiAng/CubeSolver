from lib import cube
import os, time

c = cube.Cube()

# White Cross

def white_cross_blue():
    loc = c.locate(cube.Piece.EDGE, ["w", "b"])
    
    dm = cube.funcs.DirectionalMoveset("front")
    
    m = []
    
    if [c.compile(c.sides, "top.8"), c.compile(c.sides, "front.2")] == ["w", "b"]:
        return m
    
    if loc in cube.consts.Edges.BOTTOM:
        if loc in cube.consts.EdgeFaces.FRONT:
            m += c.run_moves([i for i in dm.c("ff")])
        elif loc in cube.consts.EdgeFaces.LEFT:
            m += c.run_moves([i for i in dm.c("dff")])
        elif loc in cube.consts.EdgeFaces.RIGHT:
            m += c.run_moves([i for i in dm.c("dddff")])
        elif loc in cube.consts.EdgeFaces.BACK:
            m += c.run_moves([i for i in dm.c("ddff")])
            
    elif loc in cube.consts.Edges.MIDDLE:
        if loc in cube.consts.EdgeFaces.FRONT:
            if loc in cube.consts.EdgeFaces.RIGHT:
                m += c.run_moves([i for i in dm.c("fff")])
            elif loc in cube.consts.EdgeFaces.LEFT:
                m += c.run_moves([i for i in dm.c("f")])
        elif loc in cube.consts.EdgeFaces.BACK:
            if loc in cube.consts.EdgeFaces.RIGHT:
                m += c.run_moves([i for i in dm.c("bbbddffb")])
            elif loc in cube.consts.EdgeFaces.LEFT:
                m += c.run_moves([i for i in dm.c("bddffbbb")])
    
    elif loc in cube.consts.Edges.TOP:
        if loc in cube.consts.EdgeFaces.FRONT:
            pass # Already in correct position
        elif loc in cube.consts.EdgeFaces.RIGHT:
            m += c.run_moves([i for i in dm.c("rrrfffr")])
        elif loc in cube.consts.EdgeFaces.LEFT:
            m += c.run_moves([i for i in dm.c("lflll")])
        elif loc in cube.consts.EdgeFaces.BACK:
            m += c.run_moves([i for i in dm.c("bbddff")])
                
    if c.compile(c.sides, "top.8") == "b":
        m += c.run_moves([i for i in dm.c("frrrdddrff")])
        
    return m

def white_cross_orange():
    loc = c.locate(cube.Piece.EDGE, ["w", "o"])
    
    dm = cube.funcs.DirectionalMoveset("right")
    
    m = []
    
    if [c.compile(c.sides, "top.6"), c.compile(c.sides, "right.2")] == ["w", "o"]:
        return m
    
    if loc in cube.consts.Edges.BOTTOM:
        if loc in cube.consts.EdgeFaces.RIGHT:
            m += c.run_moves([i for i in dm.c("ff")])
        elif loc in cube.consts.EdgeFaces.FRONT:
            m += c.run_moves([i for i in dm.c("dff")])
        elif loc in cube.consts.EdgeFaces.BACK:
            m += c.run_moves([i for i in dm.c("dddff")])
        elif loc in cube.consts.EdgeFaces.LEFT:
            m += c.run_moves([i for i in dm.c("ddff")])
            
    elif loc in cube.consts.Edges.MIDDLE:
        if loc in cube.consts.EdgeFaces.RIGHT:
            if loc in cube.consts.EdgeFaces.BACK:
                m += c.run_moves([i for i in dm.c("fff")])
            elif loc in cube.consts.EdgeFaces.FRONT:
                m += c.run_moves([i for i in dm.c("f")])
        elif loc in cube.consts.EdgeFaces.LEFT:
            if loc in cube.consts.EdgeFaces.BACK:
                m += c.run_moves([i for i in dm.c("bbbddffb")])
            elif loc in cube.consts.EdgeFaces.FRONT:
                m += c.run_moves([i for i in dm.c("bddffbbb")])
    
    elif loc in cube.consts.Edges.TOP:
        if loc in cube.consts.EdgeFaces.RIGHT:
            pass # Already in correct position
        elif loc in cube.consts.EdgeFaces.BACK:
            m += c.run_moves([i for i in dm.c("rrrfffr")])
        elif loc in cube.consts.EdgeFaces.FRONT:
            m += c.run_moves([i for i in dm.c("lflll")])
        elif loc in cube.consts.EdgeFaces.LEFT:
            m += c.run_moves([i for i in dm.c("bbddff")])
                
    if c.compile(c.sides, "top.6") == "o":
        m += c.run_moves([i for i in dm.c("frrrdddrff")])
        
    return m

def white_cross_red():
    loc = c.locate(cube.Piece.EDGE, ["w", "r"])
    
    dm = cube.funcs.DirectionalMoveset("left")
    
    m = []
    
    if [c.compile(c.sides, "top.4"), c.compile(c.sides, "left.2")] == ["w", "r"]:
        return m
    
    if loc in cube.consts.Edges.BOTTOM:
        if loc in cube.consts.EdgeFaces.LEFT:
            m += c.run_moves([i for i in dm.c("ff")])
        elif loc in cube.consts.EdgeFaces.BACK:
            m += c.run_moves([i for i in dm.c("dff")])
        elif loc in cube.consts.EdgeFaces.FRONT:
            m += c.run_moves([i for i in dm.c("dddff")])
        elif loc in cube.consts.EdgeFaces.RIGHT:
            m += c.run_moves([i for i in dm.c("ddff")])
            
    elif loc in cube.consts.Edges.MIDDLE:
        if loc in cube.consts.EdgeFaces.LEFT:
            if loc in cube.consts.EdgeFaces.FRONT:
                m += c.run_moves([i for i in dm.c("fff")])
            elif loc in cube.consts.EdgeFaces.BACK:
                m += c.run_moves([i for i in dm.c("f")])
        elif loc in cube.consts.EdgeFaces.RIGHT:
            if loc in cube.consts.EdgeFaces.FRONT:
                m += c.run_moves([i for i in dm.c("bbbddffb")])
            elif loc in cube.consts.EdgeFaces.BACK:
                m += c.run_moves([i for i in dm.c("bddffbbb")])
    
    elif loc in cube.consts.Edges.TOP:
        if loc in cube.consts.EdgeFaces.LEFT:
            pass # Already in correct position
        elif loc in cube.consts.EdgeFaces.FRONT:
            m += c.run_moves([i for i in dm.c("rrrfffr")])
        elif loc in cube.consts.EdgeFaces.BACK:
            m += c.run_moves([i for i in dm.c("lflll")])
        elif loc in cube.consts.EdgeFaces.RIGHT:
            m += c.run_moves([i for i in dm.c("bbddff")])
                
    if c.compile(c.sides, "top.4") == "r":
        m += c.run_moves([i for i in dm.c("frrrdddrff")])
        
    return m

def white_cross_green():
    loc = c.locate(cube.Piece.EDGE, ["w", "g"])
    
    dm = cube.funcs.DirectionalMoveset("back")
    
    m = []
    
    if [c.compile(c.sides, "top.2"), c.compile(c.sides, "back.2")] == ["w", "g"]:
        return m
    
    if loc in cube.consts.Edges.BOTTOM:
        if loc in cube.consts.EdgeFaces.BACK:
            m += c.run_moves([i for i in dm.c("ff")])
        elif loc in cube.consts.EdgeFaces.RIGHT:
            m += c.run_moves([i for i in dm.c("dff")])
        elif loc in cube.consts.EdgeFaces.LEFT:
            m += c.run_moves([i for i in dm.c("dddff")])
        elif loc in cube.consts.EdgeFaces.FRONT:
            m += c.run_moves([i for i in dm.c("ddff")])
            
    elif loc in cube.consts.Edges.MIDDLE:
        if loc in cube.consts.EdgeFaces.BACK:
            if loc in cube.consts.EdgeFaces.LEFT:
                m += c.run_moves([i for i in dm.c("fff")])
            elif loc in cube.consts.EdgeFaces.RIGHT:
                m += c.run_moves([i for i in dm.c("f")])
        elif loc in cube.consts.EdgeFaces.FRONT:
            if loc in cube.consts.EdgeFaces.LEFT:
                m += c.run_moves([i for i in dm.c("bbbddffb")])
            elif loc in cube.consts.EdgeFaces.RIGHT:
                m += c.run_moves([i for i in dm.c("bddffbbb")])
    
    elif loc in cube.consts.Edges.TOP:
        if loc in cube.consts.EdgeFaces.BACK:
            pass # Already in correct position
        elif loc in cube.consts.EdgeFaces.LEFT:
            m += c.run_moves([i for i in dm.c("rrrfffr")])
        elif loc in cube.consts.EdgeFaces.RIGHT:
            m += c.run_moves([i for i in dm.c("lflll")])
        elif loc in cube.consts.EdgeFaces.FRONT:
            m += c.run_moves([i for i in dm.c("bbddff")])
                
    if c.compile(c.sides, "top.2") == "g":
        m += c.run_moves([i for i in dm.c("frrrdddrff")])
        
    return m

def blue_orange_corner():
    loc = c.locate(cube.Piece.CORNER, ["w", "b", "o"])
    
    m = []
    
    dm = cube.funcs.DirectionalMoveset("front")
    
    if [c.compile(c.sides, "top.9"), c.compile(c.sides, "front.3"), c.compile(c.sides, "right.1")] == ["w", "b", "o"]:
        return m
    
    if loc in cube.consts.Corners.BOTTOM:
        if loc in cube.consts.CornerFaces.FRONT:
            if loc in cube.consts.CornerFaces.RIGHT:
                pass # Already in correct position
            elif loc in cube.consts.CornerFaces.LEFT:
                m += c.run_moves([i for i in dm.c("d")])
        elif loc in cube.consts.CornerFaces.BACK:
            if loc in cube.consts.CornerFaces.RIGHT:
                m += c.run_moves([i for i in dm.c("ddd")])
            elif loc in cube.consts.CornerFaces.LEFT:
                m += c.run_moves([i for i in dm.c("dd")])
                
    elif loc in cube.consts.Corners.TOP:
        if loc in cube.consts.CornerFaces.FRONT:
            if loc in cube.consts.CornerFaces.RIGHT:
                pass # Already in correct Position
            elif loc in cube.consts.CornerFaces.LEFT:
                m += c.run_moves([i for i in dm.c("fffddfddd")])
        elif loc in cube.consts.CornerFaces.BACK:
            if loc in cube.consts.CornerFaces.RIGHT:
                m += c.run_moves([i for i in dm.c("bbbdddb")])
            elif loc in cube.consts.CornerFaces.LEFT:
                m += c.run_moves([i for i in dm.c("bddbbb")])
        
    e = False
    o = 0
    
    while not e:
        if o > 20:
            raise RecursionError("error: blue_orange_corner surpassed loop limit")
        
        m += c.run_moves([i for i in dm.c("rfffrrrf")])
        
        if [c.compile(c.sides, "top.9"), c.compile(c.sides, "front.3"), c.compile(c.sides, "right.1")] == ["w", "b", "o"]:
            e = True
            
        o += 1
            
    return m

def orange_green_corner():
    loc = c.locate(cube.Piece.CORNER, ["w", "o", "g"])
    
    m = []
    
    dm = cube.funcs.DirectionalMoveset("right")
    
    if [c.compile(c.sides, "top.3"), c.compile(c.sides, "right.3"), c.compile(c.sides, "back.1")] == ["w", "o", "g"]:
        return m
    
    if loc in cube.consts.Corners.BOTTOM:
        if loc in cube.consts.CornerFaces.RIGHT:
            if loc in cube.consts.CornerFaces.BACK:
                pass # Already in correct position
            elif loc in cube.consts.CornerFaces.FRONT:
                m += c.run_moves([i for i in dm.c("d")])
        elif loc in cube.consts.CornerFaces.LEFT:
            if loc in cube.consts.CornerFaces.BACK:
                m += c.run_moves([i for i in dm.c("ddd")])
            elif loc in cube.consts.CornerFaces.FRONT:
                m += c.run_moves([i for i in dm.c("dd")])
                
    elif loc in cube.consts.Corners.TOP:
        if loc in cube.consts.CornerFaces.RIGHT:
            if loc in cube.consts.CornerFaces.BACK:
                pass # Already in correct Position
            elif loc in cube.consts.CornerFaces.FRONT:
                m += c.run_moves([i for i in dm.c("fffddfddd")])
        elif loc in cube.consts.CornerFaces.LEFT:
            if loc in cube.consts.CornerFaces.BACK:
                m += c.run_moves([i for i in dm.c("bbbdddb")])
            elif loc in cube.consts.CornerFaces.FRONT:
                m += c.run_moves([i for i in dm.c("bddbbb")])
        
    e = False
    o = 0
    
    c.visualize()
    
    while not e:
        if o > 20:
            raise RecursionError("error: orange_green_corner surpassed loop limit")
            
        m += c.run_moves([i for i in dm.c("rfffrrrf")])
        
        if [c.compile(c.sides, "top.3"), c.compile(c.sides, "right.3"), c.compile(c.sides, "back.1")] == ["w", "o", "g"]:
            e = True
            
        o += 1
            
    return m

def green_red_corner():
    loc = c.locate(cube.Piece.CORNER, ["w", "g", "r"])
    
    m = []
    
    dm = cube.funcs.DirectionalMoveset("back")
    
    if [c.compile(c.sides, "top.1"), c.compile(c.sides, "back.3"), c.compile(c.sides, "left.1")] == ["w", "g", "r"]:
        return m
    
    if loc in cube.consts.Corners.BOTTOM:
        if loc in cube.consts.CornerFaces.BACK:
            if loc in cube.consts.CornerFaces.LEFT:
                pass # Already in correct position
            elif loc in cube.consts.CornerFaces.RIGHT:
                m += c.run_moves([i for i in dm.c("d")])
        elif loc in cube.consts.CornerFaces.FRONT:
            if loc in cube.consts.CornerFaces.LEFT:
                m += c.run_moves([i for i in dm.c("ddd")])
            elif loc in cube.consts.CornerFaces.RIGHT:
                m += c.run_moves([i for i in dm.c("dd")])
                
    elif loc in cube.consts.Corners.TOP:
        if loc in cube.consts.CornerFaces.BACK:
            if loc in cube.consts.CornerFaces.LEFT:
                pass # Already in correct Position
            elif loc in cube.consts.CornerFaces.RIGHT:
                m += c.run_moves([i for i in dm.c("fffddfddd")])
        elif loc in cube.consts.CornerFaces.FRONT:
            if loc in cube.consts.CornerFaces.LEFT:
                m += c.run_moves([i for i in dm.c("bbbdddb")])
            elif loc in cube.consts.CornerFaces.RIGHT:
                m += c.run_moves([i for i in dm.c("bddbbb")])
        
    e = False
    o = 0
    
    while not e:
        if o > 20:
            raise RecursionError("error: green_red_corner surpassed loop limit")
        
        m += c.run_moves([i for i in dm.c("rfffrrrf")])
        
        if [c.compile(c.sides, "top.1"), c.compile(c.sides, "back.3"), c.compile(c.sides, "left.1")] == ["w", "g", "r"]:
            e = True
            
        o += 1
            
    return m

def red_blue_corner():
    loc = c.locate(cube.Piece.CORNER, ["w", "r", "b"])
    
    m = []
    
    dm = cube.funcs.DirectionalMoveset("left")
    
    if [c.compile(c.sides, "top.7"), c.compile(c.sides, "left.3"), c.compile(c.sides, "front.1")] == ["w", "r", "b"]:
        return m
    
    if loc in cube.consts.Corners.BOTTOM:
        if loc in cube.consts.CornerFaces.LEFT:
            if loc in cube.consts.CornerFaces.FRONT:
                pass # Already in correct position
            elif loc in cube.consts.CornerFaces.BACK:
                m += c.run_moves([i for i in dm.c("d")])
        elif loc in cube.consts.CornerFaces.RIGHT:
            if loc in cube.consts.CornerFaces.FRONT:
                m += c.run_moves([i for i in dm.c("ddd")])
            elif loc in cube.consts.CornerFaces.BACK:
                m += c.run_moves([i for i in dm.c("dd")])
                
    elif loc in cube.consts.Corners.TOP:
        if loc in cube.consts.CornerFaces.LEFT:
            if loc in cube.consts.CornerFaces.FRONT:
                pass # Already in correct Position
            elif loc in cube.consts.CornerFaces.BACK:
                m += c.run_moves([i for i in dm.c("fffddfddd")])
        elif loc in cube.consts.CornerFaces.RIGHT:
            if loc in cube.consts.CornerFaces.FRONT:
                m += c.run_moves([i for i in dm.c("bbbdddb")])
            elif loc in cube.consts.CornerFaces.BACK:
                m += c.run_moves([i for i in dm.c("bddbbb")])
        
    e = False
    o = 0
    
    while not e:
        if o > 20:
            raise RecursionError("error: red_blue_corner surpassed loop limit")
        
        m += c.run_moves([i for i in dm.c("rfffrrrf")])
        
        if [c.compile(c.sides, "top.7"), c.compile(c.sides, "left.3"), c.compile(c.sides, "front.1")] == ["w", "r", "b"]:
            e = True
            
        o += 1
            
    return m

def blue_orange_edge():
    loc = c.locate(cube.Piece.EDGE, ["b", "o"])

    m = []
    
    dm = cube.funcs.DirectionalMoveset("front")
    
    if [c.compile(c.sides, "front.6"), c.compile(c.sides, "right.4")] == ["b", "o"]:
        return m
    
    if loc in cube.consts.Edges.BOTTOM:
        if loc in cube.consts.EdgeFaces.FRONT:
            pass
        elif loc in cube.consts.EdgeFaces.RIGHT:
            m += c.run_moves([i for i in dm.c("ddd")])
        elif loc in cube.consts.EdgeFaces.LEFT:
            m += c.move("d")
        elif loc in cube.consts.EdgeFaces.BACK:
            m += c.run_moves([i for i in dm.c("dd")])
    
    elif loc in cube.consts.Edges.MIDDLE:
        if loc in cube.consts.EdgeFaces.FRONT:
            if loc in cube.consts.EdgeFaces.RIGHT:
                m += c.run_moves([i for i in dm.c("rrrdrfffrfrrrdd")])
            elif loc in cube.consts.EdgeFaces.LEFT:
                m += c.run_moves([i for i in dm.c("fffdflllflfffddd")])
        elif loc in cube.consts.EdgeFaces.BACK:
            if loc in cube.consts.EdgeFaces.RIGHT:
                m += c.run_moves([i for i in dm.c("bbbdbrrrbrbbbd")])
            elif loc in cube.consts.EdgeFaces.LEFT:
                m += c.run_moves([i for i in dm.c("llldlbbblblll")])
    
    if c.compile(c.sides, "front.8") == "b":
        m += c.run_moves([i for i in dm.c("dddrrrdrfffrfrrr")])
    elif c.compile(c.sides, "front.8") == "o":
        m += c.run_moves([i for i in dm.c("ddfdddfffrfffrrrf")])

def orange_green_edge():
    loc = c.locate(cube.Piece.EDGE, ["o", "g"])

    m = []
    
    dm = cube.funcs.DirectionalMoveset("right")
    
    if [c.compile(c.sides, "right.6"), c.compile(c.sides, "back.4")] == ["o", "g"]:
        return m
    
    if loc in cube.consts.Edges.BOTTOM:
        if loc in cube.consts.EdgeFaces.RIGHT:
            pass
        elif loc in cube.consts.EdgeFaces.BACK:
            m += c.run_moves([i for i in dm.c("ddd")])
        elif loc in cube.consts.EdgeFaces.FRONT:
            m += c.move("d")
        elif loc in cube.consts.EdgeFaces.LEFT:
            m += c.run_moves([i for i in dm.c("dd")])
    
    elif loc in cube.consts.Edges.MIDDLE:
        if loc in cube.consts.EdgeFaces.RIGHT:
            if loc in cube.consts.EdgeFaces.BACK:
                m += c.run_moves([i for i in dm.c("rrrdrfffrfrrrdd")])
            elif loc in cube.consts.EdgeFaces.FRONT:
                m += c.run_moves([i for i in dm.c("fffdflllflfffddd")])
        elif loc in cube.consts.EdgeFaces.LEFT:
            if loc in cube.consts.EdgeFaces.BACK:
                m += c.run_moves([i for i in dm.c("bbbdbrrrbrbbbd")])
            elif loc in cube.consts.EdgeFaces.FRONT:
                m += c.run_moves([i for i in dm.c("llldlbbblblll")])
    
    if c.compile(c.sides, "right.8") == "o":
        m += c.run_moves([i for i in dm.c("dddrrrdrfffrfrrr")])
    elif c.compile(c.sides, "right.8") == "g":
        m += c.run_moves([i for i in dm.c("ddfdddfffrfffrrrf")])
        
def green_red_edge():
    loc = c.locate(cube.Piece.EDGE, ["g", "r"])

    m = []
    
    dm = cube.funcs.DirectionalMoveset("back")
    
    if [c.compile(c.sides, "back.6"), c.compile(c.sides, "left.4")] == ["g", "r"]:
        return m
    
    if loc in cube.consts.Edges.BOTTOM:
        if loc in cube.consts.EdgeFaces.BACK:
            pass
        elif loc in cube.consts.EdgeFaces.LEFT:
            m += c.run_moves([i for i in dm.c("ddd")])
        elif loc in cube.consts.EdgeFaces.RIGHT:
            m += c.move("d")
        elif loc in cube.consts.EdgeFaces.FRONT:
            m += c.run_moves([i for i in dm.c("dd")])
    
    elif loc in cube.consts.Edges.MIDDLE:
        if loc in cube.consts.EdgeFaces.BACK:
            if loc in cube.consts.EdgeFaces.LEFT:
                m += c.run_moves([i for i in dm.c("rrrdrfffrfrrrdd")])
            elif loc in cube.consts.EdgeFaces.RIGHT:
                m += c.run_moves([i for i in dm.c("fffdflllflfffddd")])
        elif loc in cube.consts.EdgeFaces.FRONT:
            if loc in cube.consts.EdgeFaces.LEFT:
                m += c.run_moves([i for i in dm.c("bbbdbrrrbrbbbd")])
            elif loc in cube.consts.EdgeFaces.RIGHT:
                m += c.run_moves([i for i in dm.c("llldlbbblblll")])
    
    if c.compile(c.sides, "back.8") == "g":
        m += c.run_moves([i for i in dm.c("dddrrrdrfffrfrrr")])
    elif c.compile(c.sides, "back.8") == "r":
        m += c.run_moves([i for i in dm.c("ddfdddfffrfffrrrf")])
        
def red_blue_edge():
    loc = c.locate(cube.Piece.EDGE, ["r", "b"])

    m = []
    
    dm = cube.funcs.DirectionalMoveset("left")
    
    if [c.compile(c.sides, "left.6"), c.compile(c.sides, "front.4")] == ["r", "b"]:
        return m
    
    if loc in cube.consts.Edges.BOTTOM:
        if loc in cube.consts.EdgeFaces.LEFT:
            pass
        elif loc in cube.consts.EdgeFaces.FRONT:
            m += c.run_moves([i for i in dm.c("ddd")])
        elif loc in cube.consts.EdgeFaces.BACK:
            m += c.move("d")
        elif loc in cube.consts.EdgeFaces.RIGHT:
            m += c.run_moves([i for i in dm.c("dd")])
    
    elif loc in cube.consts.Edges.MIDDLE:
        if loc in cube.consts.EdgeFaces.LEFT:
            if loc in cube.consts.EdgeFaces.FRONT:
                m += c.run_moves([i for i in dm.c("rrrdrfffrfrrrdd")])
            elif loc in cube.consts.EdgeFaces.BACK:
                m += c.run_moves([i for i in dm.c("fffdflllflfffddd")])
        elif loc in cube.consts.EdgeFaces.RIGHT:
            if loc in cube.consts.EdgeFaces.FRONT:
                m += c.run_moves([i for i in dm.c("bbbdbrrrbrbbbd")])
            elif loc in cube.consts.EdgeFaces.BACK:
                m += c.run_moves([i for i in dm.c("llldlbbblblll")])
    
    if c.compile(c.sides, "left.8") == "r":
        m += c.run_moves([i for i in dm.c("dddrrrdrfffrfrrr")])
    elif c.compile(c.sides, "left.8") == "b":
        m += c.run_moves([i for i in dm.c("ddfdddfffrfffrrrf")])
        
def yellow_cross():
    llp = cube.consts.LastLayerPatterns()
    
    m = []
    
    if c.compile(c.sides, "bottom.2") == "y" and \
       c.compile(c.sides, "bottom.4") == "y" and \
       c.compile(c.sides, "bottom.5") == "y" and \
       c.compile(c.sides, "bottom.6") == "y" and \
       c.compile(c.sides, "bottom.8") == "y":
        return m
    
    single = llp.single(c.sides.bottom.state)
    straight = llp.straight(c.sides.bottom.state)
    l_shape = llp.l_shape(c.sides.bottom.state)
    
    if single[0]:
        m += c.run_moves([i for i in "fldllldddfffddfldllldddldllldddfff"])
    elif straight[0]:
        if straight[1][0]:
            m += c.run_moves([i for i in "fldllldddfff"])
        else:
            m += c.run_moves([i for i in f"{straight[1][1]}fldllldddfff"])
    elif l_shape[0]:
        if l_shape[1][0]:
            m += c.run_moves([i for i in "fldllldddldllldddfff"])
        else:
            m += c.run_moves([i for i in f"{l_shape[1][1]}fldllldddldllldddfff"])
            
    return m
            
def yellow_top():
    llp = cube.consts.LastLayerPatterns()
    
    m = []
    
    fish = llp.fish(c.sides.bottom.state)
    nc = llp.no_corners(c.sides.bottom.state)
    tc = llp.two_corners(c.sides.bottom.state)
    
    if fish[0]:
        if fish[1][0]:
            if c.compile(c.sides, "front.7") == "y":
                m += c.run_moves([i for i in "ldllldlddlll"])
            else:
                m += c.run_moves([i for i in "ldllldlddlllddldllldlddlll"])
        else:
            c.run_moves([i for i in fish[1][1]]) # type: ignore
            
            if c.compile(c.sides, "front.7") == "y":
                m += c.run_moves([i for i in "ldllldlddlll"])
            else:
                m += c.run_moves([i for i in "ldllldlddlllddldllldlddlll"])
    elif nc[0]:
        e = False
        
        o = 0
        
        while not e:
            if o > 20:
                raise RecursionError("error: yellow_top surpassed loop limit")
            
            if c.compile(c.sides, "right.7") == "y":
                e = True
            else:
                m += c.move("d")
                
            o += 1
        
        m += c.run_moves([i for i in "ldllldlddlll"])
        
        fsh = llp.fish(c.sides.bottom.state)
        
        if fsh[1][0]:
            if c.compile(c.sides, "front.7") == "y":
                m += c.run_moves([i for i in "ldllldlddlll"])
            else:
                m += c.run_moves([i for i in "ldllldlddlllddldllldlddlll"])
        else:
            c.run_moves([i for i in fsh[1][1]]) # type: ignore
            
            if c.compile(c.sides, "front.7") == "y":
                m += c.run_moves([i for i in "ldllldlddlll"])
            else:
                m += c.run_moves([i for i in "ldllldlddlllddldllldlddlll"])
    elif tc[0]:
        e = False
        o = 0
        
        while not e:
            if o > 20:
                raise RecursionError("error: yellow_top surpassed loop limit")
            
            if c.compile(c.sides, "front.9") == "y":
                e = True
            else:
                m += c.move("d")
        
        m += c.run_moves([i for i in "ldllldlddlll"])
        
        fsh = llp.fish(c.sides.bottom.state)
        
        if fsh[1][0]:
            if c.compile(c.sides, "front.7") == "y":
                m += c.run_moves([i for i in "ldllldlddlll"])
            else:
                m += c.run_moves([i for i in "ldllldlddlllddldllldlddlll"])
        else:
            c.run_moves([i for i in fsh[1][1]]) # type: ignore
            
            if c.compile(c.sides, "front.7") == "y":
                m += c.run_moves([i for i in "ldllldlddlll"])
            else:
                m += c.run_moves([i for i in "ldllldlddlllddldllldlddlll"])
                
    return m

def permute_last_layer():
    llp = cube.consts.LastLayerPatterns()
    
    m = []
    
    headlights = llp.headlights(c.sides)
    
    if len(headlights) == 1:
        e = False
        o = 0
        
        while not e:
            if o > 20:
                raise RecursionError("error: permute_last_layer surpassed loop limit")
            
            if [c.compile(c.sides, "back.7"), c.compile(c.sides, "back.9")] == [headlights[0]["color"], headlights[0]["color"]]:
                e = True
            else:
                m += c.move("d")
                
        m += c.run_moves([i for i in "lllflllbblffflllbbllddd"])
        
        hl = llp.headlights(c.sides)
        
        m += c.run_moves(hl[0]["orient"])
    elif len(headlights) == 0:
        m += c.run_moves([i for i in "lllflllbblffflllbbllddd"])
        
        hl = llp.headlights(c.sides)
        
        e = False
        o = 0
        
        while not e:
            if o > 20:
                raise RecursionError("error: permute_last_layer surpassed loop limit")
            
            c.visualize()
            
            if [c.compile(c.sides, "back.7"), c.compile(c.sides, "back.9")] == [hl[0]["color"], hl[0]["color"]]:
                e = True
            else:
                m += c.move("d")
        
        m += c.run_moves([i for i in "lllflllbblffflllbbllddd"])
        
        hl = llp.headlights(c.sides)
        
        m += c.run_moves(hl[0]["orient"])
        
    c.visualize()
        
    if c.to_str() == "wwwwwwwwwrrrrrrrrrbbbbbbbbbooooooooogggggggggyyyyyyyyy":
        return m # Cube is solved
    
    # Do 4 Headlights
    
    t = llp.headlights(c.sides)
    
    if len(t) >= 1:
        c.run_moves(t[0]["orient"])
    
    hlc = cube.consts.Headlights()
    
    rot = hlc.rotation(c.sides)
    
    if rot[0]:
        dm = cube.funcs.DirectionalMoveset(rot[1]) # type: ignore
        
        o = False
        n = 0
        
        while not o:
            if n > 20:
                raise RecursionError("error: permute_last_layer surpassed loop limit")
            
            if c.solved():
                o = True
            else:
                m += c.run_moves([i for i in dm.c("ffdrlllffrrrldff")])
    else:
        m += c.run_moves([i for i in "ffdrlllffrrrldff"])
        
        rot = hlc.rotation(c.sides)
        
        c.visualize()
        
        dm = cube.funcs.DirectionalMoveset(rot[1]) # type: ignore
        
        o = False
        n = 0
        
        while not o:
            if n > 20:
                raise RecursionError("error: permute_last_layer surpassed loop limit")
            
            if c.solved():
                o = True
            else:
                m += c.run_moves([i for i in dm.c("ffdrlllffrrrldff")])
        
                
    return m
    
#        tttttttttlllllllllfffffffffrrrrrrrrrbbbbbbbbbddddddddd
#        123456789123456789123456789123456789123456789123456789
state = "wobywbbobrgwrroywyrwybbyrgwoyooobgyowggwgbgrrbrogyrgwy"

c.load(state)

c.visualize()

input()

c.verify()

os.system("cls")

demo = cube.CubeDemo()
demo.load(state)
        
white_cross_blue()
white_cross_orange()
white_cross_green()
white_cross_red()

blue_orange_corner()
orange_green_corner()
green_red_corner()
red_blue_corner()

blue_orange_edge()
orange_green_edge()
green_red_edge()
red_blue_edge()

yellow_cross()
yellow_top()

permute_last_layer()

c.simplify()

o = 1

for move in c.moves:
    os.system("cls")
    print(f"Current move: {move}")
    print(f"Move: {o}/{len(c.moves)}")
    
    if move in cube.consts.UNDO_TICK:
        demo.run_moves([i for i in cube.consts.UNDO_TICK[move]])
    else:
        demo.move(move)
        
    demo.visualize(move)
    print()
    
    time.sleep(1.5)
    
    o += 1