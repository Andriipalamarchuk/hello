import os 

def fileLengthy(fname):
        with open(fname) as f:
                for i, l in enumerate(f):
                        pass
        return i + 1

def readFile(pathToFile):
    list = ["prova1.txt", "prova2.txt", "prova3.txt"]
    i = 0
    contList = 0
    for x in list:
        f = open(pathToFile + list[contList], "r")
        lines = f.readlines()
        if contList == 0:
            numberOfLines = fileLengthy(pathToFile + "prova1.txt")
            for i in range(numberOfLines):
                writeFile (pathToFile, lines[i])
            contList +=1    
        else:            
            numberOfLines = fileLengthy(pathToFile + list[contList])
            totalLineNumberInAll = fileLengthy(pathToFile + "createFile.txt")
            for i in range(numberOfLines):
                print ("Line content: " + lines[i])
                j = 0
                for j in range(totalLineNumberInAll):
                    if lines[i] == existInFile(pathToFile + "createFile.txt", j, totalLineNumberInAll):
                        print ("The name already exists in the file and the name is: " + existInFile)
                    else:
                        if j == 0:
                            writeFile (pathToFile, "\n")
                        else:
                            writeFile (pathToFile, lines[i])
            contList +=1


def writeFile(pathToFile, valueToWrite):
    fwrite = open(pathToFile + "createFile.txt", "a")
    fwrite.write(valueToWrite)    

def existInFile(pathToFile, lineNumber, totalNumber):
    fread = open(pathToFile, "r")
    if lineNumber == totalNumber:
        return "Finish"
    else:
        return fread.readlines(lineNumber)
        

    
def main():
#    pathToFile = os.getcwd()
    pathToFile = "C:/Users/palaa/Desktop/develop/python/"
    readFile(pathToFile)

if __name__ == "__main__":
    main()