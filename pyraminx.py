from tkinter import *
from tkinter import ttk
import random
import heapq
from heapq import heapify, heappush
import copy

#For confidentiality reasons that were mentioned by Dr. Goldsmith,
#I the author was warned not to put my name in this code.
#Therefore, I will refer to myself as the author and the friend who wrote the basics of the GUI as the Peer.
#From hereon, Peer code will be designated as such, and otherwise the code will be mine as the Author.

flag = 0
counterClockToggle = 0
startingcolors = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
startingcopy = startingcolors



class Node():
    def __init__(self, parent = None, configuration = None):
        self.parent = parent
        self.configuration = configuration
        self.g = 0  # Distance from start to current node
        self.h = 0  # Heuristic cost to the goal
        self.f = 0  # Total cost (g + h)


    def __eq__(self, other):
        return self.configuration == other.configuration


    def __lt__(self, other):
        return self.f < other.f


def findHeuristic(startPyramid):
        return 1

def astar(startPyramid, endPyramid):
    startNode = Node(None, startPyramid)
    startNode.configuration = startPyramid
    startNode.g = startNode.f = 0
    startNode.h = findHeuristic(startPyramid)


    endNode = Node(None, endPyramid)
    endNode.g = endNode.h = endNode.f = 0

    #open list that I am storing as a prio queue min heap
    #Storing nodes that have yet to be reached
    heap = []

    #Closed list to store visited nodes
    closedList = []

    heappush(heap, startNode)
    heapify(heap)


    while (heap):
        currentNode = heap[0]
        if currentNode.configuration is None:
            print("Error: currentNode.config at top is None!")



        for entry in heap:
            if entry.f < currentNode.f:
                currentNode = entry


        heapq.heappop(heap)
        closedList.append(currentNode)

        if solved(currentNode.configuration, endPyramid):
            print("Solved!!!")
            global currentcolors
            currentcolors = currentNode.configuration

            global flag
            if (flag == 1):
                toggle_func()
            updateGui()
            break

        possibleMoves = fetchPossibleMoves()

        for move in possibleMoves:
            currentNodeClone = copy.deepcopy(currentNode)
            newConfiguration = applyMoves(currentNodeClone.configuration, move)

            child = Node(parent = currentNode, configuration = newConfiguration)
            child.g = currentNode.g + 1
            child.h = findHeuristic(child.configuration)
            child.f = child.g + child.h



            if any(node.configuration == child.configuration for node in closedList):
                continue

            heapq.heappush(heap,child)

        heapify(heap)


def applyMoves(configuration, move):
    configurationClone = configuration
    if configurationClone is None:
        print("Error: pcolors is None!")
    newConfiguration = move(configurationClone)
    return newConfiguration


def fetchPossibleMoves():
    global counterClockToggle
    possibleMoves = []
    totalMoves = []

    totalMoves.append(rTopClock)
    totalMoves.append(rSecondClock)
    totalMoves.append(rThirdClock)
    totalMoves.append(rBottomClock)
    totalMoves.append(bTopClock)
    totalMoves.append(bSecondClock)
    totalMoves.append(bThirdClock)
    totalMoves.append(bBottomClock)
    totalMoves.append(rBLFPC)
    totalMoves.append(rBLTPC)
    totalMoves.append(rBRFPC)
    totalMoves.append(rBRTPC)
    totalMoves.append(yBLFPC)
    totalMoves.append(yBLTPC)

    totalMoves.append(rTopCounterClock)
    totalMoves.append(rSecondCounterClock)
    totalMoves.append(rThirdCounterClock)
    totalMoves.append(rBottomCounterClock)
    totalMoves.append(bTopCounterClock)
    totalMoves.append(bSecondCounterClock)
    totalMoves.append(bThirdCounterClock)
    totalMoves.append(bBottomCounterClock)
    totalMoves.append(rBLFPCU)
    totalMoves.append(rBLTPCU)
    totalMoves.append(rBRFPCU)
    totalMoves.append(rBRTPCU)
    totalMoves.append(yBLFPCU)
    totalMoves.append(yBLTPCU)

    if (counterClockToggle == 0):
        for i in range(28):
            possibleMoves.append(totalMoves[i])
    elif (counterClockToggle == 1):
        for i in range(14,28):
            possibleMoves.append(totalMoves[i])
    elif (counterClockToggle == 2):
        for i in range(15):
            possibleMoves.append(totalMoves[i])

    return possibleMoves


#GUI code is from peer, not from author
def reset():
    global startingcolors
    global currentcolors
    startingcolors = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
    currentcolors = startingcolors

    clock_list = [
        {"button": Button(root, text="Top Clock", bg = "red"), "function": rTopClock, "arg1": currentcolors},
        {"button": Button(root, text="Top Counter Clock", bg = "red"), "function": rTopCounterClock, "arg1": currentcolors},
        {"button": Button(root, text="Second Clock", bg = "red"), "function": rSecondClock, "arg1": currentcolors},
        {"button": Button(root, text="Second Counter Clock", bg = "red"), "function": rSecondCounterClock, "arg1": currentcolors},
        {"button": Button(root, text="Third Clock", bg = "red"), "function": rThirdClock, "arg1": currentcolors},
        {"button": Button(root, text="Third Counter Clock", bg = "red"), "function": rThirdCounterClock, "arg1": currentcolors},
        {"button": Button(root, text="Bottom Clock", bg = "red"), "function": rBottomClock, "arg1": currentcolors},
        {"button": Button(root, text="Bottom Counter Clock", bg = "red"), "function": rBottomCounterClock, "arg1": currentcolors},


        {"button": Button(root, text="Top (row of 7) Clock", bg = "blue"), "function": bTopClock, "arg1": currentcolors},
        {"button": Button(root, text="Top (row of 7) Counterclock", bg = "blue"), "function": bTopCounterClock, "arg1": currentcolors},
        {"button": Button(root, text="Second Clock", bg = "blue"), "function": bSecondClock, "arg1": currentcolors},
        {"button": Button(root, text="Second Counter Clock", bg = "blue"), "function": bSecondCounterClock, "arg1": currentcolors},
        {"button": Button(root, text="Third Clock", bg = "blue"), "function": bThirdClock, "arg1": currentcolors},
        {"button": Button(root, text="Third Counter Clock", bg = "blue"), "function": bThirdCounterClock, "arg1": currentcolors},
        {"button": Button(root, text="Bottom Clock (YBG Corner)", bg = "blue"), "function": bBottomClock, "arg1": currentcolors},
        {"button": Button(root, text="Bottom Counter (YBG Corner)", bg = "blue"), "function": bBottomCounterClock, "arg1": currentcolors},


        {"button": Button(root, text="Top Clock", bg = "green"), "function": gTopClock, "arg1": currentcolors},
        {"button": Button(root, text="Top Counter Clock", bg = "green"), "function": gTopCounterClock, "arg1": currentcolors},
        {"button": Button(root, text="Second Clock", bg = "green"), "function": gSecondClock, "arg1": currentcolors},
        {"button": Button(root, text="Second Counter Clock", bg = "green"), "function": gSecondCounterClock, "arg1": currentcolors},
        {"button": Button(root, text="Third Clock", bg = "green"), "function": gThirdClock, "arg1": currentcolors},
        {"button": Button(root, text="Third Counter Clock", bg = "green"), "function": gThirdCounterClock, "arg1": currentcolors},
        {"button": Button(root, text="Bottom Clock", bg = "green"), "function": gBottomClock, "arg1": currentcolors},
        {"button": Button(root, text="Bottom Counter Clock", bg = "green"), "function": gBottomCounterClock, "arg1": currentcolors},


        {"button": Button(root, text="Top Clock", bg = "yellow"), "function": yTopClock, "arg1": currentcolors},
        {"button": Button(root, text="Top Counter Clock", bg = "yellow"), "function": yTopCounterClock, "arg1": currentcolors},
        {"button": Button(root, text="Second Clock", bg = "yellow"), "function": ySecondClock, "arg1": currentcolors},
        {"button": Button(root, text="Second Counter Clock", bg = "yellow"), "function": ySecondCounterClock, "arg1": currentcolors},
        {"button": Button(root, text="Third Clock", bg = "yellow"), "function": yThirdClock, "arg1": currentcolors},
        {"button": Button(root, text="Third Counter Clock", bg = "yellow"), "function": yThirdCounterClock, "arg1": currentcolors},
        {"button": Button(root, text="Bottom Clock", bg = "yellow"), "function": yBottomClock, "arg1": currentcolors},
        {"button": Button(root, text="Bottom Counter", bg = "yellow"), "function": yBottomCounterClock, "arg1": currentcolors},

    ]

    clock_list_two = [
        {"button": Button(root, text="Bottom Left 5 Pyramid Clock", bg="red"), "function": rBLFPC, "arg1": currentcolors},
        {"button": Button(root, text="Bottom Left 5 Pyramid Counter", bg="red"), "function": rBLFPCU, "arg1": currentcolors},
        {"button": Button(root, text="Bottom Left 3 Pyramid Clock", bg="red"), "function": rBLTPC, "arg1": currentcolors},
        {"button": Button(root, text="Bottom Left 3 Pyramid Counter", bg="red"), "function": rBLTPCU, "arg1": currentcolors},
        {"button": Button(root, text="Bottom Right 5 Pyramid Clock", bg="red"), "function": rBRFPC, "arg1": currentcolors},
        {"button": Button(root, text="Bottom Right 5 Pyramid Counter", bg="red"), "function": rBRFPCU, "arg1": currentcolors},
        {"button": Button(root, text="Bottom Right 3 Pyramid Clock", bg="red"), "function": rBRTPC, "arg1": currentcolors},
        {"button": Button(root, text="Bottom Right 3 Pyramid Counter", bg="red"), "function": rBRTPCU, "arg1": currentcolors},

        {"button": Button(root, text="Bottom Left 5 Pyramid Clock", bg="green"), "function": gBLFPC, "arg1": currentcolors},
        {"button": Button(root, text="Bottom Left 5 Pyramid Counter", bg="green"), "function": gBLFPCU, "arg1": currentcolors},
        {"button": Button(root, text="Bottom Left 3 Pyramid Clock", bg="green"), "function": gBLTPC, "arg1": currentcolors},
        {"button": Button(root, text="Bottom Left 3 Pyramid Counter", bg="green"), "function": gBLTPCU, "arg1": currentcolors},
        {"button": Button(root, text="Bottom Right 5 Pyramid Clock", bg="green"), "function": gBRFPC, "arg1": currentcolors},
        {"button": Button(root, text="Bottom Right 5 Pyramid Counter", bg="green"), "function": gBRFPCU, "arg1": currentcolors},
        {"button": Button(root, text="Bottom Right 3 Pyramid Clock", bg="green"), "function": gBRTPC, "arg1": currentcolors},
        {"button": Button(root, text="Bottom Right 3 Pyramid Counter", bg="green"), "function": gBRTPCU, "arg1": currentcolors},

        {"button": Button(root, text="Bottom Left 5 Pyramid Clock", bg="yellow"), "function": yBLFPC, "arg1": currentcolors},
        {"button": Button(root, text="Bottom Left 5 Pyramid Counter", bg="yellow"), "function": yBLFPCU, "arg1": currentcolors},
        {"button": Button(root, text="Bottom Left 3 Pyramid Clock", bg="yellow"), "function": yBLTPC, "arg1": currentcolors},
        {"button": Button(root, text="Bottom Left 3 Pyramid Counter", bg="yellow"), "function": yBLTPCU, "arg1": currentcolors},
        {"button": Button(root, text="Bottom Right 5 Pyramid Clock", bg="yellow"), "function": yBRFPC, "arg1": currentcolors},
        {"button": Button(root, text="Bottom Right 5 Pyramid Counter", bg="yellow"), "function": yBRFPCU, "arg1": currentcolors},
        {"button": Button(root, text="Bottom Right 3 Pyramid Clock", bg="yellow"), "function": yBRTPC, "arg1": currentcolors},
        {"button": Button(root, text="Bottom Right 3 Pyramid Counter", bg="yellow"), "function": yBRTPCU, "arg1": currentcolors},

        {"button": Button(root, text="Red Green Blue Corner Clock", bg="blue"), "function": rgbCC, "arg1": currentcolors},
        {"button": Button(root, text="Red Green Blue Corner Counter", bg="blue"), "function": rgbCCU, "arg1": currentcolors},
        {"button": Button(root, text="Red Yellow Blue Corner Clock", bg="blue"), "function": rybCC, "arg1": currentcolors},
        {"button": Button(root, text="Red Yellow Blue Corner Counter", bg="blue"), "function": rybCCU, "arg1": currentcolors},


    ]

    yval = 0
    for button_info in clock_list:
        button_info["button"].place(x=1000, y=yval)
        button_info["button"].config(command=lambda b=button_info: (update_current_button(b), b["function"](b["arg1"],)))
        yval = yval + 30

    yval = 0
    for button_info in clock_list_two:
        button_info["button"].place(x=1175, y=yval)
        button_info["button"].config(command=lambda b=button_info: (update_current_button(b), b["function"](b["arg1"],)))
        yval = yval + 30
    updateGui()

