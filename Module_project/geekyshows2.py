#main file for first and second module name

import first
import second

print(first.a)
first.name()

print(second.b)
second.name()

print()
# agar is tarah import kare to
from first import a, name

print(a)
name()

