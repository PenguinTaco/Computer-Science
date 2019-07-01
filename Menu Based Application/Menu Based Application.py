import csv

def printing(printingList):
    for i in range (0, len(printingList), 1):
        print (f'Enter {i + 1} for {printingList [i]}')

def getchoice():
    choice = str(input('Please Enter Your Selection \n'))
    return choice

def processchoice(choice, printingList, songList, artistList, listeningHistory, ext = 0, paid = 0):
    if len(choice) == 1:
        if choice <= '0':
                print('Invalid Input')
        elif choice <= str(len(printingList)):
            for i in range (0, len(printingList), 1):
                if choice == str(i + 1):
                    option = str.lower(printingList[i].replace(' ', ''))
                    if option == 'recconmendations':
                        listeningHistory = eval(option)(songList, artistList, listeningHistory, ext)
                    elif option == 'premium' or option == 'exit':
                        ext, paid = eval(option)(paid)
                    elif option == 'listeninghistory':
                        eval(option)(listeningHistory)
                    elif option == 'gobacktomainmenu':
                        eval(option)()
                    else:
                        listeningHistory = eval(option)(songList, artistList, listeningHistory)
        elif choice > str(len(printingList)):
            print('Invalid Input')
    else:
        print('Invalid Input')
    return listeningHistory, ext, paid

def initialize():
    choice = 0
    songList = []
    artistList = []
    listeningHistory = []
    openFile = open('top2018.csv')
    reader = csv.reader(openFile)
    for line in reader:
        songList.append(line[0])
        artistList.append(line[1])
    ext = 0
    paid = 0
    return choice, songList, artistList, listeningHistory, ext, paid

def exit(paid):
    ext = 1
    return ext, paid

def mainmenu():
    choice, songList, artistList, listeningHistory, ext, paid = initialize()
    while (ext == 0):
        if paid == 1:
            printingList = ['Home', 'Search', 'Exit']
            printing(printingList)
            choice = getchoice()
            listeningHistory, ext, paid = processchoice(choice, printingList, songList, artistList, listeningHistory, ext, paid)
        else:
            printingList = ['Home', 'Search', 'Premium', 'Exit']
            printing(printingList)
            choice = getchoice()
            listeningHistory, ext, paid = processchoice(choice, printingList, songList, artistList, listeningHistory)

def gobacktomainmenu():
    pass

def home(songList, artistList, listeningHistory):
    printingList = ['Recconmendations', 'Listening History', 'Go Back To Main Menu']
    printing(printingList)
    choice = getchoice()
    listeningHistory, ext, paid = processchoice(choice, printingList, songList, artistList, listeningHistory)
    return listeningHistory

def recconmendations(songList, artistList, listeningHistory, ext):
    songs = []
    a = 0
    for i in range (0, len(artistList), 1):
        if artistList[i] == 'Drake':
            a = a + 1
            songs.append(songList[i]) 
            print('Enter', a, 'To Play', songList[i])
    print('Enter 0 To Go Back To Main Menu')
    choice = getchoice()
    listeningHistory = playsong(songs, choice, listeningHistory)
    return listeningHistory

def playsong(songs, choice, listeningHistory):
    if len(choice) == 1:
        if choice < '0':
            print('Invalid Input')
        elif choice > '0' and choice <= str(len(songs)):
            song = songs [int(choice) - 1]
            listeningHistory = addtohistory(listeningHistory, song)
        elif choice > str(len(songs)):
            print('Invalid Input')
    else:
        print('Invalid Input')
    return listeningHistory

def listeninghistory(listeningHistory):
    printhistory(listeningHistory)
    
def printhistory(listeningHistory):
        for i in range (0, len(listeningHistory), 1):
            print(listeningHistory[i])
        if len(listeningHistory) == 0:
            print('Your Listening History is Empty')

def addtohistory(listeningHistory, song):
    print('You Played', song)
    if song in listeningHistory:
        listeningHistory.remove(song)
    listeningHistory.insert(0, song)
    return listeningHistory

def search(songList, artistList, listeningHistory):
    search = input('Please Enter The Song Name You Would Like To Search For \n')
    i = 0
    invalid = 0
    songs = []
    while(i < len(songList)):
        for letter in search:
            if str.lower(letter) in str.lower(songList[i]):
                if songList[i] in songs:
                    songs.remove(songList[i])
                songs.append(songList[i])
        i = i + 1
    if len(songs) == 0:
        print(f'Your Search For {search} Had 0 Results')
    else:
        choice, invalid = getchoicesearch(songs)
        if invalid == 0:
            song = songs [choice]
            listeningHistory = addtohistory(listeningHistory, song)
    return listeningHistory

def getchoicesearch(songs):
    invalid = 0
    loops = 0
    ext = 0
    correct = 0
    while(ext == 0):
        stop = 0
        count = 0
        if (count + (10 * loops)) >= (len(songs) + 1):
            ext = 1
            invalid = 1
        else:
            while(stop != 1):
                count = count + 1
                if count == 10:
                    stop = 1
                else:
                    if (count + (10 * loops)) >= (len(songs) + 1):
                        stop = 1
                    else:
                        print(f'Enter {count} To Play {songs [(count - 1) + (10 * loops)]}')
            if (count + (10 * loops)) < (len(songs) + 1):
                print('Enter Anything Else To See Other Options')
                print('Enter 0 To Go Back To Main Menu')
            else:
                print('Enter Anything Else To Go Back To Main Menu')
            choice = getchoice()
            if len(choice) == 1:
                if choice == '0':
                    invalid = 1
                    ext = 1
                elif choice >= '1' and choice <= '9':
                    if (int(choice) + (10 * loops)) >= (len(songs) + 1):
                        ext = 1
                        invalid = 1
                    else:
                        choice = (int(choice) + (10 * loops) - 1)
                        ext = 1
            else:
                invalid = 0
            loops = loops + 1
    return choice, invalid

def premium(paid):
    print('Do You Want to Activate Premium')
    printingList = ['Yes I Would Like To Activate Premium', 'Go Back To Main Menu']
    printing(printingList)
    choice = getchoice()
    if len(choice) == 1:
        if choice == '1':
            paid = 1
        elif choice <= '0' or choice >= '3':
            print('Invalid Input')
    else:
        print('Invalid Input')
    ext = 0
    return ext, paid

#main

mainmenu()
