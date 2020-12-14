import random
import sqlite3
import smtplib
import os

###globals###
global EquitmentList
global MonsterKills
MonsterKills = 0

###SQL setup###
connection = sqlite3.connect("Adventure_Game.db")
c = connection.cursor()
#c.execute("""CREATE TABLE Saved_Game_Character (Name text, Strength integer, Health integer, Agility integer, Dexterity integer, Luck integer, Level integer)""")
#c.execute("""CREATE TABLE Saved_Game_Equitment (Name text, Head text, Weapon text, Chest text, Feet text, Legs text, Hands text)""")

###Monsters###
class Monster(object):
    Instances = []
    def __init__(self, Level, Name, Strength, Health, Agility, Dexterity, Luck):
        self.Level = Level
        self.Name = Name
        self.Strength = Strength
        self.Health = Health
        self.Agility = Agility
        self.Dexterity = Dexterity
        self.Luck = Luck
        self.__class__.Instances.append(self.Name)
    def Level(self):
        return self.Level
    def Name(self):
        return self.Name
    def Strength(self):
        return self.Strength
    def Health(self):
        return self.Health
    def Agility(self):
        return self.Agility
    def Dexterity(self):
        return self.Dexterity
    def Luck(self):
        return self.Luck

    def Death(self):
        Sayings = ["You got me bastard","Ill get you next time!","You fought well","You have bested me","Arghhh"]
        X = random.randint(0,4)
        print(Sayings[X])
        print("")
        Item_Drop(Monster.Level(self))

###Starter Monster###
Target_Dummy = Monster(1,"Target Dummy", 1, 10, 0, 0, 0)

###Level 1 Monsters###
Goblin = Monster(1,"Goblin", 10, 20, 10, 2, 5)
Oger = Monster(1,"Oger", 5, 100, 2, 2, 10)
Knight = Monster(1,"Knight", 15, 50, 0, 0, 0)
Spider = Monster(1,"Spider", 10, 30, 10, 2, 2)
Thug = Monster(1,"Thug", 10, 25, 5, 5, 2)

###Level 2 Monsters###
Wizard = Monster(2,"Wizard", 10, 40, 20, 4, 10)
Barbarian = Monster(2,"Barbarian", 15, 200, 4, 4, 20)
Dwarf = Monster(2,"Dwarf", 10, 100, 4, 10, 4)
Wolf = Monster(2,"Wolf", 15, 60, 20, 4, 4)
Skeleton = Monster(2,"Skeleton", 20, 50, 10, 10, 4)

###Level 3 Monsters###
Zombie = Monster(3,"Zombie", 40, 80, 40, 8, 20)
Guard = Monster(3,"Guard", 20, 400, 8, 8, 40)
Giant = Monster(3,"Giant", 60, 200, 8, 20, 8)
Basilisk = Monster(3,"Basilisk", 40, 120, 40, 8, 8)
Icefiend = Monster(3,"Icefiend", 40, 100, 20, 20, 8)

###Bosses###
Grand_Wizard = Monster(2,"Grand_Wizard", 10, 100, 10, 5, 5)
Grand_Knight = Monster(3,"Grand_Knight", 15, 200, 20, 10, 10)
Tom = Monster(3,"Tom", 60, 400, 40, 20, 20)

###Archive###
MonsterList={"Goblin":Goblin, "Oger":Oger, "Knight":Knight, "Spider":Spider, "Thug":Thug, "Wizard":Wizard, "Barbarian":Barbarian,
             "Dwarf":Dwarf,"Wolf":Wolf,"Skeleton":Skeleton,"Zombie":Zombie,"Guard":Guard,"Icefiend":Icefiend,"Basilisk":Basilisk,"Giant":Giant}

###Equitment###
class Equitment(object):
    Instances = []
    def __init__(self, Level, Name, Strength, Health, Agility, Dexterity, Luck, Armour, Type):
        self.Level = Level
        self.Name = Name
        self.Strength = Strength
        self.Health = Health
        self.Agility = Agility
        self.Dexterity = Dexterity
        self.Luck = Luck
        self.Armour = Armour
        self.Type = Type
        self.__class__.Instances.append(self.Name)
    def Level(self):
        return self.Level
    def Name(self):
        return self.Name
    def Strength(self):
        return self.Strength
    def Health(self):
        return self.Health
    def Agility(self):
        return self.Agility
    def Dexterity(self):
        return self.Dexterity
    def Luck(self):
        return self.Luck
    def Armour(self):
        return self.Armour
    def Type(self):
        return self.Type    
    
