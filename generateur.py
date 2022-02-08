import numpy
import matplotlib.pyplot as afficheur

p = 20 
bruit = numpy.zeros(shape=(p + 1, p + 1, 2))
intensité_perlin = 12
xperlin = (
    intensité_perlin * p
) 
bruit_perlin = numpy.zeros(
    shape=(xperlin, xperlin)
) 


for a in range(p + 1):
    for b in range(p + 1):
        x = numpy.random.normal()  
        y = numpy.random.normal() 

        
        normal = (x ** 2 + y ** 2) ** 0.5
        x /= normal
        y /= normal

        bruit[a, b, 0] = x
        bruit[a, b, 1] = y


def grille(gx, gy, x, y):
    grille_x = x - gx
    grille_y = y - gy
    return (
        grille_x * bruit[gx, gy, 0] + grille_y * bruit[gx, gy, 1]
    )  


def diffusion(d0, d1, w):  
    return d0 + w * (d1 - d0)


def perlin(h, j):
    x0 = int(h)
    y0 = int(j)
    x1 = x0 + 1
    y1 = y0 + 1
    lx = h - x0
    ly = j - y0
    a0 = grille(x0, y0, h, j)
    a1 = grille(x1, y0, h, j)
    ax0 = diffusion(a0, a1, lx)
    a0 = grille(x0, y1, h, j)
    a1 = grille(x1, y1, h, j)
    ax1 = diffusion(a0, a1, lx)

    return diffusion(ax0, ax1, ly)


for x in range(xperlin): 
    for y in range(xperlin):
        bruit_perlin[x, y] = perlin(
            x / intensité_perlin, y / intensité_perlin
        ) 
bruit_de_perlin, axes = afficheur.subplots()
axes.imshow(
    bruit_perlin, cmap="binary"
)
afficheur.show() 
