import pygame, sys
from pygame.locals import *

# Programmed by John Costello
# In this program the next colour is an adjacent colour to the previous colour in 'Colour-space'

global locationIndex
locationIndex=1
global cubeLength
cubeLength=16
global cubeVolume
cubeVolume=cubeLength**3

FPS = 60
WINDOWWIDTH=800
WINDOWHEIGHT=800
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

#============================================================================   
def main():
   global MAINCLOCK, SCREEN
   global locationIndex
   global blackToWhiteDirection
   blackToWhiteDirection=True
   pygame.init()
   SCREEN=pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))  
   SCREEN.fill(BLACK)
   pygame.display.set_caption("Multicolour Brush")
   font=pygame.font.Font('freesansbold.ttf',10)
   text=font.render("Move The Mouse",True,WHITE,BLACK)
   textRect=text.get_rect()
   textRect.center=(400,400)
   SCREEN.blit(text,textRect)
   pygame.display.update() 
   MAINCLOCK=pygame.time.Clock()
   running=True
   while(running):
      for event in pygame.event.get():
         if(event.type==pygame.QUIT):
            running=False
      if(running==True):
         SRC_returnValues=shellRingCell(locationIndex)         
         shellNumber=SRC_returnValues[0]
         ringNumber=SRC_returnValues[1]
         cellNumber=SRC_returnValues[2]
         modifiedShellSubLocationNumber=SRC_returnValues[3]
         xyzNumbers=xyzVal(shellNumber,modifiedShellSubLocationNumber)
         xNumber=xyzNumbers[0]
         yNumber=xyzNumbers[1]
         zNumber=xyzNumbers[2]
         rNumber=(xNumber-1)*(cubeLength)+(xNumber-1)
         gNumber=(yNumber-1)*(cubeLength)+(yNumber-1)
         bNumber=(zNumber-1)*(cubeLength)+(zNumber-1)
         colour=(rNumber,gNumber,bNumber)
         rel=pygame.mouse.get_rel()
         if((rel[0]**2+rel[1]**2)>0):
            pos=pygame.mouse.get_pos()
            pygame.draw.circle(SCREEN,colour,pos,40)
         #----------------------------------------------------
         pygame.draw.rect(SCREEN,BLACK,(10,30,61,21))
         pygame.draw.rect(SCREEN,WHITE,(10,30,61,21),1)
         text=font.render(str(locationIndex),True,WHITE,BLACK)
         textRect=text.get_rect()
         textRect.center=(40,40)
         SCREEN.blit(text,textRect)
                    #-----------------
         pygame.draw.rect(SCREEN,colour,(10,50,61,51))
         pygame.draw.rect(SCREEN,WHITE,(10,50,61,51),1)
                    #-----------------
         pygame.draw.rect(SCREEN,BLACK,(10,100,61,21))
         pygame.draw.rect(SCREEN,WHITE,(10,100,61,21),1)
         text=font.render(str(bNumber),True,BLUE,BLACK)
         textRect=text.get_rect()
         textRect.center=(40,110)
         SCREEN.blit(text,textRect)
                    #-----------------
         pygame.draw.rect(SCREEN,BLACK,(10,120,61,21))
         pygame.draw.rect(SCREEN,WHITE,(10,120,61,21),1)
         text=font.render(str(gNumber),True,GREEN,BLACK)
         textRect=text.get_rect()
         textRect.center=(40,130)
         SCREEN.blit(text,textRect)
                    #-----------------
         pygame.draw.rect(SCREEN,BLACK,(10,140,61,21))
         pygame.draw.rect(SCREEN,WHITE,(10,140,61,21),1)
         text=font.render(str(rNumber),True,RED,BLACK)
         textRect=text.get_rect()
         textRect.center=(40,150)
         SCREEN.blit(text,textRect)
                    #-----------------
         pygame.draw.rect(SCREEN,BLACK,(10,160,61,63))
         pygame.draw.rect(SCREEN,WHITE,(10,160,61,63),1)
         
         pygame.draw.rect(SCREEN,BLUE,(12,222-((zNumber-1)*4),17,((zNumber-1)*4)))
         pygame.draw.rect(SCREEN,GREEN,(32,222-((yNumber-1)*4),17,((yNumber-1)*4)))
         pygame.draw.rect(SCREEN,RED,(52,222-((xNumber-1)*4),17,((xNumber-1)*4)))
         #----------------------------------------------------         
         MAINCLOCK.tick(FPS)    
         pygame.display.update() 
         #----------------------------------------------------         
         if(blackToWhiteDirection==True):
            locationIndex=locationIndex+1
            if(locationIndex==cubeVolume):    
               blackToWhiteDirection=False
         else:
            locationIndex=locationIndex-1
            if(locationIndex==1):
               blackToWhiteDirection=True               
   pygame.quit()
   sys.exit()
   
