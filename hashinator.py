from PIL import Image 
from PIL import ImageChops
import os 

#Uncomment if you want to record how long it takes
'''
import time 
start = time.process_time()
'''

directory = os.path.dirname(os.path.realpath(__file__))


dumpedFiles = os.listdir(directory+"\dumpedTex")
inputFiles = os.listdir(directory+"\inputTex")

outputList = []

cropcoords = (0, 0, 143, 232)

for i in range(len(inputFiles)):
    inputPath = directory+"\inputTex\\" + inputFiles[i]
    inputImage = Image.open(inputPath).crop(cropcoords)

    for j in range(len(dumpedFiles)):
        #remove from list if found
        dumpPath = directory+"\dumpedTex\\" + dumpedFiles[j]
        dumpImage = Image.open(dumpPath).crop(cropcoords)
        
        diff = ImageChops.difference(inputImage, dumpImage)

        if not diff.getbbox():
            outputList.append((inputFiles[i], dumpedFiles.pop(j)))
            break


outputString = ""

for combo in outputList:
    outputString += combo[1].strip(".png")+"="+combo[0]+"\n"

outputFile = open(directory+"\output.txt", "w")
outputFile.write(outputString)
outputFile.close()

#print(time.process_time()-start)