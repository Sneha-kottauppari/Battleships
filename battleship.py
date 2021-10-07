"""
Battleship Project
Name:
Roll No:
"""

import battleship_tests as test

project = "Battleship" # don't edit this

### SIMULATION FUNCTIONS ###

from tkinter import *
import random

EMPTY_UNCLICKED = 1
SHIP_UNCLICKED = 2
EMPTY_CLICKED = 3
SHIP_CLICKED = 4


'''
makeModel(data)
Parameters: dict mapping strs to values
Returns: None
'''
def makeModel(data):
    data["rows"] = 10
    data["cols"] = 10
    data["board_size"] = 500
    data["cell_size"] = (data["board_size"]/(data["rows"]))
    data["user_ship_number"] = 5
    data["comp_ship_number"] = 5
    data["user_board"] = emptyGrid(10,10)
    data["computer_board"] = addShips(emptyGrid(10,10),5)
    data["temp_ship"]=test.testShip()
    return
    
'''
makeView(data, userCanvas, compCanvas)
Parameters: dict mapping strs to values ; Tkinter canvas ; Tkinter canvas
Returns: None
'''
def makeView(data, userCanvas, compCanvas):
    grid = emptyGrid(10, 10)
    # usergrid=test.testGrid()
    # compgrid=addShips(grid_new,5)
    drawGrid(data,userCanvas,grid, True)
    drawGrid(data,compCanvas,grid,True)
    drawShip(data,userCanvas,data["temp_ship"])
    return


'''
keyPressed(data, events)
Parameters: dict mapping strs to values ; key event object
Returns: None
'''
def keyPressed(data, event):
    pass


'''
mousePressed(data, event, board)
Parameters: dict mapping strs to values ; mouse event object ; 2D list of ints
Returns: None
'''
def mousePressed(data, event, board):
    pass

#### WEEK 1 ####

'''
emptyGrid(rows, cols)
Parameters: int ; int
Returns: 2D list of ints
'''
def emptyGrid(rows, cols):
    grid_created = []
    for i in range(rows):
        list_2 = []
        for j in range(cols):
            list_2.append(EMPTY_UNCLICKED)
        grid_created.append(list_2)
    return grid_created

'''
createShip()
Parameters: no parameters
Returns: 2D list of ints
'''
def createShip():
    row_centre= random.randint(1,8)
    col_centre= random.randint(1,8)
    orientation=random.randint(0,1)
    if orientation==0:
        ship_placement=[[row_centre,col_centre-1],[row_centre,col_centre],[row_centre,col_centre+1]]
    else:
        ship_placement=[[row_centre-1,col_centre],[row_centre,col_centre],[row_centre+1,col_centre]]
    
    return ship_placement
    