#============================================================================  
def shellRingCell(location):
   #----------------------------------------------------
   shellIndex=1
   while(location>shellIndex**3):   
      shellIndex=shellIndex+1
   shellValue=shellIndex
   #----------------------------------------------------   
   shellSubLocation=location-((shellValue-1)**3)
   ringIndex=1
   shellSubLocation_index=1
   while(shellSubLocation_index<shellSubLocation):
      ringIndex+=1
      shellSubLocation_index+=((6*ringIndex)-6)
   ringValue=ringIndex;
   previousRingValue=ringValue-1
   previousRingIndex=1
   previousRingsCellsIndex=0
   while(previousRingIndex<=previousRingValue):
      if(previousRingIndex==1):
         previousRingsCellsIndex=1
      else:
         previousRingsCellsIndex+=((6*previousRingIndex)-6)
      previousRingIndex=previousRingIndex+1  
   previousRingsCellsValue=previousRingsCellsIndex
   ringSubLocation=shellSubLocation-previousRingsCellsValue
   cellValue=ringSubLocation
   #------------------------------------------------------
   numOfCellsPerShellIndex=1
   ringIndex=1
   while(ringIndex<shellValue):
      ringIndex+=1
      numOfCellsPerShellIndex+=((6*ringIndex)-6)
   numOfCellsPerShellIndexValue=numOfCellsPerShellIndex
   #-------------------------------------------------------
   modifiedShellSubLocation=0
   if(shellValue%2==0):
      modifiedShellSubLocation=shellSubLocation
   else:
      modifiedShellSubLocation=numOfCellsPerShellIndexValue+1-shellSubLocation   
   #-------------------------------------------------------
   returnValues=(shellValue,ringValue,cellValue,modifiedShellSubLocation)
   return(returnValues)
#============================================================================   
def xyzVal(shellValue,modifiedShellSubLocation):
   xValue=0
   yValue=0
   zValue=0
   nextDirection=0
   #--------------------------------------------------------
   xIndex=shellValue
   yIndex=shellValue
   zIndex=shellValue
   stepsIndex=1
   stepDirection=1
   fewSteps=1
   incrementFewSteps=False
   while(stepsIndex<modifiedShellSubLocation):
      fewStepsIndex=0;
      while(stepsIndex<modifiedShellSubLocation and stepDirection==1 and fewStepsIndex<fewSteps):
         zIndex-=1
         fewStepsIndex+=1
         stepsIndex+=1
         nextDirection=2
      fewStepsIndex=0 
      while(stepsIndex<modifiedShellSubLocation and stepDirection==2 and fewStepsIndex<fewSteps):
         xIndex-=1
         fewStepsIndex+=1
         stepsIndex+=1
         nextDirection=3
      fewStepsIndex=0 
      while(stepsIndex<modifiedShellSubLocation and stepDirection==3 and fewStepsIndex<fewSteps): 
         zIndex+=1
         fewStepsIndex+=1
         stepsIndex+=1
         nextDirection=4
      fewStepsIndex=0 
      while(stepsIndex<modifiedShellSubLocation and stepDirection==4 and fewStepsIndex<fewSteps):             
         yIndex-=1
         fewStepsIndex+=1
         stepsIndex+=1
         nextDirection=5
      fewStepsIndex=0 
      while(stepsIndex<modifiedShellSubLocation and stepDirection==5 and fewStepsIndex<fewSteps):   
         xIndex+=1
         fewStepsIndex+=1
         stepsIndex+=1
         nextDirection=6
      fewStepsIndex=0
      while(stepsIndex<modifiedShellSubLocation and stepDirection==6 and fewStepsIndex<fewSteps+1):   
         zIndex-=1
         fewStepsIndex+=1
         stepsIndex+=1
         nextDirection=7
      while(stepsIndex<modifiedShellSubLocation and stepDirection==7 and fewStepsIndex<fewSteps):  
         yIndex+=1
         fewStepsIndex+=1
         stepsIndex+=1
         nextDirection=2
         incrementFewSteps=True   
      stepDirection=nextDirection
      if(incrementFewSteps==True):
         fewSteps+=1
         incrementFewSteps=False         
   xValue=xIndex
   yValue=yIndex
   zValue=zIndex   
   #--------------------------------------------------------
   xyzValues=(xValue,yValue,zValue)
   return(xyzValues)  
#============================================================================   
if __name__ == '__main__':
    main()   