# Version 1:
A “working” version updated for v1 of the java. Has only the very basics. It does not guess if it is stuck (this means that when the first guess is a number and doesn’t open up anything, you basically just have to redo it), but when the first guess is relatively open, it seems to get the answer. It also prints out a lot of debug info,  so you have to sift through some of that. 
## REFERENCE:
Tile States:
n#: the number (#)
UNKNOWN: an unknown tile
REVEALED: a tile that is going to be revealed, but has not been updated by the java yet, since the board is not updated after every action. 
FLAG: a flag
TEST: only for testing
ANY: used for tile.findSurrounding() only, to return any tile

class Game:
	Game(board): pass in a set of data and get a game object. The data should be a 3d table representing the size of the board filled with the Tile class. Also has flagsleft, the number of flags left, and play, if it’s playing, and clicks (1.1), the number of “clicks” made during a set of logic

	game.printBoard(): prints the board
	game.revealTile(z,y,x,override=False): reveals the tile at the z y x coord, and (v1.1) will override certain conditions of override is true
NOTE: Everything is done by z then y then x because that’s the order you need to input them into the table, but it is flipped when giving input, since it expects x y z.
	game.flagTile(z,y,x): flags the tile at the z y x coord
	game.onBoard(z,y,x): return True if the tile is on the board, else returns false
	game.checkForData(): runs update board if there is data (1.1)
	game.updateBoard(): updates the board based on the info given by the java
	game.flushOutput(): flushes out an excess print from the java
	game.playing(): returns if the game is still being played
	game.logic(): runs one set of logic on the board
game.clickAll(): Clicks all unknown tiles
game.clickRandom(): Clicks a “random” unknown tile
class Tile:
	Tile(z,y,x,state,game=False): sets the x y z coords and the state, if game is not created yet, that’s okay, just only create unknown tiles. Also has rstate, what it’s real state is without changes, and fstate, what it’s fake state is with adjustments based on the number of flags around it. 
	tile.update(game): updates a tile to what it’s real and fake states should be
	tile.setState(state, game=False): sets the new states, but fstate and rstate
	tile.getRealState(): gets the real state, with some slight (helpful) adjustments
	tile.getFakeState(): gets the real state, with some slight (helpful) adjustments
tile.subtractFlags(game): subtracts the number based on the surrounding flags, you should never need this
tile.findSurrouding(game, check): returns a list of all the tiles surrounding a tile (26 or <) if their state equals the check state. Pass in ANY to get a list of all of them

# Version 1.1: 
Patch Notes:
Updated to v1.3.3 of java
	-noPrint is implemented
	added game.checkForData() which only updates the board if there is data to reads
Implemented random revealing whenever stuck
	Implemented game.clicks
Added a click all function that clicks all unknowns
Added an override to reveal a tile no matter what
Possibly more I forgot, it’s not important enough to keep it perfectly up to date
Things to add:
	Updating to the newer versions when they are working
	Restarting?
	Optimization: Slow on 10x10x10. Specifically, try to run the subset code as little as possible, also, maybe the other logic will speed it up?
	Probably More
	
# Version 1.2:
This is probably the first version where I could say that I could stop here if I wanted. It works almost everytime and rarely guesses (especially on large boards). Of course, there’s always optimizations to make, and I don’t know if the person I’m working with has any other plans for the java side of things. But, if I stopped here, it would be good. Now let’s make it better in 1.3!
Patch Notes:
Added logging for additional information:
	Set the LOGPATH before running, or create a log folder directory in the same place the python is store
It will now ask for a difficulty, but you cannot input exact numbers yet (“easy, medium, hard”)
The last piece of simple logic was added
Optimized the number of times the game checks for a board update
	Removes the printing of WON twice by doing this
You can now select the “custom” difficulty level to set exact numbers for all dimensions 
Cleaned up the code and made it follow conventions more thoroughly. Reference may be off now cause I’m too lazy to get it up to date
Optimized the logic to make it run faster

# Version 1.3:
Patch Notes:
Updated to Version 1.4 of the java
Optimized the efficiency and readability of the logic
If the log directory does not exist, it will instead be saved in the current directory, and tell you what the log directory should look like. 
Things to add:
	Make a latest log for python
	Make the log directory if it doesn’t exist?
	
# Version 2:
Patch Notes:
Updated to Version 2 of the java
	You can now run as many games as you want all at once

After updating to version 2, the project is done! It ran 100 hard games without losing, and only a few took longer than 1 second, and that was just getting unlucky and having to run the random function several times, which takes a lot of time. It’s relatively user friendly too, so feel free to download the java and python and run it, and it should work with no problems. Email me at namesarehard6600@gmail.com if you have any questions.
	