###Level 0 Equitment###
Wooden_Helm = Equitment(0, "Wooden_Helm", 0, 2, 0, 0, 0, 1, 0)
Wooden_Sword = Equitment(0, "Wooden_Sword", 5, 0, 0, 0, 0, 0, 1)
Wooden_Boots = Equitment(0, "Wooden_Boots", 0, 1, 1, 0, 0, 1, 2)
Wooden_Chestplate = Equitment(0, "Wooden_Chestplate", 0, 1, 0, 0, 0, 2, 3)
Wooden_Leggings = Equitment(0, "Wooden_Leggings", 0, 1, 0, 1, 0, 1, 4)
Wooden_Gauntlets = Equitment(0, "Wooden_Gauntlets", 0, 1, 0, 0, 1, 1, 5)

###Level 1 Equitment###
Warriors_Helm = Equitment(1, "Warriors_Helm", 0, 4, 0, 0, 0, 2, 0)
Warriors_Sword = Equitment(1, "Warriors_Sword", 10, 0, 0, 0, 0, 0, 1)
Warriors_Boots = Equitment(1, "Warriors_Boots", 0, 2, 2, 0, 0, 2, 2)
Warriors_Chestplate = Equitment(1, "Warriors_Chestplate", 0, 2, 0, 0, 0, 4, 3)
Warriors_Leggings = Equitment(1, "Warriors_Leggings", 0, 2, 0, 2, 0, 2, 4)
Warriors_Gauntlets = Equitment(1, "Warriors_Gauntlets", 0, 2, 0, 0, 2, 2, 5)

###Level 2 Equitment###
Knights_Helm = Equitment(2, "Knights_Helm", 0, 6, 0, 0, 0, 3, 0)
Knights_Sword = Equitment(2, "Knights_Sword", 15, 0, 0, 0, 0, 0, 1)
Knights_Boots = Equitment(2, "Knights_Boots", 0, 3, 3, 0, 0, 3, 2)
Knights_Chestplate = Equitment(2, "Knights_Chestplate", 0, 3, 0, 0, 0, 6, 3)
Knights_Leggings = Equitment(2, "Knights_Leggings", 0, 3, 0, 3, 0, 3, 4)
Knights_Gauntlets = Equitment(2, "Knights_Gauntlets", 0, 3, 0, 0, 3, 3, 5)

###Level 3 Equitment###
Heros_Helm = Equitment(3, "Heros_Helm", 0, 8, 0, 0, 0, 4, 0)
Heros_Sword = Equitment(3, "Heros_Sword", 20, 0, 0, 0, 0, 0, 1)
Heros_Boots = Equitment(3, "Heros_Boots", 0, 3, 4, 0, 0, 4, 2)
Heros_Chestplate = Equitment(3, "Heros_Chestplate", 0, 3, 0, 0, 0, 8, 3)
Heros_Leggings = Equitment(3, "Heros_Leggings", 0, 3, 0, 4, 0, 4, 4)
Heros_Gauntlets = Equitment(3, "Heros_Gauntlets", 0, 3, 0, 0, 4, 4, 5)

###Level 4 Equitment###
Legenday_Helm = Equitment(4, "Legenday_Helm", 0, 10, 0, 0, 0, 5, 0)
Legenday_Sword = Equitment(4, "Legenday_Sword", 25, 0, 0, 0, 0, 0, 1)
Legenday_Boots = Equitment(4, "Legenday_Boots", 0, 4, 5, 0, 0, 5, 2)
Legenday_Chestplate = Equitment(4, "Legenday_Chestplate", 0, 4, 0, 0, 0, 10, 3)
Legenday_Leggings = Equitment(4, "Legenday_Leggings", 0, 4, 0, 5, 0, 5, 4)
Legenday_Gauntlets = Equitment(4, "Legenday_Gauntlets", 0, 4, 0, 0, 5, 5, 5)

###Special Equitment###
Toms_Helm = Equitment(5, "Toms_Helm", 0, 20, 0, 0, 0, 10, 0)
Toms_Sword = Equitment(5, "Toms_Sword", 25, 0, 0, 0, 0, 0, 1)
Toms_Boots = Equitment(5, "Toms_Boots", 0, 8, 10, 0, 0, 10, 4)
Toms_Chestplate = Equitment(5, "Toms_Chestplate", 0, 8, 0, 0, 0, 20, 3)
Toms_Leggings = Equitment(5, "Toms_Leggings", 0, 8, 0, 10, 0, 10, 4)
Toms_Gauntlets = Equitment(5, "Toms_Gauntlets", 0, 8, 0, 0, 10, 10, 5)

