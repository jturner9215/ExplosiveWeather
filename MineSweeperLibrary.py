#test
print("MineSweeperLibrary Run")

#imports 
import numpy
import random
#Board presets 
"I havent quite figured this out but Im thinking that it might be a func that returns a Board_Array I would like to "
"   do it this way so that MineSweeperBoard can stay relatively clean as putting in these presets would bloat the code."

"Board_Preset_1 Easy"
"-1  3  2  1  0"
" 2 -1 -1  1  0"
" 1  2  2  1  1"
" 1  1  2 -1  1"
" 1 -1  2  1  1"
Board_Preset_1_easy = [[-1, 3, 2, 1, 0],[2, -1, -1, 1, 0], [1, 2, 2, 1, 1], [ 1, 1, 2, -1, 1], [1, -1, 2, 1, 1]]

"Board_Preset_2_easy"
"-1  2  1  0  0"
" 3 -1  2  0  0"
" 2 -1  2  0  0"
" 2  2  1  0  0"
"-1  1  0  0  0"
Board_Preset_2_easy = [[-1, 2, 1, 0, 0],[3,-1, 2, 0, 0],[2,-1, 2, 0, 0],[2, 2, 1, 0, 0],[-1, 1, 0, 0, 0]]


Board_Revealed_Preset_easy = [[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0]]


"Board_Preset_1_hard"
" 1  1  0  0  1  1  1  0"
"-1  1  1  1  2 -1  1  0"
" 2  2  2 -1  3  2  2  1"
"-1  1  2 -1  2  1 -1  1"
" 2  2  2  1  2  2  2  1"
" 1 -1  2  1  2 -1  2  1"
" 1  1  2 -1  1  2 -1  1"
" 0  0  1  1  1  1  1  1"
Board_Preset_1_hard = [[1, 1, 0, 0, 1, 1, 1, 0], [-1, 1, 1, 1, 2, -1, 1, 0], [2, 2, 2, -1, 3, 2, 2, 1], [-1, 1, 2, -1, 2, 1, -1, 1], [2, 2, 2, 1, 2, 2, 2, 1], [1, -1, 2, 1, 2, -1, 2, 1],[1, 1, 2, -1, 1, 2, -1, 1],[0, 0, 1, 1, 1, 1, 1, 1]]

Board_Revealed_Preset_hard = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0]]


#Class MineSweeperGame - this might be added to the minesweeper board class later
"-This object encapsulates everything needed to keep track of the current game"

"Player Score"

"Score_Get()"
"-Returns current score"

"Score_Manual_Update(int)"
"-Allows manual update of the score, adds whatever parameter to score"

"UserName"
"-default AAA not needed but Im going to leave this in here in case it is needed."

"Game_Difficulty"
"-options are 'Easy' and 'Hard'"

"Difficulty_Set(string difficulty)"
"-used to set the Game_Difficulty string"

class MineSweeperGame:

  #player score var
  __player_score = 0

  #Returns current score
  def score_get(self):
    return self.player_score
  
  #Allows manual update of the score, adds whatever parameter to score
  def Score_Manual_Update(self, int_score):
    self.__player_score += int_score
  
  #default AAA not needed but Im going to leave this in here in case it is needed
  UserName ="AAA"

  #options are 'Easy' and 'Hard'
  __GameDifficulty = "Easy"

  #returns game difficulty
  def difficulty_get(self):
    return self.__GameDifficulty

  #used to set the difficulty of the game
  def difficulty_set(self, new_difficulty):
    
    if(new_difficulty == "Easy" or new_difficulty == "Hard"):#data validation, if invalid sets to Easy by default
      self.__GameDifficulty = new_difficulty
    else:
      self.__GameDifficulty = "Easy"

    print(self.__GameDifficulty + " set method")

  
  def __init__(self, difficulty):
    print("game constructor")
    self.difficulty_set(difficulty)





