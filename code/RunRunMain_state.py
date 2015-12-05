import random
import RunRun_Framework
import RunRunRank_state
from pico2d import *





lava = None
stage = None
trapManager = None
itemManager = None
life = None
balls = None
big_balls =None
frame = 0
stageNum = 1
TrapList = []
ItemList = []
rotation = 0
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class Map:
    global stageNum,lava, rotation
    def __init__(self):
        self.bkframe = 0
        self.doubleX = 600
        self.doubleY = 400
        self.groundX = 600
        self.groundY = 0
        self.groundH = 0

        self.background = None
        self.doublebackground = None
        self.stageOneBackground = None
        self.stageTwoBackground = None
        self.stageThreeBackground = None
        self.stageFourBackground = None
        self.stageOnedoublebackground = None
        self.stageTwodoublebackground = None
        self.stageThreedoublebackground = None
        self.stageFourdoublebackground = None
        self.stageOneGround = None
        self.stageTwoGround = None
        self.stageThreeGround = None
        self.stageFourGround = None
        self.SetStageImage()
    def LoadStageImage(self):
        self.stageOneBackground = load_image('background2.2.png')
        self.stageTwoBackground = load_image('background2.png')
        self.stageThreeBackground = load_image('background3.png')
        self.stageFourBackground = load_image('background4.png')
        self.stageOnedoublebackground = load_image('doublebackground.png')
        self.stageTwodoublebackground = load_image('doublebackground1.png')
        self.stageThreedoublebackground = load_image('doublebackground3.png')
        self.stageFourdoublebackground = load_image('doublebackground4.png')
        self.stageOneGround = load_image('ground1.png')
        self.stageTwoGround = load_image('ground2.png')
        self.stageThreeGround = load_image('grass.png')
        self.stageFourGround = load_image('ground4.png')

    def SetStageImage(self):
        if stageNum == 1:
            self.background = self.stageOneBackground
            self.doublebackground = self.stageOnedoublebackground
            self.ground = self.stageOneGround
            self.groundY, self.groundH = 30, 240
        elif stageNum == 2:
            self.background = self.stageTwoBackground
            self.doublebackground = self.stageTwodoublebackground
            self.ground = self.stageTwoGround
            self.groundY, self.groundH = 30, 240
        elif stageNum == 3:
            self.background = self.stageThreeBackground
            self.doublebackground = self.stageThreedoublebackground
            self.ground = self.stageThreeGround
            self.groundY, self.groundH = 600, 1200
        elif stageNum == 4:
            self.background = self.stageFourBackground
            self.doublebackground = self.stageFourdoublebackground
            self.ground = self.stageFourGround
            self.groundY, self.groundH = 70, 130
    def rotatePos(self):
        if stageNum == 1:
            self.doubleX, self.doubleY = self.doubleY, self.doubleX
    def update(self):
        if stageNum == 1:
           self.doubleX -= 5
           if self.doubleX <= -600:
               self.doubleX = 600
           self.groundX -= 20
           if self.groundX <= -600:
                self.groundX = 600
        elif stageNum == 2:
           self.doubleX -= 5
           if self.doubleX <= -600:
               self.doubleX = 600
           self.groundX -= 20
           if self.groundX <= -600:
                self.groundX = 600
        elif stageNum == 3:
           self.doubleX += 5
           if self.doubleX >= 1800:
               self.doubleX = 600
           self.groundX += 20
           if self.groundX >= 1800:
                self.groundX = 600
        elif stageNum == 4:
           self.doubleX += 5
           if self.doubleX >= 1800:
               self.doubleX = 600
           self.groundX += 20
           if self.groundX >= 1800:
                self.groundX = 600

    def draw(self):
        if stageNum == 1:
            self.doublebackground.rotate_draw(rotation, self.doubleX, self.doubleY, 1200, 800)
            self.doublebackground.rotate_draw(rotation, self.doubleX+1200, self.doubleY, 1200, 800)
            self.background.rotate_draw(rotation, self.groundX, self.doubleY, 1200, 800)
            self.background.rotate_draw(rotation, self.groundX+1200, self.doubleY, 1200, 800)
            self.ground.rotate_draw(rotation, self.groundX, self.groundY, 1200, self.groundH)
            self.ground.rotate_draw(rotation, self.groundX+1200, self.groundY, 1200, self.groundH)
        elif stageNum == 2:
            self.doublebackground.rotate_draw(rotation, 600,self.doubleX, 1200, 1200)
            self.doublebackground.rotate_draw(rotation, 600,self.doubleX+1200, 1200, 1200)
            self.background.rotate_draw(rotation, 700, self.groundX, 1200, 1200)
            self.background.rotate_draw(rotation, 700, self.groundX+1200, 1200, 1200)
            self.ground.rotate_draw(rotation, 1160, self.groundX, 1200, 220)
            self.ground.rotate_draw(rotation, 1160, self.groundX+1200, 1200, 220)
        elif stageNum == 3:
            self.doublebackground.rotate_draw(rotation, self.doubleX, 400, 1200, 800)
            self.doublebackground.rotate_draw(rotation, self.doubleX-1200, 400, 1200, 800)
            self.background.rotate_draw(rotation, self.groundX, 400, 1200, 800)
            self.background.rotate_draw(rotation, self.groundX-1200, 400, 1200, 800)
            self.ground.rotate_draw(rotation, self.groundX, 200, 1200, 1200)
            self.ground.rotate_draw(rotation, self.groundX-1200, 200, 1200, 1200)
        elif stageNum == 4:
            self.doublebackground.rotate_draw(rotation,  600,self.doubleX,  1200, 1200)
            self.doublebackground.rotate_draw(rotation, 600, self.doubleX-1200, 1200, 1200)
            self.background.rotate_draw(rotation, 500, self.groundX,  1200, 1200)
            self.background.rotate_draw(rotation, 500, self.groundX-1200,  1200, 1200)
            self.ground.rotate_draw(rotation, 67, self.groundX, 1200, 130)
            self.ground.rotate_draw(rotation, 67, self.groundX-1200, 1200, 130)

