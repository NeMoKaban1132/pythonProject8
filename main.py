import random

num_1 = int(input(f"Print number of Players: \n"))

class NumError(Exception):
    def __str__(self):
        return f"It`s so much players"
def checker (num_1, limit_of_pl):
    if num_1 < limit_of_pl:
        return "not enough players"
    else:
        raise NumError(num_1)
checker(num_1, limit_of_pl=4)



class Human:
    def __init__(self, name="Human", job=None, home=None, car=None, pet=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home
        self.pet = pet
    def get_home(self):
        self.home = House()
    def get_car(self):
        self.car = Auto(brands_of_car)
    def get_pet(self):
        self.pet = Pet(list_of_pets)
    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)
    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5
    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4

        if self.pet.happy():
            pass
        else:
            if self.pet.happy < 5:
                self.play_with_pet("game_with_pets")
                return
            else:
                pass

        if self.pet.feed():
            pass
        else:
            if self.pet.hunger < 5:
                self.shop_2("food_for_pets")
                return
            else:
                pass

    def play_with_pet(self, play):
        if self.pet.happy():
            pass
        else:
            if self.pet.happy < 5:
                play = "game_with_pets"
            else:
                pass
        if play == "game_with_pets":
            print("I' play with my pet")
            self.gladness -= 10
            self.pet.happy += 10

    def shop_2(self, manage_2):
        if self.pet.feed():
            pass
        else:
            if self.pet.hunger < 5:
                manage_2 = "food_for_pets"
            else:
                pass
        if manage_2 == "food_for_pets":
            print("I bought food for pets")
            self.money -= 10
            self.pet.hunger += 10
    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = "fuel"
            else:
                self.to_repair()
                return
        if manage == "fuel":
            print("I bought fuel")
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            print("Bought food")
            self.money -= 50
            self.home.food += 50
        elif manage == "delicacies":
            print("Hooray! Delicious!")
            self.gladness += 10
            self.satiety += 2
            self.money -= 15
    def chill(self):
        self.gladness += 10
        self.home.mess += 5
    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0
    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    def days_indexes(self, day):
        day = f" Today the {day} of {self.name}'s life "
        print(f"{day:=^50}","\n")
        human_indexes = self.name + "'s indexes"
        print(f"{human_indexes:^50}","\n")
        print(f"Money – {self.money}")
        print(f"Satiety – {self.satiety}")
        print(f"Gladness – {self.gladness}")
        home_indexes = "Home indexes"
        print(f"{home_indexes:^50}", "\n")
        print(f"Food – {self.home.food}")
        print(f"Mess – {self.home.mess}")
        car_indexes = f"{self.car.brand} car indexes"
        print(f"{car_indexes:^50}", "\n")
        print(f"Fuel – {self.car.fuel}")
        print(f"Strength – {self.car.strength}")
        pet_indexes = f"{self.pet.pet} pet indexes"
        print(f"{pet_indexes:^50}", "\n")
        print(f"Hunger – {self.pet.hunger}")
        print(f"Happiness – {self.pet.happy}", "\n")
    def is_alive(self):
        if self.gladness < 0:
            print("Depression…")
            return False
        if self.satiety < 0:
            print("Dead…")
            return False
        if self.money <- 500:
            print("Bankrupt…")
            return False
    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.pet is None:
            self.get_pet()
        if self.home is None:
            print("Settled in the house")
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"I bought a car {self.car.brand}")
        if self.job is None:
            self.get_job()
            print(f"I don't have a job, going to get a job {self.job.job} with salary {self.job.salary}")
        self.days_indexes(day)
        dice = random.randint(1, 4)
        if self.satiety < 20:
            print("I'll go eat")
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                print("I want to chill, but there is so much mess…\nSo I will clean the house")
                self.clean_home()
            else:
                print("Let`s chill!")
                self.chill()
        elif self.money < 0:
            print("Start working")
            self.work()
        elif self.car.strength < 15:
            print("I need to repair my car")
            self.to_repair()
        elif dice == 1:
            print("Let`s chill!")
            self.chill()
        elif dice == 2:
            print("Start working")
            self.work()
        elif dice == 3:
            print("Cleaning time!")
            self.clean_home()
        elif dice == 4:
            print("Time for treats!")
            self.shopping(manage="delicacies")

class Pet:
    def __init__(self, pets_list):
        self.pet = random.choice(list(pets_list))
        self.hunger = pets_list[self.pet]["hunger"]
        self.happy = pets_list[self.pet]["happiness"]
        self.lazzy = pets_list[self.pet]["laziness"]
    def feed(self):
        if self.hunger <= 5:
            self.hunger -= self.lazzy
            return True
    def happy(self):
        if self.pet.happy <= 5:
            self.happy -= self.lazzy
            return True

class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]
    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("The car cannot move")
            return False
class House:
    def __init__(self):
        self.mess = 0
        self.food = 0

job_list = {"Java developer": {"salary":50, "gladness_less": 10 }, "Python developer": {"salary":40, "gladness_less": 3 },
"C++ developer": {"salary":45, "gladness_less": 25 }, "Rust developer":{"salary":70, "gladness_less": 1 },}

brands_of_car = {"BMW":{"fuel":100, "strength":100,"consumption": 6},
"Opel":{"fuel":50, "strength":40,"consumption": 10},
"Volvo":{"fuel":70, "strength":150,"consumption": 8},
"Ferrari":{"fuel":80, "strength":120,"consumption": 14},}
list_of_pets = {"Dog": {"hunger": 2, "happiness": 10, "laziness": 5}, "Cat": {"hunger": 2, "happiness": 10, "laziness": 15},
"Turtle": {"hunger": 2, "happiness": 5, "laziness": 5}}
class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]

nick = Human(name="Nick")

for day in range(1, 8):
    if nick.live(day) == False:
        break