#Class MineSweeperBoard
"-This object stores all data revelant to the minesweeper board and preforms any immediate relevant game tasks"
" PS for all functions the indexes are going to be automatically adjusted so you do not need to -1 on the indexes"

"Constructor"
"-Chooses from the board presets (based on difficulty) and populates the board."

"Board_Array"
"-A 2 index array that stores the board in a (x, y, Bomb_data, Revealed) format."
"-Note: Bomb_data > 0 means the amount of bombs near that square, Bomb_data == 0, no bomb there or near"
"-      Bomb_data == -1 means that there is a bomb there. revealed keep track of whether or not the square "
"-      has been revealed. If Revealed == -1 then the square is non-revealed and flagged. This board should "
"       also be read only to outside of class."

"Lost_var, bool"
"-keeps track of whether or not the player has revealed a bomb with a square in it. "

"Board_Preset"
"-This holds the board preset that was randomly chosen, after board object constructor this wil mainly be used for "
"   debug."

"Board_Bombless_Clear(x, y)"
"-When the player selects a square that does not have a bomb or is next to one, Bomb_data == 0, "
"   The remaining touching squares are removed until squares touching bombs are revealed."

"Player_Reveal_Guess(x, y), int"
"-This function takes the players guess and reveals the specified square, If it is a bomb update the "
"   loss var and return a -1, otherwise return the Bomb_data. If the Bomb_data == 0, call Board_Bombless_Clear(x, y)."
"   "

"Win_Lose_Check(), string"
"-this checks the board to see if the player has won or lost. First checks lost var, then increments through "
"   the Board_Array to find if there are any non revealed non bomb squares left. If won returns 'win', lost returns 'loss'"
"   ,no win or loss returns 'continue'"

"flag_square(x, y), void"
"  -This flags a non-revealed square at the point x, y"

