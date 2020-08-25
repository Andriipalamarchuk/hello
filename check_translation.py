import os, sys, getopt, time

PORTLETS = ["BASE", "CRUD", "BACKOFFICE", "MASSIVE", "CUSTOM LOGIN", "INTEGRATION", "LIFERAY TRANSLATION", "NOTIFICATION", "REPORT", "FRONTEND"]
defaultDirectory = os.getcwd()
warningsFile = "warnings.txt"
allLabelsFile = "allLabels.txt"


def allPortlets(list_i18n, list_language):
    crudCheck(list_i18n, list_language, "CRUD")
    baseCheck(list_language, "BASE")
    backOfficeCheck(list_language, "BACKOFFICE")
    massiveFirmwareUpdateCheck(list_language, "MASSIVE")
    customLoginCheck(list_language, "CUSTOM LOGIN")
    integrationCheck(list_language, "INTEGRATION")
    liferayTranslationCheck(list_language, "LIFERAY TRANSLATION")
    notificationCheck(list_language, "NOTIFICATION")
    reportCheck(list_language, "REPORT")
    v2FrontEndCheck(list_language, "FRONTEND")

def crudCheck (list_i18n, list_language, portletName):
    i18nPath = "\\portlets\\intouch-crud-portlet\\docroot\\WEB-INF\\src\\"
    languagePath = "\\portlets\\intouch-crud-portlet\\docroot\\WEB-INF\\src\\content\\"
    if os.path.isfile(i18nPath + warningsFile):
        os.remove(i18nPath + warningsFile)

    if os.path.isfile(languagePath + warningsFile):
        os.remove(languagePath + warningsFile)  

    takingAllLabels(defaultDirectory + i18nPath, list_i18n)
    confrontFilesWithAllLabels(defaultDirectory + i18nPath, list_i18n, portletName)
    takingAllLabels(defaultDirectory + languagePath, list_language)
    confrontFilesWithAllLabels(defaultDirectory + languagePath, list_language, portletName)
    if os.path.isfile(defaultDirectory + i18nPath + warningsFile):
        displayWarnings(defaultDirectory + i18nPath + warningsFile)

    else:
        print("\nAll 'i18n' labels in: " + portletName + " are translated")

    if os.path.isfile(defaultDirectory + languagePath + warningsFile):
        displayWarnings(defaultDirectory + languagePath + warningsFile)
    
    else:
        print("\nAll 'Language' labels in: " + portletName + " are translated")

def baseCheck (list_language, portletName):

    languagePath = "\\portlets\\intouch-crud-portlet\\docroot\\WEB-INF\\src\\content\\"
    print("Working on " + portletName)
    takingAllLabels(defaultDirectory + languagePath, list_language)
    confrontFilesWithAllLabels(defaultDirectory + languagePath, list_language, portletName)
    if os.path.isfile(languagePath + warningsFile):
        displayWarnings(defaultDirectory + languagePath + warningsFile)

    else:
        print("All labels in " + portletName + " are translated")

def backOfficeCheck (list_language, portletName):

    languagePath = "\\portlets\\cobo-backoffice-portlet\\docroot\\WEB-INF\\src\\content\\"
    print("Working on " + portletName)
    takingAllLabels(defaultDirectory + languagePath, list_language)
    confrontFilesWithAllLabels(defaultDirectory + languagePath, list_language, portletName)
    if os.path.isfile(languagePath + warningsFile):
        displayWarnings(defaultDirectory + languagePath + warningsFile)

    else:
        print("All labels in " + portletName + " are translated")

def massiveFirmwareUpdateCheck(list_language, portletName):

    languagePath = "\\portlets\\intouch-aggiornamento-massivo-firmware-portlet\\docroot\\WEB-INF\\src\\content\\"
    print("Working on " + portletName)
    takingAllLabels(defaultDirectory + languagePath, list_language)  
    if os.path.isfile(defaultDirectory + allLabelsFile):
        print("FILE è PRESENTE PRIMA DI CONFRONTO")
        fmassive = open(defaultDirectory + languagePath + allLabelsFile, "r")
        lines = fmassive.readlines()
        print("Ti printo contenuto del file MASSIVE\n\n\n")
        for k in lines:
            print(k)
    confrontFilesWithAllLabels(defaultDirectory + languagePath, list_language, portletName)
    if os.path.isfile(languagePath + warningsFile):
        displayWarnings(defaultDirectory + languagePath + warningsFile)

    else:
        print("All labels in " + portletName + " are translated")

