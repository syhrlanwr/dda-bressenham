import matplotlib.pyplot as plt
import pandas as pd

def bressenham(x0, y0, x1, y1):
    x = x0
    y = y0
    dx = x1 - x0
    dy = y1 - y0
    p = 2 * dy - dx
    dict = {'p': [p], 'x': [x], 'y': [y]}
    while True:
        yield x, y
        if x == x1 and y == y1:
            break
        if p > 0:
            x += 1
            y += 1
            p += 2 * dy - 2 * dx
        else:
            x += 1
            p += 2 * dy
        dict['p'].append(p)
        dict['x'].append(x)
        dict['y'].append(y)
    df = pd.DataFrame(dict)
    print(df)

def main():
    x0 = 10
    y0 = 10
    x1 = 17
    y1 = 16
    x, y = zip(*bressenham(x0, y0, x1, y1))
    plt.title('Algoritma Bressenham')
    plt.plot(x, y)
    plt.show()

main()