class ItemManager:
    global ItemList, stageNum
    def __init__(self):
        self.x = 1500
    def SetStageItem(self):
        for i in range(30):
            if stageNum == 1:
                ItemList.append(Item((i*550)+random.randint(-250,250)+1200, random.randint(200,300), random.randint(1,4)))
            elif stageNum == 2:
                ItemList.append(Item((i*550)+random.randint(-250,250)+1200, random.randint(200,300), random.randint(1,4)))
            elif stageNum == 3:
                ItemList.append(Item(((-i)*550)+random.randint(-250,250)-1200, random.randint(200,300), random.randint(1,4)))
            elif stageNum == 4:
                ItemList.append(Item(((-i)*550)+random.randint(-250,250)+1200, random.randint(200,300), random.randint(1,4)))
    def updata(self):
        pass

class Item:
    global stageNum
    global lava
    global ItemList
    global life
    global rotation
    load = False
    FirstItem = None
    SecondItem = None
    ThirdItem = None
    FourthItem = None
    def __init__(self, x, y, itemType):
        self.itemX = x
        self.itemY = y
        self.frame = 0
        self.MaxFrame = 6
        self.type = itemType
        self.item = None
        self.imageX = 0
        self.imageY = 0
        self.width = 0
        self.height = 0
        self.LoadItemImage()
        self.SetItemImage()

    def LoadItemImage(self):
        if Item.load == False:
            Item.FirstItem = load_image('item1.png')
            Item.SecondItem = load_image('item1.png')
            Item.ThirdItem = load_image('item1.png')
            Item.FourthItem = load_image('item1.png')
            Item.load = True

    def SetItemImage(self):
        if self.type == 1:
            self.item = Item.FirstItem
            self.MaxFrame = 10
            self.imageX = 67
            self.imageY = 59
            self.width = 67
            self.height = 59
        elif self.type == 2:
            self.item = Item.SecondItem
            self.MaxFrame = 10
            self.imageX = 67
            self.imageY = 59
            self.width = 67
            self.height = 59
        elif self.type == 3:
            self.item = Item.ThirdItem
            self.MaxFrame = 10
            self.imageX = 67
            self.imageY = 59
            self.width = 67
            self.height = 59
        elif self.type == 4:
            self.item = Item.FourthItem
            self.MaxFrame = 10
            self.imageX = 67
            self.imageY = 59
            self.width = 67
            self.height = 59

    def hit(self):
        for item in ItemList:
            if stageNum == 1:
                if (lava.lavaX+lava.width/3) >= (item.itemX - item.width/4) and (lava.lavaX-lava.width/3) <= (item.itemX + item.width/4):
                    if (lava.lavaY - lava.height/3) <= (item.itemY + item.height/3) and (lava.lavaY + lava.height/3) >= (item.itemY - item.height/3):
                        ItemList.remove(item)
                        return True
            if stageNum == 2:
                if (600-lava.lavaX+(lava.height/3)) >= (item.itemX-(item.width/2)) and (600-lava.lavaX-(lava.height/3)) <= (item.itemX+(item.width/2)):
                    if (1200-lava.lavaY+(lava.width/2)) >= (1200-item.itemY-(item.height/2)) and (1200-lava.lavaY-(lava.width/2)) <= (1200-item.itemY+(item.height/2)):
                        ItemList.remove(item)
                        return True
            if stageNum == 3:
                if (1200-lava.lavaX+(lava.width/3)) >= (item.itemX-(item.width/2)) and (1200-lava.lavaX-(lava.width/3)) <= (item.itemX+(item.width/2)):
                    if (800-lava.lavaY-(lava.height/2)) <= (800-item.itemY+(item.height/2)) and (800-lava.lavaY+(lava.height/2)) >= (800-item.itemY-(item.height/2)):
                        ItemList.remove(item)
                        return True
            if stageNum == 4:
                if (lava.lavaX+200+(lava.height/3)) >= (item.itemX+200-(item.width/2)) and (lava.lavaX+200-(lava.height/3)) <= (item.itemX+200+(item.width/2)):
                    if (lava.lavaY+(lava.width/2)) >= (item.itemY-(item.height/2)) and (lava.lavaY-(lava.width/2)) <= (item.itemY+(item.height/2)):
                        ItemList.remove(item)
                        return True
        return False

    def removeItem(self):
        for item in ItemList:
            if self.itemX <= -50:
                ItemList.remove(item)



    def update(self):
        self.frame = (self.frame+1) % self.MaxFrame
        self.moving()


    def moving(self):
        if stageNum == 1:
            self.itemX = (self.itemX-lava.speed)
        elif stageNum == 2:
            self.itemX = (self.itemX-lava.speed)
        elif stageNum == 3:
            self.itemX = (self.itemX+lava.speed)
        elif stageNum == 4:
            self.itemX = (self.itemX+lava.speed)


        if self.hit() == True:
            if self.type == 1 or self.type ==2 or self.type == 3 or self.type == 4:
                life.onelife += 5


    def draw(self):
        if stageNum == 1:
            self.item.clip_rotate_draw(rotation, self.frame * self.imageX, 0, self.imageX, self.imageY, self.itemX, self.itemY, self.width, self.height)

        elif stageNum == 2:
            self.item.clip_rotate_draw(rotation, self.frame * self.imageX, 0, self.imageX, self.imageY, 1200-self.itemY, self.itemX, self.width, self.height)

        elif stageNum == 3:
            self.item.clip_rotate_draw(rotation, self.frame * self.imageX, 0, self.imageX, self.imageY, self.itemX, 800-self.itemY, self.width, self.height)

        elif stageNum == 4:
            self.item.clip_rotate_draw(rotation, self.frame * self.imageX, 0, self.imageX, self.imageY, self.itemY, self.itemX+200, self.width, self.height)






