import subprocess
import sys
import logging
from datetime import datetime
import time
import os

# Commands
# r,x,y,z
# f,x,y,z
# p
# stop
# restart

    

# Constants
LOGPATH = 'logs\\python\\'
# Game States  Note: Balancing between string numbers and integer numbers is not easy
# sorry if there is some weird casting that's excessive
if True:
  UNKNOWN = "+"
  REVEALED = "R"
  FLAG = "F"
  TEST = "T"
  MINE = "#"
  n0 = 0
  n1 = 1
  n2 = 2
  n3 = 3
  n4 = 4
  n5 = 5
  n6 = 6
  n7 = 7
  n8 = 8
  n9 = 9
  n10 = 10
  n11 = 11
  n12 = 12
  n13 = 13
  n14 = 14
  n15 = 15
  n16 = 16
  n17 = 17
  n18 = 18
  n19 = 19
  n20 = 20
  n21 = 21
  n22 = 22
  n23 = 23
  n24 = 24
  n25 = 25
  n26 = 26
  n27 = 27
  ANY = "A"


def getFirstData():
    data = [[]]
    p.stdin.write("p\n")
    p.stdin.flush()
    for i in range((HEIGHT + 1) * LENGTH - 1):
      # print(data)
      curr = p.stdout.readline().rstrip()
      if curr != "":
        data[-1].append(curr.split(","))
      else:
        data.append([])

    for z in range(len(data)):
      for y in range(len(data[z])):
        for x in range(len(data[z][y])):
          data[z][y][x] = Tile(z, y, x, data[z][y][x])
    return data


def configLogger():
  date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
  if os.path.isdir(LOGPATH):
    print(LOGPATH)
    logging.basicConfig(filename=f"{LOGPATH}python_{date}.log".replace(":", "-"), format='%(asctime)s %(message)s',
                        filemode='w')
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
  else:
    err_string = f"ERROR: Log path directory:\n" \
                 f"{os.getcwd()}\\{LOGPATH}\n" \
                 f"does not exist. Saving log file in current directory."
    print(err_string)
    time.sleep(3)
    logging.basicConfig(filename=f"python_{date}.log".replace(":", "-"), format='%(asctime)s %(message)s',
                        filemode='w')
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.error(err_string)
  return logger


def LOG(data):
  global logger
  logger.debug(data)