'''
checkShip(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def checkShip(grid, ship):
    for each in ship:
        index_1 = each[0]
        index_2 = each[1]
        if grid[index_1][index_2]!= EMPTY_UNCLICKED:
            return False
    return True


'''
addShips(grid, numShips)
Parameters: 2D list of ints ; int
Returns: 2D list of ints
'''
def addShips(grid, numShips):
    count=0
    while count < numShips:
        ship = createShip()
        if checkShip(grid,ship) == True:
            for each in ship:
                index1 = each[0]
                index2 = each[1]
                grid[index1][index2]=SHIP_UNCLICKED
            count=count+1
    return grid


'''
drawGrid(data, canvas, grid, showShips)
Parameters: dict mapping strs to values ; Tkinter canvas ; 2D list of ints ; bool
Returns: None
'''
def drawGrid(data, canvas, grid, showShips):
    for col in range(data["cols"]):
        for row in range(data["rows"]):
            if grid[row][col] == SHIP_UNCLICKED:
                canvas.create_rectangle(data["cell_size"]*col,data["cell_size"]*row,data["cell_size"]*(col+1),data["cell_size"]*(row+1),fill="yellow")
            else:
                canvas.create_rectangle(data["cell_size"] * col, data["cell_size"] * row, data["cell_size"] * (col + 1),data["cell_size"] * (row + 1), fill="blue")



### WEEK 2 ###

'''
isVertical(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isVertical(ship):
    index1 = []
    index2 = []
    for each in ship:
        index1.append(each[0])
        index2.append(each[1])
    if index2[0] == index2[1] and index2[1] == index2[2]:
        if max(index1)-min(index1) <= 2:
            return True
    return False



'''
isHorizontal(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isHorizontal(ship):
    index1 = []
    index2 = []
    for each in ship:
        index1.append(each[0])
        index2.append(each[1])
    if index1[0] == index1[1] and index1[1] == index1[2]:
        if max(index2) - min(index2) <= 2:
            return True
    return False


'''
getClickedCell(data, event)
Parameters: dict mapping strs to values ; mouse event object
Returns: list of ints
'''
def getClickedCell(data, event):
    coord1 = int(event.x/data["cell_size"])
    coord2 = int(event.y/data["cell_size"])
    return [coord2,coord1]


'''
drawShip(data, canvas, ship)
Parameters: dict mapping strs to values ; Tkinter canvas; 2D list of ints
Returns: None
'''
def drawShip(data, canvas, ship):
    for each in ship:
        # print(each[0],each[1])
        canvas.create_rectangle(data["cell_size"]*each[1],data["cell_size"]*each[0],data["cell_size"]*(each[1]+1),data["cell_size"]*(each[0]+1),fill="white")

    return


'''
shipIsValid(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def shipIsValid(grid, ship):
    if checkShip(grid,ship) and (isVertical(ship) or isHorizontal(ship)):
        return True
    return False
    


'''
placeShip(data)
Parameters: dict mapping strs to values
Returns: None
'''
def placeShip(data):
    return


'''
clickUserBoard(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def clickUserBoard(data, row, col):
    return


### WEEK 3 ###

'''
updateBoard(data, board, row, col, player)
Parameters: dict mapping strs to values ; 2D list of ints ; int ; int ; str
Returns: None
'''
def updateBoard(data, board, row, col, player):
    return


'''
runGameTurn(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def runGameTurn(data, row, col):
    return


'''
getComputerGuess(board)
Parameters: 2D list of ints
Returns: list of ints
'''
def getComputerGuess(board):
    return


'''
isGameOver(board)
Parameters: 2D list of ints
Returns: bool
'''
def isGameOver(board):
    return


'''
drawGameOver(data, canvas)
Parameters: dict mapping strs to values ; Tkinter canvas
Returns: None
'''
def drawGameOver(data, canvas):
    return


### SIMULATION FRAMEWORK ###

from tkinter import *

def updateView(data, userCanvas, compCanvas):
    userCanvas.delete(ALL)
    compCanvas.delete(ALL)
    makeView(data, userCanvas, compCanvas)
    userCanvas.update()
    compCanvas.update()

def keyEventHandler(data, userCanvas, compCanvas, event):
    keyPressed(data, event)
    updateView(data, userCanvas, compCanvas)

def mouseEventHandler(data, userCanvas, compCanvas, event, board):
    mousePressed(data, event, board)
    updateView(data, userCanvas, compCanvas)

def runSimulation(w, h):
    data = { }
    makeModel(data)

    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window

    # We need two canvases - one for the user, one for the computer
    Label(root, text = "USER BOARD - click cells to place ships on your board.").pack()
    userCanvas = Canvas(root, width=w, height=h)
    userCanvas.configure(bd=0, highlightthickness=0)
    userCanvas.pack()

    compWindow = Toplevel(root)
    compWindow.resizable(width=False, height=False) # prevents resizing window
    Label(compWindow, text = "COMPUTER BOARD - click to make guesses. The computer will guess on your board.").pack()
    compCanvas = Canvas(compWindow, width=w, height=h)
    compCanvas.configure(bd=0, highlightthickness=0)
    compCanvas.pack()

    makeView(data, userCanvas, compCanvas)

    root.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    compWindow.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    userCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "user"))
    compCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "comp"))

    updateView(data, userCanvas, compCanvas)

    root.mainloop()


### RUN CODE ###

# This code runs the test cases to check your work
if __name__ == "__main__":

    ## Finally, run the simulation to test it manually ##
    # runSimulation(500, 500)
    # test.testMakeModel()
    # test.testIsVertical()
    # test.testIsHorizontal()
    # test.testGetClickedCell()
    test.testShipIsValid()