class TrapManager:
    global TrapList, stageNum
    def __init__(self):
        self.x = 1500
    def SetStageTrap(self):
        for i in range(30):
            if stageNum == 1:
                TrapList.append(Trap((i*750)+random.randint(-250,250)+1200, random.randint(1,3)))
            if stageNum == 2:
                TrapList.append(Trap((i*750)+random.randint(-250,250)+1200, random.randint(1,3)))
            if stageNum == 3:
                TrapList.append(Trap(((-i)*750)+random.randint(-250,250)-1200, random.randint(1,3)))
            if stageNum == 4:
                TrapList.append(Trap(((-i)*750)+random.randint(-250,250)+1200, random.randint(1,3)))
    def updata(self):
        pass

class Trap:
    global stageNum
    global lava
    global TrapList
    global life
    global rotation
    load = False
    firstStageOneTrap = None
    firstStageTwoTrap = None
    firstStageThreeTrap = None
    firstStageFourTrap = None
    SecondStageOneTrap = None
    SecondStageTwoTrap = None
    SecondStageThreeTrap = None
    SecondStageFourTrap = None
    ThirdStageOneTrap = None
    ThirdStageTwoTrap = None
    ThirdStageThreeTrap = None
    ThirdStageFourTrap = None
    FourthStageOneTrap = None
    FourthStageTwoTrap = None
    FourthStageThreeTrap = None
    FourthStageFourTrap = None
    def __init__(self, x, trapType):
        self.trapX = x
        self.trapY = 0
        self.frame = 0
        self.MaxFrame = 6
        self.type = trapType
        self.trap = None
        self.imageX = 0
        self.imageY = 0
        self.width = 0
        self.height = 0
        self.LoadTrapImage()
        self.SetTrapImage()

    def LoadTrapImage(self):
        if Trap.load == False:
            Trap.firstStageOneTrap = load_image('1.1Trap.png')
            Trap.firstStageTwoTrap = load_image('1.2Trap.png')
            Trap.firstStageThreeTrap = load_image('1.3Trap.png')
            Trap.firstStageFourTrap = None
            Trap.SecondStageOneTrap = load_image('2.1Trap.png')
            Trap.SecondStageTwoTrap = load_image('2.2Trap.png')
            Trap.SecondStageThreeTrap = load_image('2.3Trap.png')
            Trap.SecondStageFourTrap = None
            Trap.ThirdStageOneTrap = load_image('3.1Trap.png')
            Trap.ThirdStageTwoTrap = load_image('3.2Trap.png')
            Trap.ThirdStageThreeTrap = load_image('1.3Trap.png')
            Trap.ThirdStageFourTrap = None
            Trap.FourthStageOneTrap = load_image('4.1Trap.png')
            Trap.FourthStageTwoTrap = load_image('2.4Trap.png')
            Trap.FourthStageThreeTrap = load_image('1.3Trap.png')
            Trap.FourthStageFourTrap = None
            Trap.load = True
            print('loadtrap')

    def SetTrapImage(self):
        if stageNum == 1:
            if self.type == 1:
                self.trap = Trap.firstStageOneTrap
                self.MaxFrame = 6
                self.imageX = 141
                self.imageY = 141
                self.trapY = 185
                self.width = 70
                self.height = 100
            elif self.type == 2:
                self.trap = Trap.firstStageTwoTrap
                self.MaxFrame = 6
                self.imageX = 133
                self.imageY = 148
                self.trapY = 195
                self.width = 100
                self.height = 135
            elif self.type == 3:
                self.trap = Trap.firstStageThreeTrap
                self.MaxFrame = 4
                self.imageX = 147
                self.imageY = 108
                self.trapY = 300
                self.width = 108
                self.height = 180
        if stageNum == 2:
            if self.type == 1:
                self.trap = Trap.SecondStageOneTrap
                self.MaxFrame = 10
                self.imageX = 84
                self.imageY = 78
                self.trapY = 180
                self.width = 100
                self.height = 100
            elif self.type == 2:
                self.trap = Trap.SecondStageTwoTrap
                self.MaxFrame = 10
                self.imageX = 110
                self.imageY = 135
                self.trapY = 210
                self.width = 100
                self.height = 200
            elif self.type == 3:
                self.trap = Trap.SecondStageThreeTrap
                self.MaxFrame = 12
                self.imageX = 173
                self.imageY = 136
                self.trapY = 415
                self.width = 173
                self.height = 400
        if stageNum == 3:
            if self.type == 1:
                self.trap = Trap.ThirdStageOneTrap
                self.MaxFrame = 6
                self.imageX = 97
                self.imageY = 149
                self.trapY = 180
                self.width= 130
                self.height = 100
            elif self.type == 2:
                self.trap = Trap.ThirdStageTwoTrap
                self.MaxFrame = 10
                self.imageX = 110
                self.imageY = 135
                self.trapY = 210
                self.width = 100
                self.height = 200
            elif self.type == 3:
                self.trap = Trap.ThirdStageThreeTrap
                self.MaxFrame = 4
                self.imageX = 147
                self.imageY = 108
                self.trapY = 300
                self.width = 108
                self.height = 180
        if stageNum == 4:
            if self.type == 1:
                self.trap = Trap.FourthStageOneTrap
                self.MaxFrame = 11
                self.imageX = 62
                self.imageY = 159
                self.trapY = 220
                self.width = 62
                self.height = 200
            elif self.type == 2:
                self.trap = Trap.FourthStageTwoTrap
                self.MaxFrame = 4
                self.imageX = 147
                self.imageY = 108
                self.trapY = 300
                self.width = 108
                self.height = 180
            elif self.type == 3:
                self.trap = Trap.FourthStageThreeTrap
                self.MaxFrame = 4
                self.imageX = 147
                self.imageY = 108
                self.trapY = 300
                self.width = 108
                self.height = 180


    def hit(self):
        for i in range(30):
            if stageNum == 1:
                if (lava.lavaX+lava.width/3) >= (TrapList[i].trapX - TrapList[i].width/4) and (lava.lavaX-lava.width/3) <= (TrapList[i].trapX + TrapList[i].width/4):
                    if TrapList[i].type == 1 and (lava.lavaY - lava.height/3) <= (TrapList[i].trapY + TrapList[i].height/3) and (lava.lavaY + lava.height/3) >= (TrapList[i].trapY - TrapList[i].height/3):
                        return True
                    if TrapList[i].type == 2 and (lava.lavaY - lava.height/3) <= (TrapList[i].trapY + TrapList[i].height/3) and (lava.lavaY + lava.height/3) >= (TrapList[i].trapY - TrapList[i].height/3):
                        return True
                    if TrapList[i].type == 3 and (lava.lavaY - lava.height/2) <= (TrapList[i].trapY + TrapList[i].height/2) and (lava.lavaY + lava.height/2) >= (TrapList[i].trapY - TrapList[i].height/2):
                        return True
            if stageNum == 2:
                if (600-lava.lavaX+(lava.height/3)) >= (TrapList[i].trapX-(TrapList[i].width/2)) and (600-lava.lavaX-(lava.height/3)) <= (TrapList[i].trapX+(TrapList[i].width/3)):
                    if (1200-lava.lavaY+(lava.width/2)) >= (1200-TrapList[i].trapY-(TrapList[i].height/2)) and (1200-lava.lavaY-(lava.width/2)) <= (1200-TrapList[i].trapY+(TrapList[i].height/2)):
                        return True

            if stageNum == 3:
                if (1200-lava.lavaX+(lava.width/3)) >= (TrapList[i].trapX-(TrapList[i].width/2)) and (1200-lava.lavaX-(lava.width/3)) <= (TrapList[i].trapX+(TrapList[i].width/2)):
                    if (800-lava.lavaY-(lava.height/2)) <= (800-TrapList[i].trapY+(TrapList[i].height/2)) and (800-lava.lavaY+(lava.height/2)) >= (800-TrapList[i].trapY-(TrapList[i].height/2)):
                        return True

            if stageNum == 4:
                if TrapList[i].type == 1 and (lava.lavaY - lava.height/3) <= (TrapList[i].trapY + TrapList[i].height/3) and (lava.lavaY + lava.height/3) >= (TrapList[i].trapY - TrapList[i].height/3):
                    return True
                if TrapList[i].type == 2 and (lava.lavaY - lava.height/2) <= (TrapList[i].trapY + TrapList[i].height/2) and (lava.lavaY + lava.height/2) >= (TrapList[i].trapY - TrapList[i].height/2):
                    return True
                if TrapList[i].type == 3 and (lava.lavaY - lava.height/2) <= (TrapList[i].trapY + TrapList[i].height/2) and (lava.lavaY + lava.height/2) >= (TrapList[i].trapY - TrapList[i].height/2):
                    return True


        return False

    def update(self):
        self.frame = (self.frame+1) % self.MaxFrame
        self.moving()

    def moving(self):
        if stageNum == 1:
            self.trapX = (self.trapX-lava.speed)
        if stageNum == 2:
            self.trapX = (self.trapX-lava.speed)
        if stageNum == 3:
            self.trapX = (self.trapX+lava.speed)
        if stageNum == 4:
            self.trapX = (self.trapX+lava.speed)


        if self.hit() == True and lava.isExistBuff('good') == False:
            lava.SetCharacterState(lava.BUMP)
            life.onelife -= 1
            lava.createBuff('good',0.8)

    def draw(self):
        if stageNum == 1:
            self.trap.clip_rotate_draw(rotation, self.frame * self.imageX, 0, self.imageX, self.imageY, self.trapX, self.trapY, self.width, self.height)

        if stageNum == 2:
            self.trap.clip_rotate_draw(rotation, self.frame * self.imageX, 0, self.imageX, self.imageY, 1200-self.trapY, self.trapX, self.width, self.height)

        if stageNum == 3:
            self.trap.clip_rotate_draw(rotation, self.frame * self.imageX, 0, self.imageX, self.imageY, self.trapX, 800-self.trapY, self.width, self.height)

        if stageNum == 4:
            self.trap.clip_rotate_draw(rotation, self.frame * self.imageX, 0, self.imageX, self.imageY, self.trapY, self.trapX+200, self.width, self.height)