class MineSweeperBoard():
  
  #full of dummy values 
  board_Array = numpy.array([0])
  #intializes the board_Array_revealed array to all 0's
  board_Array_Revealed = numpy.array([0])

  #defines board size based on difficulty
  __board_row_length = 5
  __board_column_length = 5

  #keeps track of whether the game has been lost or won. I assumed doing it this way would make it easier for Jessica to watch for a loss condition
  #instead of her also having to look for a loss/win condition. 1 (true) = won, 0 (neutral) =  no win/loss, -1 (false) = loss
  Win_Loss_Flag = 0

  #"-This holds the board preset that was randomly chosen, after board object constructor this wil mainly be used for debug."
  Board_Preset =  2

  #I decided to move the minesweepergame data object into the minesweeper board instead of vice versa 
  GameData = MineSweeperGame("Easy")

  #constructor
  #Chooses from the board presets (based on difficulty) and populates the board.
  def __init__(self, difficulty):
    
    print("board constructor enter")
    #changes difficulty
    self.GameData.difficulty_set(difficulty)
    print(self.GameData.difficulty_get() + " board constructor leave")
    
    #creates new board
    self.new_board()

  #When the player selects a square that does not have a bomb or is next to one, Bomb_data == 0,
  #The remaining touching squares are removed until squares touching bombs are revealed
  @staticmethod
  def __Board_Bombless_Clear(self, x, y):
     
     #debug stuff
     #print("recursive func enter" + str(x) + ", " + str(y))
     #we are asssuming that the coordinates have already been converted into indexes

     #x = rows, y = columns, kinda weird but its makes sense to me

     #reveals the current location
     self.board_Array_Revealed[x][y] = 1

     #checks indexes one "up", "down", "left", "right", if the index exists and there is not a bomb there and the square has not been revealed, recursively call the func 
     #in order to check all bombless squares in section and reveal them
     if(x + 1 < self.__board_row_length and x + 1 > -1 and self.board_Array[x+1][y] == 0 and self.board_Array_Revealed[x+1][y] != 1):#up, doesnt need x + 1 > -1 but kept it for consistancy
      self.__Board_Bombless_Clear(self, x+1, y)

     if(x - 1 < self.__board_row_length and x - 1 > -1 and self.board_Array[x-1][y] == 0 and self.board_Array_Revealed[x-1][y] != 1):#down
      self.__Board_Bombless_Clear(self, x-1, y)

     if(y - 1 < self.__board_column_length and y - 1 > -1 and self.board_Array[x][y -1] == 0 and self.board_Array_Revealed[x][y-1] != 1):#left
      self.__Board_Bombless_Clear(self, x, y -1)

     if(y + 1 < self.__board_row_length and y + 1 > -1 and self.board_Array[x][y+1] == 0 and self.board_Array_Revealed[x][y+1] != 1):#right
      self.__Board_Bombless_Clear(self, x, y+1)


  #"-This function takes the players guess and reveals the specified square, If it is a bomb update the "
  #" Win_loss_Flag and return a -1, otherwise return the Bomb_data. If the Bomb_data == 0, call Board_Bombless_Clear(x, y)."
  #takes coordinates based out of the top left
  def Player_Reveal_Guess(self, x, y):
     #Adjusting coords to indexes
     row_index = y-1
     col_index = x-1 
      

    #reveals square 
     self.board_Array_Revealed[row_index][col_index] = 1

    #checks for bomb
     if(self.board_Array[row_index][col_index] == -1): #if there is a bomb
      #trips loss conditions
      self.Win_Loss_Flag = -1
      return -1
     else: 
        if(self.board_Array[row_index][col_index] == 0): # if there are no bombs adjacent, clear area on board
           MineSweeperBoard.__Board_Bombless_Clear(self, row_index, col_index)

        #if the guess was correct and there is no bomb there, return the number of bombs that are adjacent
        return self.board_Array[row_index][col_index] 
     

   #this checks the board to see if the player has won or lost. First checks lost var, then increments through "
   #the Board_Array to find if there are any non revealed non bomb squares left. If won returns 'win', lost returns 'loss',"
   #no win or loss returns 'continue'
  def Win_Lose_Check(self):
   
   #checks if loss condition flag has been tripped
   if(self.Win_Loss_Flag == -1):
     return "loss"

   #index values
   row_index = 0
   col_index = 0
   

   #iterates through the boards to look for a win condition, if all bombless squares are revealed then the player has won. 
   while (row_index < self.__board_row_length):
     while (col_index < self.__board_column_length):
       #debug stuff
       #print("row: " + str(row_index)  + ", col: " + str(col_index))
       if(self.board_Array_Revealed[row_index][col_index] == 0 and self.board_Array[row_index][col_index] != -1):#if the current index location is both a non-bomb and is not revealed, return 'continue'
         return "continue" #player has not won because they still need to reveal some non-bomb square
       col_index = col_index + 1 # increments column
      
     #resets for next row 
     col_index = 0
     row_index =  row_index + 1 #increments row
   
   #win condition has been found 
   Win_Loss_Flag =  1
   return "win"
      

       
  #this is mainly used for debugging minsweeperBoard or debugging in general. All it does is print out both 
  #of the current boards
  def debug_board_console_print(self):

    #output string, the func iterates through both arrays and puts together a string for the final output as it goes
    BoardOutputString = ""
    RevealedOutputString =  ""
    #index values
    col = 0
    row = 0
    while(row < self.__board_row_length):
      while(col < self.__board_column_length):
            #debug print
            #print("col"+ str(col) + " " + "row" + str(row))

            #if statements to correct spacing due to negative numbers
            if(self.board_Array[row][col] >= 0): # if current board value is positive, add an additional space
               BoardOutputString += " "
            
            if(self.board_Array_Revealed[row][col] >= 0): # if current revealed board value is positive, add an additional space
               RevealedOutputString += " "
               
            #adds current board value to output string
            BoardOutputString += " " + str(self.board_Array[row][col])

            #adds current revealed board value to output string
            RevealedOutputString += " " + str(self.board_Array_Revealed[row][col])


            col = col + 1
      #resets for new row in board 
      BoardOutputString += "\n"
      RevealedOutputString += "\n"
      row = row + 1
      col = 0
    
    #debug output
    print("This is the main board array/bomb array")
    print(BoardOutputString)
    print("This is the revealed board array")
    print(RevealedOutputString)


  # This flags a non-revealed square at the point x, y
  def flag_square(self, x, y):
    
    #coordinates to indexes 
    row_index = y-1
    column_index = x-1

    #checks to make sure square isnt already revealed
    if(self.board_Array_Revealed[row_index][column_index] == 0):
      self.board_Array_Revealed[row_index][column_index] = -1 #flags the square


  #used to validate user coordinate information, this is not used in any of the above methods. The above methods assume that the user data has
  #already been validated. Accepts Coordinates NOT indexes, returns true if both coords are valid. 
  @staticmethod
  def user_input_validation(self, x_coord, y_coord):
    if(x_coord > 0 and x_coord < self.__board_column_length):#validates x-coords
      if(y_coord > 0 and y_coord < self.__board_row_length ):#validates y-coords
          return True
      else:
        return False
    else:
      return False
    

  #used to keep track of all of the previously played boards 
  previous_boards_easy = numpy.array([0])
  previous_boards_hard = numpy.array([0])


  #used to select boards to either start or restart the game
  def new_board(self):
    "NOT FINISHED AT ALL"
    #random num used to select board 
    random_board_num  = 0

    #updates index lengths for boards 
    if(self.GameData.difficulty_get() ==  "Easy"):
      self.__board_row_length = 5
      self.__board_column_length = 5
    else: #if game is hard
      self.__board_row_length = 8
      self.__board_column_length = 8



    #holds number of easy boards so that we know when to reset prvious boards 
    num_of_easy_boards = 2 + 1 #since the array cant be empty, add one for the array index that is never empty
    #akin to num_of_easy_boards
    num_of_hard_boards = 1 + 1

    #keeps generating new board numbers until an unused one is found
    while(True):
      random_board_num = random.randint(1,3)#new random num

      if(self.GameData.difficulty_get() == "Easy"):#easy difficulty boards 
        if(random_board_num in self.previous_boards_easy):#checks if current board has been used
          if(self.previous_boards_easy.len == num_of_easy_boards):#if all boards have been used
            self.previous_boards_easy = numpy.array[0]#resets used boards
          else:
           continue #easy board has already been used 
        else:#found an acceptable easy board
          self.previous_boards_easy = numpy.insert(self.previous_boards_easy, 0, random_board_num)#adds to used board
          self.board_Array_Revealed = Board_Revealed_Preset_easy.copy()#resets revealed board 
          break
      else: #hard difficulty boards
        if(random_board_num in self.previous_boards_hard):#checks if current board has been used
          if(self.previous_boards_hard.len == num_of_hard_boards):#if all boards have been used
            self.previous_boards_hard = numpy.array[0]#resets used boards
          else:
            continue #hard board has already been used 
        else:#found an acceptable hard board
          self.previous_boards_hard = numpy.insert(self.previous_boards_hard, 0, random_board_num)#adds to used boards
          self.board_Array_Revealed = Board_Revealed_Preset_hard.copy()#resets revealed board 
          break


    #actually sets the board
    if(self.GameData.difficulty_get() == "Easy"):
     match random_board_num: #a case needs to be made for each board preset
       case 1:
         self.board_Array = Board_Preset_1_easy.copy()
       case 2:
         self.board_Array = Board_Preset_1_easy.copy()
    else:#if difficulty hard
       match random_board_num: #a case needs to be made for each board preset
        case 1:
         self.board_Array = Board_Preset_1_hard.copy()
 


