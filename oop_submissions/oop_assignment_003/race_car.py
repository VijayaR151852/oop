import math
from car import Car
class RaceCar(Car):
    horn="Peep Peep\nBeep Beep"
    def __init__(self,color=None,max_speed=0,acceleration=0,tyre_friction=0):
        super().__init__(color,max_speed,acceleration,tyre_friction)
        self._nitro=0

    @property
    def nitro(self):
        return self._nitro
        
    def apply_brakes(self):
        if(self._current_speed>=(self.max_speed//2)):
            self._nitro+=10
        super().apply_brakes()        
        
    def accelerate(self):
        nitro_boost=0
        if(self.is_engine_started==True and self._nitro>=10):
            nitro_boost=math.ceil(self._acceleration*0.3)
            self._nitro-=10
        self._current_speed+=nitro_boost
        super().accelerate()