#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class Character:
    global rotation
    hit_sound = None
    RUN, SLIDING, JUMP, BUMP = 0, 1, 2, 3

    def __init__(self):
        self.speed = 20
        self.lavaY = 175
        self.lavaYJumpRun = 175
        self.lavaYSilde = 165
        self.lavaX = 400
        self.frame = 0
        self.character = load_image('YlarvaRun.png')
        self.runningCharacter = None
        self.slidingCharacter = None
        self.jumpingCharacter = None
        self.bumpingCharacter = None
        self.gravitySpeed = 0
        self.state = self.RUN
        self.MaxFrame = 5
        self.width = 90
        self.height = 90
        self.heightJumpRun = 90
        self.heightSlide = 70
        self.lastAnimateTime = get_time()
        self.buffList = []
        self.jumpNum = 0



    def gravity(self):
        if (self.lavaY-(self.height/2)-self.gravitySpeed) > 130:
            self.gravitySpeed += 5
            self.lavaY -=self.gravitySpeed
        else:

            self.lavaY = 130 + (self.height/2)
            self.gravitySpeed = 0

    def createBuff(self,name,remainTime):
        self.buffList.append( buff(name, remainTime) )
    def isExistBuff(self,name):
        for buff in self.buffList:
            if( buff.name == name ):
                return True
        return False
    def deleteTimeoverBuff(self):
        for buff in self.buffList:
            if( buff.remainTime <= 0 ):
                self.removeBuff(buff)
    def removeBuff(self,buff):
        self.buffList.remove(buff)

    def LoadCharacterImage(self):
        self.runningCharacter = load_image('YlarvaRun.png')
        self.slidingCharacter = load_image('YlarvaSlide.png')
        self.jumpingCharacter = load_image('YlarvaJump.png')
        self.bumpingCharacter = load_image('YlarvaBump.png')
        print('loadchar')

    def SetCharacterImage(self):
        self.frame = 0
        self.lastAnimateTime = get_time()
        if self.state == self.RUN:
            self.character = self.runningCharacter
            self.MaxFrame = 5
        elif self.state == self.SLIDING:
            self.character = self.slidingCharacter
            self.MaxFrame = 6
        elif self.state == self.JUMP:
            self.character = self.jumpingCharacter
            self.MaxFrame = 7
        elif self.state == self.BUMP:
            self.character = self.bumpingCharacter
            self.MaxFrame = 5

    def SetCharacterState(self, state):
        if state != self.state:
            if state == self.BUMP:
                self.state = self.BUMP
            elif state == self.RUN:
                self.state = self.RUN
            elif state == self.SLIDING:
                self.state = self.SLIDING
            elif state == self.JUMP:
                self.state = self.JUMP
            self.SetCharacterImage()

    def animate(self):
        if get_time() - self.lastAnimateTime > 0.05:
            self.lastAnimateTime = get_time()
            self.frame = (self.frame + 1)
            if (self.state == self.BUMP) and (self.frame >= self.MaxFrame):
                self.SetCharacterState(self.RUN)
            if (self.state != self.BUMP):
                self.frame = self.frame % self.MaxFrame
    def jumpCount(self):
        self.jumpNum += 1
        if (self.lavaY-(self.height/2)) == 130:
            self.jumpNum = 0
    def jumpToRun(self):
        if (self.state == self.JUMP) and (self.lavaY-(self.height/2)) == 130:
            lava.SetCharacterState(lava.RUN)

    def update(self):
        self.animate()
        self.gravity()
        self.jumpToRun()
        #buff
        for buff in self.buffList:
            buff.update()
        self.deleteTimeoverBuff()

    def draw(self):
        if stageNum == 1:
            self.character.clip_rotate_draw(rotation, self.frame * 90, 0, self.width, self.height, self.lavaX, self.lavaY, self.width, self.height)

        if stageNum == 2:
            self.character.clip_rotate_draw(rotation, self.frame * 90, 0, self.width, self.height, 1200-self.lavaY, 600-self.lavaX, self.width, self.height)

        if stageNum == 3:
            self.character.clip_rotate_draw(rotation, self.frame * 90, 0, self.width, self.height, 1200-self.lavaX, 800-self.lavaY, self.width, self.height)

        if stageNum == 4:
            self.character.clip_rotate_draw(rotation, self.frame * 90, 0, self.width, self.height, self.lavaY, self.lavaX+200, self.width, self.height)