#To save processing power, add ability to toggle on/off updating of the graphics
def toggle_func():
    global flag
    global toggleButton, toggleText
    if ((flag == 0) or (flag == 2)):
        flag = 1
        toggleText = canvas.create_text(206, 750, text="Toggle is On", fill="black", font=('Helvetica 15 bold'))
        toggleButton.config(bg="green")
    else:
        toggleButton.config(bg="gray")
        flag = 2
        updateGui()

def counterClockToggle_func():
    global counterClockToggle

    if (counterClockToggle == 0):
        counterClockToggle = 1
        counterClockToggleButton.config(bg="blue", text = "Counter Moves Only")
    elif (counterClockToggle == 1):
        counterClockToggle = 2
        counterClockToggleButton.config(bg="orange", text = "Clockwise Moves Only")
    else:
        counterClockToggle = 0
        counterClockToggleButton.config(bg="gray", text = "All Moves Possible")


#As this function and the next 3 below it are GUI,
#these were wrote by the peer and not the author
def triangle(x,y):
    x1 = x
    x2 = x - 30
    x3 = x + 30
    y1 =  y - 50
    y2 =  y
    y3 = y2
    return [x1,y1, x2,y2, x3,y3]

def triangle_upsidedown(x,y):
    x1 = x
    x2 = x - 30
    x3 = x + 30
    y1 =  y
    y2 =  y - 50
    y3 = y2
    return [x1,y1, x2,y2, x3,y3]

def update_current_button(button_info):
    global current_button_info
    current_button_info = button_info

def solved(a, b):
    for i in range(63):
        if a[i] != b[i]:
            return False
    return True

#GUI for creating the faces of the Pyraminx, Peer work that was heavily tweaked by Author
def updateGui():


    #Is toggle flag on
    global flag
    if (flag == 1):
        return


    canvas.delete("all")

    solvedText = canvas.create_text(300, 50, text="Currently Solved!", fill="black", font=('Helvetica 15 bold'))
    if solved(startingcopy, currentcolors):
        solvedText = canvas.create_text(300, 50, text="Currently Solved!", fill="black", font=('Helvetica 15 bold'))
    else:
        canvas.itemconfig(solvedText, text= "")



    #1 Red
    canvas.create_polygon(triangle(500, 150), fill=colors[currentcolors[0]], outline = "black")
    #2
    canvas.create_polygon(triangle(460, 210), fill=colors[currentcolors[1]], outline = "black")
    canvas.create_polygon(triangle_upsidedown(500, 210), fill=colors[currentcolors[2]], outline = "black")
    canvas.create_polygon(triangle(540, 210), fill=colors[currentcolors[3]], outline = "black")
    #3
    canvas.create_polygon(triangle(420, 270), fill=colors[currentcolors[4]], outline = "black")
    canvas.create_polygon(triangle_upsidedown(460, 270), fill=colors[currentcolors[5]], outline = "black")
    canvas.create_polygon(triangle(500, 270), fill=colors[currentcolors[6]], outline = "black")
    canvas.create_polygon(triangle_upsidedown(540, 270), fill=colors[currentcolors[7]], outline = "black")
    canvas.create_polygon(triangle(580, 270), fill=colors[currentcolors[8]], outline = "black")
    #4
    canvas.create_polygon(triangle(380, 330), fill=colors[currentcolors[9]], outline = "black")
    canvas.create_polygon(triangle_upsidedown(420, 330), fill=colors[currentcolors[10]], outline = "black")
    canvas.create_polygon(triangle(460, 330), fill=colors[currentcolors[11]], outline = "black")
    canvas.create_polygon(triangle_upsidedown(500, 330), fill=colors[currentcolors[12]], outline = "black")
    canvas.create_polygon(triangle(540, 330), fill=colors[currentcolors[13]], outline = "black")
    canvas.create_polygon(triangle_upsidedown(580, 330), fill=colors[currentcolors[14]], outline = "black")
    canvas.create_polygon(triangle(620, 330), fill=colors[currentcolors[15]], outline = "black")

    #debugging tool
    #canvas.create_text(380, 340, text = "9")
    #canvas.create_text(620, 340, text = "15")
    #canvas.create_text(500, 90, text = "0")
    canvas.create_text(500, 80, text="Red", font=("Helvetica", 30, "bold"), fill="red")



    #1 Blue
    canvas.create_polygon(triangle_upsidedown(500, 610), fill=colors[currentcolors[16]], outline = "black")
    #2
    canvas.create_polygon(triangle_upsidedown(460, 550), fill=colors[currentcolors[17]], outline = "black")
    canvas.create_polygon(triangle(500, 550), fill=colors[currentcolors[18]], outline = "black")
    canvas.create_polygon(triangle_upsidedown(540, 550), fill=colors[currentcolors[19]], outline = "black")
    #3
    canvas.create_polygon(triangle_upsidedown(420, 490), fill=colors[currentcolors[20]], outline = "black")
    canvas.create_polygon(triangle(460, 490), fill=colors[currentcolors[21]], outline = "black")
    canvas.create_polygon(triangle_upsidedown(500, 490), fill=colors[currentcolors[22]], outline = "black")
    canvas.create_polygon(triangle(540, 490), fill=colors[currentcolors[23]], outline = "black")
    canvas.create_polygon(triangle_upsidedown(580, 490), fill=colors[currentcolors[24]], outline = "black")
    #4
    canvas.create_polygon(triangle_upsidedown(380, 430), fill=colors[currentcolors[25]], outline = "black")
    canvas.create_polygon(triangle(420, 430), fill=colors[currentcolors[26]], outline = "black")
    canvas.create_polygon(triangle_upsidedown(460, 430), fill=colors[currentcolors[27]], outline = "black")
    canvas.create_polygon(triangle(500, 430), fill=colors[currentcolors[28]], outline = "black")
    canvas.create_polygon(triangle_upsidedown(540, 430), fill=colors[currentcolors[29]], outline = "black")
    canvas.create_polygon(triangle(580, 430), fill=colors[currentcolors[30]], outline = "black")
    canvas.create_polygon(triangle_upsidedown(620, 430), fill=colors[currentcolors[31]], outline = "black")

    #debugging tool
    #canvas.create_text(500, 620, text = "16")
    #canvas.create_text(380, 370, text = "25")
    #canvas.create_text(620, 370, text = "31")
    canvas.create_text(500, 650, text="Blue", font=("Helvetica", 30, "bold"), fill="blue")



    #1 Yellow
    canvas.create_polygon(triangle(160, 150), fill=colors[currentcolors[32]], outline = "black")
    #2
    canvas.create_polygon(triangle(120, 210), fill=colors[currentcolors[33]], outline = "black")
    canvas.create_polygon(triangle_upsidedown(160, 210), fill=colors[currentcolors[34]], outline = "black")
    canvas.create_polygon(triangle(200, 210), fill=colors[currentcolors[35]], outline = "black")
    #3
    canvas.create_polygon(triangle(80, 270), fill=colors[currentcolors[36]], outline = "black")
    canvas.create_polygon(triangle_upsidedown(120, 270), fill=colors[currentcolors[37]], outline = "black")
    canvas.create_polygon(triangle(160, 270), fill=colors[currentcolors[38]], outline = "black")
    canvas.create_polygon(triangle_upsidedown(200, 270), fill=colors[currentcolors[39]], outline = "black")
    canvas.create_polygon(triangle(240, 270), fill=colors[currentcolors[40]], outline = "black")
    #4
    canvas.create_polygon(triangle(40, 330), fill=colors[currentcolors[41]], outline = "black")
    canvas.create_polygon(triangle_upsidedown(80, 330), fill=colors[currentcolors[42]], outline = "black")
    canvas.create_polygon(triangle(120, 330), fill=colors[currentcolors[43]], outline = "black")
    canvas.create_polygon(triangle_upsidedown(160, 330), fill=colors[currentcolors[44]], outline = "black")
    canvas.create_polygon(triangle(200, 330), fill=colors[currentcolors[45]], outline = "black")
    canvas.create_polygon(triangle_upsidedown(240, 330), fill=colors[currentcolors[46]], outline = "black")
    canvas.create_polygon(triangle(280, 330), fill=colors[currentcolors[47]], outline = "black")

    #debugging tool
    #canvas.create_text(160, 90, text = "32")
    #canvas.create_text(40, 340, text = "41")
    #canvas.create_text(280, 340, text = "47")
    canvas.create_text(160, 80, text="Yellow", font=("Helvetica", 30, "bold"), fill="Yellow")

    #1 Green
    canvas.create_polygon(triangle(840, 150), fill=colors[currentcolors[48]], outline = "black")
    #2
    canvas.create_polygon(triangle(800, 210), fill=colors[currentcolors[49]], outline = "black")
    canvas.create_polygon(triangle_upsidedown(840, 210), fill=colors[currentcolors[50]], outline = "black")
    canvas.create_polygon(triangle(880, 210), fill=colors[currentcolors[51]], outline = "black")
    #3
    canvas.create_polygon(triangle(760, 270), fill=colors[currentcolors[52]], outline = "black")
    canvas.create_polygon(triangle_upsidedown(800, 270), fill=colors[currentcolors[53]], outline = "black")
    canvas.create_polygon(triangle(840, 270), fill=colors[currentcolors[54]], outline = "black")
    canvas.create_polygon(triangle_upsidedown(880, 270), fill=colors[currentcolors[55]], outline = "black")
    canvas.create_polygon(triangle(920, 270), fill=colors[currentcolors[56]], outline = "black")
    #4
    canvas.create_polygon(triangle(720, 330), fill=colors[currentcolors[57]], outline = "black")
    canvas.create_polygon(triangle_upsidedown(760, 330), fill=colors[currentcolors[58]], outline = "black")
    canvas.create_polygon(triangle(800, 330), fill=colors[currentcolors[59]], outline = "black")
    canvas.create_polygon(triangle_upsidedown(840, 330), fill=colors[currentcolors[60]], outline = "black")
    canvas.create_polygon(triangle(880, 330), fill=colors[currentcolors[61]], outline = "black")
    canvas.create_polygon(triangle_upsidedown(920, 330), fill=colors[currentcolors[62]], outline = "black")
    canvas.create_polygon(triangle(960, 330), fill=colors[currentcolors[63]], outline = "black")

    #debugging tool
    #canvas.create_text(840, 90, text = "48")
    #canvas.create_text(720, 340, text = "57")
    #canvas.create_text(960, 340, text = "63")
    canvas.create_text(840, 80, text="Green", font=("Helvetica", 30, "bold"), fill="green")

    #Reprint counterClockToggle because it was getting deleted by my canvas clear at the top of this function
    global counterClockToggleText
    counterClockToggleText = canvas.create_text(455, 750, text="A* Moveset", fill="black", font=('Helvetica 15 bold'))