class Game:
  def __init__(self, board):
    global HEIGHT, WIDTH, LENGTH
    self.board = board  # [z][y][x]
    self.flagsleft = TOTALFLAGS  # Unknown
    self.play = True
    self.clicks = 0
    self.height = HEIGHT
    self.width = WIDTH
    self.length = LENGTH

  def printBoard(self):
    for i in range(self.height):
      for j in range(self.length):
        for k in range(self.width):
          curr = self.board[i][j][k].getRealState()
          if len(str(curr)) > 1:
            print(curr, end=",")
          else:
            print(" " + str(curr), end=",")
        print()
      print()
    print()

  def revealTile(self, z, y, x, override=False):
    # print(self.board[z][y][x])
    if self.playing() and self.board[z][y][x].getRealState() == UNKNOWN or override:
      LOG("REVEALING " + str(z) + " " + str(y) + " " + str(x))
      self.clicks += 1
      p.stdin.write("r," + str(x) + "," + str(y) + "," + str(z) + "\n")
      p.stdin.flush()
      curr = self.board[z][y][x]
      curr.setState(REVEALED, self)
      # self.checkForData()
      # self.flushOutput()

  def flagTile(self, z, y, x):
    # print(self.board[z][y][x])
    if self.playing() and self.board[z][y][x].getRealState() == UNKNOWN:
      LOG("FLAGGING " + str(z) + " " + str(y) + " " + str(x))
      self.clicks += 1
      self.flagsleft -= 1
      curr = self.board[z][y][x]
      curr.setState(FLAG, self)
      '''
            p.stdin.write("f,"+str(x)+","+str(y)+","+str(z)+"\n")
            p.stdin.flush()
            self.checkForData()
            '''
      # self.flushOutput()

  def checkForData(self):
    p.stdin.write("p\n")
    p.stdin.flush()
    self.updateBoard()

  def onBoard(self, z, y, x):
    if x < 0 or y < 0 or z < 0 or x >= self.width or y >= self.length or z >= self.height:
      return False
    return True

  def updateBoard(self):
    global p
    data = [[]]
    for _ in range((self.height + 1) * self.length - 1):
      curr = p.stdout.readline().rstrip()
      if curr.find("ERROR") != -1 or curr.find("WON") != -1 or curr.find("MINE") != -1:
        self.play = False
        print(curr)
        LOG(curr)
        if curr.find("WON") != -1 or curr.find("MINE") != -1:
          self.updateBoard()
        return
      elif curr != "":
        data[-1].append(curr.split(","))
      else:
        data.append([])
    for z in range(len(data)):
      for y in range(len(data[z])):
        for x in range(len(data[z][y])):
          self.board[z][y][x].setState(data[z][y][x], self)

  def flushOutput(self):
    global p
    for _ in range((self.height + 1) * self.length - 1):
      curr = p.stdout.readline().rstrip()
      if curr.find("ERROR") != -1 or curr.find("WON") != -1 or curr.find("MINE") != -1:
        self.play = False
        print(curr)
        return

  def playing(self):
    return self.play and self.flagsleft > 0

  def logic(self):
    self.clicks = 0
    for z in range(self.height):
      for y in range(self.length):
        for x in range(self.width):
          curr = self.board[z][y][x]
          curr_state = curr.getRealState()
          if curr_state == UNKNOWN or curr_state == FLAG or curr_state == REVEALED:
            continue
          elif self.playing():
            # Simple Logic
            unknowns = curr.findSurrounding(self, UNKNOWN)
            curr.update(self)
            # print(curr.getFakeState(),flags,unknowns)
            if curr.getFakeState() == n0:
              for tile in unknowns:
                self.revealTile(tile[0], tile[1], tile[2])
              continue
            if len(unknowns) == curr.getFakeState():
              for tile in unknowns:
                self.flagTile(tile[0], tile[1], tile[2])
              continue

            # Subset Logic: This might be really slow

            numbers = curr.findSurrounding(self, ANY)
            for tile in numbers:
              o_curr = self.board[tile[0]][tile[1]][tile[2]]
              if type(o_curr.getFakeState()) != int:
                continue
              curr.update(self)
              o_curr.update(self)
              # If there is the same number of bombs left around two tiles and the open tiles have the same subset of
              # tiles except one is larger, then all the tiles in the larger subset not in the smaller subset can be
              # clicked
              if o_curr.getFakeState() == curr.getFakeState() != n0:
                o_unknowns = o_curr.findSurrounding(self, UNKNOWN)
                if len(o_unknowns) > 0 and len(unknowns) > 0:
                  if set(o_unknowns).issubset(set(unknowns)):
                    for i in [x for x in unknowns if x not in o_unknowns]:
                      self.revealTile(i[0], i[1], i[2])
                  elif set(unknowns).issubset(set(o_unknowns)):
                    for i in [x for x in o_unknowns if x not in unknowns]:
                      self.revealTile(i[0], i[1], i[2])
              # If there is a different number of bombs around two tiles and the difference in the subsets of tiles is
              # equal to the difference of the two numbers, then all the tiles in the larger subset not in the
              # smaller subset are bombs
              elif type(o_curr.getFakeState()) == int and o_curr.getFakeState() != n0:
                o_unknowns = o_curr.findSurrounding(self, UNKNOWN)
                difference = abs(len(o_unknowns) - len(unknowns))
                difference2 = abs(curr.getFakeState() - o_curr.getFakeState())
                if difference == difference2:
                  if set(o_unknowns).issubset(set(unknowns)):
                    for i in [x for x in unknowns if x not in o_unknowns]:
                      self.flagTile(i[0], i[1], i[2])
                  elif set(unknowns).issubset(set(o_unknowns)):
                    for i in [x for x in o_unknowns if x not in unknowns]:
                      self.flagTile(i[0], i[1], i[2])

    # Click all unrevelaed tiles if I have all the flags
    if self.flagsleft == 0:
      self.clickAll()
    # Click Randomly if no moves were made
    if self.clicks == 0:
      self.clickRandom()

  def clickAll(self):
    LOG("CLICKING ALL")
    for z in range(self.height):
      for y in range(self.length):
        for x in range(self.width):
          curr = self.board[z][y][x]
          if curr.getRealState() == UNKNOWN:
            self.revealTile(z, y, x, True)

  def clickRandom(self):
    for z in range(self.height):
      for y in range(self.length):
        for x in range(self.width):
          curr = self.board[z][y][x]
          if curr.getRealState() == UNKNOWN:
            LOG("RANDOM " + str(z) + " " + str(y) + " " + str(x))
            self.revealTile(z, y, x)
            return


