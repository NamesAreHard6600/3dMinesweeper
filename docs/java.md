# Code:
subprosses.Popen([“java”, “-jar”, “Minesweeper3D-v1.4.jar”, “-noPrint”], stdout=subprosses.PIPE, stdin=subprosses.PIPE, stderr=sys.stdout.buffer);
# Arguments:
[x] [y] [z] [numBombs] : Sets the board size, and the number of bombs
<easy|medium|hard> : Sets the board size and number of bombs from defautls 
(easy: 5x5x5 10 bombs, medium 7x7x7 33 bombs, hard 10x10x10 99 bombs)
-noPrint : Does not print the board after each command (v1.1)
--tiles=”0,1,2..." : Sets the tile set (the first 27 are the numbers, then hidden, flagged, bomb) (v1.2)
# Commands:
r,[x],[y],[z] : Reveals the cell (x,y,z)
f,[x],[y],[z] : Flags the cell (x,y,z)
p : Prints the board, and win or death states to stdout
stop : Stops and properly terminates the program
restart : Restarts the game using the same settings (v2)

# Default Board cells:
empty: 0
number: The number
+: Hidden
F: Flag
#: Bomb

These are changeable with the argument --tiles (v1.2)
# Outputs:
ERROR :If something was wrong with the command
WON : If you won
MINE : If you select a mine
Or the new state of the board board