#Peer code that takes user input for randomizer
def randomizer_func():
    entry_text = entry.get()
    if entry_text.isdigit():
        randompyraminx(int(entry_text))

#Below is nearly 2000 lines that handle pyraminx rotations
#Using naming convention devised by peer. Written by author
def rTopClock(pcolors):
    tempcolor = pcolors[0]
    pcolors[0] = pcolors[48]
    pcolors[48] = pcolors[32]
    pcolors[32] = tempcolor
    updateGui()
    return pcolors

def rTopCounterClock(pcolors):
    tempcolor = pcolors[0]
    pcolors[0] = pcolors[32]
    pcolors[32] = pcolors[48]
    pcolors[48] = tempcolor
    updateGui()
    return pcolors

def rSecondClock(pcolors):
    tempcolor1 = pcolors[1]
    tempcolor2 = pcolors[2]
    tempcolor3 = pcolors[3]

    pcolors[1] = pcolors[49]
    pcolors[2] = pcolors[50]
    pcolors[3] = pcolors[51]

    pcolors[49] = pcolors[33]
    pcolors[50] = pcolors[34]
    pcolors[51] = pcolors[35]

    pcolors[33] = tempcolor1
    pcolors[34] = tempcolor2
    pcolors[35] = tempcolor3
    updateGui()
    return pcolors

def rSecondCounterClock(pcolors):
    tempcolor1 = pcolors[1]
    tempcolor2 = pcolors[2]
    tempcolor3 = pcolors[3]

    pcolors[1] = pcolors[33]
    pcolors[2] = pcolors[34]
    pcolors[3] = pcolors[35]

    pcolors[33] = pcolors[49]
    pcolors[34] = pcolors[50]
    pcolors[35] = pcolors[51]

    pcolors[49] = tempcolor1
    pcolors[50] = tempcolor2
    pcolors[51] = tempcolor3
    updateGui()
    return pcolors

def rThirdClock(pcolors):
    tempcolor1 = pcolors[4]
    tempcolor2 = pcolors[5]
    tempcolor3 = pcolors[6]
    tempcolor4 = pcolors[7]
    tempcolor5 = pcolors[8]

    pcolors[4] = pcolors[52]
    pcolors[5] = pcolors[53]
    pcolors[6] = pcolors[54]
    pcolors[7] = pcolors[55]
    pcolors[8] = pcolors[56]

    pcolors[52] = pcolors[36]
    pcolors[53] = pcolors[37]
    pcolors[54] = pcolors[38]
    pcolors[55] = pcolors[39]
    pcolors[56] = pcolors[40]

    pcolors[36] = tempcolor1
    pcolors[37] = tempcolor2
    pcolors[38] = tempcolor3
    pcolors[39] = tempcolor4
    pcolors[40] = tempcolor5
    updateGui()
    return pcolors

def rThirdCounterClock(pcolors):
    tempcolor1 = pcolors[4]
    tempcolor2 = pcolors[5]
    tempcolor3 = pcolors[6]
    tempcolor4 = pcolors[7]
    tempcolor5 = pcolors[8]

    pcolors[4] = pcolors[36]
    pcolors[5] = pcolors[37]
    pcolors[6] = pcolors[38]
    pcolors[7] = pcolors[39]
    pcolors[8] = pcolors[40]

    pcolors[36] = pcolors[52]
    pcolors[37] = pcolors[53]
    pcolors[38] = pcolors[54]
    pcolors[39] = pcolors[55]
    pcolors[40] = pcolors[56]

    pcolors[52] = tempcolor1
    pcolors[53] = tempcolor2
    pcolors[54] = tempcolor3
    pcolors[55] = tempcolor4
    pcolors[56] = tempcolor5
    updateGui()
    return pcolors

def rBottomClock(pcolors):

    #handle the red, yellow, green
    tempcolor1 = pcolors[9]
    tempcolor2 = pcolors[10]
    tempcolor3 = pcolors[11]
    tempcolor4 = pcolors[12]
    tempcolor5 = pcolors[13]
    tempcolor6 = pcolors[14]
    tempcolor7 = pcolors[15]

    pcolors[9] = pcolors[57]
    pcolors[10] = pcolors[58]
    pcolors[11] = pcolors[59]
    pcolors[12] = pcolors[60]
    pcolors[13] = pcolors[61]
    pcolors[14] = pcolors[62]
    pcolors[15] = pcolors[63]

    pcolors[57] = pcolors[41]
    pcolors[58] = pcolors[42]
    pcolors[59] = pcolors[43]
    pcolors[60] = pcolors[44]
    pcolors[61] = pcolors[45]
    pcolors[62] = pcolors[46]
    pcolors[63] = pcolors[47]

    pcolors[41] = tempcolor1
    pcolors[42] = tempcolor2
    pcolors[43] = tempcolor3
    pcolors[44] = tempcolor4
    pcolors[45] = tempcolor5
    pcolors[46] = tempcolor6
    pcolors[47] = tempcolor7

    #handle the blue underbelly, brute force
    tempcolor16 = pcolors[16]
    tempcolor17 = pcolors[17]
    tempcolor18 = pcolors[18]
    tempcolor19 = pcolors[19]
    tempcolor20 = pcolors[20]
    tempcolor21 = pcolors[21]
    tempcolor22 = pcolors[22]
    tempcolor23 = pcolors[23]
    tempcolor24 = pcolors[24]
    tempcolor25 = pcolors[25]
    tempcolor26 = pcolors[26]
    tempcolor27 = pcolors[27]
    tempcolor28 = pcolors[28]
    tempcolor29 = pcolors[29]
    tempcolor30 = pcolors[30]
    tempcolor31 = pcolors[31]

    pcolors[16] = tempcolor25
    pcolors[18] = tempcolor26
    pcolors[17] = tempcolor27
    pcolors[21] = tempcolor28
    pcolors[20] = tempcolor29
    pcolors[26] = tempcolor30
    pcolors[25] = tempcolor31

    pcolors[31] = tempcolor16
    pcolors[30] = tempcolor18
    pcolors[24] = tempcolor17
    pcolors[23] = tempcolor21
    pcolors[19] = tempcolor20
    pcolors[18] = tempcolor26
    pcolors[16] = tempcolor25

    pcolors[25] = tempcolor31
    pcolors[26] = tempcolor30
    pcolors[27] = tempcolor24
    pcolors[28] = tempcolor23
    pcolors[29] = tempcolor19
    pcolors[30] = tempcolor18
    pcolors[31] = tempcolor16
    updateGui()
    return pcolors

def rBottomCounterClock(pcolors):

    #handle the red, yellow, green
    tempcolor1 = pcolors[9]
    tempcolor2 = pcolors[10]
    tempcolor3 = pcolors[11]
    tempcolor4 = pcolors[12]
    tempcolor5 = pcolors[13]
    tempcolor6 = pcolors[14]
    tempcolor7 = pcolors[15]

    pcolors[9] = pcolors[41]
    pcolors[10] = pcolors[42]
    pcolors[11] = pcolors[43]
    pcolors[12] = pcolors[44]
    pcolors[13] = pcolors[45]
    pcolors[14] = pcolors[46]
    pcolors[15] = pcolors[47]

    pcolors[41] = pcolors[57]
    pcolors[42] = pcolors[58]
    pcolors[43] = pcolors[59]
    pcolors[44] = pcolors[60]
    pcolors[45] = pcolors[61]
    pcolors[46] = pcolors[62]
    pcolors[47] = pcolors[63]

    pcolors[57] = tempcolor1
    pcolors[58] = tempcolor2
    pcolors[59] = tempcolor3
    pcolors[60] = tempcolor4
    pcolors[61] = tempcolor5
    pcolors[62] = tempcolor6
    pcolors[63] = tempcolor7

    #handle the blue underbelly
    tempcolor16 = pcolors[16]
    tempcolor17 = pcolors[17]
    tempcolor18 = pcolors[18]
    tempcolor19 = pcolors[19]
    tempcolor20 = pcolors[20]
    tempcolor21 = pcolors[21]
    tempcolor22 = pcolors[22]
    tempcolor23 = pcolors[23]
    tempcolor24 = pcolors[24]
    tempcolor25 = pcolors[25]
    tempcolor26 = pcolors[26]
    tempcolor27 = pcolors[27]
    tempcolor28 = pcolors[28]
    tempcolor29 = pcolors[29]
    tempcolor30 = pcolors[30]
    tempcolor31 = pcolors[31]

    pcolors[31] = tempcolor25
    pcolors[30] = tempcolor26
    pcolors[24] = tempcolor27
    pcolors[23] = tempcolor28
    pcolors[19] = tempcolor29
    pcolors[18] = tempcolor30
    pcolors[16] = tempcolor31

    pcolors[16] = tempcolor31
    pcolors[18] = tempcolor30
    pcolors[17] = tempcolor24
    pcolors[21] = tempcolor23
    pcolors[20] = tempcolor19
    pcolors[26] = tempcolor18
    pcolors[25] = tempcolor16

    pcolors[25] = tempcolor16
    pcolors[26] = tempcolor18
    pcolors[27] = tempcolor17
    pcolors[28] = tempcolor21
    pcolors[29] = tempcolor20
    pcolors[30] = tempcolor26
    pcolors[31] = tempcolor25
    updateGui()
    return pcolors

#Blues
def bTopClock(pcolors):
    tempcolor0 = pcolors[0]
    tempcolor1 = pcolors[1]
    tempcolor2 = pcolors[2]
    tempcolor3 = pcolors[3]
    tempcolor4 = pcolors[4]
    tempcolor5 = pcolors[5]
    tempcolor7 = pcolors[7]
    tempcolor8 = pcolors[8]
    tempcolor9 = pcolors[9]
    tempcolor10 = pcolors[10]
    tempcolor11 = pcolors[11]
    tempcolor12 = pcolors[12]
    tempcolor13 = pcolors[13]
    tempcolor14 = pcolors[14]
    tempcolor15 = pcolors[15]

    pcolors[0] = tempcolor9
    pcolors[2] = tempcolor10
    pcolors[1] = tempcolor11
    pcolors[5] = tempcolor12
    pcolors[4] = tempcolor13
    pcolors[10] = tempcolor14
    pcolors[9] = tempcolor15

    pcolors[15] = tempcolor0
    pcolors[14] = tempcolor2
    pcolors[8] = tempcolor1
    pcolors[7] = tempcolor5
    pcolors[3] = tempcolor4
    pcolors[2] = tempcolor10
    pcolors[0] = tempcolor9

    pcolors[9] = tempcolor15
    pcolors[10] = tempcolor14
    pcolors[11] = tempcolor8
    pcolors[12] = tempcolor7
    pcolors[13] = tempcolor3
    pcolors[14] = tempcolor2
    pcolors[15] = tempcolor0

    tempcolor25 = pcolors[25]
    tempcolor26 = pcolors[26]
    tempcolor27 = pcolors[27]
    tempcolor28 = pcolors[28]
    tempcolor29 = pcolors[29]
    tempcolor30 = pcolors[30]
    tempcolor31 = pcolors[31]

    pcolors[25] = pcolors[32]
    pcolors[26] = pcolors[34]
    pcolors[27] = pcolors[35]
    pcolors[28] = pcolors[39]
    pcolors[29] = pcolors[40]
    pcolors[30] = pcolors[46]
    pcolors[31] = pcolors[47]

    pcolors[32] = pcolors[57]
    pcolors[34] = pcolors[58]
    pcolors[35] = pcolors[52]
    pcolors[39] = pcolors[53]
    pcolors[40] = pcolors[49]
    pcolors[46] = pcolors[50]
    pcolors[47] = pcolors[48]

    pcolors[57] = tempcolor25
    pcolors[58] = tempcolor26
    pcolors[52] = tempcolor27
    pcolors[53] = tempcolor28
    pcolors[49] = tempcolor29
    pcolors[50] = tempcolor30
    pcolors[48] = tempcolor31
    updateGui()
    return pcolors