class buff():
    def __init__(self, name, remainTime):
        self.name = name
        self.remainTime = remainTime
        self.lastTime = get_time()
    def update(self):
        if( get_time() - self.lastTime > 0.1 ):
            self.lastTime = get_time()
            self.remainTime -= 0.1


class Music:
    def __init__(self):
        self.bgm = load_music('MAIN.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

    def __del__(self):
        del self.bgm


class Life():
    def __init__(self, maxlife, onelife):
        self.maxlife = maxlife
        self.onelife = onelife
        self.maxLifeBar = None
        self.oneLifeBar = None
        self.barValue = (self.onelife/self.maxlife)*(500/10)
    def LoadLifeImage(self):
        self.maxLifeBar = load_image('maxLifeBar.png')
        self.oneLifeBar = load_image('oneLifeBar.png')
    def SetLifeBar(self):
        self.barValue = (self.onelife/self.maxlife)*(500/10)
    def update(self):
        self.onelife -= 0.1
    def draw(self):
        self.maxLifeBar.draw(300, 720, 506, 56)
        for i in range(int(self.barValue)):
            self.oneLifeBar.draw(55+i*10, 720, 10, 50)





def enter():
    global lava, stage, trapManager, stageNum, frame, life, TrapList, mainMusic, itemManager
    mainMusic = Music()
    stage = Map()
    stage.LoadStageImage()
    stage.SetStageImage()
    life = Life(100, 100)
    life.LoadLifeImage()
    lava = Character()
    lava.LoadCharacterImage()
    trapManager = TrapManager()
    trapManager.SetStageTrap()
    itemManager = ItemManager()
    itemManager.SetStageItem()
    show_cursor()
    frame = 0
    stageNum = 1

def exit():
    global lava, stage, trapManager, life, trap, mainMusic, itemManager, item
    del(mainMusic)
    del(stage)
    del(lava)
    del(trapManager)
    del(itemManager)
    del(life)
    for trap in TrapList:
        del(trap)
    for item in ItemList:
        del(item)



def pause():
    pass
    global mainMusic
    mainMusic.bgm.pause()


def resume():
    global stage, stageNum, rotation, life
    global mainMusic
    mainMusic.bgm.resume()
    stageNum = 1
    stage.bkframe = 0
    stage.doubleX = 600
    stage.doubleY = 400
    stage.groundX = 600
    stage.groundY = 0
    stage.groundH = 0
    rotation = 0
    life.onelife = 100
    stage.SetStageImage()


def handle_events(frame_time):
    global lava
    global stageNum
    global rotation
    global stage
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
             RunRun_Framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_UP:
                lava.jumpCount()
                if 0 <= lava.jumpNum <= 1:
                    lava.gravitySpeed = -40
                lava.SetCharacterState(lava.JUMP)
            if event.key == SDLK_DOWN:
                if (lava.lavaY-(lava.height/2)) == 130:
                    lava.gravitySpeed = 0
                    lava.lavaY = lava.lavaYSilde
                    lava.height = lava.heightSlide
                    lava.SetCharacterState(lava.SLIDING)
            elif event.key == SDLK_ESCAPE:
                RunRun_Framework.quit()

            elif event.key == SDLK_b:
                rotation += 1.5707963267948966
                stageNum += 1
                if stageNum == 5:
                    stageNum = 1
                if stageNum == 1 or stageNum == 3:
                    stage.doubleX, stage.groundX = 600,600
                if stageNum == 2 or stageNum == 4:
                    stage.doubleX, stage.groundX = 400,400
                stage.SetStageImage()
                TrapList.clear()
                trapManager.SetStageTrap()
                ItemList.clear()
                itemManager.SetStageItem()

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_DOWN:
                if (lava.lavaY-(lava.height/2)) == 130:
                    lava.lavaY = lava.lavaYJumpRun
                    lava.height = lava.heightJumpRun
                    lava.SetCharacterState(lava.RUN)

def update(frame_time):
    global lava, stage, trap, life, item, rotation, stageNum
    stage.update()
    for trap in TrapList:
        trap.update()
    for item in ItemList:
        item.update()
    lava.update()
    if life.onelife <= 0:
        life.onelife = 100
    life.update()
    life.SetLifeBar()


    if life.onelife <= 0:
        life.onelife = 100
        RunRun_Framework.push_state(RunRunRank_state)
    life.update()
    life.SetLifeBar()
##
    delay(0.02)

def draw(frame_time):
    global lava, stage, trap, life, item
    clear_canvas()
    stage.draw()
    for trap in TrapList:
        trap.draw()
    for item in ItemList:
        item.draw()
    life.draw()
    lava.draw()
    update_canvas()