###Arcive###
EquitmentList={"Wooden_Helm":Wooden_Helm, "Wooden_Sword":Wooden_Sword, "Wooden_Boots":Wooden_Boots, "Wooden_Chestplate":Wooden_Chestplate, "Wooden_Leggings":Wooden_Leggings, "Wooden_Gauntlets":Wooden_Gauntlets,
               "Warriors_Helm":Warriors_Helm, "Warriors_Sword":Warriors_Sword, "Warriors_Boots":Warriors_Boots, "Warriors_Chestplate":Warriors_Chestplate, "Warriors_Leggings":Warriors_Leggings, "Warriors_Gauntlets":Warriors_Gauntlets,
               "Knights_Helm":Knights_Helm, "Knights_Sword":Knights_Sword, "Knights_Boots":Knights_Boots, "Knights_Chestplate":Knights_Chestplate, "Knights_Leggings":Knights_Leggings, "Knights_Gauntlets":Knights_Gauntlets,
               "Heros_Helm":Heros_Helm, "Heros_Sword":Heros_Sword, "Legenday_Boots":Legenday_Boots, "Legenday_Chestplate":Legenday_Chestplate, "Legenday_Leggings":Legenday_Leggings, "Legenday_Gauntlets":Legenday_Gauntlets,
               "Legenday_Helm":Legenday_Helm, "Legenday_Sword":Legenday_Sword, "Heros_Boots":Heros_Boots, "Heros_Chestplate":Heros_Chestplate, "Heros_Leggings":Heros_Leggings, "Heros_Gauntlets":Heros_Gauntlets,
               "Toms_Helm":Toms_Helm, "Toms_Sword":Toms_Sword, "Toms_Boots":Toms_Boots, "Toms_Chestplate":Toms_Chestplate, "Toms_Leggings":Toms_Leggings, "Toms_Gauntlets":Toms_Gauntlets
               }

###Hero###
class Character:
    def __init__(self):
        self.Level = 0
        self.Name = ""
        self.Strength = 5
        self.Health = 10
        self.Agility = 0
        self.Dexterity = 0
        self.Luck = 0
        self.Head = Wooden_Helm
        self.Weapon = Wooden_Sword
        self.Feet = Wooden_Boots
        self.Chest = Wooden_Chestplate
        self.Legs = Wooden_Leggings
        self.Hands = Wooden_Gauntlets
    def Strength(self):
        HeroStrength = Hero.Strength + Equitment.Strength(Hero.Head) + Equitment.Strength(Hero.Weapon) + Equitment.Strength(Hero.Chest) + Equitment.Strength(Hero.Feet) + Equitment.Strength(Hero.Legs) + Equitment.Strength(Hero.Hands)
        return HeroStrength
    def Health(self):
        HeroHealth = Hero.Health + Equitment.Health(Hero.Head) + Equitment.Health(Hero.Weapon) + Equitment.Health(Hero.Chest) + Equitment.Health(Hero.Feet) + Equitment.Health(Hero.Legs) + Equitment.Health(Hero.Hands)
        return HeroHealth
    def Agility(self):
        HeroAgility = Hero.Agility + Equitment.Agility(Hero.Head) + Equitment.Agility(Hero.Weapon) + Equitment.Agility(Hero.Chest) + Equitment.Agility(Hero.Feet) + Equitment.Agility(Hero.Legs) + Equitment.Agility(Hero.Hands)
        return HeroAgility
    def Dexterity(self):
        HeroDexterity = Hero.Dexterity + Equitment.Dexterity(Hero.Head) + Equitment.Dexterity(Hero.Weapon) + Equitment.Dexterity(Hero.Chest) + Equitment.Dexterity(Hero.Feet) + Equitment.Dexterity(Hero.Legs) + Equitment.Dexterity(Hero.Hands)
        return HeroDexterity
    def Luck(self):
        HeroLuck = Hero.Luck + Equitment.Luck(Hero.Head) + Equitment.Luck(Hero.Weapon) + Equitment.Luck(Hero.Chest) + Equitment.Luck(Hero.Feet) + Equitment.Luck(Hero.Legs) + Equitment.Luck(Hero.Hands)
        return HeroLuck
    def Armour(self):
        HeroArmour = Equitment.Armour(Hero.Head) + Equitment.Armour(Hero.Weapon) + Equitment.Armour(Hero.Chest) + Equitment.Armour(Hero.Feet) + Equitment.Armour(Hero.Legs) + Equitment.Armour(Hero.Hands)
        return HeroArmour
    def Death(self):
        print("")
        print("You have died returning to main menu")
        print("")
        Menu()
    def Upgrade(self, Item, Type):
        if Type == 0:
            Hero.Head = Item
        if Type == 1:
            Hero.Weapon = Item
        if Type == 2:
            Hero.Feet = Item
        if Type == 3:
            Hero.Chest = Item
        if Type == 4:
            Hero.Legs = Item
        if Type == 5:
            Hero.Hands = Item
        
      