def bTopCounterClock(pcolors):

    tempcolor0 = pcolors[0]
    tempcolor1 = pcolors[1]
    tempcolor2 = pcolors[2]
    tempcolor3 = pcolors[3]
    tempcolor4 = pcolors[4]
    tempcolor5 = pcolors[5]
    tempcolor7 = pcolors[7]
    tempcolor8 = pcolors[8]
    tempcolor9 = pcolors[9]
    tempcolor10 = pcolors[10]
    tempcolor11 = pcolors[11]
    tempcolor12 = pcolors[12]
    tempcolor13 = pcolors[13]
    tempcolor14 = pcolors[14]
    tempcolor15 = pcolors[15]

    pcolors[15] = tempcolor9
    pcolors[14] = tempcolor10
    pcolors[8] = tempcolor11
    pcolors[7] = tempcolor12
    pcolors[3] = tempcolor13
    pcolors[2] = tempcolor14
    pcolors[0] = tempcolor15

    pcolors[0] = tempcolor15
    pcolors[2] = tempcolor14
    pcolors[1] = tempcolor8
    pcolors[5] = tempcolor7
    pcolors[4] = tempcolor3
    pcolors[10] = tempcolor2
    pcolors[9] = tempcolor0

    pcolors[9] = tempcolor0
    pcolors[10] = tempcolor2
    pcolors[11] = tempcolor1
    pcolors[12] = tempcolor5
    pcolors[13] = tempcolor4
    pcolors[14] = tempcolor10
    pcolors[15] = tempcolor9

    tempcolor25 = pcolors[25]
    tempcolor26 = pcolors[26]
    tempcolor27 = pcolors[27]
    tempcolor28 = pcolors[28]
    tempcolor29 = pcolors[29]
    tempcolor30 = pcolors[30]
    tempcolor31 = pcolors[31]

    pcolors[25] = pcolors[57]
    pcolors[26] = pcolors[58]
    pcolors[27] = pcolors[52]
    pcolors[28] = pcolors[53]
    pcolors[29] = pcolors[49]
    pcolors[30] = pcolors[50]
    pcolors[31] = pcolors[48]

    pcolors[57] = pcolors[32]
    pcolors[58] = pcolors[34]
    pcolors[52] = pcolors[35]
    pcolors[53] = pcolors[39]
    pcolors[49] = pcolors[40]
    pcolors[50] = pcolors[46]
    pcolors[48] = pcolors[47]

    pcolors[32] = tempcolor25
    pcolors[34] = tempcolor26
    pcolors[35] = tempcolor27
    pcolors[39] = tempcolor28
    pcolors[40] = tempcolor29
    pcolors[46] = tempcolor30
    pcolors[47] = tempcolor31
    updateGui()
    return pcolors

def bSecondClock(pcolors):
    #For traditional blue
    tempcolor20 = pcolors[20]
    tempcolor21 = pcolors[21]
    tempcolor22 = pcolors[22]
    tempcolor23 = pcolors[23]
    tempcolor24 = pcolors[24]

    #For traditional green
    tempcolor56 = pcolors[56]
    tempcolor55 = pcolors[55]
    tempcolor54 = pcolors[54]
    tempcolor53 = pcolors[53]
    tempcolor52 = pcolors[52]

    #For traditional yellow
    tempcolor40 = pcolors[40]
    tempcolor39 = pcolors[39]
    tempcolor38 = pcolors[38]
    tempcolor37 = pcolors[37]
    tempcolor36 = pcolors[36]

    pcolors[40] = tempcolor20
    pcolors[39] = tempcolor21
    pcolors[38] = tempcolor22
    pcolors[37] = tempcolor23
    pcolors[36] = tempcolor24

    pcolors[56] = tempcolor40
    pcolors[55] = tempcolor39
    pcolors[54] = tempcolor38
    pcolors[53] = tempcolor37
    pcolors[52] = tempcolor36

    pcolors[20] = tempcolor56
    pcolors[21] = tempcolor55
    pcolors[22] = tempcolor54
    pcolors[23] = tempcolor53
    pcolors[24] = tempcolor52
    updateGui()
    return pcolors

def bSecondCounterClock(pcolors):
    #For traditional blue
    tempcolor20 = pcolors[20]
    tempcolor21 = pcolors[21]
    tempcolor22 = pcolors[22]
    tempcolor23 = pcolors[23]
    tempcolor24 = pcolors[24]

    #For traditional green
    tempcolor56 = pcolors[56]
    tempcolor55 = pcolors[55]
    tempcolor54 = pcolors[54]
    tempcolor53 = pcolors[53]
    tempcolor52 = pcolors[52]

    #For traditional yellow
    tempcolor40 = pcolors[40]
    tempcolor39 = pcolors[39]
    tempcolor38 = pcolors[38]
    tempcolor37 = pcolors[37]
    tempcolor36 = pcolors[36]

    pcolors[56] = tempcolor20
    pcolors[55] = tempcolor21
    pcolors[54] = tempcolor22
    pcolors[53] = tempcolor23
    pcolors[52] = tempcolor24

    pcolors[40] = tempcolor56
    pcolors[39] = tempcolor55
    pcolors[38] = tempcolor54
    pcolors[37] = tempcolor53
    pcolors[36] = tempcolor52

    pcolors[20] = tempcolor40
    pcolors[21] = tempcolor39
    pcolors[22] = tempcolor38
    pcolors[23] = tempcolor37
    pcolors[24] = tempcolor36
    updateGui()
    return pcolors

def bThirdClock(pcolors):
    #I'm trying to go back to some sort of efficiency here
    tempcolor17 = pcolors[17]
    tempcolor18 = pcolors[18]
    tempcolor19 = pcolors[19]

    pcolors[17] = pcolors[51]
    pcolors[18] = pcolors[50]
    pcolors[19] = pcolors[49]

    pcolors[51] = pcolors[35]
    pcolors[50] = pcolors[34]
    pcolors[49] = pcolors[33]

    pcolors[35] = tempcolor17
    pcolors[34] = tempcolor18
    pcolors[33] = tempcolor19
    updateGui()
    return pcolors

def bThirdCounterClock(pcolors):
    tempcolor17 = pcolors[17]
    tempcolor18 = pcolors[18]
    tempcolor19 = pcolors[19]

    pcolors[17] = pcolors[35]
    pcolors[18] = pcolors[34]
    pcolors[19] = pcolors[33]

    pcolors[35] = pcolors[51]
    pcolors[34] = pcolors[50]
    pcolors[33] = pcolors[49]

    pcolors[51] = tempcolor17
    pcolors[50] = tempcolor18
    pcolors[49] = tempcolor19
    updateGui()
    return pcolors

def bBottomClock(pcolors):
    tempcolor16 = pcolors[16]
    pcolors[16] = pcolors[48]
    pcolors[48] = pcolors[32]
    pcolors[32] = tempcolor16
    updateGui()
    return pcolors

def bBottomCounterClock(pcolors):
    tempcolor16 = pcolors[16]
    pcolors[16] = pcolors[32]
    pcolors[32] = pcolors[48]
    pcolors[48] = tempcolor16
    updateGui()
    return pcolors

def gTopClock(pcolors):
    tempcolor = pcolors[0]
    pcolors[0] = pcolors[48]
    pcolors[48] = pcolors[32]
    pcolors[32] = tempcolor
    updateGui()
    return pcolors

def gTopCounterClock(pcolors):
    tempcolor = pcolors[0]
    pcolors[0] = pcolors[32]
    pcolors[32] = pcolors[48]
    pcolors[48] = tempcolor
    updateGui()
    return pcolors

def gSecondClock(pcolors):
    tempcolor1 = pcolors[1]
    tempcolor2 = pcolors[2]
    tempcolor3 = pcolors[3]

    pcolors[1] = pcolors[49]
    pcolors[2] = pcolors[50]
    pcolors[3] = pcolors[51]

    pcolors[49] = pcolors[33]
    pcolors[50] = pcolors[34]
    pcolors[51] = pcolors[35]

    pcolors[33] = tempcolor1
    pcolors[34] = tempcolor2
    pcolors[35] = tempcolor3
    updateGui()
    return pcolors

def gSecondCounterClock(pcolors):
    tempcolor1 = pcolors[1]
    tempcolor2 = pcolors[2]
    tempcolor3 = pcolors[3]

    pcolors[1] = pcolors[33]
    pcolors[2] = pcolors[34]
    pcolors[3] = pcolors[35]

    pcolors[33] = pcolors[49]
    pcolors[34] = pcolors[50]
    pcolors[35] = pcolors[51]

    pcolors[49] = tempcolor1
    pcolors[50] = tempcolor2
    pcolors[51] = tempcolor3
    updateGui()
    return pcolors

def gThirdClock(pcolors):
    tempcolor1 = pcolors[4]
    tempcolor2 = pcolors[5]
    tempcolor3 = pcolors[6]
    tempcolor4 = pcolors[7]
    tempcolor5 = pcolors[8]

    pcolors[4] = pcolors[52]
    pcolors[5] = pcolors[53]
    pcolors[6] = pcolors[54]
    pcolors[7] = pcolors[55]
    pcolors[8] = pcolors[56]

    pcolors[52] = pcolors[36]
    pcolors[53] = pcolors[37]
    pcolors[54] = pcolors[38]
    pcolors[55] = pcolors[39]
    pcolors[56] = pcolors[40]

    pcolors[36] = tempcolor1
    pcolors[37] = tempcolor2
    pcolors[38] = tempcolor3
    pcolors[39] = tempcolor4
    pcolors[40] = tempcolor5
    updateGui()
    return pcolors

def gThirdCounterClock(pcolors):
    tempcolor1 = pcolors[4]
    tempcolor2 = pcolors[5]
    tempcolor3 = pcolors[6]
    tempcolor4 = pcolors[7]
    tempcolor5 = pcolors[8]

    pcolors[4] = pcolors[36]
    pcolors[5] = pcolors[37]
    pcolors[6] = pcolors[38]
    pcolors[7] = pcolors[39]
    pcolors[8] = pcolors[40]

    pcolors[36] = pcolors[52]
    pcolors[37] = pcolors[53]
    pcolors[38] = pcolors[54]
    pcolors[39] = pcolors[55]
    pcolors[40] = pcolors[56]

    pcolors[52] = tempcolor1
    pcolors[53] = tempcolor2
    pcolors[54] = tempcolor3
    pcolors[55] = tempcolor4
    pcolors[56] = tempcolor5
    updateGui()
    return pcolors

