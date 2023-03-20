# Code:
    subprosses.Popen([“java”, “-jar”, “Minesweeper3D-v1.4.jar”, “-noPrint”], stdout=subprosses.PIPE, stdin=subprosses.PIPE, stderr=sys.stdout.buffer);
# Arguments:
`[x] [y] [z] [numBombs]`: Sets the board size, and the number of bombs <br>
`<easy|medium|hard>` : Sets the board size and number of bombs from defautls <br>
&nbsp;&nbsp;&nbsp;&nbsp;(easy: 5x5x5 10 bombs, medium 7x7x7 33 bombs, hard 10x10x10 99 bombs) <br>
`-noPrint` : Does not print the board after each command (v1.1) <br>
`--tiles=”0,1,2..."` : Sets the tile set (the first 27 are the numbers, then hidden, flagged, bomb) (v1.2) <br>
# Commands:
`r,[x],[y],[z]` : Reveals the cell (x,y,z) <br>
`f,[x],[y],[z]` : Flags the cell (x,y,z) <br>
`p` : Prints the board, and win or death states to stdout <br>
`stop` : Stops and properly terminates the program <br>
`restart` : Restarts the game using the same settings (v2) <br>

# Default Board cells:
empty: 0 <br>
number: The number <br>
+: Hidden <br>
F: Flag <br>
#: Bomb <br>

These are changeable with the argument --tiles (v1.2)
# Outputs:
`ERROR` :If something was wrong with the command <br>
`WON` : If you won <br>
`MINE` : If you select a mine <br>
