#!/usr/bin/python

import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy import var
from scipy import mean
from scipy import std
from scipy import sqrt

def errorCurve(data, color):
    _data = abs(data.copy())
    _data.sort()
    
    y_values = np.ones(_data.size)
    y_values = y_values / _data.size      
    y_values = np.cumsum(y_values)
    
    x_values = _data
        
    plt.plot(x_values, y_values, color = color, linewidth = 2)

def main():
    print 'Number of arguments:', len(sys.argv), 'arguments.'
    print 'Argument List:', str(sys.argv)
    
    data  = np.genfromtxt("/home/amndan/dev/bobby_ws/src/carmen_publisher/benchmarks/09/sorted2ndTsTrans.errors.raw", dtype=None, delimiter=';') #pdf
    data2 = np.genfromtxt("/home/amndan/dev/bobby_ws/src/carmen_publisher/benchmarks/11/sorted2ndTsTrans.errors.raw", dtype=None, delimiter=';') #icp
    
    data[:,0] = sqrt(data[:,1]**2 + data[:,2]**2)
    data2[:,0] = sqrt(data2[:,1]**2 + data2[:,2]**2)
    
    i = 1
    data2 = data2[:,i]
    data = data[:,i]
    
    plt.rcParams.update({'font.size': 16})
    
    print std(data)
    print var(data)
    print mean(data)
    
    size = max(abs(min(data)), abs(max(data)))
    
    size = 0.6 * size
    
    x_axis = np.arange(-size, size, 0.001)
    ax = plt.gca()
    ax.set_xlim(-size, size)
    ax.set_title('Distribution of Error')
    ax.set_xlabel('error [m]')
    ax.set_ylabel('probability density [a.u.]')
    line, = plt.plot(x_axis, norm.pdf(x_axis,mean(data),std(data)))
    line.set_linewidth(5)
    line.set_linestyle('--')
    line.set_color('r')
    
    plt.figure(1)
    
    plt.hist(data,normed=1, bins=101, color='b') #this is the histogram 
    
    plt.figure(2)
    
    errorCurve(data, 'r')
    errorCurve(data2, 'b')
    
    ax = plt.gca()
    ax.set_xlim(0, 0.2)
    ax.set_ylim(0, 1)
    #ax.set_xscale('log')
    #ax.set_yscale('log')
    #ax.set_title('Distribution of Error')
    #ax.set_xlabel('error boundary [m]')
    #ax.set_ylabel('measurements [%]')
    ax.grid()
    
    plt.show()
    plt.close()

if __name__ == "__main__":
    main()
