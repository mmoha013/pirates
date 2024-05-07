import game.event as event
import random
import game.combat as combat
import game.config as config
from game.display import menu
import game.superclasses as superclasses
from game.display import announce

class SharkAttack (event.Event):
    '''
    A combat encounter with a crew of drowned pirate zombies.
    When the event is drawn, creates a combat encounter with 2 to 6 drowned pirates, kicks control over to the combat code to resolve the fight, then adds itself and a simple success message to the result
    '''

    def __init__ (self):
        self.name = " drowed pirate attack"

    def process (self, world):
        '''Process the event. Populates a combat with Drowned monsters. The first Drowned may be modified into a "Pirate captain" by buffing its speed and health.'''
        result = {}
        result["message"] = "the drowned pirates are defeated!"

        #Step 1: "The ship is leaking!"
        print("The ship is leaking! You need to fix it!")
        #Step 2: Pick a crewmate to fix the ship and set them aside
        crew = config.the_player.get_pirates()
        choice = crew[menu (crew)]
        config.the_player.pirates.remove(choice)

        #Step 3: Combat with shark and remaining pirates
        monsters = [Shark('shark')]

        announce ("You are attacked by a crew of drowned pirates!")
        combat.Combat(monsters).combat()
        #Step 4: Re-join crewmate with crew
        config.the_player.pirates.append(choice)
        result["newevents"] = [ self ]
        return result


class Shark (combat.Monster):
    def __init__ (self, name):
        attacks = {}
        attacks["bite"] = ["bites",random.randrange(70,101), (10,20)]
        #7 to 19 hp, bite attack, 160 to 200 speed (100 is "normal")
        super().__init__(name, random.randrange(7,20), attacks, 180 + random.randrange(-20,21))
