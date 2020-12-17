from day13rw.AgeException import AgeException
from day13rw.rw1 import person

p=person()
p.setAge(10)
try:
    p.age()
except AgeException as e:
    print(e)