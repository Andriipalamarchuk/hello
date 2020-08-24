import os, time

def takingAllLabels(checkPathDirectory):
    list = ["prova1.properties", "prova2.properties", "prova2.properties"]
    checkPathDirectory += '\\portlets\\intouch-crud-portlet\\docroot\\WEB-INF\\src\\'
    f = open(checkPathDirectory + "allLabels.txt", "a")
    firstWrite = True
    if firstWrite:
        lineNumbers = file_len(checkPathDirectory + list[0])
        for k in range(lineNumbers):
            writeFile(checkPathDirectory + "allLabels.txt", readLineOfFile(checkPathDirectory + i, k))
        firstWrite = False
    else:
        for i in list:
            for lineFirstFile in range(file_len(checkPathDirectory + "allLabels.txt"))
                for lineSecondFile in range(file_len(checkPathDirectory + i))
                    checkIfExist(checkPathDirectory, "allLabels.txt",  i)

def writeFile(pathToFile, valueToWrite):
    fwrite = open(pathToFile, "a")
    fwrite.write(valueToWrite + "\n")  

def file_len(fname):
    leng = 0
    with open(fname) as f:
        for leng, l in enumerate(f):
            pass
    if leng == 0:
        return leng
    else:
        return leng+1

def readLineOfFile(fileName, lineNumber):
    fo = open(fileName, "r")
    lines = fo.readlines()
    lineResult = lines[lineNumber]
    finalLine = ""
    for char in lineResult:
        if char == '=':
           break
        else:
            finalLine += char
    
    return finalLine.rstrip()

def check_crud(checkPathDirectory, firstFile, secondFile):
    lineFirstFile = ""
    lineSecondFile = ""
    x = 0
    y = 0
    print("Path: " + checkPathDirectory)  
    xMax = file_len(checkPathDirectory + firstFile)
   # print ("Valore di xMax: " + str(xMax))
    yMax = file_len(checkPathDirectory + secondFile)
   # print ("Valore di yMax: " + yMax)
    fowrite = open(checkPathDirectory + "out.txt", 'a')
        for x in range(xMax):
            lineFirstFile = readLineOfFile(checkPathDirectory + firstFile, x)
            confrontResult = False
            for y in range (yMax):
                lineSecondFile = readLineOfFile(checkPathDirectory + secondFile, y)
                print("Riga del file 1: " + lineFirstFile + "\nRiga del file 2: " + lineSecondFile)
                fowrite.write("\n Riga del file 1: " + lineFirstFile + " --- Riga del file 2: " + lineSecondFile)
                if lineFirstFile == lineSecondFile:
                    confrontResult = True
                    print ("\n MATCHING!!!!! linea 1: " + lineFirstFile + "\nLinea 2 :" + lineSecondFile)
                    fowrite.write("\n MATCHING!!!!! Due linee prese -> Linea 1: " + lineFirstFile + " ----  Linea 2 :" + lineSecondFile)
                    break
                elif (y == yMax-1 and confrontResult == False):
                    print("\n ATTENTION!!!!!! Manca traduzione per: " + lineFirstFile + " in file: " + secondFile)
                    fowrite.write("\nATTENTION!!!!! Manca traduzione per: " + lineFirstFile + " in file: " + secondFile)               
    
def main():
#    checkPathDirectory = os.getcwd()
    checkPathDirectory = 'C:\\projects\\INTOUCH\\Project\\LIFERAY\\SDK'
    takingAllLabels(checkPathDirectory)
    print("\nFinished to elaborate the file")

main()