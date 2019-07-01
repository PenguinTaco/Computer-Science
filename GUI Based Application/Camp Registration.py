#Import Modules
from tkinter import *
from tkinter import messagebox

#Functions
def darkMode():
    options.entryconfig(0, label = 'Light Mode', command = lightMode)
    root.config(bg = '#000000')
    mainframe.config(bg = '#000000')
    firstNameLabel.config(fg = '#ffffff', bg = '#000000')
    firstNameEntry.config(fg = '#ffffff', bg = '#808080')
    lastNameLabel.config(fg = '#ffffff', bg = '#000000')
    lastNameEntry.config(fg = '#ffffff', bg = '#808080')
    genderframe.config(fg = '#ffffff',bg = '#000000')
    male.config(fg = '#ffffff', bg = '#000000', activeforeground = '#ffffff', activebackground = '#000000', selectcolor = '#000000')
    female.config(fg = '#ffffff', bg = '#000000', activeforeground = '#ffffff', activebackground = '#000000', selectcolor = '#000000')
    processButton.config(fg = '#ffffff', bg = '#000000', activeforeground = '#ffffff', activebackground = '#000000')
    ageframe.config(fg = '#ffffff',bg = '#000000')
    ageGroup1.config(fg = '#ffffff', bg = '#000000', activeforeground = '#ffffff', activebackground = '#000000', selectcolor = '#000000')
    ageGroup2.config(fg = '#ffffff', bg = '#000000', activeforeground = '#ffffff', activebackground = '#000000', selectcolor = '#000000')
    ageGroup3.config(fg = '#ffffff', bg = '#000000', activeforeground = '#ffffff', activebackground = '#000000', selectcolor = '#000000')
    programframe.config(fg = '#ffffff',bg = '#000000')
    program1Check.config(fg = '#ffffff', bg = '#000000', activeforeground = '#ffffff', activebackground = '#000000', selectcolor = '#000000')
    program2Check.config(fg = '#ffffff', bg = '#000000', activeforeground = '#ffffff', activebackground = '#000000', selectcolor = '#000000')
    program3Check.config(fg = '#ffffff', bg = '#000000', activeforeground = '#ffffff', activebackground = '#000000', selectcolor = '#000000')
    searchframe.config(fg = '#ffffff',bg = '#000000')
    searchEntry.config(fg = '#ffffff', bg = '#808080')
    searchBox.config(fg = '#ffffff', bg = '#000000')
    listChildrenProgram.config(fg = '#ffffff', bg = '#000000', activeforeground = '#ffffff', activebackground = '#000000')
    displayframe.config(fg = '#ffffff',bg = '#000000')
    displaySet.config(fg = '#ffffff', bg = '#000000', activeforeground = '#ffffff', activebackground = '#000000')
    displaySet['menu'].config(fg = '#ffffff', bg = '#000000', activeforeground = '#ffffff', activebackground = '#808080')
    displayChildSelect.config(fg = '#ffffff', readonlybackground = '#000000')
    displayInfo.config(fg = '#ffffff',bg = '#000000')
    