def gBottomClock(pcolors):
    #handle the red, yellow, green
    tempcolor1 = pcolors[9]
    tempcolor2 = pcolors[10]
    tempcolor3 = pcolors[11]
    tempcolor4 = pcolors[12]
    tempcolor5 = pcolors[13]
    tempcolor6 = pcolors[14]
    tempcolor7 = pcolors[15]

    pcolors[9] = pcolors[57]
    pcolors[10] = pcolors[58]
    pcolors[11] = pcolors[59]
    pcolors[12] = pcolors[60]
    pcolors[13] = pcolors[61]
    pcolors[14] = pcolors[62]
    pcolors[15] = pcolors[63]

    pcolors[57] = pcolors[41]
    pcolors[58] = pcolors[42]
    pcolors[59] = pcolors[43]
    pcolors[60] = pcolors[44]
    pcolors[61] = pcolors[45]
    pcolors[62] = pcolors[46]
    pcolors[63] = pcolors[47]

    pcolors[41] = tempcolor1
    pcolors[42] = tempcolor2
    pcolors[43] = tempcolor3
    pcolors[44] = tempcolor4
    pcolors[45] = tempcolor5
    pcolors[46] = tempcolor6
    pcolors[47] = tempcolor7

    #handle the blue underbelly, brute force
    tempcolor16 = pcolors[16]
    tempcolor17 = pcolors[17]
    tempcolor18 = pcolors[18]
    tempcolor19 = pcolors[19]
    tempcolor20 = pcolors[20]
    tempcolor21 = pcolors[21]
    tempcolor22 = pcolors[22]
    tempcolor23 = pcolors[23]
    tempcolor24 = pcolors[24]
    tempcolor25 = pcolors[25]
    tempcolor26 = pcolors[26]
    tempcolor27 = pcolors[27]
    tempcolor28 = pcolors[28]
    tempcolor29 = pcolors[29]
    tempcolor30 = pcolors[30]
    tempcolor31 = pcolors[31]

    pcolors[16] = tempcolor25
    pcolors[18] = tempcolor26
    pcolors[17] = tempcolor27
    pcolors[21] = tempcolor28
    pcolors[20] = tempcolor29
    pcolors[26] = tempcolor30
    pcolors[25] = tempcolor31

    pcolors[31] = tempcolor16
    pcolors[30] = tempcolor18
    pcolors[24] = tempcolor17
    pcolors[23] = tempcolor21
    pcolors[19] = tempcolor20
    pcolors[18] = tempcolor26
    pcolors[16] = tempcolor25

    pcolors[25] = tempcolor31
    pcolors[26] = tempcolor30
    pcolors[27] = tempcolor24
    pcolors[28] = tempcolor23
    pcolors[29] = tempcolor19
    pcolors[30] = tempcolor18
    pcolors[31] = tempcolor16
    updateGui()
    return pcolors

def gBottomCounterClock(pcolors):
     #handle the red, yellow, green
    tempcolor1 = pcolors[9]
    tempcolor2 = pcolors[10]
    tempcolor3 = pcolors[11]
    tempcolor4 = pcolors[12]
    tempcolor5 = pcolors[13]
    tempcolor6 = pcolors[14]
    tempcolor7 = pcolors[15]

    pcolors[9] = pcolors[41]
    pcolors[10] = pcolors[42]
    pcolors[11] = pcolors[43]
    pcolors[12] = pcolors[44]
    pcolors[13] = pcolors[45]
    pcolors[14] = pcolors[46]
    pcolors[15] = pcolors[47]

    pcolors[41] = pcolors[57]
    pcolors[42] = pcolors[58]
    pcolors[43] = pcolors[59]
    pcolors[44] = pcolors[60]
    pcolors[45] = pcolors[61]
    pcolors[46] = pcolors[62]
    pcolors[47] = pcolors[63]

    pcolors[57] = tempcolor1
    pcolors[58] = tempcolor2
    pcolors[59] = tempcolor3
    pcolors[60] = tempcolor4
    pcolors[61] = tempcolor5
    pcolors[62] = tempcolor6
    pcolors[63] = tempcolor7

    #handle the blue underbelly
    tempcolor16 = pcolors[16]
    tempcolor17 = pcolors[17]
    tempcolor18 = pcolors[18]
    tempcolor19 = pcolors[19]
    tempcolor20 = pcolors[20]
    tempcolor21 = pcolors[21]
    tempcolor22 = pcolors[22]
    tempcolor23 = pcolors[23]
    tempcolor24 = pcolors[24]
    tempcolor25 = pcolors[25]
    tempcolor26 = pcolors[26]
    tempcolor27 = pcolors[27]
    tempcolor28 = pcolors[28]
    tempcolor29 = pcolors[29]
    tempcolor30 = pcolors[30]
    tempcolor31 = pcolors[31]

    pcolors[31] = tempcolor25
    pcolors[30] = tempcolor26
    pcolors[24] = tempcolor27
    pcolors[23] = tempcolor28
    pcolors[19] = tempcolor29
    pcolors[18] = tempcolor30
    pcolors[16] = tempcolor31

    pcolors[16] = tempcolor31
    pcolors[18] = tempcolor30
    pcolors[17] = tempcolor24
    pcolors[21] = tempcolor23
    pcolors[20] = tempcolor19
    pcolors[26] = tempcolor18
    pcolors[25] = tempcolor16

    pcolors[25] = tempcolor16
    pcolors[26] = tempcolor18
    pcolors[27] = tempcolor17
    pcolors[28] = tempcolor21
    pcolors[29] = tempcolor20
    pcolors[30] = tempcolor26
    pcolors[31] = tempcolor25
    updateGui()
    return pcolors

def yTopClock(pcolors):
    tempcolor = pcolors[0]
    pcolors[0] = pcolors[48]
    pcolors[48] = pcolors[32]
    pcolors[32] = tempcolor
    updateGui()
    return pcolors

def yTopCounterClock(pcolors):
    tempcolor = pcolors[0]
    pcolors[0] = pcolors[32]
    pcolors[32] = pcolors[48]
    pcolors[48] = tempcolor
    updateGui()
    return pcolors

def ySecondClock(pcolors):
    tempcolor1 = pcolors[1]
    tempcolor2 = pcolors[2]
    tempcolor3 = pcolors[3]

    pcolors[1] = pcolors[49]
    pcolors[2] = pcolors[50]
    pcolors[3] = pcolors[51]

    pcolors[49] = pcolors[33]
    pcolors[50] = pcolors[34]
    pcolors[51] = pcolors[35]

    pcolors[33] = tempcolor1
    pcolors[34] = tempcolor2
    pcolors[35] = tempcolor3
    updateGui()
    return pcolors

def ySecondCounterClock(pcolors):
    tempcolor1 = pcolors[1]
    tempcolor2 = pcolors[2]
    tempcolor3 = pcolors[3]

    pcolors[1] = pcolors[33]
    pcolors[2] = pcolors[34]
    pcolors[3] = pcolors[35]

    pcolors[33] = pcolors[49]
    pcolors[34] = pcolors[50]
    pcolors[35] = pcolors[51]

    pcolors[49] = tempcolor1
    pcolors[50] = tempcolor2
    pcolors[51] = tempcolor3
    updateGui()
    return pcolors

def yThirdClock(pcolors):
    tempcolor1 = pcolors[4]
    tempcolor2 = pcolors[5]
    tempcolor3 = pcolors[6]
    tempcolor4 = pcolors[7]
    tempcolor5 = pcolors[8]

    pcolors[4] = pcolors[52]
    pcolors[5] = pcolors[53]
    pcolors[6] = pcolors[54]
    pcolors[7] = pcolors[55]
    pcolors[8] = pcolors[56]

    pcolors[52] = pcolors[36]
    pcolors[53] = pcolors[37]
    pcolors[54] = pcolors[38]
    pcolors[55] = pcolors[39]
    pcolors[56] = pcolors[40]

    pcolors[36] = tempcolor1
    pcolors[37] = tempcolor2
    pcolors[38] = tempcolor3
    pcolors[39] = tempcolor4
    pcolors[40] = tempcolor5
    updateGui()
    return pcolors

def yThirdCounterClock(pcolors):
    tempcolor1 = pcolors[4]
    tempcolor2 = pcolors[5]
    tempcolor3 = pcolors[6]
    tempcolor4 = pcolors[7]
    tempcolor5 = pcolors[8]

    pcolors[4] = pcolors[36]
    pcolors[5] = pcolors[37]
    pcolors[6] = pcolors[38]
    pcolors[7] = pcolors[39]
    pcolors[8] = pcolors[40]

    pcolors[36] = pcolors[52]
    pcolors[37] = pcolors[53]
    pcolors[38] = pcolors[54]
    pcolors[39] = pcolors[55]
    pcolors[40] = pcolors[56]

    pcolors[52] = tempcolor1
    pcolors[53] = tempcolor2
    pcolors[54] = tempcolor3
    pcolors[55] = tempcolor4
    pcolors[56] = tempcolor5
    updateGui()
    return pcolors

def yBottomClock(pcolors):
    #handle the red, yellow, green
    tempcolor1 = pcolors[9]
    tempcolor2 = pcolors[10]
    tempcolor3 = pcolors[11]
    tempcolor4 = pcolors[12]
    tempcolor5 = pcolors[13]
    tempcolor6 = pcolors[14]
    tempcolor7 = pcolors[15]

    pcolors[9] = pcolors[57]
    pcolors[10] = pcolors[58]
    pcolors[11] = pcolors[59]
    pcolors[12] = pcolors[60]
    pcolors[13] = pcolors[61]
    pcolors[14] = pcolors[62]
    pcolors[15] = pcolors[63]

    pcolors[57] = pcolors[41]
    pcolors[58] = pcolors[42]
    pcolors[59] = pcolors[43]
    pcolors[60] = pcolors[44]
    pcolors[61] = pcolors[45]
    pcolors[62] = pcolors[46]
    pcolors[63] = pcolors[47]

    pcolors[41] = tempcolor1
    pcolors[42] = tempcolor2
    pcolors[43] = tempcolor3
    pcolors[44] = tempcolor4
    pcolors[45] = tempcolor5
    pcolors[46] = tempcolor6
    pcolors[47] = tempcolor7

    #handle the blue underbelly, brute force
    tempcolor16 = pcolors[16]
    tempcolor17 = pcolors[17]
    tempcolor18 = pcolors[18]
    tempcolor19 = pcolors[19]
    tempcolor20 = pcolors[20]
    tempcolor21 = pcolors[21]
    tempcolor22 = pcolors[22]
    tempcolor23 = pcolors[23]
    tempcolor24 = pcolors[24]
    tempcolor25 = pcolors[25]
    tempcolor26 = pcolors[26]
    tempcolor27 = pcolors[27]
    tempcolor28 = pcolors[28]
    tempcolor29 = pcolors[29]
    tempcolor30 = pcolors[30]
    tempcolor31 = pcolors[31]

    pcolors[16] = tempcolor25
    pcolors[18] = tempcolor26
    pcolors[17] = tempcolor27
    pcolors[21] = tempcolor28
    pcolors[20] = tempcolor29
    pcolors[26] = tempcolor30
    pcolors[25] = tempcolor31

    pcolors[31] = tempcolor16
    pcolors[30] = tempcolor18
    pcolors[24] = tempcolor17
    pcolors[23] = tempcolor21
    pcolors[19] = tempcolor20
    pcolors[18] = tempcolor26
    pcolors[16] = tempcolor25

    pcolors[25] = tempcolor31
    pcolors[26] = tempcolor30
    pcolors[27] = tempcolor24
    pcolors[28] = tempcolor23
    pcolors[29] = tempcolor19
    pcolors[30] = tempcolor18
    pcolors[31] = tempcolor16
    updateGui()
    return pcolors

