import time, random, os, webbrowser

fileObj = open("links.txt", "w+") #opens file, creates one if it doesn't exist
if(os.stat("links.txt").st_size == 0):
    fileObj.write("https://www.youtube.com/watch?v=TYRDgd3Tb44")
    fileObj.close()
    fileObj = open("links.txt", "r")

links = fileObj.readlines()  

alarm = input("Set alarm in HH:MM format: ")
currentTime = time.strftime("%H:%M")

while currentTime != alarm:
    currentTime = time.strftime("%H:%M")

if currentTime == alarm:
    print ("Waking up...")
    webbrowser.open(random.choice(links), new=0)
