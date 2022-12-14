### CubeSolver
A 3x3 Rubik's cube solver

### Usage

1. Clone this repository `git clone https://github.com/ZenpaiAng/CubeSolver.git`
2. Change directory `cd CubeSolver`
3. Run the script `python main.py`

### Format

Accepted chars:

+ `d` (Down)
+ `r` (Right)
+ `f` (Front)
+ `u` (Top)
+ `l` (Left)
+ `b` (Back)

Example string (solved):

`"yyyyyyyyyrrrrrrrrrbbbbbbbbbooooooooogggggggggyyyyyyyyy"`

The cube state is formatted like this (all starting from top left corner):

`[chars 0-8] : White top (blue side facing user), white is upright`  
`[chars 9-17]: Red side (red side facing user), white is upright`  
`[chars 18-26]: Blue side (blue side facing user), white is upright`  
`[chars 27-35]: Orange side (orange side facing user), white is upright`  
`[chars 35-44]: Green side (green side facing user), white is upright`  
`[chars 45-53]: Yellow side (yellow side facing user), blue is upright`  
