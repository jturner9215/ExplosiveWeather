import PySimpleGUI as sg
import MineSweeperLibrary as MSLib
import APICaller as api







#-----theme browser-----

def layoutTheme():
       

        layoutT = [[sg.Text('Theme Browser')],
                [sg.Text('Click a theme color to see what this program could have looked like')],
                [sg.Listbox(values=sg.theme_list(), size=(20, 12), key='-LIST-', enable_events=True)],
                [sg.Button('Exit')]]
        return sg.Window('Themes', layoutT, finalize=True)


#------changing city function window------

def layoutCity():

    layoutZ = [[sg.Text("Enter your city:")],
               [sg.Input(key='-IN-', enable_events=True)],
               [sg.Button("Enter")]]
    return sg.Window('City', layoutZ, finalize=True)

city = "indianapolis"


#temperature, humidity, precipitationProbability, dewPoint, windSpeed
data = api.r
temp = ''
hum = ''
rain = ''
dew = ''
wind = ''

for val in data["data"]["values"]:
    if val == 'dewPoint':
        dew = data["data"]["values"][val]
    elif val == 'humidity':
        hum = data["data"]["values"][val]
    elif val == 'precipitationProbablity':
        rain = data["data"]["values"][val]
    elif val == 'temperature':
        temp = data["data"]["values"][val]
    elif val == 'windSpeed':
        wind = data["data"]["values"][val]
    #print(val, ": ", data["data"]["values"][val])

layoutWeather = [
    [sg.Text("Temperature: " + str(temp))],
    [sg.Text("Humidity: "+ str(hum))],
    [sg.Text("Rain chance: "+ str(rain))],
    [sg.Text("Dew point: "+ str(dew))],
    [sg.Text("Wind speed: "+ str(wind))]

    ]


#menu bar for main window
menu_def = [['File', ['Exit']],
            ['Settings', ['View themes', 'Change city']],
            ['Help', ['How to play']],]



layoutDiffPopup = [
    [sg.Text("Choose the difficulty:")],
    [sg.Button('Easy'), sg.Button('Hard')]

    ]



#---------setting how many rows/columns will be played-----------

row = 5
column = 5
#revealedBoard = []

window = sg.Window('Hello!', layoutDiffPopup)       #sg.Window('Minesweeper', layoutMine)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break 

    if event == 'Easy':
        boardObj = MSLib.MineSweeperBoard("Easy")      #building the object for the board class
        
        break

    if event == 'Hard':
        boardObj = MSLib.MineSweeperBoard("Hard")
        row = 8
        column = 8
        break


window.close()

#copying game board to secondary array to track what has been revealed
revealedBoard = [row[:] for row in boardObj.board_Array]

#counting how many bombs are in play
bombCount = 0



for j in range(column):
    for i in range(row):
        if boardObj.board_Array[i][j] == -1:
            bombCount += 1


#secondary board to keep track of revealed spaces
for j in range(column):
    for i in range(row):
        revealedBoard[i][j] = 0



#-----layout for the actual main game screen---------
theme = 'BluePurple'

def layoutMine():
    layout = [
        [sg.Menu(menu_def, )],
        [sg.Text("Score: " + str(boardObj.GameData.score_get())), sg.Text("Bombs: " + str(bombCount))],
        [[sg.Button('', size=(4, 2), key=(i, j), pad=(0,0)) for j in range(row)] for i in range(column)]     
        ]
    
    return sg.Window('Minesweeper', layout, resizable=True, finalize=True)


#-------------------------------------------------------------------------------------------

def keepCount():
    total = 0
    for j in range(column):
        for i in range(row):
            total += revealedBoard[i][j]
    return total


#----------------------------main game loop-------------------------------




window = layoutMine() #sg.Window('Minesweeper', layoutMine)

boardObj.Win_Loss_Flag = 0


while True:
    event, values = window.read()
    sg.theme(theme)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break

    if boardObj.Win_Loss_Flag == 1:
        sg.Popup("You win!")
        if event in (sg.WIN_CLOSED, 'Exit', 'Ok!'):
            break
        window.close()

        window4 = sg.Window('test', layoutWeather)
        while True:
            event, values = window4.read()
            if event in (sg.WIN_CLOSED, 'Exit', 'Enter'):
                  break
        window4.close()



    
    #funny way to make sure that the events on the menu bar don't get confused with the game board buttons
    if boardObj.Win_Loss_Flag != 1:
        if event != "View themes":
            if event != "Change city":
                if event != "How to play":
                    
                    window[event].update(boardObj.board_Array[event[0]][event[1]], button_color=('white','black')) 
                    #to visually update the playing board when user clicks 

                    if boardObj.board_Array[event[0]][event[1]] == -1:         
                        #breaks the loop if user clicks a bomb and shuts window
                        boardObj.Win_Loss_Flag = -1
                        sg.popup("You lost :(",
                                "Score: " + str(boardObj.GameData.score_get()))
                        break 

                    if boardObj.board_Array[event[0]][event[1]] != -1:
                        revealedBoard[event[0]][event[1]] = 1
    
                        if (keepCount() + bombCount) == (row * column):
                            boardObj.Win_Loss_Flag = 1

                        
                        





        
    if event == "View themes": #window pops up to show possible themes. doesnt do much else. its for fun
          window2 = layoutTheme()
          while True:  # Event Loop
              event, values = window2.read()
              if event in (sg.WIN_CLOSED, 'Exit'):
                  break
              sg.theme(values['-LIST-'][0])
              sg.popup_get_text('This is {}'.format(values['-LIST-'][0]))

          window2.close()
          


    if event == "Change city":#window pops up to allow changing of city for weather api
        window3 = layoutCity()
        while True:
            event, values = window3.read()
            if event in (sg.WIN_CLOSED, 'Exit', 'Enter'):
                  break
            city = values
        #print(city)    
        window3.close()

######################------------#######################temp, change values to reflect info box
    if event == "How to play":
        sg.Popup("To play minesweeper, you click a square.",
                 "The number that appears is how many bombs are touching that square!",
                 "But if you click a bomb, you lose! Try to avoid those spots!",
                 "You win once all non-bombs are uncovered.")


