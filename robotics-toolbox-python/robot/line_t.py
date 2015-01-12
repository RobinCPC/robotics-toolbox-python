# -*- coding: utf-8 -*-
"""
Created on Mon Jan 12 10:45:58 2015

@author: USER
"""
#from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d.axes3d

def line_t(name_d1 = 'x', data1 = [], name_d2 = 'y', data2 = [], name_d3 = 'z', data3 = [], *arguments):
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d')
    axw = ax.plot_wireframe(data1, data2, data3)
    ax.set_xlabel(name_d1)
    ax.set_ylabel(name_d2)
    ax.set_zlabel(name_d3)
    for a in range(len(arguments)/2):
        if arguments[2*a] == 'LineWidth':
            #plt.setp(axw, arguments[2*a], arguments[2*a+1])
            axw.set_linewidth(arguments[2*a+1])
        if arguments[2*a] == 'color':
            axw.set_color(arguments[2*a+1])
    plt.show()

line_t('xdata', [1, 2, 3], 'ydata',[6,4,3], 'zdata',[4,6,20], 'LineWidth', 4, 'color', 'red')

#def text_t(pos_x = 0, pos_y = 0, s = ' ', *arguments):
#    import matplotlib.pyplot as plt