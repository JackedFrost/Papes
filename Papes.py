import os
import shutil
import colorgram

def color_sorter(entry):
    picture = entry.path
    dropper = colorgram.extract(picture ,1)
    #the arguments are the picture and how many values of rgb you want it to return, sorted by their percentage shown in the picture
    color = dropper[0]
    #the color pulled from dropper will pull the rgb value specifically from the data colorgram will return
    hsl = color.hsl
    #section below will pull the value from rgb and sort in to the correct foler [0] being red


    if hsl[2]in range(0,10):
        shutil.move(picture , 'C:\Pictures\sorted\Black')
    elif hsl[2]in range(90,100):
        shutil.move(picture , 'C:\Pictures\sorted\White')
    elif hsl[1]in range(10,30):
        shutil.move(picture , 'C:\Pictures\sorted\Gray')
    elif hsl[0] in range(0,10) or hsl[0] in range(340,360):
        shutil.move(picture , 'C:\Pictures\sorted\Red')
    elif hsl[0] in range(11,44):
        shutil.move(picture , 'C:\Pictures\sorted\Orange')
    elif hsl[0] in range(140,260):
        shutil.move(picture , 'C:\Pictures\sorted\Blue')
    elif hsl[0]in range(70,139):
        shutil.move( picture , 'C:\Pictures\sorted\Green')
    elif hsl[0]in range(295,339):
        shutil.move(picture , 'C:\Pictures\sorted\Pink')
    elif hsl[0] in range(45,69):
        shutil.move(picture , 'C:\Pictures\sorted\Yellow')
    elif hsl[0] in range (260,295):
        shutil.move(picture , 'C:\Pictures\sorted\Purple')
    else:
        shutil.move(picture , 'C:\Pictures\sorted\ManualSort')

try:
    os.mkdir('C:\Pictures')
    os.mkdir('C:\Pictures\sorted')
    os.mkdir('C:\Pictures\sorted\Red')
    os.mkdir('C:\Pictures\sorted\Orange')
    os.mkdir('C:\Pictures\sorted\Blue')
    os.mkdir('C:\Pictures\sorted\Green')
    os.mkdir('C:\Pictures\sorted\Pink')
    os.mkdir('C:\Pictures\sorted\Yellow')
    os.mkdir('C:\Pictures\sorted\Purple')
    os.mkdir('C:\Pictures\sorted\Black')
    os.mkdir('C:\Pictures\sorted\Gray')
    os.mkdir('C:\Pictures\sorted\White')
    os.mkdir('C:\Pictures\sorted\ManualSort')
except:
    print("Folders have been created, commencing sort")
finally:
    with os.scandir(r"C:\Users\apoca\OneDrive\Desktop\testenv") as files:
        for entry in files:
            color_sorter(entry)
