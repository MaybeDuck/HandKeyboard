import cv2
import keyboard

leeterorder = ["","E", "T", "A", "O","I",
               "N","enter","S","R","H","D",
               "L","U","C"," ","M","F","Y",
               "W","G","P","B","V","K","X",
               "Q","J","Z", "backspace" ]
ticks = 0
lastKey = ""
FistHand = 0
def indentify(map,width,img):
    global FistHand
    set = []

    FingerTipindex = [4,8,12,16,20, 25,29,33,37,41,45]
    for index in range(len(map)):
        if index in FingerTipindex:

            if index == 4 or index == 25:
                #right hand
                if map[index][1]>map[index+16][1]:
                    if(len(set)==0):
                        FistHand = 0
                    if (map[(index)][1] > map[(index) -2][1]):
                        set.append(1)
                    else:
                        set.append(0)
                #left hand
                else:
                    if (len(set) == 0):
                        FistHand = 1
                    if (map[(index)][1] < map[(index) -2][1]):
                        set.append(1)
                    else:
                        set.append(0)
            #fingers
            else:
                if(map[(index)][2]<map[(index)-2][2]):
                    set.append(1)
                else:
                    set.append(0)
    numberindefyer(set,img)



def numberindefyer(set,img):
    global lastKey
    global ticks
    id = 0
    tickcap = 50

    if (len(set)) == 10:
        newset = []
        #set = [0,1,2,3,4,5,6,7,8,9]
        for i in range(5):

            if(FistHand == 0):
                newset.append(set[i])
                newset.append(set[i + 5])


            else:
                newset.append(set[i + 5])
                newset.append(set[i])





        set = newset
        print((FistHand," , ",set))

    for i in range(len(set)):
        id += set[i]*(2**(i))
    if id < len(leeterorder):
        key = leeterorder[id]
        cv2.putText(img, str(key), ((400, 50)), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)
        cv2.putText(img, str(tickcap-ticks), ((450, 50)), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 1)
        if lastKey == key and ticks >= tickcap:
            if len(key) <= 1:
                keyboard.write(key)
            else:
                keyboard.press(key)
                keyboard.release(key)
            ticks -= ticks
        elif lastKey != key:
            ticks -= ticks
            lastKey = key
        else:
            ticks +=1







