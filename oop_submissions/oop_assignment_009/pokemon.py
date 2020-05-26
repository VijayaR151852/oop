class Pokemon:
    sound=""
    def __init__(self,name,level=1):
        if(name==""):
            raise ValueError("name cannot be empty")
        if(level<=0):
            raise ValueError("level should be > 0")
        self._name=name
        self._level=level
        self._master=None

    def setmaster(self,master):
        self._master=master
        
    @property
    def master(self):
        if(self._master==None):
            print("No Master")
        else:
            return (self._master)
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
        #super().attack(self)
        
class Zapdos(ElectricPokemon,FlyingPokemon):
    pokemon="Zapdos"
    sound="Zap...Zap"
    def attack(self):
        ElectricPokemon.attack(self)
        FlyingPokemon.attack(self)
        
class Island:
    all_islands=[]
    def __init__(self,name,max_no_of_pokemon,total_food_available_in_kgs):
        self._name=name
        self._max_no_of_pokemon=max_no_of_pokemon
        self._total_food_available_in_kgs=total_food_available_in_kgs
        self._pokemon_left_to_catch=0
        self._pokemon_list=[]
        Island.all_islands.append(self)
        
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
        
    def set_total_food_available_in_kgs(self,food):
        self._total_food_available_in_kgs=food
    
    def __str__(self):
        return f"{self.name} - {self.pokemon_left_to_catch} pokemon - {self.total_food_available_in_kgs} food"
    
    def add_pokemon(self,pokemon):
        if(self.pokemon_left_to_catch<self.max_no_of_pokemon):
            self.pokemon_list.append(pokemon)
            self._pokemon_left_to_catch+=1
        else:
            print("Island at its max pokemon capacity")
    
    @classmethod
    def get_all_islands(cls):
        return (cls.all_islands)
        
class Trainer:
    def __init__(self,name):
        self._name=name
        self._experience=100
        self._food_in_bag=0
        self._current_island=None
        self._pokemon_caught=[]
        
    @property
    def name(self):
        return self._name 
    @property
    def experience(self):
        return self._experience
    @property
    def food_in_bag(self):
        return self._food_in_bag
    @property
    def max_food_in_bag(self):
        return self._experience*10
    @property
    def pokemon_caught(self):
        return self._pokemon_caught
    @property
    def current_island(self):
        if(self._current_island==None):
            print("You are not on any island")
        else:
            return (self._current_island)
            
    def __str__(self):
        return f"{self.name}"
        
    def move_to_island(self,island):
        self._current_island=island
        
    def collect_food(self):
        if(self._current_island==None):
            print("Move to an island to collect food")
        else:
            if(self.current_island.total_food_available_in_kgs<=self.experience):
                self._food_in_bag=self.current_island.total_food_available_in_kgs
                self.current_island.set_total_food_available_in_kgs(0)
                
            elif(self._food_in_bag<self.max_food_in_bag):
                self._food_in_bag=self.max_food_in_bag
                remaining_food=self.current_island.total_food_available_in_kgs-self.max_food_in_bag
                self.current_island.set_total_food_available_in_kgs(remaining_food)
        
    def catch(self,pokemon):
        if(self._experience>=100*pokemon.level):
            self._experience+=pokemon.level*20
            self._pokemon_caught.append(pokemon)
            pokemon.setmaster(self)
            print("You caught {}".format(pokemon.name))
        else:
            print("You need more experience to catch {}".format(pokemon.name))
            
    def get_my_pokemon(self):
        return self._pokemon_caught
        
island1 =Island(name="Island1",max_no_of_pokemon=5,total_food_available_in_kgs=10000)
trainer=Trainer(name="Bot")
#trainer.move_to_island(island1)
trainer.current_island
#print(trainer.current_island==island1)