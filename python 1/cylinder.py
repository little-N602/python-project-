# Luis Nigoa
# PA 2
import math
radius = float(input())
height = float(input())
volume = math.pi*pow(radius,2)*height
surfacearea = (2*math.pi*radius*height) + (2*math.pi*pow(radius,2))
print("volume: {:1f}".format(volume))
print("surface area{:1f}".format(surfacearea))