def lightMode():
    options.entryconfig(0, label = 'Dark Mode', command = darkMode)
    root.config(bg = '#f0f0f0')
    mainframe.config(bg = '#f0f0f0')
    firstNameLabel.config(fg = '#000000', bg = '#f0f0f0')
    firstNameEntry.config(fg = '#000000', bg = '#ffffff')
    lastNameLabel.config(fg = '#000000', bg = '#f0f0f0')
    lastNameEntry.config(fg = '#000000', bg = '#ffffff')
    genderframe.config(fg = '#000000',bg = '#f0f0f0')
    male.config(fg = '#000000', bg = '#f0f0f0', activeforeground = '#000000', activebackground = '#f0f0f0', selectcolor = '#ffffff')
    female.config(fg = '#000000', bg = '#f0f0f0', activeforeground = '#000000', activebackground = '#f0f0f0', selectcolor = '#ffffff')
    processButton.config(fg = '#000000', bg = '#f0f0f0', activeforeground = '#000000', activebackground = '#f0f0f0')
    ageframe.config(fg = '#000000',bg = '#f0f0f0')
    ageGroup1.config(fg = '#000000', bg = '#f0f0f0', activeforeground = '#000000', activebackground = '#f0f0f0', selectcolor = '#ffffff')
    ageGroup2.config(fg = '#000000', bg = '#f0f0f0', activeforeground = '#000000', activebackground = '#f0f0f0', selectcolor = '#ffffff')
    ageGroup3.config(fg = '#000000', bg = '#f0f0f0', activeforeground = '#000000', activebackground = '#f0f0f0', selectcolor = '#ffffff')
    programframe.config(fg = '#000000',bg = '#f0f0f0')
    program1Check.config(fg = '#000000', bg = '#f0f0f0', activeforeground = '#000000', activebackground = '#f0f0f0', selectcolor = '#ffffff')
    program2Check.config(fg = '#000000', bg = '#f0f0f0', activeforeground = '#000000', activebackground = '#f0f0f0', selectcolor = '#ffffff')
    program3Check.config(fg = '#000000', bg = '#f0f0f0', activeforeground = '#000000', activebackground = '#f0f0f0', selectcolor = '#ffffff')
    searchframe.config(fg = '#000000',bg = '#f0f0f0')
    searchEntry.config(fg = '#000000', bg = '#ffffff')
    searchBox.config(fg = '#000000', bg = '#ffffff')
    listChildrenProgram.config(fg = '#000000', bg = '#f0f0f0', activeforeground = '#000000', activebackground = '#f0f0f0')
    displayframe.config(fg = '#000000',bg = '#f0f0f0')
    displaySet.config(fg = '#000000', bg = '#f0f0f0', activeforeground = '#000000', activebackground = '#f0f0f0')
    displaySet['menu'].config(fg = '#000000', bg = '#f0f0f0', activeforeground = '#ffffff', activebackground = '#0078D7')
    displayChildSelect.config(fg = '#000000', readonlybackground = '#f0f0f0')
    displayInfo.config(fg = '#000000', bg = '#f0f0f0')
    
def reset():
    anwser = messagebox.askquestion('Reset', 'Are You Sure You Want To Reset')
    if anwser == 'yes':
        nameList.clear()
        names.set(value = nameList)
        genderList.clear()
        genders.set(value = genderList)
        ageList.clear
        ageGroups.set(ageList)
        programList.clear()
        programGroup.set(value = programList)
        lightMode()
        clearEntry()
        search.set('')
        query = ''
        searchProcess(query)
        sameNames = []
        displayChildSelect.config(values = sameNames)
        child.set('Select A Child')
        display.set('')
    else:
        pass
    
def exit():
    anwser = messagebox.askquestion('Exit', 'Are You Sure You Want To Exit')
    if anwser == 'yes':
        root.destroy()
    else:
        pass
    
def helpGeneral():
    messagebox.showinfo('How To Use This Program', 'Enter Info Into All The Fields And Select The Options The Child Applies For And Hit Submit To Add The Child Into The Registry')

def helpSearch():
    messagebox.showinfo('How To Use Search', 'Enter The Desired Query Into The Searchbox, Once You Find Who You Want To See More Info For Just Left Click On Them To See More Info')

def infoSearch():
    messagebox.showinfo('Special Info', 'The Search Groups People Together That Have The Same Name')

