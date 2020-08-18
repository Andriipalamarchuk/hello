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
            j = 0
            for j in range(totalLineNumberInAll):
                if existInFile(pathToFile + "createFile.txt", fileLengthy(pathToFile + "createFile.txt"), lines[j]):
                    print ("The name already exists in the file and the name is: " + lines[j])
                else:
                    writeFile (pathToFile, lines[j])
            contList +=1


def writeFile(pathToFile, valueToWrite):
    fwrite = open(pathToFile + "createFile.txt", "a")
    fwrite.write(valueToWrite)    

def existInFile(pathToFile, totalNumber, wordToConfront):
    fread = open(pathToFile, "r")
    lines = fread.readlines()
    exist = False 
    for z in range(totalNumber):
        if wordToConfront == lines[z]:
            exist = True
        if exist:
            break
    return exist    
        

    
def main():
    pathToFile = os.getcwd() + '/'
    #pathToFile = "C:/Users/palaa/Desktop/develop/python/"
    readFile(pathToFile)

if __name__ == "__main__":
    main()