def yBottomCounterClock(pcolors):
     #handle the red, yellow, green
    tempcolor1 = pcolors[9]
    tempcolor2 = pcolors[10]
    tempcolor3 = pcolors[11]
    tempcolor4 = pcolors[12]
    tempcolor5 = pcolors[13]
    tempcolor6 = pcolors[14]
    tempcolor7 = pcolors[15]

    pcolors[9] = pcolors[41]
    pcolors[10] = pcolors[42]
    pcolors[11] = pcolors[43]
    pcolors[12] = pcolors[44]
    pcolors[13] = pcolors[45]
    pcolors[14] = pcolors[46]
    pcolors[15] = pcolors[47]

    pcolors[41] = pcolors[57]
    pcolors[42] = pcolors[58]
    pcolors[43] = pcolors[59]
    pcolors[44] = pcolors[60]
    pcolors[45] = pcolors[61]
    pcolors[46] = pcolors[62]
    pcolors[47] = pcolors[63]

    pcolors[57] = tempcolor1
    pcolors[58] = tempcolor2
    pcolors[59] = tempcolor3
    pcolors[60] = tempcolor4
    pcolors[61] = tempcolor5
    pcolors[62] = tempcolor6
    pcolors[63] = tempcolor7

    #handle the blue underbelly
    tempcolor16 = pcolors[16]
    tempcolor17 = pcolors[17]
    tempcolor18 = pcolors[18]
    tempcolor19 = pcolors[19]
    tempcolor20 = pcolors[20]
    tempcolor21 = pcolors[21]
    tempcolor22 = pcolors[22]
    tempcolor23 = pcolors[23]
    tempcolor24 = pcolors[24]
    tempcolor25 = pcolors[25]
    tempcolor26 = pcolors[26]
    tempcolor27 = pcolors[27]
    tempcolor28 = pcolors[28]
    tempcolor29 = pcolors[29]
    tempcolor30 = pcolors[30]
    tempcolor31 = pcolors[31]

    pcolors[31] = tempcolor25
    pcolors[30] = tempcolor26
    pcolors[24] = tempcolor27
    pcolors[23] = tempcolor28
    pcolors[19] = tempcolor29
    pcolors[18] = tempcolor30
    pcolors[16] = tempcolor31

    pcolors[16] = tempcolor31
    pcolors[18] = tempcolor30
    pcolors[17] = tempcolor24
    pcolors[21] = tempcolor23
    pcolors[20] = tempcolor19
    pcolors[26] = tempcolor18
    pcolors[25] = tempcolor16

    pcolors[25] = tempcolor16
    pcolors[26] = tempcolor18
    pcolors[27] = tempcolor17
    pcolors[28] = tempcolor21
    pcolors[29] = tempcolor20
    pcolors[30] = tempcolor26
    pcolors[31] = tempcolor25
    updateGui()
    return pcolors


#Below here is the nightmare that is the pyramidal turns


#This is the same as the gBRFPCU
def yBLFPC(pcolors):
    tempcolor33 = pcolors[33]
    tempcolor36 = pcolors[36]
    tempcolor37 = pcolors[37]
    tempcolor38 = pcolors[38]
    tempcolor41=  pcolors[41]
    tempcolor42 = pcolors[42]
    tempcolor43 = pcolors[43]
    tempcolor44 = pcolors[44]
    tempcolor45 = pcolors[45]

    pcolors[33] = pcolors[29]
    pcolors[36] = pcolors[27]
    pcolors[37] = pcolors[28]
    pcolors[38] = pcolors[22]
    pcolors[41] = pcolors[25]
    pcolors[42] = pcolors[26]
    pcolors[43] = pcolors[20]
    pcolors[44] = pcolors[21]
    pcolors[45] = pcolors[17]

    pcolors[29] = pcolors[59]
    pcolors[27] = pcolors[61]
    pcolors[28] = pcolors[60]
    pcolors[22] = pcolors[54]
    pcolors[25] = pcolors[63]
    pcolors[26] = pcolors[62]
    pcolors[20] = pcolors[56]
    pcolors[21] = pcolors[55]
    pcolors[17] = pcolors[51]

    pcolors[59] = tempcolor33
    pcolors[61] = tempcolor36
    pcolors[60] = tempcolor37
    pcolors[54] = tempcolor38
    pcolors[63] = tempcolor41
    pcolors[62] = tempcolor42
    pcolors[56] = tempcolor43
    pcolors[55] = tempcolor44
    pcolors[51] = tempcolor45
    updateGui()
    return pcolors

#This is the same as the gBRFPC
def yBLFPCU(pcolors):
    tempcolor33 = pcolors[33]
    tempcolor36 = pcolors[36]
    tempcolor37 = pcolors[37]
    tempcolor38 = pcolors[38]
    tempcolor41=  pcolors[41]
    tempcolor42 = pcolors[42]
    tempcolor43 = pcolors[43]
    tempcolor44 = pcolors[44]
    tempcolor45 = pcolors[45]

    pcolors[33] = pcolors[59]
    pcolors[36] = pcolors[61]
    pcolors[37] = pcolors[60]
    pcolors[38] = pcolors[54]
    pcolors[41] = pcolors[63]
    pcolors[42] = pcolors[62]
    pcolors[43] = pcolors[56]
    pcolors[44] = pcolors[55]
    pcolors[45] = pcolors[51]

    pcolors[59] = pcolors[29]
    pcolors[61] = pcolors[27]
    pcolors[60] = pcolors[28]
    pcolors[54] = pcolors[22]
    pcolors[63] = pcolors[25]
    pcolors[62] = pcolors[26]
    pcolors[56] = pcolors[20]
    pcolors[55] = pcolors[21]
    pcolors[51] = pcolors[17]

    pcolors[29] = tempcolor33
    pcolors[27] = tempcolor36
    pcolors[28] = tempcolor37
    pcolors[22] = tempcolor38
    pcolors[25] = tempcolor41
    pcolors[26] = tempcolor42
    pcolors[20] = tempcolor43
    pcolors[21] = tempcolor44
    pcolors[17] = tempcolor45
    updateGui()
    return pcolors

#This is the same as the gBRTPCU
def yBLTPC(pcolors):
    tempcolor36 = pcolors[36]
    tempcolor41 = pcolors[41]
    tempcolor42 = pcolors[42]
    tempcolor43 = pcolors[43]

    pcolors[36] = pcolors[27]
    pcolors[41] = pcolors[25]
    pcolors[42] = pcolors[26]
    pcolors[43] = pcolors[20]

    pcolors[27] = pcolors[61]
    pcolors[25] = pcolors[63]
    pcolors[26] = pcolors[62]
    pcolors[20] = pcolors[56]

    pcolors[61] = tempcolor36
    pcolors[63] = tempcolor41
    pcolors[62] = tempcolor42
    pcolors[56] = tempcolor43
    updateGui()
    return pcolors

#This is the same as the gBRTPC
def yBLTPCU(pcolors):
    tempcolor36 = pcolors[36]
    tempcolor41 = pcolors[41]
    tempcolor42 = pcolors[42]
    tempcolor43 = pcolors[43]

    pcolors[36] = pcolors[61]
    pcolors[41] = pcolors[63]
    pcolors[42] = pcolors[62]
    pcolors[43] = pcolors[56]

    pcolors[61] = pcolors[27]
    pcolors[63] = pcolors[25]
    pcolors[62] = pcolors[26]
    pcolors[56] = pcolors[20]

    pcolors[27] = tempcolor36
    pcolors[25] = tempcolor41
    pcolors[26] = tempcolor42
    pcolors[20] = tempcolor43
    updateGui()
    return pcolors

#The same as rBLFPCU
def yBRFPC(pcolors):
    tempcolor1 = pcolors[1]
    tempcolor4 = pcolors[4]
    tempcolor5 = pcolors[5]
    tempcolor6 = pcolors[6]
    tempcolor9 = pcolors[9]
    tempcolor10 = pcolors[10]
    tempcolor11 = pcolors[11]
    tempcolor12 = pcolors[12]
    tempcolor13 = pcolors[13]

    pcolors[1] = pcolors[43]
    pcolors[4] = pcolors[45]
    pcolors[5] = pcolors[44]
    pcolors[6] = pcolors[38]
    pcolors[9] = pcolors[47]
    pcolors[10] = pcolors[46]
    pcolors[11] = pcolors[40]
    pcolors[12] = pcolors[39]
    pcolors[13] = pcolors[35]

    pcolors[43] = pcolors[29]
    pcolors[45] = pcolors[27]
    pcolors[44] = pcolors[28]
    pcolors[38] = pcolors[22]
    pcolors[47] = pcolors[25]
    pcolors[46] = pcolors[26]
    pcolors[40] = pcolors[20]
    pcolors[39] = pcolors[21]
    pcolors[35] = pcolors[17]

    pcolors[29] = tempcolor1
    pcolors[27] = tempcolor4
    pcolors[28] = tempcolor5
    pcolors[22] = tempcolor6
    pcolors[25] = tempcolor9
    pcolors[26] = tempcolor10
    pcolors[20] = tempcolor11
    pcolors[21] = tempcolor12
    pcolors[17] = tempcolor13
    updateGui()
    return pcolors

#The same as rBLFPC
def yBRFPCU(pcolors):
    tempcolor1 = pcolors[1]
    tempcolor4 = pcolors[4]
    tempcolor5 = pcolors[5]
    tempcolor6 = pcolors[6]
    tempcolor9 = pcolors[9]
    tempcolor10 = pcolors[10]
    tempcolor11 = pcolors[11]
    tempcolor12 = pcolors[12]
    tempcolor13 = pcolors[13]

    pcolors[1] = pcolors[29]
    pcolors[4] = pcolors[27]
    pcolors[5] = pcolors[28]
    pcolors[6] = pcolors[22]
    pcolors[9] = pcolors[25]
    pcolors[10] = pcolors[26]
    pcolors[11] = pcolors[20]
    pcolors[12] = pcolors[21]
    pcolors[13] = pcolors[17]

    pcolors[29] = pcolors[43]
    pcolors[27] = pcolors[45]
    pcolors[28] = pcolors[44]
    pcolors[22] = pcolors[38]
    pcolors[25] = pcolors[47]
    pcolors[26] = pcolors[46]
    pcolors[20] = pcolors[40]
    pcolors[21] = pcolors[39]
    pcolors[17] = pcolors[35]

    pcolors[43] = tempcolor1
    pcolors[45] = tempcolor4
    pcolors[44] = tempcolor5
    pcolors[38] = tempcolor6
    pcolors[47] = tempcolor9
    pcolors[46] = tempcolor10
    pcolors[40] = tempcolor11
    pcolors[39] = tempcolor12
    pcolors[35] = tempcolor13
    updateGui()
    return pcolors

#The same as rBLTPCU
def yBRTPC(pcolors):
    tempcolor4 = pcolors[4]
    tempcolor9 = pcolors[9]
    tempcolor10 = pcolors[10]
    tempcolor11 = pcolors[11]

    pcolors[4] = pcolors[45]
    pcolors[9] = pcolors[47]
    pcolors[10] = pcolors[46]
    pcolors[11] = pcolors[40]

    pcolors[45] = pcolors[27]
    pcolors[47] = pcolors[25]
    pcolors[46] = pcolors[26]
    pcolors[40] = pcolors[20]

    pcolors[27] = tempcolor4
    pcolors[25] = tempcolor9
    pcolors[26] = tempcolor10
    pcolors[20] = tempcolor11
    updateGui()
    return pcolors

