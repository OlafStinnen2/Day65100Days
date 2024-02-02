#My game needs to have a character with a name, health and magic points.
class character:
  name = None
  health = None
  magicPoints = None
  
  # It needs these values setup when it is initialized.

  def __init__(self, name, health, magicPoints):
    self.name = name
    self.health = health
    self.magicPoints = magicPoints

  #It needs a method to output this data.
  def printCharacter(self):
    print(f'''
Name: {self.name}
Health: {self.health}
Magic Points: {self.magicPoints}
        ''') 

#There should be a sub-class 'player' which inherits from character and also has a number of lives.
class player(character):
  lives = None

  def __init__(self,name, health, magicPoints, lives, alive):
    self.name = name
    self.health = health
    self.magicPoints = magicPoints
    self.lives = lives
    self.alive = alive

  def printPlayer(self):
    print(f'''
Name: {self.name}
Health: {self.health}
Magic Points: {self.magicPoints}
Lives: {self.lives}
Alive: {self.alive}''') 
#There should also be an 'enemy' sub-class with additional 'type' and 'strength'.
class enemy(character):
  type = None
  strength = None
  
  def __init__(self,name, health, magicPoints, lives, alive, type, strength):
    self.name = name
    self.health = health
    self.magicPoints = magicPoints
    self.type = type
    self.strength = strength

  def printEnemy(self):
    print(f'''
Name: {self.name}
Health: {self.health}
Magic Points: {self.magicPoints}
Type: {self.type}
Strength: {self.strength}
      ''')

#'enemy' should have two sub-classes:
#'orc' with a 'speed' attribute.
#'vampire' with a 'day/night' tracker
class orc(enemy):
  speed = None
  
  def __init__(self,name, health, magicPoints, type, strength, speed):
    
    self.name = name
    self.health = health
    self.magicPoints = magicPoints
    self.type = type
    self.strength = strength
    self.speed = speed

  def printOrc(self):
    print(f'''
  Name: {self.name}
  Health: {self.health}
  Magic Points: {self.magicPoints}
  Type: {self.type}
  Strength: {self.strength}
  Speed: {self.speed}
      ''')

class vampire(enemy):
  day_night = None

  def __init__(self,name, health, magicPoints, type, strength, day_night):

    self.name = name
    self.health = health
    self.magicPoints = magicPoints
    self.type = type
    self.strength = strength
    self.day_night = day_night

  def printVampire(self):
    print(f'''
Name: {self.name}
Health: {self.health}
Magic Points: {self.magicPoints}
Type: {self.type}
Strength: {self.strength}
Day/Night: {self.day_night}
      ''')


print('''🌟Generic RPG🌟

Player''')
one_player=player("Olaf", 100, 100, 3, "Yes")
one_player.printPlayer()

one_vampire = vampire("Vampire 1", 100, 100, "Vampire", 100, "Day")
one_vampire.printVampire()

two_vampire = vampire("Vampire 2", 100, 100, "Vampire", 100, "Day")
two_vampire.printVampire()

one_orc = orc("Orc 1", 100, 100, "Orc 1", 100, "Day")
one_orc.printOrc()

two_orc = orc("Orc 2", 100, 100, "Orc 2", 100, "Day")
two_orc.printOrc()

three_orc = orc("Orc 3", 100, 100, "Orc 2", 100, "Day")
two_orc.printOrc()