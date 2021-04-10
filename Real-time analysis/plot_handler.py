from matplotlib import pyplot as plt

def flow_rate_plot(flowrate, Altitude):
    #flowrate-time or altitude
    pass

def concentrations_plot(CO2_C, O3_C, Altitude):
    #create a plot with different scaling left-right axis
    #return plot-subplot
    pass

def temp_and_press_plot(df):
    #create a plot with different scaling left-right axis
    #return plot-subplot
    pass

def humidity_plot(Hum_in, Hum_out, Altitude):
    #create a plot with different scaling left-right axis
    #return plot-subplot
    pass

def centre_of_mass(Altitude, Concentration):
    #return plot-subplot
    pass


# =============================================================================
# import matplotlib
# 
# 
# παιρνει δεδομένα απο την main
# 
# return plt
# =============================================================================


""" Sample"""

from intertools import count
from matplotlib.animation import FuncAnimation
import random

plt.style.use('seaborn')


dev_x = [25, 26, 27, 28]

dev_y = [1, 2, 3, 4]

plt.plot(dev_x, dev_y, marker = 'o', label = "sample variables")

plt.title("Sample Plot")
plt.xlabel("x")
plt.ylabel("y")

plt.legend()

plt.tight_layout()


#Για την center of mass ΜΟΝΟ:
t_start = 2
plt.fill_between(dev_x,dev_y, t_start, where = (dev_x > t_start), alpha = 0.25)
#Γιατί δεν λειτουργεί το where??

#Δεν είναι αναγκαία η count
index=count()
x_vals = []
y_vals = []

def animate (i):
    x_vals.append(next(index))
    y_vals.append(random.randint(0,5))
    
    plt.cla()
    plt.plot(x_vals, y_vals)
    
ani = FuncAnimation(plt.gcf(), animate, interval = 1000)

    





plt.show()
