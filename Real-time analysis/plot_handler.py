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
plt.style.use('seaborn')


dev_x = [25, 26, 27, 28]

dev_y = [1, 2, 3, 4]

colors=[300, 315, 270, 305]



plt.scatter(dev_x, dev_y, s=100, c=colors, cmap='Reds', edgecolor='k', linewidth=1, label = "sample variables")

cbar = plt.colorbar()
cbar.set_label('Temperature')

plt.title("Sample Plot")
plt.xlabel("x")
plt.ylabel("y")

plt.legend()

plt.tight_layout()

"""
#Για την center of mass ΜΟΝΟ:
t_start = 2
plt.fill_between(dev_x,dev_y, t_start, where = (dev_x > t_start), alpha = 0.25)
#Γιατί δεν λειτουργεί το where??
"""
#ERRORS
y_errormin = [0.1 , 0.2, 0.5, 0.1]
y_errormax = [0.2 , 0.4, 0.1, 0.9]
y_error = [y_errormin,y_errormax]

x_error= 0.5

plt.errorbar(dev_x,dev_y, yerr = y_error,
             xerr = x_error, fmt=' ',
             elinewidth=1, capsize=5,
             errorevery=1, capthick=1)

plt.show()
