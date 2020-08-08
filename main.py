"""
This code is an attempt to work out the classes and perform some basic methods with them.
"""
import random
import math
class species:
    # later this should be a nice little GUI
    # add growth later...
    # make preset models later too with types of species ie wolf rabbit, so they don't have to add all the variables
    # odds maturing should be a number between 1 and 100 representing percentage survived to adulthood
    def __init__(self, odds_maturing_to_adult, adult_age, av__adult_weight, av_max_age, annual_growth_rate,
                 gestation_period, dependency_time,
                 predators, prey, av_speed, av_range, vision, sound, smell, temp_min, temp_max, water_needs,
                 food_needs):

        # age, alive or dead
        self.age = random.randint(0, av_max_age)
        #print("age", self.age, "age of maturation", adult_age)
        if self.age < adult_age:  # if they are not mature yet
            x = random.randint(1,100)
            #print(x)
            if x <= odds_maturing_to_adult:
                self.alive = True
            else:
                self.alive = False
        else:
            self.alive = True

        self.age_days = self.age * 365

        #print(self.alive)
        # make all of these actual stats a bell curve distribution later

        self.gestation_period = gestation_period
        self.dependency_time = dependency_time

        self.predators = predators
        self.prey = prey

        # personal abiities
        self.speed = av_speed * random.randint(75,125)/100
        self.range = av_range * random.randint(75,125)/100
        self.vision = vision * random.randint(85,115)/100
        self.sound = sound * random.randint(85,115)/100
        self.smell = smell * random.randint(85,115)/100
        #print(self.speed, self.range, self.vision, self.sound, self.smell)

        self.temp_min = temp_min
        self.temp_max = temp_max
        self.water_needs = water_needs
        self.food_needs = food_needs

        # determining gender - can be weighted if a species has an uneven distribution
        y = random.randint(0,1)
        if y == 1:
            self.gender = "Male"
        else:
            self.gender = "Female"
       # print(self.gender)
        # determining fertility
        if self.gender == "Female":
            if self.age >= av_max_age - (av_max_age/10): # could be fine tuned to a species
                self.fertility = False
                self.pregnancy = False
            else:
                self.fertility = True

        if self.gender == "Male":
            self.fertility = True
        #print(self.fertility)

        # making an empty dictionary
        self.food_history = {}
        self.water_history = {}


        # determining weight - not based on food......
        if self.age >= adult_age:
            self.weight = av__adult_weight * random.randint(70,130)/100
        else:
            ratio = self.age / adult_age
            self.weight = av__adult_weight * ratio
            # add birth weight later so weight is never zero

        #print(self.weight)
        self.adult_age = adult_age

        self.annual_growth_rate = annual_growth_rate

        self.personal_maximum_age = av_max_age * random.randint(85,115)/100
        #print(self.personal_maximum_age)

        
    def print(self):
        print("age is ", self.age)   # FIXME Make ages follow a more realistic distribution
        print("age in days is", self.age_days)
        print("status is", self.alive)
        print("speed is", self.speed)
        print("range is", self.range)
        print("smell is", self.smell)
        print("vision is", self.vision)
        print("weight is", self.weight)
        print("prey are", self.prey)
        print("predators are", self.predators)
        print("fertility status is", self.fertility)
        # add number of kids, dependency status, etc


    def day(self):
        self.age_days = self.age_days + 1

"""
    def time_basics(self, duration):  # duration is in years
        for i in range(0, duration + 1):
            self.age = self.age + 1
            if self.age >= self.adult_age:
                self.weight = self.weight * self.annual_growth_rate
        if self.age == self.personal_maximum_age:
            self.alive = False
            # otherwise, weight is going to depend on amount eaten... deal with this later
            # deal with whether or not they get eaten.... or starve
"""

