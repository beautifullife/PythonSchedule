# This program will read csv data end display schedule by time
# example of a csv file
""" 
Class           Title                       datetime

Reading II,     Tell No One CHs 30-35,      Mar. 28 2018
Reading II,     CH 5 Main Ideas,            Mar. 29 11:59PM
Reading II,     CH 6 Supporting Details,    Mar. 29 11:59PM
Reading II,     TNO 36-40,                  April 2 2018
"""

from datetime import datetime, timedelta
from dateutil import parser

def printMenu():
    print(  "\n----MENU-----------\n"
            "t: show today tasks.\n"
            "t: show tomorrow tasks.\n"
            "o: show overdue tasks.\n"
            "u: show upcomming task.\n"
            "s: search tasks by date (ex: mar. 26).\n"
            "----END OF MENU----\n")

"""
Mark the task is done base on ID (how to make ID?)
"""
def markTaskIsDone():
    pass

"""
Show calendar and tasks for days of week
"""
def showCalendar():
    pass

"""
Manage and auto decide what task to learn for each day every week
input: 
output:
"""
def autoDecidedTask():
    pass

def showTodayTask():
    return searchByDate(datetime.today().isoformat(), type='today')

def showTomorrowTask():
    return searchByDate(str(datetime.today() + timedelta(days=1)), type='tomorrow')

def showOverDueTask():
    return searchByDate(datetime.today().isoformat(), type="overdue")

def showUpcommingTask():
    return searchByDate(datetime.today().isoformat(), type="upcomming")

def searchTask():
    userDate = input("Please input your date: ")
    return searchByDate(userDate)           

# order by date - increase - FIX ME
def searchByDate(userDate, type='none'):
    hasTask = False
    #debug 
    #print(formatedData)
    try:
        userDateFormated = parser.parse(userDate).strftime("%m-%d-%Y")
        print("\nPLANNER:")
        print(type.upper() + "\n")
        
        for i in range(len(formatedData))[::3]:
            plannerClass = formatedData[i]
            plannerTitle = formatedData[i+1]
            plannerDate = formatedData[i+2]
            plannerDateFormated = parser.parse(plannerDate).strftime("%m-%d-%Y")
            # if the date match -> print out planner
            if type == 'overdue':
                if  plannerDateFormated < userDateFormated:
                    print("%s ---> %s ---> %s" % (plannerClass, plannerTitle, plannerDate))
                    hasTask = True
            elif type == 'upcomming': # FIX ME
                if  plannerDateFormated > userDateFormated:
                    print("%s ---> %s ---> %s" % (plannerClass, plannerTitle, plannerDate))
                    hasTask = True
            elif plannerDateFormated == userDateFormated:
                print("%s ---> %s ---> %s" % (plannerClass, plannerTitle, plannerDate))
                hasTask = True
        # empty task
        if not hasTask:
            print("Empty task for that day but keep learning for the other days.")
    except Exception as identifier:
        print(identifier)
        print("Error occur. Please input the correct value.")
        return False

    return True

def quitProgram():
    print("No task.")
    return True
        
def loopPrompt():
    while True:
        # print the menu
        printMenu()
        userChosen = input("Please type the task you want to do: ").strip()
        if userChosen == "s":
            searchTask()            
        if userChosen == "t":
            showTodayTask()
        if userChosen == "m":
            showTomorrowTask()
        if userChosen == "o":
            showOverDueTask()
        if userChosen == "u":
            showUpcommingTask()
        else:
            break

def readCsvFile(filePath):
    try:
        file = open(filePath, 'r')
        dataPerLine = file.read().split('\n')
    except FileNotFoundError as identifier:
        print(identifier)

    return dataPerLine

def getFormatedData(dataPerLine):
    result = []
    #debug
    #print(dataPerLine)
    for item in dataPerLine:
        if item.replace("-","").strip() != "":
            tmpArr = item.split(',')  
            for ite in tmpArr:
                result.append(ite.strip().upper())
    #debug
    #print(result)

    return result

def main():
    #define params
    global formatedData
    # read csv files
    filePath = 'planner.csv'
    dataPerLine = readCsvFile(filePath)
    # process data
    formatedData = getFormatedData(dataPerLine)
    # ask user for task (loop)
    loopPrompt()
    # print the result

if __name__ == '__main__':
    main()