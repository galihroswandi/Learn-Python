a = 1
b = "String 1"
c = 1.0
d = True

print("Nilai a bertipe = ", type(a))
print("Nilai b bertipe = ", type(b))
print("Nilai c bertipe = ", type(c))
print("Nilai c bertipe = ", type(d))

## type data khusus 

# type data kompleks 
aritMathics = complex(10, 3)

# type data dari bahasa c
from ctypes import c_double, c_char;

doubleValue = c_double(10.9)
charValue = c_char(b'A')

print("Nilai aritMathics bertipe = ", type(aritMathics))
print("Nilai doubleValue bertipe = ", type(doubleValue))
print("Nilai charValue bertipe = ", type(charValue))
