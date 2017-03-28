openedFile = False
while (not openedFile):
    fileName = raw_input("Open what file: ")
    try:
        inFile = open(fileName,"r")
        openedFile = True
    except IOError:
        print "File opening failed,try again"

fileParts = fileName.split(".")
outFile = open(fileParts[0] + "Rev." + fileParts[1],"w")

for line in inFile:
    words = line.split()
    words.reverse()
    for w in words:
        outFile.write(w)
        outFile.write(" ")
    outFile.write("\n")

inFile.close()
outFile.close()