def process():
    if firstName.get() != '' and lastName.get() != '':
        if program1Var.get() == 1 or program2Var.get() == 1 or program3Var.get() == 1:
            #Name Set
            tempString = f'{firstName.get()} {lastName.get()}'
            nameList.append(tempString)
            names.set(nameList)
            #Gender Set
            genderList.append(gender.get())
            genders.set(genderList)
            #Age Set
            tempInt = ageGroup.get()
            if tempInt == 1:
                ageList.append('4-6')
            elif tempInt == 2:
                ageList.append('7-9')
            elif tempInt == 3:
                ageList.append('10-12')
            ageGroups.set(ageList)
            #Program Set
            tempInt = program1Var.get()
            tempInt2 = program2Var.get()
            tempInt3 = program3Var.get()
            if tempInt == 1 and tempInt2 == 1 and tempInt3 == 1:
                programList.append('Day, Evening, Night')
                tempInt = 0
                tempInt2 = 0
                tempInt3 = 0
            elif tempInt2 == 1 and tempInt3 == 1:
                programList.append('Evening, Night')
                tempInt2 = 0
                tempInt3 = 0
            elif tempInt == 1 and tempInt2 == 1:
                programList.append('Day, Evening')
                tempInt = 0
                tempInt2 = 0
            elif tempInt == 1 and tempInt3 == 1:
                programList.append('Day, Night')
                tempInt = 0
                tempInt3 = 0
            elif tempInt == 1:
                programList.append('Day')
                tempInt = 0
            elif tempInt2 == 1:
                programList.append('Evening')
                tempInt2 = 0
            elif tempInt3 == 1:
                programList.append('Night')
                tempInt3 = 0
            programGroup.set(programList)
            #Update Listbox
            query = search.get()
            if searchBox.get(ANCHOR) == tempString:
                displayStart()
            searchProcess(query)
            clearEntry()
        else:
            messagebox.showerror('Error', 'All Fields Must Be Entered')
    else:
        messagebox.showerror('Error', 'All Fields Must Be Entered')

def clearEntry():
    firstName.set('')
    lastName.set('')
    gender.set('Male')
    ageGroup.set(2)
    program1Var.set(0)
    program2Var.set(0)
    program3Var.set(0)

def searchEntrys(entry):
    if len(entry.char) != 0:
        if ord(entry.char) == 8:
            query = search.get()
            query = query [:-1]
        else:
            query = search.get() + entry.char
    else:
        query = search.get()
    searchProcess(query)

def searchProcess(query):
    i = 0
    kids = nameList
    results = []
    if query == '':
        query = ' '
    while(i < len(kids)):
        for letter in query:
            if str.lower(letter) in str.lower(kids[i]):
                if kids[i] in results:
                    results.remove(kids[i])
                results.append(kids[i])
        i = i + 1
    updateListbox(results, query)

def updateListbox(results, query):
    searchResults.set(results)
    
def displayStart(click = ''):
    selection = searchBox.get(ANCHOR)
    kids = nameList
    sameNames = []
    for i in range (0, len(kids), 1):
        if selection == kids[i]:
            sameNames.append(f'Entry {str(i + 1)}')
    displayChildSelect.config(values = sameNames)
    if len(sameNames) >> 0:
        child.set(sameNames[0])
        updateDisplay()

def updateDisplay(selection = ''):
    selection = choice.get()
    selChild = child.get()
    if selChild != 'Select A Child':
        selChild = (int(selChild.replace('Entry ', '')) - 1)
        if selection == 'All Info':
            display.set(f'Name: {nameList[selChild]}\nGender: {genderList[selChild]}\nAge Group: {ageList[selChild]}\nProgram(s): {programList[selChild]}')
        elif selection == 'Gender and Age Group':
            display.set(f'Gender: {genderList[selChild]}\nAge Group: {ageList[selChild]}')
        elif selection == 'Programs Selected':
            display.set(f'Program(s): {programList[selChild]}')
    else:
        messagebox.showerror('Error', 'You Need To Select A Child First To Display Their Info')

