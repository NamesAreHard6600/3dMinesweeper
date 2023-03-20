# Version 1:
A “working” version updated for v1 of the java. Has only the very basics. It does not guess if it is stuck (this means that when the first guess is a number and doesn’t open up anything, you basically just have to redo it), but when the first guess is relatively open, it seems to get the answer. It also prints out a lot of debug info,  so you have to sift through some of that. 
## REFERENCE:
Tile States: 

n#: the number (#) <br>
UNKNOWN: an unknown tile <br>
REVEALED: a tile that is going to be revealed, but has not been updated by the java yet, since the board is not updated after every action. <br>
FLAG: a flag <br>
TEST: only for testing <br>
ANY: used for tile.findSurrounding() only, to return any tile <br>

`class Game:` <br>
`Game(board)`: pass in a set of data and get a game object. The data should be a 3d table representing the size of the board filled with the Tile class. Also has flagsleft, the number of flags left, and play, if it’s playing, and clicks (1.1), the number of “clicks” made during a set of logic

`game.printBoard()`: prints the board <br>
`game.revealTile(z,y,x,override=False)`: reveals the tile at the z y x coord, and (v1.1) will override certain conditions of override is true <br>
 Note: Everything is done by z then y then x because that’s the order you need to input them into the table, but it is flipped when giving input, since it expects x y z. <br> <br>
`game.flagTile(z,y,x)`: flags the tile at the z y x coord <br>
`game.onBoard(z,y,x)`: return True if the tile is on the board, else returns false <br>
`game.checkForData()`: runs update board if there is data (1.1) <br>
`game.updateBoard()`: updates the board based on the info given by the java <br>
`game.flushOutput()`: flushes out an excess print from the java <br>
`game.playing()`: returns if the game is still being played <br>
`game.logic()`: runs one set of logic on the board <br>
`game.clickAll()`: Clicks all unknown tiles <br>
`game.clickRandom()`: Clicks a “random” unknown tile

`class Tile`: <br>
`Tile(z,y,x,state,game=False)`: sets the x y z coords and the state, if game is not created yet, that’s okay, just only create unknown tiles. Also has rstate, what it’s real state is without changes, and fstate, what it’s fake state is with adjustments based on the number of flags around it. <br>
`tile.update(game)`: updates a tile to what it’s real and fake states should be <br>
`tile.setState(state, game=False)`: sets the new states, but fstate and rstate <br>
`tile.getRealState()`: gets the real state, with some slight (helpful) adjustments <br>
`tile.getFakeState()`: gets the real state, with some slight (helpful) adjustments <br>
`tile.subtractFlags(game)`: subtracts the number based on the surrounding flags, you should never need this <br>
`tile.findSurrouding(game, check)`: returns a list of all the tiles surrounding a tile (26 or <) if their state equals the check state. Pass in ANY to get a list of all of them

# Version 1.1: 
Patch Notes: <br>
Updated to v1.3.3 of java <br>
-noPrint is implemented <br>
added game.checkForData() which only updates the board if there is data to reads <br>
Implemented random revealing whenever stuck <br>
Implemented game.clicks <br>
Added a click all function that clicks all unknowns <br>
Added an override to reveal a tile no matter what <br>
Possibly more I forgot, it’s not important enough to keep it perfectly up to date <br>
Things to add: <br>
Updating to the newer versions when they are working <br>
Restarting? <br>
Optimization: Slow on 10x10x10. Specifically, try to run the subset code as little as possible, also, maybe the other logic will speed it up? <br>
Probably More
	
# Version 1.2:
This is probably the first version where I could say that I could stop here if I wanted. It works almost everytime and rarely guesses (especially on large boards). Of course, there’s always optimizations to make, and I don’t know if the person I’m working with has any other plans for the java side of things. But, if I stopped here, it would be good. Now let’s make it better in 1.3! <br>
Patch Notes: <br>
Added logging for additional information: <br>
Set the LOGPATH before running, or create a log folder directory in the same place the python is store <br>
It will now ask for a difficulty, but you cannot input exact numbers yet (“easy, medium, hard”) <br>
The last piece of simple logic was added <br>
Optimized the number of times the game checks for a board update <br>
Removes the printing of WON twice by doing this <br>
You can now select the “custom” difficulty level to set exact numbers for all dimensions <br>
Cleaned up the code and made it follow conventions more thoroughly. Reference may be off now cause I’m too lazy to get it up to date <br>
Optimized the logic to make it run faster<br>

# Version 1.3:
Patch Notes: <br> 
Updated to Version 1.4 of the java <br>
Optimized the efficiency and readability of the logic <br>
If the log directory does not exist, it will instead be saved in the current directory, and tell you what the log directory should look like.  <br>
Things to add: <br>
Make a latest log for python <br>
Make the log directory if it doesn’t exist? <br>
	
# Version 2:
Patch Notes: <br>
Updated to Version 2 of the java <br>
You can now run as many games as you want all at once <br>

After updating to version 2, the project is done! It ran 100 hard games without losing, and only a few took longer than 1 second, and that was just getting unlucky and having to run the random function several times, which takes a lot of time. It’s relatively user friendly too, so feel free to download the java and python and run it, and it should work with no problems. Email me at namesarehard6600@gmail.com if you have any questions.
	
