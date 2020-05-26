from car import Car
class Truck(Car):
    horn="Honk Honk"
    def __init__(self,color=None,max_speed=0,acceleration=0,tyre_friction=0,max_cargo_weight=0):
        super().__init__(color,max_speed,acceleration,tyre_friction)
        if(max_cargo_weight<0):
            raise ValueError("Invalid value for max_cargo_weight")
        self._max_cargo_weight=max_cargo_weight
        self._load=0
            
    @property
    def max_cargo_weight(self):
        return self._max_cargo_weight
        
    def load(self,cargo_weight):
        if(cargo_weight<0):
            raise ValueError("Invalid value for cargo_weight")
        if(self._current_speed==0):
            if(self._load+cargo_weight<=self._max_cargo_weight):
                self._load+=cargo_weight
            else:
                print("Cannot load cargo more than max limit: {}".format(self._max_cargo_weight))
        else:
            print("Cannot load cargo during motion")
                
    def unload(self,cargo_weight):
        if(cargo_weight<0):
            raise ValueError("Invalid value for cargo_weight")
        if(self._current_speed==0):
            self._load-=cargo_weight
        else:
            print("Cannot unload cargo during motion")
            
            