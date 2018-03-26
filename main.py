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
            "s: search planner by date (ex: mar. 26)\n"
            "----END OF MENU----\n")

def searchByDate():
    #debug 
    #print(formatedData)
    userDate = input("Please input your date: ")
    #debug
        #print(userDateFormated)
    try:
        userDateFormated = parser.parse(userDate)
        
        for i in range(len(formatedData))[::3]:
            plannerClass = formatedData[i]
            plannerTitle = formatedData[i+1]
            plannerDate = formatedData[i+2]
            plannerDateFormated = parser.parse(plannerDate)
            # if the date match -> print out planner
            if  (userDateFormated.day == plannerDateFormated.day) and (userDateFormated.month == plannerDateFormated.month):
                print("%s ---> %s ---> %s" % (plannerClass, plannerTitle, plannerDate))
    except Exception as identifier:
        print(identifier)
        print("Error occur. Please input the correct value.")

    return False

def quitProgram():
    print("No task.")
    # quit
    return True
        
def loopPrompt():
    while True:
        userChosen = input("Please type the task you want to do: ")
        if userChosen == 's':
            searchByDate()
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
    # print the menu
    printMenu()
    # ask user for task (loop)
    loopPrompt()
    # print the result

if __name__ == '__main__':
    main()