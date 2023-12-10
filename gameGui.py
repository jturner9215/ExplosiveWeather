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

    layoutZ = [[sg.Text("Enter your city or zipcode:")],
               [sg.Input(key='-IN-', enable_events=True)],
               [sg.Button("Enter")]]
    return sg.Window('City', layoutZ, finalize=True)

location = "indianapolis"


#temperature, humidity, precipitationProbability, dewPoint, windSpeed#####################################################################
"""data = api.r
temp = ''
hum = ''
rain = ''
dew = ''
wind = ''"""

#humidity0, precipitationProbability1, pressureSurfaceLevel2, temperature3, temperatureApparent4, weatherCode5, windSpeed6


#doing it like this to hopefully cut down on calls to the api
"""def cityData(function):
    
    data = function
    return data"""


#data = api.API_Call(location, "imperial")

 
pressure = ""
    
hum = ""
    
rain = ""

temp = ""
    
wind = ""
    

def layoutWeather():

    layoutWea = [#################################################################################################################
        [sg.Text("Temperature: ", key='-tempd-')],
        [sg.Text("Humidity: ", key='-humd-')],
        [sg.Text("Rain chance: ", key='-raind-')],
        [sg.Text("Pressure level: ", key='-pressd-')],
        [sg.Text("Wind speed: ", key='-windd-')]

        ]
    return sg.Window('Weather', layoutWea, resizable=True, finalize=True)


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
        revealedBoard = MSLib.Board_Revealed_Preset_easy
        gameBoard = boardObj.board_Array
        break

    if event == 'Hard':
        boardObj = MSLib.MineSweeperBoard("Hard")
        row = 8
        column = 8
        revealedBoard = MSLib.Board_Revealed_Preset_hard
        gameBoard = boardObj.board_Array
        break


window.close()

#copying game board to secondary array to track what has been revealed
#revealedBoard = [row[:] for row in boardObj.board_Array]
#revealedBoard = boardObj.board_Array.copy()

#counting how many bombs are in play
bombCount = 0

flagOn = False


for j in range(column):
    for i in range(row):
        if gameBoard[i][j] == -1:
            bombCount += 1





#-----layout for the actual main game screen---------
theme = 'BluePurple'

def layoutMine():
    layout = [
        [sg.Menu(menu_def, )],
        [sg.Text("Score: " + str(boardObj.GameData.score_get()), key = 'xxx'), sg.Text("Bombs: " + str(bombCount)), sg.Button('Flag')],
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


        data = api.API_Call(location, "imperial")
        pressure = data[2]  
        hum = data[0]               
        rain = data[1]
        temp = data[3]
        wind = data[6]

        #print(data)
        #print(str(hum) + "test")

        
        window4 = layoutWeather()
        window4['-tempd-'].update("Temperature: " + str(temp))
        window4['-humd-'].update("Humidity: "+ str(hum))
        window4['-raind-'].update("Rain chance: "+ str(rain))
        window4['-pressd-'].update("Pressure level: "+ str(pressure))
        window4['-windd-'].update("Wind speed: "+ str(wind))
        

        while True:
            
            event, values = window4.read()

            

            """window4['-tempd-'].update("Temperature: " + str(temp))
            window4['-humd-'].update("Humidity: "+ str(hum))
            window4['-raind-'].update("Rain chance: "+ str(rain))
            window4['-pressd-'].update("Pressure level: "+ str(pressure))
            window4['-windd-'].update("Wind speed: "+ str(wind))"""
            if event in (sg.WIN_CLOSED, 'Exit', 'Enter'):
                  break
        window4.close()



    
    #funny way to make sure that the events on the menu bar don't get confused with the game board buttons
    if boardObj.Win_Loss_Flag != 1:
        if event != "View themes":
            if event != "Change city":
                if event != "How to play":
                    if event != 'Flag':

                        if flagOn == False:

                        
                            window[event].update(gameBoard[event[0]][event[1]], button_color=('white','black')) 
                            #to visually update the playing board when user clicks 

                            if gameBoard[event[0]][event[1]] == -1:         
                                #breaks the loop if user clicks a bomb and shuts window
                                boardObj.Win_Loss_Flag = -1
                                sg.popup("You lost :(",
                                        "Score: " + str(boardObj.GameData.score_get()))
                                break 

                            if gameBoard[event[0]][event[1]] != -1:

                                if revealedBoard[event[0]][event[1]] != 1:

                                    revealedBoard[event[0]][event[1]] = 1
                                    boardObj.GameData.Score_Manual_Update(5)
                                    window['xxx'].update('Score: ' + str(boardObj.GameData.score_get()))
            
                                if (keepCount() + bombCount) == (row * column):
                                    boardObj.Win_Loss_Flag = 1

                            
                            

                        if flagOn == True:

                            window[event].update('X', button_color=('black','white'))

                        
                        





        
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
            location = values
            """data = api.API_Call(location, "imperial")
            pressure = data[2]  
            hum = data[0]               
            rain = data[1]
            temp = data[3]
            wind = data[6]"""
        #print(city)    
        window3.close()


    if event == "How to play":
        sg.Popup("To play minesweeper, you click a square.",
                 "The number that appears is how many bombs are touching that square!",
                 "But if you click a bomb, you lose! Try to avoid those spots!",
                 "You win once all non-bombs are uncovered and you click 'flag'.")
        


    if event == 'Flag':
        if flagOn == False:
            flagOn = True
            window[event].update(button_color=('green'))
        else:
            flagOn = False
            window[event].update(button_color=('#122e52'))


