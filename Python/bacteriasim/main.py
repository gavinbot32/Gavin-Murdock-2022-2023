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
    def __init__(self,strength):
        self.strength = strength
        if self.strength == None:
            self.strength = random.randint(1,20)
        else:
            if random.randint(1,75) == 1:
                if random.randint(1,100) <= 15:
                    self.strength -= random.randint(1,50)
                else:
                    self.strength += random.randint(1,50)


class Game():
    def __init__(self):
        self.running = True


    def new(self):
        defPop = 1000
        self.antibod = random.randint(1,25)
        self.colony = []
        self.generation = 0
        self.gencount = 0
        for i in range(defPop):
            bac = Bacteria(None)
            self.colony.append(bac)
        self.pause()
        self.run()
    def run(self):
        # game loop
        self.playing = True
        while self.playing:
            self.update()

    def update(self):
        self.generation += 1
        self.gencount += 1

        if len(self.colony > 0):

        else:
            self.pause()




        if self.gencount >= 10:
            self.gencount = 0
            self.pause()
    def pause(self):
        maxStrength = 0
        for i in self.colony:
            if i.strength > maxStrength:
                maxStrength = i.strength

        print("generation:",self.generation)
        print("highest strength:",maxStrength)
        print("antibod:",self.antibod)
        print("amount of bacteria:",len(self.colony))
        input("Press enter to continue")






g = Game()
while g.running:
    g.new()