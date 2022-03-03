from matplotlib import projections
import numpy as np
import matplotlib.pyplot as plt

def sigmoid():
    x = np.linspace(-10, 10, 100)
    y = 1 / (1 + np.exp(-x))

    plt.plot(x, y, 'black', linewidth = 3)
    plt.xlim(-10, 10)
    plt.ylim(-1, 2)
    plt.grid(True)
    plt.show()

def softmax(x1, x2, x3):
    y = np.exp(x1) + np.exp(x2) + np.exp(x3)
    return np.exp(x1) / y, np.exp(x2) / y, np.exp(x3)

def softmax_test():
    x1 = np.linspace(-5, 5, 20)
    x2 = np.linspace(-5, 5, 20)
    # x3 = 1 로 고정

    y = np.zeros((20, 20, 3))
    for i in range(20):
        for j in range(20):
            y[i, j, :] = softmax(x1[i], x2[j], 1)
    
    m_x1, m_x2 = np.meshgrid(x1, x2)

    plt.figure(figsize=(8, 3))
    for i in range(2):
        ax = plt.subplot(1, 2, i+1, projection = '3d')
        ax.plot_surface(m_x1, m_x2, y[:, :, i], rstride = 1, cstride = 1, alpha= 0.3, color='blue', edgecolor='black')
        ax.set_xlabel('x1', fontsize=14)
        ax.set_ylabel('y1', fontsize = 14)
        ax.view_init(40, -125)
    
    plt.show()

def gauss(x, mu, sigma, a):
    return a * np.exp(-(x - mu)**2 / sigma ** 2)

def gauss_test():
    x = np.linspace(-4, 8, 100)

    plt.plot(x, gauss(x, 0, 1, 1), 'red', linewidth = 3, label = 'y=exp(-x^2)')
    plt.plot(x, gauss(x, 2, 3, 0.5), 'blue', linewidth= 3, label = 'y=0.5exp(-(x-2)^2 / 3^2)')
    plt.legend(loc = 'upper left')
    plt.xlim(-4, 8)
    plt.ylim(-0.5, 1.5)
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    # sigmoid()
    # softmax_test()
    gauss_test()