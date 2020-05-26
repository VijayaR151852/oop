class Pokemon:
    sound=""
    def __init__(self,name,level=1):
        if(name==""):
            raise ValueError("name cannot be empty")
        if(level<=0):
            raise ValueError("level should be > 0")
        self._name=name
        self._level=level
    
    @property
    def name(self):
        return self._name
    
    @property
    def level(self):
        return self._level
        
    @classmethod
    def make_sound(cls):
        print(cls.sound)
    
    def __str__(self):
        return (f"{self.name} - Level {self.level}")

class ElectricPokemon(Pokemon):
    def attack(self):
        print(f"Electric attack with {10*self.level} damage")
    
class WaterPokemon(Pokemon):
    pokemon=""
    def attack(self):
        print(f"Water attack with {9*self.level} damage")
    @classmethod
    def swim(cls):
        print(f"{cls.pokemon} swimming...")
        
class FlyingPokemon(Pokemon):
    pokemon=""
    def attack(self):
        print(f"Air attack with {5*self.level} damage")
    @classmethod
    def fly(cls):
        print(f"{cls.pokemon} flying...")
    
class RunningPokemon:
    pokemon=""
    @classmethod
    def run(cls):
        print(f"{cls.pokemon} running...")
        
class Pikachu(ElectricPokemon,RunningPokemon):
    sound="Pika Pika"
    pokemon="Pikachu"
    
class Squirtle(WaterPokemon,RunningPokemon):
    pokemon="Squirtle"
    sound="Squirtle...Squirtle"
    
class Pidgey(FlyingPokemon):
    pokemon="Pidgey"
    sound="Pidgey...Pidgey"
    
class Swanna(WaterPokemon,FlyingPokemon):
    pokemon="Swanna"
    sound="Swanna...Swanna"
    def attack(self):
        WaterPokemon.attack(self)
        FlyingPokemon.attack(self)
    
class Zapdos(ElectricPokemon,FlyingPokemon):
    pokemon="Zapdos"
    sound="Zap...Zap"
    def attack(self):
        ElectricPokemon.attack(self)
        FlyingPokemon.attack(self)
        
class Island:
    def __init__(self,name,max_no_of_pokemon,total_food_available_in_kgs):
        self._name=name
        self._max_no_of_pokemon=max_no_of_pokemon
        self._total_food_available_in_kgs=total_food_available_in_kgs
        self._pokemon_left_to_catch=0
        self._pokemon_list=[]
        
    @property
    def name(self):
        return self._name
    
    @property
    def max_no_of_pokemon(self):
        return self._max_no_of_pokemon
        
    @property
    def total_food_available_in_kgs(self):
        return self._total_food_available_in_kgs
    
    @property
    def pokemon_left_to_catch(self):
        return self._pokemon_left_to_catch
        
    @property
    def pokemon_list(self):
        return self._pokemon_list
    
    def __str__(self):
        return f"{self.name} - {self.pokemon_left_to_catch} pokemon - {self.total_food_available_in_kgs} food"
    
    def add_pokemon(self,pokemon):
        if(self.pokemon_left_to_catch<self.max_no_of_pokemon):
            self.pokemon_list.append(pokemon)
            self._pokemon_left_to_catch+=1
        else:
            print("Island at its max pokemon capacity")
            
class Trainer:
    def __init__(self,name):
        self._name=name
        self.        
    @property
    def name(self):
        return self._name 
'''my_swanna = Swanna(name="Misty")
print(my_swanna.name)
print(my_swanna.level)
print(my_swanna)
my_swanna.make_sound()
my_swanna.fly()  
my_swanna.swim() 
my_swanna.attack()'''