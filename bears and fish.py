import random
class Bear:#creating object bear
    def __init__(self):
        self.name = "Bear"

    def __str__(self):
        return "B"


class Fish:#creating object fish
    def __init__(self):
        self.name = "Fish"

    def __str__(self):
        return "F"


class ecosystem:
    def __init__(self, river_length, number_of_fish, number_of_bears, steps):
        self.river = list()
        self.river_length = river_length
        self.number_of_fish = number_of_fish
        self.number_of_bears = number_of_bears
        self.steps = steps
        self.notMove = []
        self.making_river()

    def making_river(self):  # making river in the beggining
        for i in range(self.river_length - self.number_of_fish - self.number_of_bears):
            self.river.append("N")
        self.adding_fish()
        self.adding_bear()
        return self.river

    def adding_fish(self):#adding fish to making_river(self)
        for i in range(self.number_of_fish):
            index = random.randint(0, self.river_length)
            self.river.insert(index, Fish())
        return self.river

    def adding_bear(self):#adding bear to making_river(self)
        for i in range(self.number_of_bears):
            index = random.randint(0, self.river_length)
            self.river.insert(index, Bear())
        return self.river

    def printRiver(self):#printing river with object bear,object fish,and N
        river = []
        for animal in self.river:
            if isinstance(animal, Bear):
                river.append("B")
            elif isinstance(animal, Fish):
                river.append("F")
            else:
                river.append("N")
        return river

    def random_move(self,pos):
        action = random.randint(-1, 1)#pick random number from -1 to 1
        river = self.river
        print("Animal:",str(self.river[pos]),"Action: ", action)
        self.notMove.append(self.river[pos])#appending to not move list
        if action != 0:
            if 0 <= pos + action < self.river_length:
                if river[pos + action] == "N":#if the index left of it or right of it is N
                    self.river[pos + action] = self.river[pos]#it will move to right or left
                    self.river[pos] = "N"#fill the index before with N
                else:
                    if (isinstance(river[pos], Bear) and isinstance(river[pos + action], Bear)) or (isinstance(river[pos], Fish) and isinstance(river[pos + action], Fish)):
                        self.random_new(pos)#if bear and bear or fish and fish collide
                    else:
                        if isinstance(river[pos], Bear):
                            self.river[pos + action] = self.river[pos]#if bear and fish collide bear will eat fish
                            self.river[pos] = "N"
                        else:
                            self.river[pos] = "N"

    def random_new(self, pos):#create a new bear or a new fish in a random position
        empty = [i for i in range(len(self.river)) if self.river[i] == "N"]

        if len(empty) != 0:#if there is an empty position
            newPos = empty[random.randint(0, len(empty) - 1)]#place bear or fish in a random empty position
            if isinstance(self.river[pos], Bear):
                self.river[newPos] = Bear()
            else:
                self.river[newPos] = Fish()
            self.notMove.append(self.river[newPos])#the new bear or fish can't move until next step


    def simulation(self):
        for i in range(self.steps):
            self.notMove = []#a list of bear and fish that can't move until the next step
            print("The ecosystem at the Beginning of the step", i + 1)
            print(self.printRiver())
            for j in range(len(self.river)):
                if self.river[j] != "N" and self.river[j] not in self.notMove:#if it meets these condtions
                    self.random_move(j)#do a random action
                    print("The current ecosystem after the action: ")
                    print(self.printRiver())

