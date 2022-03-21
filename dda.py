import matplotlib.pyplot as plt
import pandas as pd

def dda(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    step = max(abs(dx), abs(dy))
    x_inc = dx / step
    y_inc = dy / step
    x = x0
    y = y0
    dict = {'x': [x], 'y': [y], 'round(x)': [x], 'round(y)': [y]}
    for i in range(step):
        yield round(x), round(y)
        x += x_inc
        y += y_inc
        dict['x'].append(x)
        dict['y'].append(y)
        dict['round(x)'].append(round(x))
        dict['round(y)'].append(round(y))
    df = pd.DataFrame(dict)
    print(df)

def main():
    x0 = 10
    y0 = 10
    x1 = 17
    y1 = 16
    x, y = zip(*dda(x0, y0, x1, y1))
    plt.title('Algoritma DDA')
    plt.plot(x, y)
    plt.show()

main()