import MineSweeperLibrary as MineSweeperBackEnd


def main():
    print("main")
    dude = MineSweeperBackEnd.MineSweeperBoard("Hard")
    print(MineSweeperBackEnd.MineSweeperBoard.GameData.difficulty_get() + " first main")
    #test = dude.board_Array[4][4]
    
    

    while(True):
        
        MineSweeperBackEnd.MineSweeperBoard.debug_board_console_print(dude)

        print("Please enter a negative number to leave game. Otherwise just enter guess coordinates")

        x_coord = int(input("X: "))
        y_coord = int(input("Y: "))

        #loop breakout 
        if (x_coord < 0  or y_coord < 0):
            break

        MineSweeperBackEnd.MineSweeperBoard.Player_Reveal_Guess(dude, x_coord, y_coord)

        #win output
        print(MineSweeperBackEnd.MineSweeperBoard.Win_Lose_Check(dude))


    

    

    MineSweeperBackEnd.MineSweeperBoard.debug_board_console_print(dude)



#have this at the bottom of the page as this runs main 
if __name__ == "__main__":
    main()