#The same as rBLTPC
def yBRTPCU(pcolors):
    tempcolor4 = pcolors[4]
    tempcolor9 = pcolors[9]
    tempcolor10 = pcolors[10]
    tempcolor11 = pcolors[11]

    pcolors[4] = pcolors[27]
    pcolors[9] = pcolors[25]
    pcolors[10] = pcolors[26]
    pcolors[11] = pcolors[20]

    pcolors[27] = pcolors[45]
    pcolors[25] = pcolors[47]
    pcolors[26] = pcolors[46]
    pcolors[20] = pcolors[40]

    pcolors[45] = tempcolor4
    pcolors[47] = tempcolor9
    pcolors[46] = tempcolor10
    pcolors[40] = tempcolor11
    updateGui()
    return pcolors

#The same as rBRFPCU
def gBLFPC(pcolors):
    tempcolor3 = pcolors[3]
    tempcolor6 = pcolors[6]
    tempcolor7 = pcolors[7]
    tempcolor8 = pcolors[8]
    tempcolor11 = pcolors[11]
    tempcolor12 = pcolors[12]
    tempcolor13 = pcolors[13]
    tempcolor14 = pcolors[14]
    tempcolor15 = pcolors[15]

    pcolors[3] = pcolors[61]
    pcolors[6] = pcolors[54]
    pcolors[7] = pcolors[60]
    pcolors[8] = pcolors[59]
    pcolors[11] = pcolors[49]
    pcolors[12] = pcolors[53]
    pcolors[13] = pcolors[52]
    pcolors[14] = pcolors[58]
    pcolors[15] = pcolors[57]

    pcolors[61] = pcolors[27]
    pcolors[54] = pcolors[22]
    pcolors[60] = pcolors[28]
    pcolors[59] = pcolors[29]
    pcolors[49] = pcolors[19]
    pcolors[53] = pcolors[23]
    pcolors[52] = pcolors[24]
    pcolors[58] = pcolors[30]
    pcolors[57] = pcolors[31]

    pcolors[27] = tempcolor3
    pcolors[22] = tempcolor6
    pcolors[28] = tempcolor7
    pcolors[29] = tempcolor8
    pcolors[19] = tempcolor11
    pcolors[23] = tempcolor12
    pcolors[24] = tempcolor13
    pcolors[30] = tempcolor14
    pcolors[31] = tempcolor15
    updateGui()
    return pcolors

#The same as rBRFPC
def gBLFPCU(pcolors):
    tempcolor3 = pcolors[3]
    tempcolor6 = pcolors[6]
    tempcolor7 = pcolors[7]
    tempcolor8 = pcolors[8]
    tempcolor11 = pcolors[11]
    tempcolor12 = pcolors[12]
    tempcolor13 = pcolors[13]
    tempcolor14 = pcolors[14]
    tempcolor15 = pcolors[15]

    pcolors[3] = pcolors[27]
    pcolors[6] = pcolors[22]
    pcolors[7] = pcolors[28]
    pcolors[8] = pcolors[29]
    pcolors[11] = pcolors[19]
    pcolors[12] = pcolors[23]
    pcolors[13] = pcolors[24]
    pcolors[14] = pcolors[30]
    pcolors[15] = pcolors[31]

    pcolors[27] = pcolors[61]
    pcolors[22] = pcolors[54]
    pcolors[28] = pcolors[60]
    pcolors[29] = pcolors[59]
    pcolors[19] = pcolors[49]
    pcolors[23] = pcolors[53]
    pcolors[24] = pcolors[52]
    pcolors[30] = pcolors[58]
    pcolors[31] = pcolors[57]

    pcolors[61] = tempcolor3
    pcolors[54] = tempcolor6
    pcolors[60] = tempcolor7
    pcolors[59] = tempcolor8
    pcolors[49] = tempcolor11
    pcolors[53] = tempcolor12
    pcolors[52] = tempcolor13
    pcolors[58] = tempcolor14
    pcolors[57] = tempcolor15
    updateGui()
    return pcolors

#The same as rBRTPCU
def gBLTPC(pcolors):
    tempcolor8 = pcolors[8]
    tempcolor13 = pcolors[13]
    tempcolor14 = pcolors[14]
    tempcolor15 = pcolors[15]

    pcolors[8] = pcolors[59]
    pcolors[13] = pcolors[52]
    pcolors[14] = pcolors[58]
    pcolors[15] = pcolors[57]

    pcolors[59] = pcolors[29]
    pcolors[52] = pcolors[24]
    pcolors[58] = pcolors[30]
    pcolors[57] = pcolors[31]

    pcolors[29] = tempcolor8
    pcolors[24] = tempcolor13
    pcolors[30] = tempcolor14
    pcolors[31] = tempcolor15
    updateGui()
    return pcolors

#The same as rBRTPC
def gBLTPCU(pcolors):
    tempcolor8 = pcolors[8]
    tempcolor13 = pcolors[13]
    tepmcolor14 = pcolors[14]
    tempcolor15 = pcolors[15]

    pcolors[8] = pcolors[29]
    pcolors[13] = pcolors[24]
    pcolors[14] = pcolors[30]
    pcolors[15] = pcolors[31]

    pcolors[29] = pcolors[59]
    pcolors[24] = pcolors[52]
    pcolors[30] = pcolors[58]
    pcolors[31] = pcolors[57]

    pcolors[59] = tempcolor8
    pcolors[52] = tempcolor13
    pcolors[58] = tepmcolor14
    pcolors[57] = tempcolor15
    updateGui()
    return pcolors

def gBRFPC(pcolors):
    tempcolor33 = pcolors[33]
    tempcolor36 = pcolors[36]
    tempcolor37 = pcolors[37]
    tempcolor38 = pcolors[38]
    tempcolor41=  pcolors[41]
    tempcolor42 = pcolors[42]
    tempcolor43 = pcolors[43]
    tempcolor44 = pcolors[44]
    tempcolor45 = pcolors[45]

    pcolors[33] = pcolors[59]
    pcolors[36] = pcolors[61]
    pcolors[37] = pcolors[60]
    pcolors[38] = pcolors[54]
    pcolors[41] = pcolors[63]
    pcolors[42] = pcolors[62]
    pcolors[43] = pcolors[56]
    pcolors[44] = pcolors[55]
    pcolors[45] = pcolors[51]

    pcolors[59] = pcolors[29]
    pcolors[61] = pcolors[27]
    pcolors[60] = pcolors[28]
    pcolors[54] = pcolors[22]
    pcolors[63] = pcolors[25]
    pcolors[62] = pcolors[26]
    pcolors[56] = pcolors[20]
    pcolors[55] = pcolors[21]
    pcolors[51] = pcolors[17]

    pcolors[29] = tempcolor33
    pcolors[27] = tempcolor36
    pcolors[28] = tempcolor37
    pcolors[22] = tempcolor38
    pcolors[25] = tempcolor41
    pcolors[26] = tempcolor42
    pcolors[20] = tempcolor43
    pcolors[21] = tempcolor44
    pcolors[17] = tempcolor45
    updateGui()
    return pcolors

def gBRFPCU(pcolors):
    tempcolor33 = pcolors[33]
    tempcolor36 = pcolors[36]
    tempcolor37 = pcolors[37]
    tempcolor38 = pcolors[38]
    tempcolor41=  pcolors[41]
    tempcolor42 = pcolors[42]
    tempcolor43 = pcolors[43]
    tempcolor44 = pcolors[44]
    tempcolor45 = pcolors[45]

    pcolors[33] = pcolors[29]
    pcolors[36] = pcolors[27]
    pcolors[37] = pcolors[28]
    pcolors[38] = pcolors[22]
    pcolors[41] = pcolors[25]
    pcolors[42] = pcolors[26]
    pcolors[43] = pcolors[20]
    pcolors[44] = pcolors[21]
    pcolors[45] = pcolors[17]

    pcolors[29] = pcolors[59]
    pcolors[27] = pcolors[61]
    pcolors[28] = pcolors[60]
    pcolors[22] = pcolors[54]
    pcolors[25] = pcolors[63]
    pcolors[26] = pcolors[62]
    pcolors[20] = pcolors[56]
    pcolors[21] = pcolors[55]
    pcolors[17] = pcolors[51]

    pcolors[59] = tempcolor33
    pcolors[61] = tempcolor36
    pcolors[60] = tempcolor37
    pcolors[54] = tempcolor38
    pcolors[63] = tempcolor41
    pcolors[62] = tempcolor42
    pcolors[56] = tempcolor43
    pcolors[55] = tempcolor44
    pcolors[51] = tempcolor45
    updateGui()
    return pcolors

def gBRTPC(pcolors):
    tempcolor36 = pcolors[36]
    tempcolor41 = pcolors[41]
    tempcolor42 = pcolors[42]
    tempcolor43 = pcolors[43]

    pcolors[36] = pcolors[61]
    pcolors[41] = pcolors[63]
    pcolors[42] = pcolors[62]
    pcolors[43] = pcolors[56]

    pcolors[61] = pcolors[27]
    pcolors[63] = pcolors[25]
    pcolors[62] = pcolors[26]
    pcolors[56] = pcolors[20]

    pcolors[27] = tempcolor36
    pcolors[25] = tempcolor41
    pcolors[26] = tempcolor42
    pcolors[20] = tempcolor43
    updateGui()
    return pcolors

def gBRTPCU(pcolors):
    tempcolor36 = pcolors[36]
    tempcolor41 = pcolors[41]
    tempcolor42 = pcolors[42]
    tempcolor43 = pcolors[43]

    pcolors[36] = pcolors[27]
    pcolors[41] = pcolors[25]
    pcolors[42] = pcolors[26]
    pcolors[43] = pcolors[20]

    pcolors[27] = pcolors[61]
    pcolors[25] = pcolors[63]
    pcolors[26] = pcolors[62]
    pcolors[20] = pcolors[56]

    pcolors[61] = tempcolor36
    pcolors[63] = tempcolor41
    pcolors[62] = tempcolor42
    pcolors[56] = tempcolor43
    updateGui()
    return pcolors

def rBLFPC(pcolors):
    tempcolor1 = pcolors[1]
    tempcolor4 = pcolors[4]
    tempcolor5 = pcolors[5]
    tempcolor6 = pcolors[6]
    tempcolor9 = pcolors[9]
    tempcolor10 = pcolors[10]
    tempcolor11 = pcolors[11]
    tempcolor12 = pcolors[12]
    tempcolor13 = pcolors[13]

    pcolors[1] = pcolors[29]
    pcolors[4] = pcolors[27]
    pcolors[5] = pcolors[28]
    pcolors[6] = pcolors[22]
    pcolors[9] = pcolors[25]
    pcolors[10] = pcolors[26]
    pcolors[11] = pcolors[20]
    pcolors[12] = pcolors[21]
    pcolors[13] = pcolors[17]

    pcolors[29] = pcolors[43]
    pcolors[27] = pcolors[45]
    pcolors[28] = pcolors[44]
    pcolors[22] = pcolors[38]
    pcolors[25] = pcolors[47]
    pcolors[26] = pcolors[46]
    pcolors[20] = pcolors[40]
    pcolors[21] = pcolors[39]
    pcolors[17] = pcolors[35]

    pcolors[43] = tempcolor1
    pcolors[45] = tempcolor4
    pcolors[44] = tempcolor5
    pcolors[38] = tempcolor6
    pcolors[47] = tempcolor9
    pcolors[46] = tempcolor10
    pcolors[40] = tempcolor11
    pcolors[39] = tempcolor12
    pcolors[35] = tempcolor13
    updateGui()
    return pcolors