def customLoginCheck(list_language, portletName):

    languagePath = "\\portlets\\intouch-custom-login-portlet\\docroot\\WEB-INF\\src\\content\\"
    print("Working on " + portletName)
    takingAllLabels(defaultDirectory + languagePath, list_language)
    confrontFilesWithAllLabels(defaultDirectory + languagePath, list_language, portletName)
    if os.path.isfile(languagePath + warningsFile):
        displayWarnings(defaultDirectory + languagePath + warningsFile)

    else:
        print("All labels in " + portletName + " are translated")

def integrationCheck(list_language, portletName):

    languagePath = "\\portlets\\intouch-integration-api-portlet\\docroot\\WEB-INF\\src\\content\\"
    print("Working on " + portletName)
    takingAllLabels(defaultDirectory + languagePath, list_language)
    confrontFilesWithAllLabels(defaultDirectory + languagePath, list_language, portletName)
    if os.path.isfile(languagePath + warningsFile):
        displayWarnings(defaultDirectory + languagePath + warningsFile)

    else:
        print("All labels in " + portletName + " are translated")

def liferayTranslationCheck(list_language, portletName):

    languagePath = "\\hooks\\intouch-liferay-translation-hook\\docroot\\WEB-INF\\src\\content\\"
    print("Working on " + portletName)
    takingAllLabels(defaultDirectory + languagePath, list_language)
    confrontFilesWithAllLabels(defaultDirectory + languagePath, list_language, portletName)
    if os.path.isfile(languagePath + warningsFile):
        displayWarnings(defaultDirectory + languagePath + warningsFile)

    else:
        print("All labels in " + portletName + " are translated")

def notificationCheck(list_language, portletName):

    languagePath = "\\portlets\\intouch-notification-portlet\\docroot\\WEB-INF\\src\\content\\"
    print("Working on " + portletName)
    takingAllLabels(defaultDirectory + languagePath, list_language)
    confrontFilesWithAllLabels(defaultDirectory + languagePath, list_language, portletName)
    if os.path.isfile(languagePath + warningsFile):
        displayWarnings(defaultDirectory + languagePath + warningsFile)

    else:
        print("All labels in " + portletName + " are translated")

def reportCheck(list_language, portletName):

    languagePath = "\\portlets\\intouch-report-portlet\\docroot\\WEB-INF\\src\\content\\"
    print("Working on " + portletName)
    takingAllLabels(defaultDirectory + languagePath, list_language)
    confrontFilesWithAllLabels(defaultDirectory + languagePath, list_language, portletName)
    if os.path.isfile(languagePath + warningsFile):
        displayWarnings(defaultDirectory + languagePath + warningsFile)

    else:
        print("All labels in " + portletName + " are translated")

def v2FrontEndCheck(list_language, portletName):

    languagePath = "\\portlets\\intouch-v2-frontend-portlet\\docroot\\WEB-INF\\src\\content\\"
    print("Working on " + portletName)
    takingAllLabels(defaultDirectory + languagePath, list_language)
    confrontFilesWithAllLabels(defaultDirectory + languagePath, list_language, portletName)
    if os.path.isfile(languagePath + warningsFile):
        displayWarnings(defaultDirectory + languagePath + warningsFile)

    else:
        print("All labels in " + portletName + " are translated")


def progress(i, mainFileLen):
    return 100 * i / mainFileLen    

def takingAllLabels(workingDirectory, list):

    if os.path.isfile(workingDirectory + allLabelsFile):
        os.remove(workingDirectory + allLabelsFile)

    firstWrite = True
    print("\n\nCopying all labels in one place")
    workingDirectory = "C:\\projects\\INTOUCH\\Project\\LIFERAY\\SDK\\portlets\\intouch-aggiornamento-massivo-firmware-portlet\\docroot\\WEB-INF\\src\\content\\"
    for i in list:
        if firstWrite:
            try:
                lineNumbers = file_len(workingDirectory + list[0])
                for k in range(lineNumbers):
                    writeFile(workingDirectory + allLabelsFile, readLineOfFile(workingDirectory + list[0], k))

                firstWrite = False
            except:
                print("FILE " + list[0] + " DOESN'T EXIST")
                firstWrite = False

        else:
            try:
                mainFileLen = file_len(workingDirectory + i)
                for lineSecondFile in range(mainFileLen):
                    lineOfControlledFile = readLineOfFile(workingDirectory + i, lineSecondFile)
                    progressOfOperation = progress (lineSecondFile, mainFileLen)
                    sys.stdout.write("Processing " + i + " %d%% \r" % (progressOfOperation))
                    sys.stdout.flush()
                    if not checkIfExist(workingDirectory + allLabelsFile, file_len(workingDirectory + allLabelsFile), lineOfControlledFile):
                        writeFile(workingDirectory + allLabelsFile,  lineOfControlledFile)
            except:
                print("FILE " + workingDirectory + i + " DOESN'T EXIST")

