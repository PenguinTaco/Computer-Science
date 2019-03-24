import os
import sys

stick = 0
boulder = 0
usedStick = 0
usedBoulder = 0
fileLocation = (sys.argv[0])

def start() :
    print ('You wake up from a faint smell coming from your bed.')
    print ('Enter 1 to Get out of bed')
    print ('Enter 2 to Stay in bed')
    print ('')
    option = input('Please Enter Your Option' + '\n')
    if option == "1" :
        wakeUp()
    elif option == "2" :
        win()
    else :
        print ('')
        print (option, 'is not a valid option')
        print ('')
        start()

def wakeUp() :
    print ('')
    print ('You Get out of Your Bed')
    print ('Enter 1 to Investigate The Smell')
    print ('Enter 2 to Ignore The Smell')
    option = input('Please Enter Your Option' + '\n')
    if option == "1" :
        deathSmell()
    elif option == "2" :
        ignoreSmell()
    else :
        print ('')
        print (option, 'is not a valid option')
        print ('')
        wakeUp()

def win() :
    print ('')
    print ("You Avoided The Whole Conflict Ahead. Victory")
    print ('')
    input('Press Enter To Exit')

def deathSmell() :
    global fileLocation
    print ('')
    print ('You Died From A Foul Smell')
    print ('')
    input('Press Enter To Exit' + '\n')

def ignoreSmell() :
    print ('')
    print ('You Ignored The Smell')
    print ('')
    print ('Enter 1 To Go Downstairs To Get Breakfast')
    print ('Enter 2 To Look Around')
    option = input('Please Enter Your Option' + '\n')
    if option == "1" :
        deathStairs()
    elif option == "2" :
        lookAroundSchool()
    else :
        print ('')
        print (option, 'is not a valid option')
        print ('')
        ignoreSmell()

def deathStairs() :
    global fileLocation
    print ('')
    print ('You Sprain Your Ankle And Fall Down The Stairs And Then Causally Explode.')
    print ('Your Dead Corpse Gets Arrested For Blowing Up A School')
    print ('')
    input('Press Enter To Exit' + '\n')

def lookAroundSchool() :
    print ('')
    print ('You Notice That You Are Not in A Familiar Room. Instead You Are In A School and You Were Sleeping On A Water Heater')
    print ('')
    print ('Enter 1 To Go Upstairs')
    print ('Enter 2 To Search The Floor You Are Currently On')
    option = input('Please Enter Your Option' + '\n')
    if option == "1" :
        forestUpstairs()
    elif option == "2" :
        searchSchool()
    else :
        print ('')
        print (option, 'is not a valid option')
        print ('')
        lookAroundSchool()

def forestUpstairs() :
    print ('')
    print ('You Go Upstairs')
    print ('')
    print ('Enter 1 To Look Around')
    print ('Enter 2 To Go Downstairs')
    option = input('Please Enter Your Option' + '\n')
    if option == "1" :
        lookAroundForest()
    elif option == "2" :
        lookAroundSchool()
    else :
        print ('')
        print (option, 'is not a valid option')
        print ('')
        forestUpstairs()

def searchSchool() :
    print ('')
    print ('You Search The Room But Find Nothing New')
    print ('')
    print ('Enter 1 To Go Back To Bed')
    print ('Enter 2 To Give Up')
    print ('Enter 3 To Go Upstairs')
    option = input('Please Enter Your Option' + '\n')
    if option == "1" :
        goBackToBed()
    elif option == "2" :
        giveUp()
    elif option == "3" :
        forestUpstairs()
    else :
        print ('')
        print (option, 'is not a valid option')
        print ('')
        searchSchool()

def giveUp() :
    print ('')
    print ('You Violently Failed')
    print ('')
    input('Press Enter To Exit' + '\n')

def goBackToBed() :
    print ('')
    print ('You Realize There Is No Bed But There Is A Water Heater')
    print ('')
    print ('Enter 1 To Give Up')
    print ('Enter 2 To Go To Bed')
    option = input('Please Enter Your Option' + '\n')
    if option == "1" :
        giveUp()
    elif option == "2" :
        goToBed()
    else :
        print ('')
        print (option, 'is not a valid option')
        print ('')
        goBackToBed()

def goToBed() :
    print ('')
    print ('You Fail To Fall Asleep')
    print ('')
    input('Press Enter To Continue' + '\n')
    searchSchool()

def lookAroundForest ():
    print ('')
    print ('You Notice That You Are In A Forest And The Stairs Behind You Have Disappeared')
    print ('')
    print ('Enter 1 To Go Left')
    print ('Enter 2 To Go Right')
    option = input('Please Enter Your Option' + '\n')
    if option == "1" :
        deathForestLeft()
    elif option == "2" :
        goRightForest()
    else :
        print ('')
        print (option, 'is not a valid option')
        print ('')
        lookAroundForest()