def readProgram():
    tempInt = program1Var.get()
    tempInt2 = program2Var.get()
    tempInt3 = program3Var.get()
    check = ''
    if tempInt == 1 and tempInt2 == 1 and tempInt3 == 1:
        check = ['Day, Evening, Night', 'Evening, Night', 'Day, Evening', 'Day, Night', 'Day', 'Evening', 'Night']
        tempInt = 0
        tempInt2 = 0
        tempInt3 = 0
    elif tempInt2 == 1 and tempInt3 == 1:
        check = ['Day, Evening, Night', 'Evening, Night', 'Day, Evening', 'Day, Night', 'Evening', 'Night']
        tempInt2 = 0
        tempInt3 = 0
    elif tempInt == 1 and tempInt2 == 1:
        check = ['Day, Evening, Night', 'Evening, Night', 'Day, Evening', 'Day, Night', 'Day', 'Evening']
        tempInt = 0
        tempInt2 = 0
    elif tempInt == 1 and tempInt3 == 1:
        check = ['Day, Evening, Night', 'Evening, Night', 'Day, Evening', 'Day, Night', 'Day', 'Night']
        tempInt = 0
        tempInt3 = 0
    elif tempInt == 1:
        check = ['Day, Evening, Night', 'Day, Evening', 'Day, Night', 'Day']
        tempInt = 0
    elif tempInt2 == 1:
        check = ['Day, Evening, Night', 'Evening, Night', 'Day, Evening', 'Evening']
        tempInt2 = 0
    elif tempInt3 == 1:
        check = ['Day, Evening, Night', 'Evening, Night', 'Day, Night', 'Night']
        tempInt3 = 0
    if check != '':
        checkProgram(check)
    else:
        messagebox.showerror('Error', 'You Need To Select A Program To Check Who Is In A Program')

def checkProgram(check):
    tempList = []
    for j in range (0, len(check), 1):
        for i in range (0, len(programList), 1):
            if check[j] == programList[i]:
                tempList.append(nameList[i])
    tempString = str(tempList)
    tempString = tempString.replace('\'', '')
    tempString = tempString.replace('[', '')
    tempString = tempString.replace(']', '')
    if tempString != '':
        messagebox.showinfo('Program Check', f'The People In The Selected Program(s) are: {tempString}')
    else:
        messagebox.showinfo('Program Check', 'There is No People In The Selected Program(s)')

#Make Window
root = Tk()
mainframe = Frame(root)
genderframe = LabelFrame(mainframe, text = 'Gender')
ageframe = LabelFrame(mainframe, text = 'Age Group')
programframe = LabelFrame(mainframe, text = 'Programs')
searchframe = LabelFrame(mainframe, text = 'Search')
displayframe = LabelFrame(mainframe, text = 'Display')
menuBar = Menu(root)
root.config(menu=menuBar, bg = '#f0f0f0')

#Make Global Variables
nameList = []
names = StringVar(value = nameList)
genderList = []
genders = StringVar(value = genderList)
ageList = []
ageGroups = StringVar(value = ageList)
programList = []
programGroup = StringVar(value = programList)

