def absRange(num1, num2):
    if num1 > num2:
        return round(abs(num1 - num2), 2)
    else:
        return round(abs(num2 - num1), 2)

print(absRange(20.5, 16.8)) #should be rounded to 3.70
print(absRange(-25.9, 21.7)) #should be rounded to 47.60

#-------------------------------------------------------------------------------
import math

def cylinVolume(radius, height):
    volume = (math.pi) * (radius ** 2) * (height)
    return round(volume, 2)

print(cylinVolume(4,12)) #should evaluate to 603.19
print(cylinVolume(7,10)) #should evaluate to 1539.38

#-------------------------------------------------------------------------------

def semiPerimeter(x, y, z):
    length = x + y + z
    semi = length / 2
    return round(semi, 2)

print(semiPerimeter(5, 7, 9)) #should evaluate to 10.5
print(semiPerimeter(8, 10, 12)) #should evaluate to 15.0

#-------------------------------------------------------------------------------
import math

def heronFormula(a, b, c):
    s = semiPerimeter(a, b, c)
    inside = (s - a) * (s - b) * (s - c)
    A = math.sqrt(abs(s * inside))
    return round(A, 2)

    
print(heronFormula(5,7,9)) #should evaluate to 17.41
print(heronFormula(8,10,12)) #should evaluate to 39.69

#---------------------------------------------------------------------------

def triangleDiff(base1, height1, base2, height2):
    area1 = 0.5 * base1 * height1
    area2 = 0.5 * base2 * height2
    diff = area1 - area2
    return round(diff, 2)

print(triangleDiff(7, 8, 6, 5)) #should evaluate to 13.00.
print(triangleDiff(9, 11, 5, 7)) #should evaluate to 32.00.
    

    