def confrontFilesWithAllLabels(workingDirectory, list, portlet):
    try:
        for i in list:
            mainFileLen = file_len(workingDirectory + allLabelsFile)
            for lineAllLabelsFile in range(mainFileLen):
                progressOfOperation = progress (lineAllLabelsFile, mainFileLen)
                sys.stdout.write("Checking " + portlet + " for translations in the file:  " + i + " %d%% \r" % (progressOfOperation))
                if progressOfOperation == 100:
                    print("Check of the file: " + i + " in " + portlet + " is completed...")
                sys.stdout.flush()

                lineOfControlledFile = readLineOfFile(workingDirectory + allLabelsFile, lineAllLabelsFile)
                if lineOfControlledFile == '':
                    continue

                else:
                    if not checkIfExist(workingDirectory + i, file_len(workingDirectory + i), lineOfControlledFile):
                        foutwarnings = open(workingDirectory + warningsFile, "a")
                        foutwarnings.write("\n Portlet: " + portlet + " Translation label: " + lineOfControlledFile + " IS NOT present in " + i + " file ")
        os.remove(workingDirectory + allLabelsFile)
    except:
            print("FILE " + workingDirectory + i + " DOESN'T EXIST")
    print("\n\nFinished to check labels in " + portlet)
    

def writeFile(pathToFile, valueToWrite):
    if valueToWrite != "\n":
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

def checkIfExist(pathToFile, totalNumber, wordToConfront):
    exist = False 
    for z in range(totalNumber):
        filteredLine = readLineOfFile(pathToFile, z)
        if wordToConfront == filteredLine or wordToConfront + "\n" == filteredLine or wordToConfront + " \n" == filteredLine:
            exist = True

        if exist:
            break

    return exist  
          
def displayWarnings(pathToTheOutputFile):
    foutuputWarnings = open(pathToTheOutputFile)
    lines = foutuputWarnings.readlines()
    for k in lines:
        print(k)

    foutuputWarnings.close()
    os.remove(pathToTheOutputFile)
    
def main():
    list_i18n = ["i18n.properties", "i18n_de.properties", "i18n_fr.properties", "i18n_it.properties", "i18n_zh.properties", "i18n_es.properties"]
    list_language = ["Language.properties", "Language_de.properties", "Language_es.properties", "Language_fr.properties", 
                 "Language_it.properties"]

#    if len(sys.argv) < 2:
#        print('Need almost one parameter, example full command: python check_translation.py ' 
#            + '[ALL | CRUD | BASE | BACKOFFICE | MASSIVE | CUSTOM LOGIN | INTEGRATION | LIFERAY TRANSLATION | NOTIFICATION| REPORT | FRONTEND]' )
#        exit()

#    portletName = sys.argv[1].upper() if sys.argv[1].upper() in PORTLETS or sys.argv[1] == "ALL" else None
    portletName = "MASSIVE"
    if portletName != "MASSIVE":
        print(portletName)
#    if portletName is None:
#        print('Not found valid portlet, must be: ' + str(PORTLETS))
#        portletName = "MASSIVE"
#        exit()
#
    else:
        
        print("\n\n\n********************* START OF SCRIPT *********************\n\n\n")

        if portletName == "ALL":
            allPortlets(list_i18n, list_language)

        else:
            if portletName == "BASE":
                allPortlets(list_i18n, list_language)

            elif portletName == "CRUD":
                crudCheck(list_i18n, list_language, portletName)

            elif portletName == "BACKOFFICE":
                backOfficeCheck(list_language, portletName)

            elif portletName == "MASSIVE":
                massiveFirmwareUpdateCheck(list_language, portletName)

            elif portletName == "CUSTOM LOGIN":
                customLoginCheck(list_language, portletName)

            elif portletName == "INTEGRATION":
                integrationCheck(list_language, portletName)

            elif portletName == "LIFERAY TRANSLATION":
                liferayTranslationCheck(list_language, portletName)

            elif portletName == "NOTIFICATION":
                notificationCheck(list_language, portletName)

            elif portletName == "REPORT":
                reportCheck(list_language, portletName)

            elif portletName == "FRONTEND":
                v2FrontEndCheck(list_language, portletName)

    
    print("\n\n\n********************* END OF SCRIPT *********************\n\n\n")

main()