class Tile:
  def __init__(self, z, y, x, state, game=False):
    self.x = x
    self.y = y
    self.z = z
    self.rstate = UNKNOWN
    self.fstate = UNKNOWN
    self.setState(state, game)

  def update(self, game):
    self.setState(self.getRealState(), game)

  def setState(self, state, game=None):
    if self.rstate == FLAG and state != MINE:
      return
    self.rstate = state
    self.fstate = state
    self.rstate = self.getRealState()
    self.fstate = self.getFakeState()
    if self.rstate == " " or self.rstate == "":
      self.rstate = n0
      self.fstate = n0
    if type(self.fstate) == int:
      self.subtractFlags(game)

  def getRealState(self):
    if str(self.rstate).isnumeric():
      return int(self.rstate)
    else:
      return self.rstate

  def getFakeState(self):
    if str(self.fstate).isnumeric():
      return int(self.fstate)
    else:
      return self.fstate

  def subtractFlags(self, game):
    flags = self.findSurrounding(game, FLAG)
    self.fstate -= len(flags)

  def findSurrounding(self, game, check):
    surrounding = []
    for x in range(-1, 2):
      for y in range(-1, 2):
        for z in range(-1, 2):
          currz = self.z + z
          curry = self.y + y
          currx = self.x + x
          if game.onBoard(currz, curry, currx) and (
                  game.board[currz][curry][currx].getRealState() == check or check == ANY):
            surrounding.append((currz, curry, currx))
    return surrounding

# RUNNER CODE
# One time:
# Difficulites
commandTable = ["java", "-jar", "Minesweeper3D-v2.jar"]
print('"easy" - "medium" - "hard" - "custom"')
difficulty = input().strip()
if difficulty == "easy":
  WIDTH = 5  # The X cordinate
  LENGTH = 5  # The Y cordinate
  HEIGHT = 5  # The Z cordinate
  TOTALFLAGS = 10
  commandTable.append("easy")
elif difficulty == "medium":
  WIDTH = 7  # The X cordinate
  LENGTH = 7  # The Y cordinate
  HEIGHT = 7  # The Z cordinate
  commandTable.append("medium")
  TOTALFLAGS = 33
elif difficulty == "hard":
  WIDTH = 10  # The X cordinate
  LENGTH = 10  # The Y cordinate
  HEIGHT = 10  # The Z cordinate
  TOTALFLAGS = 99
  commandTable.append("hard")
elif difficulty == "custom":
  print("Width (x) of the board: ")
  WIDTH = int(input().strip())
  print("Width (y) of the board: ")
  LENGTH = int(input().strip())
  print("Width (z) of the board: ")
  HEIGHT = int(input().strip())
  print("Total bombs: ")
  TOTALFLAGS = int(input().strip())
  commandTable.append(str(WIDTH))
  commandTable.append(str(LENGTH))
  commandTable.append(str(HEIGHT))
  commandTable.append(str(TOTALFLAGS))
else:
  WIDTH = 4  # The X cordinate
  LENGTH = 4  # The Y cordinate
  HEIGHT = 4  # The Z cordinate
  TOTALFLAGS = 4
print("How many games do you want to solve? (int)")
iterations = int(input().strip())
commandTable.append("-noPrint")

# Open subprocess
print("Running...")
p = subprocess.Popen(commandTable, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=sys.stdout.buffer,
                     encoding="UTF-8")
#Log Starting info
logger = configLogger()
LOG(difficulty.capitalize())
LOG(commandTable)
#Iterations
for i in range(iterations):
    data = getFirstData()
    # print("Data Received...") # IF YOU WANT EXTRA DATA UNCOMMENT THIS LINE
    
    #Create Game
    game = Game(data)
    print(f'Starting game {i+1}.')
    LOG(f'Starting game {i+1}.')
    startTime = time.time_ns()
    

    # Start reveal
    game.revealTile(0, 0, 0)
    game.checkForData()
    count = 1
    
    while game.playing():  # loop logic
      game.logic()
      LOG("Completed logic set " + str(count))
      # print("Completed logic set " + str(count) + "...") # IF YOU WANT EXTRA DATA UNCOMMENT THIS LINE
      count += 1
      game.checkForData()
    
    #Finish and restart
    LOG("Game " + str(i+1) + " finished. Time Taken (msec): " + str((time.time_ns() - startTime) / 1000000))
    game.printBoard()
    p.stdin.write("restart\n")
    p.stdin.flush()

# Shut off program and print final data
p.stdin.write("stop\n")
p.stdin.flush()
