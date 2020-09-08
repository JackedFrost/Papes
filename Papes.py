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

    if rgb[0] >rgb[1]+rgb[2]:
        shutil.move(picture , 'C:\Pictures\sorted\Red')
    elif rgb[2]>rgb[0]+rgb[1]:
        shutil.move(picture , 'C:\Pictures\sorted\Blue')
    elif rgb[1]>rgb[0]+rgb[2]:
        shutil.move( picture , 'C:\Pictures\sorted\Green')
    elif rgb[0] +rgb[2]>rgb[1] and rgb[2]<rgb[1]:
        shutil.move(picture , 'C:\Pictures\sorted\Pink')
    elif rgb[0] +rgb[1]>rgb[2] and rgb[0] + rgb[1] > 360 and rgb[2]<100:
        shutil.move(picture , 'C:\Pictures\sorted\Yellow')
    elif rgb[0] +rgb[2]>rgb[1] and rgb[2]<rgb[0]:
        shutil.move(picture , 'C:\Pictures\sorted\Purple')
    elif rgb[0] in range(25,100) and rgb[1] in range(25,100) and rgb[2] in range(25,100):
        shutil.move(picture , 'C:\Pictures\sorted\Gray')
    elif rgb[0] +rgb[1]>rgb[2] and rgb[1]>rgb[0]:
        shutil.move(picture , 'C:\Pictures\sorted\Gray')
    elif rgb[0] in range(0,25) and rgb[1] in range(0,25) and rgb[2] in range(0,25):
        shutil.move(picture , 'C:\Pictures\sorted\Black')
    elif rgb[0] in range(230,255) and rgb[1] in range(230,255) and rgb[2] in range(230,255):
        shutil.move(picture , 'C:\Pictures\sorted\White')
    else:
        shutil.move(picture , 'C:\Pictures\sorted\ManualSort')

try:
    os.mkdir('C:\Pictures')
    os.mkdir('C:\Pictures\sorted')
    os.mkdir('C:\Pictures\sorted\Red')
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