def deathForestLeft ():
    global fileLocation
    print ('')
    print ('Died')
    print ('')
    input('Press Enter To Exit' + '\n')

def goRightForest ():
    print ('')
    print ('You Explored To Your Right With No Exit In Sight')
    print ('')
    print ('Enter 1 To Go Back To Where You Started In the Forest')
    print ('Enter 2 To Go Right Again')
    option = input('Please Enter Your Option' + '\n')
    if option == "1" :
        leftForestToRoom()
    elif option == "2" :
        goRightForestAgain()
    else :
        print ('')
        print (option, 'is not a valid option')
        print ('')
        goRightForest()

def leftForestToRoom ():
    print ('')
    print ('You See a Door Where You Got Into The Forest And Go Back In It')
    print ('')
    print ('Enter 1 To Look Around')
    option = input('Please Enter Your Option' + '\n')
    if option == "1" :
        lookAroundRoom()
    else :
        print ('')
        print (option, 'is not a valid option')
        print ('')
        leftForestToRoom()

def lookAroundRoom ():
    print ('')
    print ('You Notice You Are Finally Back In Your Room, It is now Midnight')
    print ('')
    print ('Enter 1 To Go To Bed')
    print ('Enter 2 To Play Tetris')
    option = input('Please Enter Your Option' + '\n')
    if option == "1" :
        bedDeath()
    elif option == "2" :
        playTetris()
    else :
        print ('')
        print (option, 'is not a valid option')
        print ('')
        lookAroundRoom()

def bedDeath ():
    global fileLocation
    print ('')
    print ('Your Bed Breaks And You Fall Through The Floor And Break Your Back')
    print ('')
    input('Press Enter To Exit' + '\n')

def playTetris ():
    print ('')
    print ('You Played Tetris 99 And Got 99th Place ')
    print ('')
    print ('Enter 1 To Go To Bed')
    print ('Enter 2 To Leave Room')
    option = input('Please Enter Your Option' + '\n')
    if option == "1" :
        bedDeath()
    elif option == "2" :
        leaveRoomToForest()
    else :
        print ('')
        print (option, 'is not a valid option')
        print ('')
        playTetris()

def leaveRoomToForest ():
    print ('')
    print ('You Left Your Room And Find A Boulder')
    print ('')
    print ('Enter 1 To PUNCH IT')
    print ('Enter 2 To Give Up')
    option = input('Please Enter Your Option' + '\n')
    if option == "1" :
        punchBoulder()
    elif option == "2" :
        giveUpBoulder()
    else :
        print ('')
        print (option, 'is not a valid option')
        print ('')
        leaveRoomToForest()

def goRightForestAgain ():
    print ('')
    print ('You Find A Boulder')
    print ('')
    print ('Enter 1 To PUNCH IT')
    print ('Enter 2 To Give Up')
    option = input('Please Enter Your Option' + '\n')
    if option == "1" :
        punchBoulder()
    elif option == "2" :
        giveUpBoulder()
    else :
        print ('')
        print (option, 'is not a valid option')
        print ('')
        goRightForestAgain()

def punchBoulder ():
    print ('')
    print ('You Break Your Knuckles But Refuse To Give Up')
    print ('')
    print ('Enter 1 To Look Around')
    print ('Enter 2 To PUNCH IT AGAIN')
    option = input('Please Enter Your Option' + '\n')
    if option == "1" :
        findStick()
    elif option == "2" :
        smashBoulder()
    else :
        print ('')
        print (option, 'is not a valid option')
        print ('')
        punchBoulder()

def giveUpBoulder ():
    global fileLocation
    print ('')
    print ('You Punch The Boulder Anyways And Died')
    print ('')
    input('Press Enter To Exit' + '\n')

def findStick ():
    global stick
    stick = 1
    print ('')
    print ('You Find A Stick On The Ground And Pick It Up.')
    print ('')
    print ('Enter 1 To Look Around')
    option = input('Please Enter Your Option' + '\n')
    if option == "1" :
        lizardBattleStart()
    else :
        print ('')
        print (option, 'is not a valid option')
        print ('')
        findStick()

def smashBoulder ():
    print ('')
    print ('YOU SMASH THE BOULDER TO SMITHEREENS')
    print ('')
    print ('Enter 1 To Pick Up The Smashed Boulder')
    print ('Enter 2 To Look Around And Ignore The Smashed Boulder')
    option = input('Please Enter Your Option' + '\n')
    if option == "1" :
        pickUpSmashedBoulder()
    elif option == "2" :
        findStick()
    else :
        print ('')
        print (option, 'is not a valid option')
        print ('')
        smashBoulder()

