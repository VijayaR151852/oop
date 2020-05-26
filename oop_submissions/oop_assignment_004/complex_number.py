import math
class ComplexNumber:
    def __init__(self,real=0,imaginary=0):
        if(isinstance(real,str)) and type(imaginary)!=str:
            raise ValueError("Invalid value for real part")
        if(isinstance(imaginary,str)) and type(real)!=str:
            raise ValueError("Invalid value for imaginary part")
        if(isinstance(real,str) and isinstance(imaginary,str)):
            raise ValueError("Invalid value for real and imaginary part")
        self.real_part=real
        self.imaginary_part=imaginary
        
    def __str__(self):
        return f"{self.real_part}{self.imaginary_part:+}i"
    
    def conjugate(self): 
        temp_imaginary_part=-(self.imaginary_part)
        return ComplexNumber(self.real_part,temp_imaginary_part)
    
    def __add__(self,other):
        temp_real_part=self.real_part+other.real_part
        temp_imaginary_part=self.imaginary_part+other.imaginary_part
        return ComplexNumber(temp_real_part,temp_imaginary_part)
    
    def __sub__(self,other):
        temp_real_part=self.real_part-other.real_part
        temp_imaginary_part=self.imaginary_part-other.imaginary_part
        return ComplexNumber(temp_real_part,temp_imaginary_part)
        
    def __mul__(self,other):
        self_real_part=self.real_part*other.real_part
        self_imaginary_part=self.imaginary_part*other.imaginary_part
        other_real_part=self.real_part*other.imaginary_part
        other_imaginary_part=self.imaginary_part*other.real_part
        temp_real_part=round((self_real_part-self_imaginary_part),2)
        temp_imaginary_part=round((other_real_part+other_imaginary_part),2)
        return ComplexNumber(temp_real_part,temp_imaginary_part)
        
    def __abs__(self):
        return round(math.sqrt((self.real_part)**2+(self.imaginary_part)**2),3)
    
    def __truediv__(self,other):
        absolute_value=abs(other)
        self_real_part,self_imaginary_part=self.real_part/absolute_value,self.imaginary_part/absolute_value 
        other_real_part,other_imaginary_part=other.real_part/absolute_value,-(other.imaginary_part/absolute_value)
        temp_real_part=ComplexNumber(self_real_part,self_imaginary_part)
        temp_imaginary_part=ComplexNumber(other_real_part,other_imaginary_part)
        return temp_real_part*temp_imaginary_part
        
    def __eq__(self,other):
        return (self.real_part==other.real_part and self.imaginary_part==other.imaginary_part)
