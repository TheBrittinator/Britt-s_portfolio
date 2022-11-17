"""Object Oriented Programming Practice
Create a pokemon game using the lesson i learned today!
TO DO: Things I would like to add:
ADD 1 - Function that causes Ash to choose an opponent at random to play against you.
ADD 2 - Input Variables that allow you to choose an opponent, or allow a random choice.
ADD 3 - Load, Extract, and reindex actual HP and attack data from a pokemon CSV, then format for the program (must have listed type with hp, attack and defense stats). 
ADD 4 - Include additional type advantages in the fight method (this might get complex, but that's where the fun is!)
ADD restart/end program from main module."""
# Object Oriented Programming
# Pokemon Game in Python!
import sys
import numpy as np
import time



# Delay printing

def delay_print(s):
    # print one character at a time
    # https://stackoverflow.com/questions/9246076/how-to-print-one-charachter-at-a-time-on-one-line
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

# Create a class
class Pokemon:
    def __init__(self, name, types, moves, EVs, health='===================='):
        # save variables as attributes
        self.name = name
        self.types = types
        self.moves = moves
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.health = health
        self.bars = 20 # Amount of health bars

    def fight(self, Pokemon2):
        #allow 2 pokemon to fight each other

        # Print fight information
        print("------POKEMON BATTLE------")
        print(f"\n{self.name}")
        print("TYPE/", self.types)
        print("ATTACK/", self.attack)
        print("DEFENSE/", self.defense)
        print("LVL/", 3*(1+np.mean([self.attack,self.defense])))
        print("/nVS")
        print(f"\n{Pokemon2.name}")
        print("TYPE/", Pokemon2.types)
        print("ATTACK/", Pokemon2.attack)
        print("DEFENSE/", Pokemon2.defense)
        print("LVL/", 3*(1+np.mean([Pokemon2.attack,Pokemon2.defense])))

        time.sleep(2)

        # Consider type advantages
        version = ['Fire', 'Water', 'Grass']
        for i,k in enumerate(version):
            if self.types == k:
                # both are same type
                if Pokemon2.types == k:
                    string_1_attack = '\nIts not very effective...'
                    string_2_attack = '\nIts not very effective...'

                # pokemon2 is strong
                if Pokemon2.types == version[(i+1)%3]: # Why did we do this?
                    Pokemon2.attack *= 2
                    Pokemon2.defense *= 2
                    self.attack /= 2
                    self.defense /= 2
                    string_1_attack = '\nIts not very effective...'
                    string_2_attack = '\nIts super effective!'

                # pokemon2 is weak
                if Pokemon2.types == version[(i+2)%3]:
                    self.attack *= 2
                    self.defense *= 2
                    Pokemon2.attack /= 2
                    Pokemon2.defense /= 2
                    string_1_attack = '\nIts super effective!'
                    string_2_attack = '\nIts not very effective...'

        # now for the actual fighting!
        # continue while pokemon still have health
        while (self.bars > 0) and (Pokemon2.bars > 0):
            # Print the health of each pokemon
            print(f"\n{self.name}\t\tHLTH\t{self.health}")
            print(f"\n{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}")

            print(f"\nGo {self.name}!")
            for i, x in enumerate(self.moves):
                print(f"{i+1}.", x)
            index = int(input('Pick a move: '))
            delay_print(f"\n{self.name} used {self.moves[index-1]}!")
            time.sleep(1)
            delay_print(string_1_attack)

            #Determine damage
            Pokemon2.bars -= self.attack
            Pokemon2.health = ""

            # Add back bars plus defense boost
            for j in range(int(Pokemon2.bars+.1*Pokemon2.defense)):
                Pokemon2.health += "="

            time.sleep(1)
            print(f"\n{self.name}\t\tHLTH\t{self.health}")
            print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")
            time.sleep(.5)

            # check to see if pokemon fainted
            if Pokemon2.bars <= 0:
                delay_print("\n...Oh no!" + Pokemon2.name + ' fainted!')
                break

            # pokemon2 turn to attack
            print(f"\nGo {Pokemon2.name}!")
            for i, x in enumerate(Pokemon2.moves):
                print(f"{i+1}.", x)
            index = int(input('Pick a move: '))
            delay_print(f"\n{Pokemon2.name} used {Pokemon2.moves[index-1]}!")
            time.sleep(1)
            delay_print(string_2_attack)

            #Determine damage
            self.bars -= Pokemon2.attack
            self.health = ""

            # Add back bars plus defense boost
            for j in range(int(self.bars+.1*self.defense)):
                self.health += "="

            time.sleep(1)
            print(f"\n{self.name}\t\tHLTH\t{self.health}")
            print(f"\n{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}")
            time.sleep(.5)

            # check to see if pokemon fainted
            if self.bars <= 0:
                delay_print("\n...Oh no!" + self.name + ' fainted!')
                break

        money = np.random.choice(5000)
        delay_print(f"\nOpponent paid you ${money}.")




if __name__ == '__main__':
    # Create pokemon in the main module. 
    Charizard = Pokemon('Charizard', 'Fire', ['Flamethrower', 'Fly', 'Blast Burn', 'Fire Punch'], {'ATTACK' :12, 'DEFENSE': 8})
    Blastoise = Pokemon('Blastoise', 'Water', ['Water Gun', 'Bubblebeam', 'Hydro Pump', 'Surf'],{'ATTACK': 10, 'DEFENSE':10})
    Venusaur = Pokemon('Venusaur', 'Grass', ['Vine Wip', 'Razor Leaf', 'Earthquake', 'Frenzy Plant'],{'ATTACK':8, 'DEFENSE':12})

    Charmander = Pokemon('Charmander', 'Fire', ['Ember', 'Scratch', 'Tackle', 'Fire Punch'],{'ATTACK':4, 'DEFENSE':2})
    Squirtle = Pokemon('Squirtle', 'Water', ['Bubblebeam', 'Tackle', 'Headbutt', 'Surf'],{'ATTACK': 3, 'DEFENSE':3})
    Bulbasaur = Pokemon('Bulbasaur', 'Grass', ['Vine Wip', 'Razor Leaf', 'Tackle', 'Leech Seed'],{'ATTACK':2, 'DEFENSE':4})

    Charmeleon = Pokemon('Charmeleon', 'Fire', ['Ember', 'Scratch', 'Flamethrower', 'Fire Punch'],{'ATTACK':6, 'DEFENSE':5})
    Wartortle = Pokemon('Wartortle', 'Water', ['Bubblebeam', 'Water Gun', 'Headbutt', 'Surf'],{'ATTACK': 5, 'DEFENSE':5})
    Ivysaur = Pokemon('Ivysaur\t', 'Grass', ['Vine Wip', 'Razor Leaf', 'Bullet Seed', 'Leech Seed'],{'ATTACK':4, 'DEFENSE':6})

    print("\nlet's go Pokemon!")
    print("\nAsh: 'I choose you!'")
    print("\nYou choose as your Pokemon! Let's go!")
    print("__"*40)
    #insert your command to begin your game = ashPokemon.fight(your pokemon)
    Charizard.fight(Venusaur)