Hero = Character()

def Instructions():
    Choice = 69
    while Choice !="5":
        print("Would you like to:")
        print("Learn about the basic stats of the game (0)")
        print("Learn about all the monsters and bosses in the game (1)")
        print("Learn how the game works (2)")
        print("Learn about all items in the game (3)")
        print("Learn about the 3 differnt attack styles (4)")
        print("Exit to main menu (5)")
        Choice = input("")
        if Choice == "0":    
            print("Their are 6 main stats:")
            print("Strength - determins how much potential extra damage you do to monsters on each hit")
            print("Health - how much damage you can sustain before death")
            print("Agility - increases your chance to dodge attacks, determins weather you or the monster strike first and increases chances of escape when retreating")
            print("Dexterity - increased chance of parrying attacks")
            print("Luck - increased chance of finding better gear and increased chances of critial strikes (max 50%)")
            print("Armour - Reduces the amount of damage you take (Gained from items only)")
        if Choice == "1":
            for x in MonsterList:
                x = MonsterList[x]
                print(Monster.Name(x))
                print("Level ",Monster.Level(x))
                print("Strength ",Monster.Strength(x))
                print("Health ",Monster.Health(x))
                print("Agility ",Monster.Agility(x))
                print("Dexterity ",Monster.Dexterity(x))
                print("Luck ",Monster.Luck(x))
                print("")
        if Choice == "2":
            print("The game consists of 3 levels filled with monsters, choices and loot to gain before eventually rescuing the princess")
            print("To advance to the next level a specified amount of monsters must be defeated but careful through advancing to the next level will increase the difficulty of monsters")
            print("When advaning you must first defeate the boss, careful you cant retreate from this battle and each boss has a special ability")
            print("When you advance to the next level you gain 10 extra attribute points and are able to redistribute your stats")
            print("The game will save automaticaly after each level completed")
        if Choice == "3":
            for x in EquitmentList:
                x = EquitmentList[x]
                print(Equitment.Name(x))
                print("Level ",Equitment.Level(x))
                print("Strength ",Equitment.Strength(x))
                print("Health ",Equitment.Health(x))
                print("Agility ",Equitment.Agility(x))
                print("Dexterity ",Equitment.Dexterity(x))
                print("Luck ",Equitment.Luck(x))
                print("Armour ",Equitment.Armour(x))
                print("")
        if Choice == "4":
            print("Normal - A normal attack")
            print("Heavy - Increased chance to crit but reduced chance to hit")
            print("Quick - Increased chance to hit reduction in damage")
                   
def Save_Game_initial():
    c.execute("""INSERT INTO Saved_Game_Character VALUES(?, ?, ?, ?, ?, ?, ?)""",(Hero.Name, Hero.Strength, Hero.Health, Hero.Agility, Hero.Dexterity, Hero.Luck, Hero.Level))
    c.execute("""INSERT INTO Saved_Game_Equitment VALUES(?, ?, ?, ?, ?, ?, ?)""",(Hero.Name, Equitment.Name(Hero.Head), Equitment.Name(Hero.Weapon), Equitment.Name(Hero.Chest), Equitment.Name(Hero.Feet), Equitment.Name(Hero.Legs), Equitment.Name(Hero.Hands)))
    connection.commit()

def Save_Game():
    c.execute("""UPDATE Saved_Game_Character SET Strength = ?, Health = ?, Agility = ?, Dexterity = ?, Luck = ?, Level = ? Where Name = ?""",(Hero.Strength, Hero.Health, Hero.Agility, Hero.Dexterity, Hero.Luck, Hero.Level, Hero.Name))
    c.execute("""UPDATE Saved_Game_Equitment SET Head = ?, Weapon = ?, Chest = ?, Feet = ?, Legs = ?, Hands = ? WHERE Name = ?""",(Equitment.Name(Hero.Head), Equitment.Name(Hero.Weapon), Equitment.Name(Hero.Chest), Equitment.Name(Hero.Feet), Equitment.Name(Hero.Legs), Equitment.Name(Hero.Hands), Hero.Name))
    connection.commit()

