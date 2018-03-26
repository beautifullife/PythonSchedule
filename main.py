# This program will read csv data end display schedule by time
# example of a csv file
""" 
Class           Title                       datetime

Reading II,     Tell No One CHs 30-35,      Mar. 28 2018
Reading II,     CH 5 Main Ideas,            Mar. 29 11:59PM
Reading II,     CH 6 Supporting Details,    Mar. 29 11:59PM
Reading II,     TNO 36-40,                  April 2 2018
"""

from datetime import date, datetime
from dateutil import parser

def printMenu():
    print(  "\n----MENU-----------\n"
            "t: show today tasks.\n"
            "o: show overdue tasks.\n"
            "u: show upcomming task\n"
            "s: search tasks by date (ex: mar. 26).\n"
            "----END OF MENU----\n")

def showTodayTask():
    return searchByDate(date.today().isoformat())

def showOverDueTask():
    return searchByDate(date.today().isoformat(), type="overdue")

def showUpcommingTask():
    return searchByDate(date.today().isoformat(), type="upcomming")

def searchTask():
    userDate = input("Please input your date: ")
    return searchByDate(userDate)           

def searchByDate(userDate, type='none'):
    hasTask = False
    #debug 
    #print(formatedData)
    try:
        userDateFormated = parser.parse(userDate)
        print("\nPLANNER:")

        if type == 'overdue':
            print("OVERDUE\n")
        elif type == 'upcomming':
            print("UPCOMMING\n")
        
        for i in range(len(formatedData))[::3]:
            plannerClass = formatedData[i]
            plannerTitle = formatedData[i+1]
            plannerDate = formatedData[i+2]
            plannerDateFormated = parser.parse(plannerDate)
            # if the date match -> print out planner
            if type == 'overdue':
                if  (plannerDateFormated.day < userDateFormated.day) and (plannerDateFormated.month <= userDateFormated.month) and (plannerDateFormated.year <= userDateFormated.year):
                    print("%s ---> %s ---> %s" % (plannerClass, plannerTitle, plannerDate))
                    hasTask = True
            elif type == 'upcomming':
                if  (plannerDateFormated.day > userDateFormated.day) and (plannerDateFormated.month >= userDateFormated.month) and (plannerDateFormated.year >= userDateFormated.year):
                    print("%s ---> %s ---> %s" % (plannerClass, plannerTitle, plannerDate))
                    hasTask = True
            elif (plannerDateFormated.day == userDateFormated.day) and (plannerDateFormated.month == userDateFormated.month) and (plannerDateFormated.year == userDateFormated.year):
                print("%s ---> %s ---> %s" % (plannerClass, plannerTitle, plannerDate))
                hasTask = True
        # empty task
        if not hasTask:
            print("Empty task for that day but keep learning for the other days.")
    except Exception as identifier:
        print(identifier)
        print("Error occur. Please input the correct value.")

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