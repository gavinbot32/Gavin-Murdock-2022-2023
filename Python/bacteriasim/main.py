# Generation Based
# Each Generation Each Bacteria has a child
# Each Generation the simulator checks if the bacteria has less resistance then the anti-biotics.
# If a bacteria has less resistance then an anti-biotics strength the bacteria dies.
# Whenever a child is born there is a 1/75 chance to have a mutation
# Mutations have a 85% chance to be positive and a 15% chance to be negative
# Mutations can go anywhere between +- 1 - 50
# Simulation will update every given generation for example, every 50 generations the sim will update or every 30 etc.
import random


class Bacteria():
    def __init__(self,strength,game):
        self.game = game
        self.strength = strength
        if self.strength == None:
            self.strength = random.randint(1,20)
        else:
            if random.randint(1,75) == 1:
                if random.randint(1,100) <= 15:
                    self.strength -= random.randint(1,50)
                else:
                    self.strength += random.randint(1,50)

    def kill(self):
        self.game.colony.remove(self)


class Game():
    def __init__(self):
        self.running = True


    def new(self):
        defPop = 2000
        self.antibod = random.randint(1,25)
        self.colony = []
        self.generation = 0
        self.gencount = 0
        self.deathrow = 0
        self.kills = 0
        for i in range(defPop):
            bac = Bacteria(None,self)
            self.colony.append(bac)

        self.pause()
        self.run()
    def run(self):
        # game loop
        self.playing = True
        while self.playing:
            self.update()

    def update(self):
        pregen = []
        for bacteria in self.colony:
            pregen.append(bacteria)
        self.generation += 1
        self.gencount += 1
        self.deathrow += 1





        if len(pregen) > 0:
            for bac in pregen:
                bacteria = Bacteria(bac.strength,self)
                self.colony.append(bacteria)
        else:
                self.pause()

        for i in self.colony:
            if i.strength <= self.antibod:
                i.kill()
                self.kills += 1

        if self.deathrow >= 5:
            self.deathrow = 0
            percent = len(self.colony) * .99
            percent = int(percent)
            for i in range(percent):
                rando = random.choice(self.colony)
                rando.kill()

        maxStrength = 0
        for i in self.colony:
            if i.strength > maxStrength:
                maxStrength = i.strength
        if maxStrength > self.antibod:
            maxDif = maxStrength - self.antibod
        elif maxStrength < self.antibod:
            maxDif = 0
        else:
            maxDif = 25

        if maxDif != 0:
            self.antibod += random.randint(maxDif-5,maxDif+5)

        if self.gencount >= 1:
            self.gencount = 0
            self.pause()
    def pause(self):
        maxStrength = 0
        for i in self.colony:
            if i.strength > maxStrength:
                maxStrength = i.strength

        print("")
        print("kills:",self.kills)
        print("generation:",self.generation)
        print("highest strength:",maxStrength)
        print("antibod:",self.antibod)
        print("amount of bacteria:",len(self.colony))
        if input("Press enter to continue or type Quit") == "Quit":
            quit()
        return maxStrength






g = Game()
while g.running:
    g.new()