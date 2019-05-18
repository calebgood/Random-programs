from pyautogui import position
import time


def full_box():
   def box_find():
      x=[]
      c=0
      while True:
         for i in range(4):         #reads mouseposition 4 times with 0.3s gap
             x.append(position())
             time.sleep(0.3)
         for i in range(4):         #checks whether all 4 readings are same
             if x[0]==x[i]:
                 c+=1
         if c==4:                   #if all four are same then break loop
             break
         else:
             x=[]                   #else restart the function
             c=0
      return(x[0])

   def splitting(x):                #jobless converting str to list of int
      x=str(x)
      x=x.strip('Point')
      x=x.split(',')   
      x[0]=x[0].strip('(x=')
      x[1]=x[1].strip(' y=')
      x[1]=x[1].strip(')')
      return(x)

   print("starting...for top left")
   time.sleep(.5)
   l,u=splitting(box_find())   
   print("waiting..")
   time.sleep(1)
   print("restart for bottom right")
   r,d=splitting(box_find())
   y=[l,u,r,d]
   y=[int(x) for x in y]
   return(y)

def wid_ht_find():               #finds width and height using boxfind
   x=full_box()
   print("Width:",abs(x[0]-x[2]))
   print("Height:",abs(x[1]-x[3]))


