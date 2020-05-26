class Animal:
    sound=""
    required_food=0
    breath=""
    def __init__(self,age_in_months,breed,required_food_in_kgs):
        if(age_in_months>1):
            raise ValueError("Invalid value for field age_in_months: {}".format(age_in_months))
        if(required_food_in_kgs<=0):
            raise ValueError("Invalid value for field required_food_in_kgs: {}".format(required_food_in_kgs))
        self._age_in_months=age_in_months
        self._breed=breed
        self._required_food_in_kgs=required_food_in_kgs
        
    @property
    def age_in_months(self):
        return self._age_in_months
    @property
    def breed(self):
        return self._breed
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
       
    @classmethod 
    def make_sound(cls):
        print(cls.sound)
    
    def grow(self):
        self._age_in_months+=1
        self._required_food_in_kgs+=self.required_food
        
    @classmethod
    def breathe(cls):
        print(cls.breath)
        
class LandAnimals(Animal):
    breath="Breathe in air"
    
class WaterAnimals(Animal):
    breath="Breathe oxygen from water"
    
class HuntingAnimals:
    animal_to_kill=""
    def hunt(self,zoo):
        Zoo.kill(zoo,self.animal_to_kill)
    
class Deer(LandAnimals):
    sound="Buck Buck"
    required_food=2
    
class Lion(LandAnimals,HuntingAnimals):
    sound="Roar Roar"
    required_food=4
    animal_to_kill="deer"
        
class Shark(WaterAnimals,HuntingAnimals):
    sound="Shark Sound"
    required_food=8
    animal_to_kill="goldfish"
    
class GoldFish(WaterAnimals):
    sound="Hum Hum"
    required_food=0.2
    
class Snake(LandAnimals,HuntingAnimals):
    sound="Hiss Hiss"
    required_food=0.5
    animal_to_kill="deer"
        
class Zoo:
    animals_in_all_zoos=0
    def __init__(self):
        self._reserved_food_in_kgs=0
        self._animals=[]
        self._deer_count=0
        self._goldfish_count=0
    
    @property
    def deer_count(self):
        return self._deer_count
    
    @property
    def goldfish_count(self):
        return self._goldfish_count
        
    @property
    def animals(self):
        return self._animals
        
    @property
    def reserved_food_in_kgs(self):
        return self._reserved_food_in_kgs
    
    def add_food_to_reserve(self,food):
        self._reserved_food_in_kgs+=food
        
    def add_animal(self,animal):
        self._animals.append(animal)
        Zoo.animals_in_all_zoos+=1
        if(type(animal)==Deer):
            self._deer_count+=1
        if(type(animal)==GoldFish):
            self._goldfish_count+=1
        
    def feed(self,animal):
        if(self.reserved_food_in_kgs>=animal.required_food_in_kgs):
            self._reserved_food_in_kgs-=animal.required_food_in_kgs
            animal.grow()
            
    @classmethod
    def count_animals_in_all_zoos(cls):
        return (cls.animals_in_all_zoos)
        
    @staticmethod
    def count_animals_in_given_zoos(animal_list=[]):
        return sum([animal.count_animals() for animal in animal_list])
        
    def count_animals(self):
        return(len(self.animals))
        
    def kill(self,animal):
        if(animal=="deer"):
            if(self.deer_count>0):
                self._deer_count-=1
            else:
                print("No deers to hunt")
        if(animal=="goldfish"):
            if(self.goldfish_count>0):
                self._goldfish_count-=1
            else:
                print("No GoldFish to hunt")
        self._animals.pop()
        Zoo.animals_in_all_zoos-=1
        