def Load_Game():
    Done = False
    while Done == False:
        print("Please input your Heros name")
        Name = input("")
        try:
            c.execute("""SELECT * FROM Saved_Game_Character WHERE Name=?""",(Name, ))
            Row = c.fetchall()
            Done = True
        except:
            print("Character not found")
    Hero.Strength = int(Row[0][1])
    Hero.Health = int(Row[0][2])
    Hero.Agility = int(Row[0][3])
    Hero.Dexterity = int(Row[0][4])
    Hero.Luck = int(Row[0][5])    
    Hero.Level = int(Row[0][6])
    print(Hero.Level)
    c.execute("""SELECT * FROM Saved_Game_Equitment WHERE Name=?""",(Name, ))
    Row = c.fetchall()
    Hero.Head = EquitmentList[Row[0][1]]
    Hero.Weapon = EquitmentList[Row[0][2]]
    Hero.Chest = EquitmentList[Row[0][3]]
    Hero.Feet = EquitmentList[Row[0][4]]
    Hero.Legs = EquitmentList[Row[0][5]]
    Hero.Hands = EquitmentList[Row[0][6]]
    Start_Game()

def CreateHero():
    Hero.Name = input("What is my brave adventurers name? ")
    Stats = {"Strength":5, "Health":10, "Agility":1, "Dexterity":1, "Luck":1}
    Equivlent = {0:"Strength", 1:"Health", 2:"Agility", 3:"Dexterity", 4:"Luck"}
    Pool = 30
    First = [0,1]
    Second = [0,1,2,3,4]
    while Pool >=1:
        print("You have ",Pool," points left to spend")
        print("Your Current stats are:")
        print(Stats["Strength"] ,"Strength")
        print(Stats["Health"] ,"Health")
        print(Stats["Agility"] ,"Agility")
        print(Stats["Dexterity"] ,"Dexterity")
        print(Stats["Luck"] ,"Luck")
        print("")
        Choice1 = int(input("Which stat would you like to increase: Strength(0) Health (1) Widsom(2) Dexterity(3) Luck(4): "))
        print("Your stats for selected skill are are:")
        Choice1=Equivlent[Choice1]
        print(Stats[Choice1])
        Change = int(input("How many points would you like to increase it by: "))
        Valid = True
        if Change > Pool:
            Vaild = False
        if Change < 0:
            Valid = False
        if Valid == False:
            print("Invalid input please try again")
        if Valid == True:
            Stats[Choice1] = Stats[Choice1]+Change
            Pool = Pool - Change
    Hero.Strength = Stats["Strength"]
    Hero.Health = Stats["Health"]
    Hero.Agility = Stats["Agility"]
    Hero.Dexterity = Stats["Dexterity"]
    Hero.Luck = Stats["Luck"]
    Hero.Level = 1
    Save_Game_initial()
    print("Your hero has been saved in the database")
    Start_Game()

def Level_Hero():
    Stats = {"Strength":Hero.Strength, "Health":Hero.Health, "Agility":Hero.Agility, "Dexterity":Hero.Dexterity, "Luck":Hero.Luck}
    Equivlent = {0:"Strength", 1:"Health", 2:"Agility", 3:"Dexterity", 4:"Luck"}
    Pool = 10
    First = [0,1]
    Second = [0,1,2,3,4]
    while Pool >=1:
        print("You have ",Pool," points left to spend")
        print("Your Current stats are:")
        print(Stats["Strength"] ,"Strength")
        print(Stats["Health"] ,"Health")
        print(Stats["Agility"] ,"Agility")
        print(Stats["Dexterity"] ,"Dexterity")
        print(Stats["Luck"] ,"Luck")
        print("")
        Choice1 = int(input("Which stat would you like to increase: Strength(0) Health (1) Widsom(2) Dexterity(3) Luck(4): "))
        print("Your stats for selected skill are are:")
        Choice1=Equivlent[Choice1]
        print(Stats[Choice1])
        Change = int(input("How many points would you like to increase it by: "))
        Valid = True
        if Change > Pool:
            Vaild = False
        if Change < 0:
            Valid = False
        if Valid == False:
            print("Invalid input please try again")
        if Valid == True:
            Stats[Choice1] = Stats[Choice1]+Change
            Pool = Pool - Change
    Hero.Strength = Stats["Strength"]
    Hero.Health = Stats["Health"]
    Hero.Agility = Stats["Agility"]
    Hero.Dexterity = Stats["Dexterity"]
    Hero.Luck = Stats["Luck"]
    Hero.Level = Hero.Level + 1
    Save_Game()

