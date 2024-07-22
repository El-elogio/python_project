#A FUNCTION THAT COMPUTES THE VOLUME OF A SPHERE
def vol_calc():
    r = float(input("input the radius (r) of the sphere: "))
    pie = 3.142
    im = 1.333
    calc = im * pie * (r**3)
    return calc


vol = vol_calc()
print(vol)