class habitat:
    # river: array, present or not, length, width, works for rivers and lengths
    def __init__(self, area, percent_shelter, average_size_shelter, river_presence, nutrient_availability, sun_availabiility, max_temp,
                 min_temp, precipitation_frequency, precipitation_amount):

        self.area = area
        self.percent_shelter = percent_shelter
        self.average_size_shelter = average_size_shelter
        self.shelter_clump_sizes  = []
        self.lines_per_clump = []
        self.river_presence = river_presence[0]
        self.river_length = river_presence[1]
        self.river_width = river_presence[2]




    def create_map(self):

        # creating the map randomly
        holder = int(math.sqrt(self.area))
        self.length = random.randint(int(holder*0.5), int(holder*1.5))
        print(self.length, "length")
        self.width = int(self.area/self.length)
        print(self.width, "width")
        self.map = []
        mini_map = []
        for i in range(0, self.length):
            for j in range(0, self.width):
                mini_map.append(0)
            self.map.append(mini_map)
            mini_map = []
        return self.map

    def create_random_shelter_units(self):
        # setting randomly sized units of shelter
        self.units_of_shelter = int(self.percent_shelter/100 * self.area)  # square feet
        #print("units total shelter", units_of_shelter)
        counter = 0
        while self.units_of_shelter > 0:
            clump_size = random.randint(int(self.average_size_shelter/2), int(2*self.average_size_shelter))
            if self.units_of_shelter < clump_size:
                clump_size = self.units_of_shelter
            self.shelter_clump_sizes.append(clump_size)
            counter = counter + clump_size
            self.units_of_shelter = self.units_of_shelter - clump_size
            #print(units_of_shelter, "units left")
        print("sizes", self.shelter_clump_sizes, "counter", counter)
        return self.shelter_clump_sizes

        # randomly spacing the units of shelter in their size clumps out
    def space_clump_sizes(self):
        clump_list = []
        lines_per_clump = []
        print(self.shelter_clump_sizes)
        for i in self.shelter_clump_sizes:
            while i > 0:
                line_size = random.randint(1, i)
                clump_list.append(line_size)
                i  = i - line_size
            lines_per_clump.append(clump_list)
            clump_list = []
        self.lines_per_clump = lines_per_clump
        print(self.lines_per_clump)
        return self.lines_per_clump

        # checking if a space is available
    def check_if_available(self): #FIXME Rename
        mini_map = []
        map_holder = []
        for i in self.map:
            for j in i:
                mini_map.append(j)
            map_holder.append(mini_map)
            mini_map = []

        #FIXME MAKE IT SO THE SHELTER CANNOT BE PLACED ON A RIVER EITHER
        for i in self.lines_per_clump:
            width_coordinate = random.randint(0, self.width)
            length_coordinate = random.randint(0, self.length)
            for j in i:
                for k in range(j):
                    if width_coordinate < (self.width) and  length_coordinate < (self.length):
                        if map_holder[length_coordinate-1][width_coordinate-1] == 0:
                            map_holder[length_coordinate-1][width_coordinate-1] = "S"
                        elif map_holder[length_coordinate-1][width_coordinate-1] == "S":
                            map_holder[length_coordinate-1][width_coordinate-1] = "DS"
                        elif map_holder[length_coordinate-1][width_coordinate-1] == "R" or "W":
                             # FIXME MAKE MORE EFFICIENT
                            return False
                    else:
                        return False
                    width_coordinate = width_coordinate + 1

                length_coordinate = length_coordinate + 1
                width_coordinate = width_coordinate - j
            #print(x_coordinate, y_coordinate)
        self.map = map_holder
        return True



    def place_rivers(self):

        mini_map_river = []
        map_holder_river = []
        for i in self.map:
            for j in i:
                mini_map_river.append(j)
            map_holder_river.append(mini_map_river)
            mini_map_river = []


        print(self.river_presence)
        if self.river_presence == True:
            # first, a flat accross river. no slope, just going across until
            print(self.river_length, self.river_width)
            length_coordinate = 0
            width_coordinate = 0
            for i in range(self.river_width):
                for i in range(self.river_length):
                    if length_coordinate < self.length and width_coordinate < self.width:
                        map_holder_river[length_coordinate-1][width_coordinate] = "R"
                        length_coordinate = length_coordinate + 1
                        width_coordinate = width_coordinate + 1
                    else:
                        random_length = random.randint(1, self.length)
                        random_width = random.randint(1, self.width)
                        while map_holder_river[random_length-1][random_width-1] != 0:
                            random_length = random.randint(1, self.length)
                            random_width = random.randint(1, self.width)
                        map_holder_river[random_length-1][random_width-1] = "W"
                length_coordinate = 1
                width_coordinate = 0
            self.map = map_holder_river



def main():

    my_creatures = []
    for i in range(50):
        my_creatures.append(species(80,10,150,20,8,1,3,[], ["rabbit"],100,100,100,100,100,100,100,100,100))
    #for animal in my_creatures:
       # animal.print()
       # print("******************")

    yes = habitat(2000,10,5, [True,10,2], 100,100,80,40,20,10)
    yes.create_map()
    yes.place_rivers()


    yes.create_random_shelter_units()
    yes.space_clump_sizes()

    while yes.check_if_available() == False:
        yes.check_if_available()

    print(yes.map)


main()