def rBLFPCU(pcolors):
    tempcolor1 = pcolors[1]
    tempcolor4 = pcolors[4]
    tempcolor5 = pcolors[5]
    tempcolor6 = pcolors[6]
    tempcolor9 = pcolors[9]
    tempcolor10 = pcolors[10]
    tempcolor11 = pcolors[11]
    tempcolor12 = pcolors[12]
    tempcolor13 = pcolors[13]

    pcolors[1] = pcolors[43]
    pcolors[4] = pcolors[45]
    pcolors[5] = pcolors[44]
    pcolors[6] = pcolors[38]
    pcolors[9] = pcolors[47]
    pcolors[10] = pcolors[46]
    pcolors[11] = pcolors[40]
    pcolors[12] = pcolors[39]
    pcolors[13] = pcolors[35]

    pcolors[43] = pcolors[29]
    pcolors[45] = pcolors[27]
    pcolors[44] = pcolors[28]
    pcolors[38] = pcolors[22]
    pcolors[47] = pcolors[25]
    pcolors[46] = pcolors[26]
    pcolors[40] = pcolors[20]
    pcolors[39] = pcolors[21]
    pcolors[35] = pcolors[17]

    pcolors[29] = tempcolor1
    pcolors[27] = tempcolor4
    pcolors[28] = tempcolor5
    pcolors[22] = tempcolor6
    pcolors[25] = tempcolor9
    pcolors[26] = tempcolor10
    pcolors[20] = tempcolor11
    pcolors[21] = tempcolor12
    pcolors[17] = tempcolor13
    updateGui()
    return pcolors

def rBLTPC(pcolors):
    tempcolor4 = pcolors[4]
    tempcolor9 = pcolors[9]
    tempcolor10 = pcolors[10]
    tempcolor11 = pcolors[11]

    pcolors[4] = pcolors[27]
    pcolors[9] = pcolors[25]
    pcolors[10] = pcolors[26]
    pcolors[11] = pcolors[20]

    pcolors[27] = pcolors[45]
    pcolors[25] = pcolors[47]
    pcolors[26] = pcolors[46]
    pcolors[20] = pcolors[40]

    pcolors[45] = tempcolor4
    pcolors[47] = tempcolor9
    pcolors[46] = tempcolor10
    pcolors[40] = tempcolor11
    updateGui()
    return pcolors

def rBLTPCU(pcolors):
    tempcolor4 = pcolors[4]
    tempcolor9 = pcolors[9]
    tempcolor10 = pcolors[10]
    tempcolor11 = pcolors[11]

    pcolors[4] = pcolors[45]
    pcolors[9] = pcolors[47]
    pcolors[10] = pcolors[46]
    pcolors[11] = pcolors[40]

    pcolors[45] = pcolors[27]
    pcolors[47] = pcolors[25]
    pcolors[46] = pcolors[26]
    pcolors[40] = pcolors[20]

    pcolors[27] = tempcolor4
    pcolors[25] = tempcolor9
    pcolors[26] = tempcolor10
    pcolors[20] = tempcolor11
    updateGui()
    return pcolors

def rBRFPC(pcolors):
    tempcolor3 = pcolors[3]
    tempcolor6 = pcolors[6]
    tempcolor7 = pcolors[7]
    tempcolor8 = pcolors[8]
    tempcolor11 = pcolors[11]
    tempcolor12 = pcolors[12]
    tempcolor13 = pcolors[13]
    tempcolor14 = pcolors[14]
    tempcolor15 = pcolors[15]

    pcolors[3] = pcolors[27]
    pcolors[6] = pcolors[22]
    pcolors[7] = pcolors[28]
    pcolors[8] = pcolors[29]
    pcolors[11] = pcolors[19]
    pcolors[12] = pcolors[23]
    pcolors[13] = pcolors[24]
    pcolors[14] = pcolors[30]
    pcolors[15] = pcolors[31]

    pcolors[27] = pcolors[61]
    pcolors[22] = pcolors[54]
    pcolors[28] = pcolors[60]
    pcolors[29] = pcolors[59]
    pcolors[19] = pcolors[49]
    pcolors[23] = pcolors[53]
    pcolors[24] = pcolors[52]
    pcolors[30] = pcolors[58]
    pcolors[31] = pcolors[57]

    pcolors[61] = tempcolor3
    pcolors[54] = tempcolor6
    pcolors[60] = tempcolor7
    pcolors[59] = tempcolor8
    pcolors[49] = tempcolor11
    pcolors[53] = tempcolor12
    pcolors[52] = tempcolor13
    pcolors[58] = tempcolor14
    pcolors[57] = tempcolor15
    updateGui()
    return pcolors

def rBRFPCU(pcolors):
    tempcolor3 = pcolors[3]
    tempcolor6 = pcolors[6]
    tempcolor7 = pcolors[7]
    tempcolor8 = pcolors[8]
    tempcolor11 = pcolors[11]
    tempcolor12 = pcolors[12]
    tempcolor13 = pcolors[13]
    tempcolor14 = pcolors[14]
    tempcolor15 = pcolors[15]

    pcolors[3] = pcolors[61]
    pcolors[6] = pcolors[54]
    pcolors[7] = pcolors[60]
    pcolors[8] = pcolors[59]
    pcolors[11] = pcolors[49]
    pcolors[12] = pcolors[53]
    pcolors[13] = pcolors[52]
    pcolors[14] = pcolors[58]
    pcolors[15] = pcolors[57]

    pcolors[61] = pcolors[27]
    pcolors[54] = pcolors[22]
    pcolors[60] = pcolors[28]
    pcolors[59] = pcolors[29]
    pcolors[49] = pcolors[19]
    pcolors[53] = pcolors[23]
    pcolors[52] = pcolors[24]
    pcolors[58] = pcolors[30]
    pcolors[57] = pcolors[31]

    pcolors[27] = tempcolor3
    pcolors[22] = tempcolor6
    pcolors[28] = tempcolor7
    pcolors[29] = tempcolor8
    pcolors[19] = tempcolor11
    pcolors[23] = tempcolor12
    pcolors[24] = tempcolor13
    pcolors[30] = tempcolor14
    pcolors[31] = tempcolor15
    updateGui()
    return pcolors

def rBRTPC(pcolors):
    tempcolor8 = pcolors[8]
    tempcolor13 = pcolors[13]
    tepmcolor14 = pcolors[14]
    tempcolor15 = pcolors[15]

    pcolors[8] = pcolors[29]
    pcolors[13] = pcolors[24]
    pcolors[14] = pcolors[30]
    pcolors[15] = pcolors[31]

    pcolors[29] = pcolors[59]
    pcolors[24] = pcolors[52]
    pcolors[30] = pcolors[58]
    pcolors[31] = pcolors[57]

    pcolors[59] = tempcolor8
    pcolors[52] = tempcolor13
    pcolors[58] = tepmcolor14
    pcolors[57] = tempcolor15
    updateGui()
    return pcolors

def rBRTPCU(pcolors):
    tempcolor8 = pcolors[8]
    tempcolor13 = pcolors[13]
    tempcolor14 = pcolors[14]
    tempcolor15 = pcolors[15]

    pcolors[8] = pcolors[59]
    pcolors[13] = pcolors[52]
    pcolors[14] = pcolors[58]
    pcolors[15] = pcolors[57]

    pcolors[59] = pcolors[29]
    pcolors[52] = pcolors[24]
    pcolors[58] = pcolors[30]
    pcolors[57] = pcolors[31]

    pcolors[29] = tempcolor8
    pcolors[24] = tempcolor13
    pcolors[30] = tempcolor14
    pcolors[31] = tempcolor15
    updateGui()
    return pcolors

def rgbCC(pcolors):
    tempcolor9 = pcolors[9]
    pcolors[9] = pcolors[25]
    pcolors[25] = pcolors[63]
    pcolors[63] = tempcolor9
    updateGui()
    return pcolors

def rgbCCU(pcolors):
    tempcolor9 = pcolors[9]
    pcolors[9] = pcolors[63]
    pcolors[63] = pcolors[25]
    pcolors[25] = tempcolor9
    updateGui()
    return pcolors

def rybCC(pcolors):
    tempcolor15 = pcolors[15]
    pcolors[15] = pcolors[31]
    pcolors[31] = pcolors[41]
    pcolors[41] = tempcolor15
    updateGui()
    return pcolors

def rybCCU(pcolors):
    tempcolor15 = pcolors[15]
    pcolors[15] = pcolors[41]
    pcolors[41] = pcolors[31]
    pcolors[31] = tempcolor15
    updateGui()
    return pcolors

#There are 28 different nonredundant moves in this program.
#Written by Author, not Peer
def randompyraminx(moves):
    if moves == 0:
        reset()

    lowerBound = 0
    upperBound = 27

    if (counterClockToggle == 1):
        lowerBound = 14
        upperBound = 27
    elif (counterClockToggle == 2):
        lowerBound = 0
        upperBound = 13

    for i in range(moves):
        move = random.randint(lowerBound, upperBound)
        match move:
            case 0:
                rTopClock(currentcolors)
            case 1:
                rSecondClock(currentcolors)
            case 2:
                rThirdClock(currentcolors)
            case 3:
                rBottomClock(currentcolors)
            case 4:
                bTopClock(currentcolors)
            case 5:
                bSecondClock(currentcolors)
            case 6:
                bThirdClock(currentcolors)
            case 7:
                bBottomClock(currentcolors)
            case 8:
                rBLFPC(currentcolors)
            case 9:
                rBLTPC(currentcolors)
            case 10:
                rBRFPC(currentcolors)
            case 11:
                rBRTPC(currentcolors)
            case 12:
                yBLFPC(currentcolors)
            case 13:
                yBLTPC(currentcolors)
            case 14:
                rTopCounterClock(currentcolors)
            case 15:
                rSecondCounterClock(currentcolors)
            case 16:
                rThirdCounterClock(currentcolors)
            case 17:
                rBottomCounterClock(currentcolors)
            case 18:
                bTopCounterClock(currentcolors)
            case 19:
                bSecondCounterClock(currentcolors)
            case 20:
                bThirdCounterClock(currentcolors)
            case 21:
                bBottomCounterClock(currentcolors)
            case 22:
                rBLFPCU(currentcolors)
            case 23:
                rBLTPCU(currentcolors)
            case 24:
                rBRFPCU(currentcolors)
            case 25:
                rBRTPCU(currentcolors)
            case 26:
                yBLFPCU(currentcolors)
            case 27:
                yBLTPCU(currentcolors)


#MAIN (GUI Code wrote by Peer, with tweaks by Author)
root = Tk()
root.title("Pyraminx")
canvas = Canvas(root, width=1500, height=1000)
colors = ["red", "blue", "yellow", "green", "black"]
canvas.pack()



reset()


#solved
#solvedText = canvas.create_text(300, 50, text="Currently Solved!", fill="black", font=('Helvetica 15 bold'))


#Randomize button and user entry
button = Button(root, text="Randomize", command=randomizer_func, bg = 'grey')
button.place(x = 715, y = 765)
entry = Entry(root)
entry.place(x = 580,  y = 770)

#Toggle graphics button
toggleButton = Button(root, text = "Toggle GUI Update", command = toggle_func, bg = 'gray')
toggleButton.place(x = 150, y = 765)

#Toggle if A* scrambler should only scramble using counter or counterclockwise movements
counterClockToggleButton = Button(root, text = "All Moves Possible", command = counterClockToggle_func, bg = 'gray')
counterClockToggleButton.place(x = 400, y = 765)
counterClockToggleText = canvas.create_text(455, 750, text="A* Moveset", fill="black", font=('Helvetica 15 bold'))

#Button to start A* search
searchButton = Button(root, text="Solve Using A*", command=lambda: astar(currentcolors, startingcopy), bg='gray')
searchButton.place(x = 800, y = 765)
root.mainloop()