#Make Widgets
options = Menu(menuBar, tearoff = 0)
options.add_command(label = 'Dark Mode', command = darkMode)
options.add_command(label = 'Reset', command = reset)
options.add_separator()
options.add_command(label = 'Exit', command = exit)
menuBar.add_cascade(label = 'Options', menu = options)
info = Menu(menuBar, tearoff = 0)
info.add_command(label = 'How To Use General', command = helpGeneral)
info.add_command(label = 'How To Use Search', command = helpSearch)
info.add_command(label = 'Additional Search Information', command = infoSearch)
menuBar.add_cascade(label = 'Help', menu = info)
firstNameLabel = Label(mainframe, text = 'First Name')
firstName = StringVar()
firstNameEntry = Entry(mainframe, width = 20, font = ('Arial', 20), textvariable = firstName)
lastNameLabel = Label(mainframe, text = 'Last Name')
lastName = StringVar()
lastNameEntry = Entry(mainframe, width = 20, font = ('Arial', 20), textvariable = lastName)
genderLabel = Label(mainframe, text = 'Gender')
gender = StringVar()
gender.set('Male')
male = Radiobutton(genderframe, text = 'Male', variable = gender, value = 'Male', width = 18)
female = Radiobutton(genderframe, text = 'Female', variable = gender, value = 'Female', width = 18)
processButton = Button(mainframe, width = 42, text = 'Submit', command = process)
ageGroup = IntVar()
ageGroup.set(2)
ageGroup1 = Radiobutton(ageframe, text = '4-6', variable = ageGroup, value = 1)
ageGroup2 = Radiobutton(ageframe, text = '7-9', variable = ageGroup, value = 2)
ageGroup3 = Radiobutton(ageframe, text = '10-12', variable = ageGroup, value = 3)
program1Var = IntVar()
program1Check = Checkbutton(programframe, text = 'Day', onvalue = 1, offvalue = 0, variable = program1Var)
program2Var = IntVar()
program2Check = Checkbutton(programframe, text = 'Evening', onvalue = 1, offvalue = 0, variable = program2Var)
program3Var = IntVar()
program3Check = Checkbutton(programframe, text = 'Night', onvalue = 1, offvalue = 0, variable = program3Var)
search = StringVar()
searchEntry = Entry(searchframe, font = ('Arial', 8), textvariable = search)
searchEntry.bind('<Key>', searchEntrys)
searched = []
searchResults = StringVar(value = searched)
searchBox = Listbox(searchframe, listvar = searchResults, selectmode = SINGLE)
yScroll = Scrollbar(searchframe, orient = VERTICAL, command = searchBox.yview)
xScroll = Scrollbar(searchframe, orient = HORIZONTAL, command = searchBox.xview)
searchBox.config(yscrollcommand = yScroll.set, xscrollcommand = xScroll.set)
searchBox.bind('<<ListboxSelect>>', displayStart)
listChildrenProgram = Button(mainframe, width = 82, text = 'Check Who Is In The Selected Program(s)', command = readProgram)
displayOptions = ['All Info', 'Gender and Age Group', 'Programs Selected']
choice = StringVar()
choice.set('All Info')
displaySet = OptionMenu(displayframe, choice, *displayOptions, command = updateDisplay)
displaySet.config(width = 90)
child = StringVar()
child.set('Select A Child')
sameNames = []
displayChildSelect = Spinbox(displayframe, textvariable = child, values = sameNames, width = 95, command = updateDisplay, state = 'readonly')
display = StringVar()
displayInfo = Label(displayframe, textvariable = display)

#Grid Widgets
root.minsize(width = 630, height = 450)
root.maxsize(width = 630, height = 450)
mainframe.grid(padx = 20, pady = 20)
firstNameLabel.grid(row = 1, column = 1)
firstNameEntry.grid(row = 2, column = 1)
lastNameLabel.grid(row = 3, column = 1)
lastNameEntry.grid(row = 4, column = 1)
genderframe.grid(row = 5, pady = 10, column = 1)
male.grid(row = 1, column = 1)
female.grid(row = 1, column = 2)
processButton.grid(row = 7, pady = 10, column = 1)
ageframe.grid(row = 1, rowspan = 3, column = 2, padx = 20)
ageGroup1.grid(row = 1, column = 1, sticky = W)
ageGroup2.grid(row = 2, column = 1, sticky = W)
ageGroup3.grid(row = 3, column = 1, sticky = W)
programframe.grid(row = 4, rowspan = 4, column = 2, padx = 20)
program1Check.grid(row = 1, column = 1, sticky = W)
program2Check.grid(row = 2, column = 1, sticky = W)
program3Check.grid(row = 3, column = 1, sticky = W)
searchframe.grid(row = 1, rowspan = 7, column = 3)
searchEntry.grid(row = 1, column = 1)
searchBox.grid(row = 2, column = 1)
yScroll.grid(row = 2, column = 2, sticky = N + S)
xScroll.grid(row = 3, column = 1, sticky = E + W)
listChildrenProgram.grid(row = 8, column = 1, columnspan = 3)
displayframe.grid(row = 9, column = 1, columnspan = 3)
displaySet.grid(row = 1, column = 1)
displayChildSelect.grid(row = 2, column = 1)
displayInfo.grid(row = 3, column = 1)

#Loop
root.mainloop()