def Fight(Target, Runaway):
    global MonsterKills
    print("")
    print("Your opponent is ", Monster.Name(Target))
    print("Their stats are:")
    print(Monster.Strength(Target) ,"Strength")
    print(Monster.Health(Target) ,"Health")
    print(Monster.Agility(Target) ,"Agility")
    print(Monster.Dexterity(Target) ,"Dexterity")
    print(Monster.Luck(Target) ,"Luck")
    print("")
    print("Your stats are:")
    print(Character.Strength(Hero) ,"Strength")
    print(Character.Health(Hero) ,"Health")
    print(Character.Agility(Hero) ,"Agility")
    print(Character.Dexterity(Hero) ,"Dexterity")
    print(Character.Luck(Hero) ,"Luck")
    print(Character.Armour(Hero) ,"Armour")
    print("")
    if Runaway == True:
        print("Would you like to Attack (0) Attempt to runaway (1): ")
        Choice = input("")
    else:
        Choice = "0"
    if Choice == "1":
        Escape = random.randint(0,100) - Monster.Agility(Target) + Character.Agility(Hero)
        if Escape >= 50:
            print("You manage to escape!")
        else:
            print("You where unable to esacpe!")
            print("")
            Choice = "0"
    if Choice == "0":
        MonsterHealth = Monster.Health(Target)
        MonsterStrength = Monster.Strength(Target)
        MonsterAgility = Monster.Agility(Target)
        MonsterDexterity = Monster.Dexterity(Target)
        MonsterLuck = Monster.Luck(Target)
        HeroHealth = Character.Health(Hero)
        HeroStrength = Character.Strength(Hero)
        HeroAgility = Character.Agility(Hero)
        HeroDexterity = Character.Dexterity(Hero)
        HeroLuck = Character.Luck(Hero)
        HeroArmour = Character.Armour(Hero)
        while HeroHealth > 0 and MonsterHealth > 0:
            Heavy = 0
            Quick = 0
            Choice = False
            while Choice == False:
                print("Would you like to preform a Heavy attack (0), Quick attack (1) Normal(2)")
                Choice1 = input("")
                if Choice1 == "2":
                    Choice = True
                if Choice1 == "1":
                    Quick = 20
                    Choice = True
                if Choice == "0":
                    Heavy = 20
                    Choice = True
            if MonsterAgility <= HeroAgility:
                Valid = True
                Attack = random.randint(0, HeroStrength)
                Critical = random.randint(0,100)
                if Critical < (1+HeroLuck+Heavy):
                    print("Critical Strike!")
                    Attack = Attack * 1.5
                Dodge = random.randint(0,100)
                if (Dodge - Quick + Heavy) < (1+MonsterAgility):
                    print("Monster dodged attack")
                    Valid = False
                Parry = random.randint(0,100)
                if Valid == True:
                    if Parry- Quick +Heavy < (1+MonsterDexterity):
                        print("Monster parried attack")
                        Valid = False
                if Valid == True:
                    print("You inflicted ", Attack," damage")
                    MonsterHealth = MonsterHealth - Attack
                    if MonsterHealth <= 0:
                        Monster.Death(Target)
                        MonsterKills = MonsterKills + 1
                        Valid = False
                    else:
                        print("Monster health remaning: ",MonsterHealth)
                        Valid = True
                Attack = random.randint(0, MonsterStrength) - (random.randint(0,HeroArmour)//2)
                if Attack < 0:
                    Attack = 0
                Critical = random.randint(0,100)
                if Critical < (1+MonsterLuck):
                    print("Critical Strike!")
                    Attack = Attack * 1.5
                Dodge = random.randint(0,100)
                if Dodge < (1+HeroAgility):
                    print("You dodged attack")
                    Valid = False
                Parry = random.randint(0,100)
                if Valid == True:
                    if Parry < (1+HeroDexterity):
                        print("You parried attack")
                        Valid = False
                if Valid == True:
                    print("You recived ", Attack," damage")
                    HeroHealth = HeroHealth - Attack
                    if HeroHealth <= 0:
                        Character.Death(Hero)
                    else:
                        print("Your remaning health: ",HeroHealth)
                        
            if MonsterAgility > HeroAgility:
                Valid = True
                Attack = random.randint(0, MonsterStrength) - (random.randint(0,HeroArmour)//2)
                if Attack < 0:
                    Attack = 0
                Critical = random.randint(0,100)
                if Critical < (1+MonsterLuck):
                    print("Critical Strike!")
                    Attack = Attack * 1.5
                Dodge = random.randint(0,100)
                if Dodge < (1+HeroAgility):
                    print("You dodged attack")
                    Valid = False
                Parry = random.randint(0,100)
                if Valid == True:
                    if Parry < (1+HeroDexterity):
                        print("You parried attack")
                        Valid = False
                if Valid == True:
                    print("You recived ", Attack," damage")
                    HeroHealth = HeroHealth - Attack
                    if HeroHealth <= 0:
                        Character.Death(Hero)
                    else:
                        print("Your remaning health: ",HeroHealth)  
                Valid = True
                Attack = random.randint(0, HeroStrength)
                Critical = random.randint(0,100)
                if Critical < (1+HeroLuck+Heavy):
                    print("Critical Strike!")
                    Attack = Attack * 1.5
                Dodge = random.randint(0,100)
                if Dodge- Quick +Heavy < (1+MonsterAgility):
                    print("Monster dodged attack")
                    Valid = False
                Parry = random.randint(0,100)
                if Valid == True:
                    if Parry - Quick +Heavy< (1+MonsterDexterity):
                        print("Monster parried attack")
                        Valid = False
                if Valid == True:
                    print("You inflicted ", Attack," damage")
                    MonsterHealth = MonsterHealth - Attack
                    if MonsterHealth <= 0:
                        Monster.Death(Target)
                        MonsterKills = MonsterKills + 1
                    else:
                        print("Monster health remaning: ",MonsterHealth)
                

def Start_Game():
    global MonsterKills
    print("Welcome Adventurer")
    print("You must save the princess!")
    print("But First lets show you combat: ")
    print("")
    print("Their are 3 types of combat:")
    print("Normal - A normal attack")
    print("Heavy - Increased chance to crit but reduced chance to hit")
    print("Quick - Increased chance to hit but reduction in damage")
    Fight(Target_Dummy, False)
    print("Wow congratulations you fought well and look youve gained a new item!")
    print("Now I think your for a real battle!")
    Fight(Goblin, False)
    print("Wow thought he had you for a second then!")
    if Hero.Level == 1:
        MonsterKills = 0
        print("")
        print("You must defeat 10 monsters to move on")
        Level1()
        Boss1()
        Level_Hero()
    if Hero.Level == 2:
        print("You must defeat 20 monsters to move on")
        MonsterKills = 0
        Level2()
        Boss2()
        Level_Hero()
    if Hero.Level == 3:
        print("You must defeat 30 monsters to move on")
        MonsterKills = 0
        Level3()
        Boss3()
        Final()

def Level1():
    global MonsterKills
    Level = True
    while Level == True:
        Path = random.randint(0,100)
        if Path <= 10:
            print("You found a chest")
            Item_Drop(Hero.Level)
            print("")
            Item_Drop((Hero.Level)+1)
        if Path >10 and Path <= 20:
            Totem = random.randint(0,4)
            Totems = ["Strength","Health","Agility","Dexterity","Luck"]
            print("")
            print("You have found a mysterious ", Totems[Totem]," totem")
            print("Increasing your ", Totems[Totem], " by 1")
            if Totem == 0:
                Hero.Strength = Hero.Strength + 1
            if Totem == 1:
                Hero.Health = Hero.Health + 1
            if Totem == 2:
                Hero.Agility = Hero.Agility + 1
            if Totem == 3:
                Hero.Dexterity = Hero.Dexterity + 1
            if Totem == 4:
                Hero.Luck = Hero.Luck + 1    
        if Path > 20:
            Enemy = random.randint(1,5)
            Enemy = Monster.Instances[Enemy]
            Enemy = MonsterList[Enemy]
            Fight(Enemy,True)
        if MonsterKills >=10:
            print("Would you like to move onto the boss Yes(0) No(1)")
            Choice = input("")
            if Choice == "0":
                Level = False

def Level2():
    global MonsterKills
    Level = True
    while Level == True:
        Path = random.randint(0,100)
        if Path <= 10:
            print("You found a chest")
            Item_Drop(Hero.Level)
            print("")
            Item_Drop((Hero.Level)+1)            
        if Path >10 and Path <= 20:
            Totem = random.randint(0,4)
            Totems = ["Strength","Health","Agility","Dexterity","Luck"]
            print("")
            print("You have found a mysterious ", Totems[Totem]," totem")
            print("Increasing your ", Totems[Totem], " by 2")
            if Totem == 0:
                Hero.Strength = Hero.Strength + 2
            if Totem == 1:
                Hero.Health = Hero.Health + 2
            if Totem == 2:
                Hero.Agility = Hero.Agility + 2
            if Totem == 3:
                Hero.Dexterity = Hero.Dexterity + 2
            if Totem == 4:
                Hero.Luck = Hero.Luck + 2    
        if Path > 20:
            Enemy = random.randint(6,10)
            Enemy = Monster.Instances[Enemy]
            Enemy = MonsterList[Enemy]
            Fight(Enemy,True)
        if MonsterKills >=20:
            print("Would you like to move onto the boss Yes(0) No(1)")
            Choice = input("")
            if Choice == "0":
                Level = False

def Level3():
    global MonsterKills
    Level = True
    while Level == True:
        Path = random.randint(0,100)
        if Path <= 15:
            print("You found a chest")
            Item_Drop(Hero.Level)
            print("")
            Item_Drop((Hero.Level)+1)
        if Path >10 and Path <= 20:
            Totem = random.randint(0,4)
            Totems = ["Strength","Health","Agility","Dexterity","Luck"]
            print("")
            print("You have found a mysterious ", Totems[Totem]," totem")
            print("Increasing your ", Totems[Totem], " by 3")
            if Totem == 0:
                Hero.Strength = Hero.Strength + 3
            if Totem == 1:
                Hero.Health = Hero.Health + 3
            if Totem == 2:
                Hero.Agility = Hero.Agility + 3
            if Totem == 3:
                Hero.Dexterity = Hero.Dexterity + 3
            if Totem == 4:
                Hero.Luck = Hero.Luck + 3    
        if Path > 20:
            Enemy = random.randint(11,15)
            Enemy = Monster.Instances[Enemy]
            Enemy = MonsterList[Enemy]
            Fight(Enemy,True)
        if MonsterKills >=30:
            print("Would you like to move onto the boss Yes(0) No(1)")
            Choice = input("")
            if Choice == "0":
                Level = False
                
def Boss1():
    print("Now your in real trouble!")
    Fight(Grand_Wizard,False)
    print("")
    print("You have been awarded with a second item for defeating the boss!")
    Item_Drop(2)
    print("")

def Boss2():
    print("Feel my wrath!")
    Fight(Grand_Knight,False)
    print("")
    print("You have been awarded with a second item for defeating the boss!")
    Item_Drop(3)
    print("")
    
def Boss3():
    print("So it has come to this....")
    Fight(Tom,False)
    
def Item_Drop(Level):
    print("")
    Type = {0:Hero.Head,1:Hero.Weapon,2:Hero.Feet,3:Hero.Chest,4:Hero.Legs,5:Hero.Hands}
    if Level == 1:
        Item = 6
    if Level == 2:
        Item = 12
    if Level == 3:
        Item = 18
    LevelUp = random.randint(0,100)
    if Character.Luck(Hero) > LevelUp:
        print("Your luck has allowed you gain a more powerful item")
        Item = Item + 6
    Item = Item + random.randint(0,5)
    Item = Equitment.Instances[Item]
    print("You have been awarded a: ", Item)
    Item = EquitmentList[Item]
    print("Its stats are:")
    print(Equitment.Strength(Item) ,"Strength")
    print(Equitment.Health(Item) ,"Health")
    print(Equitment.Agility(Item) ,"Agility")
    print(Equitment.Dexterity(Item) ,"Dexterity")
    print(Equitment.Luck(Item) ,"Luck")    
    print(Equitment.Armour(Item) ,"Armour")
    print("")
    Compare = Equitment.Type(Item)
    Compare = Type[Compare]
    print("Your current items stats are:")
    print(Equitment.Strength(Compare) ,"Strength")
    print(Equitment.Health(Compare) ,"Health")
    print(Equitment.Agility(Compare) ,"Agility")
    print(Equitment.Dexterity(Compare) ,"Dexterity")
    print(Equitment.Luck(Compare) ,"Luck")    
    print(Equitment.Armour(Compare) ,"Armour")    
    print("Would you like to equip the new item Yes(0) No(1):")
    Choice = input("")
    if Choice == "0":
        Character.Upgrade(Hero, Item, Equitment.Type(Item))
    print("")

def Final():
    print("")
    print("Congratulations on saving the princess")
    print("As a reward your name has been added to list of winners")
    File = open("Winners.txt","a")
    File.write("\n")
    File.write(Hero.Name)
    File.close()
    os.startfile("Winners.txt")
    os.startfile("Win.jpg")
    

def Menu():
    State = 69
    while State != "0":
        print("Please choose one of the following:")
        print("Load previous game (1)")
        print("Start new game (2)")
        print("Game instructions (3)")
        print("Exit game (0)")
        State = input("")
        if State == "1":
            Load_Game()
        if State == "2":
            CreateHero()
        if State == "3":
            Instructions()      

print("Welcome user")
Menu()