def pickUpSmashedBoulder ():
    global boulder
    boulder = 1
    print ('')
    print ('You Picked Up The Smashed Boulder')
    print ('')
    print ('Enter 1 To Look Around')
    print ('Enter 2 To Walk Around')
    option = input('Please Enter Your Option' + '\n')
    if option == "1" :
        findStick()
    elif option == "2" :
        lizardBattleStart()
    else :
        print ('')
        print (option, 'is not a valid option')
        print ('')
        pickUpSmashedBoulder()

def lizardBattleStart ():
    print ('')
    print ('You Find A Lizard')
    print ('')
    print ('Enter 1 To Fight It')
    print ('Enter 2 To Run Away')
    option = input('Please Enter Your Option' + '\n')
    if option == "1" :
        fightLizard()
    elif option == "2" :
        runLizard()
    else :
        print ('')
        print (option, 'is not a valid option')
        print ('')
        lizardBattleStart()

def fightLizard ():
    print ('')
    print ('You Start A Battle With The Lizard')
    print ('')
    print ('Enter 1 To Punch The Lizard')
    print ('Enter 2 To Hit The Lizard With Your Stick')
    print ('Enter 3 To Throw The Smashed Boulder At The Lizard')
    option = input('Please Enter Your Option' + '\n')
    if option == "1" :
        punchLizard()
    elif option == "2" :
        stickLizard()
    elif option == "3" :
        boulderLizard()
    else :
        print ('')
        print (option, 'is not a valid option')
        print ('')
        fightLizard()

def runLizard ():
    print ('')
    print ('The Lizard Attacks Anyways')
    print ('')
    print ('Enter 1 To Punch The Lizard')
    print ('Enter 2 To Hit The Lizard With Your Stick')
    print ('Enter 3 To Throw The Smashed Boulder At The Lizard')
    option = input('Please Enter Your Option' + '\n')
    if option == "1" :
        punchLizard()
    elif option == "2" :
        stickLizard()
    elif option == "3" :
        boulderLizard()
    else :
        print ('')
        print (option, 'is not a valid option')
        print ('')
        runLizard()

def punchLizard ():
    global fileLocation
    print ('')
    print ('The Lizard Attacks You With A Booster Seat Before You Can Land Your Hit And It Kills You.')
    print ('')
    input('Press Enter To Exit' + '\n')

def stickLizard ():
    global stick
    global usedStick
    global usedBoulder
    if stick == 1 :
        print ('')
        print ('You Hit It With Your Stick And It Snaps')
        if usedBoulder == 1 :
            print ('Enter 1 To Punch The Lizard')
            option = input('Please Enter Your Option' + '\n')
            if option == "1" :
                stick = 0
                punchLizard()
            else :
                print ('')
                print (option, 'is not a valid option')
                print ('')
                stickLizard()
        else :
            print ('Enter 1 To Punch The Lizard')
            print ('Enter 2 To Throw The Smashed Boulder At The Lizard')
            option = input('Please Enter Your Option' + '\n')
            if option == "1" :
                stick = 0
                usedStick = 1
                punchLizard()
            if option == "2" :
                stick =  0
                usedStick = 1
                boulderLizard()
            else :
                print ('')
                print (option, 'is not a valid option')
                print ('')
                stickLizard()
    else :
        global fileLocation
        print ('')
        print ('You Try To Pull Out A Stick But You Don\'t Have One. The Lizard Attacks With A Book And Hits You In The Face Killing You And Ending Your Journey')
        print ('')
        input('Press Enter To Exit' + '\n')
            

def boulderLizard ():
    global boulder
    global usedBoulder
    global usedStick
    if boulder == 1 :
        print ('')
        print ('You Miss The Lizard And It Attacks You With A Bowling Ball But A Man Named Daniel Interferes With It And Then Walks Away')
        if usedStick == 1 :
            print ('Enter 1 To Punch The Lizard')
            option = input('Please Enter Your Option' + '\n')
            if option == "1" :
                boulder = 0
                punchLizard()
            else :
                print ('')
                print (option, 'is not a valid option')
                print ('')
                boulderLizard()
        else :
            print ('Enter 1 To Punch The Lizard')
            print ('Enter 2 To Hit The Lizard With Your Stick')
            option = input('Please Enter Your Option' + '\n')
            if option == "1" :
                boulder = 0
                usedBoulder = 1
                punchLizard()
            if option == "2" :
                boulder = 0
                usedBoulder = 1
                stickLizard()
            else :
                print ('')
                print (option, 'is not a valid option')
                print ('')
                boulderLizard()
    else :
        global fileLocation
        print ('')
        print (' You Try To Pull Out The Smashed Boulder But You Don\'t Have It. The Lizard Attacks With A Book And Hits You In The Face Killing You And Ending Your Journey ')
        print ('')
        input('Press Enter To Exit' + '\n')

start()
