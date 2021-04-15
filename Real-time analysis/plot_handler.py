from matplotlib import pyplot as plt
import pandas as pd


def flow_rate_plot(df):
    #flowrate-time or altitude
    plt.style.use('seaborn')
    
    plt.scatter(df['Time'], df['flow_rate'], s=10, 
                edgecolor='k', linewidth=0, label = "ECO-WISE 2021")
    
    plt.title("Pump's flowrate")
    plt.xlabel("Time (min)")
    plt.ylabel("Flowrate (V/min)")
    plt.legend()
    plt.tight_layout()
    
    plt.show()
    pass

#NOT going to happen
def concentrations_plot(CO2_C, O3_C, Altitude):
    #create a plot with different scaling left-right axis
    #return plot-subplot
    pass

def temp_press_out_plot(df):
    df = pd.read_excel('./Bexus 24.xls')
    #create a plot with different scaling left-right axis
    #return plot-subplot
    
    plt.style.use('seaborn')
    
    colors=df['Temp out']
    
    plt.scatter(df['Air press'], df['Altitude'], s=10, c=colors, cmap='Reds', 
                edgecolor='k', linewidth=0, label = "ECO-WISE 2021")
    
    cbar = plt.colorbar()
    cbar.set_label('Temperature out(°C)')
    
    plt.title("Environmental variables")
    plt.xlabel("Pressure (mbar)")
    plt.ylabel("Altitude (m)")
    plt.legend()
    plt.tight_layout()
    
    #ERRORS
    
    p = 10/100 #ποσοστό σφάλματος στην πίεση
    
    y_errormin = p*df['Air press']
    y_errormax = p*df['Air press']
    y_error = [y_errormin,y_errormax]
    
    x_error= 0
    
    plt.errorbar(df['Air press'], 
                 df['Altitude'], 
                 yerr = y_error,
                 xerr = x_error, 
                 fmt=' ',
                 elinewidth=1,
                 capsize=5,
                 errorevery=100, 
                 capthick=1)  #ERROR EVERY για να φαίνεται στο γράφημα

    plt.show()
    pass

def humidity_plot(df):
    #create a plot with different scaling left-right axis
    #return plot-subplot
    plt.style.use('seaborn')
    
    plt.plot(df['Time'], df['Hum_in'], label = "Hum in (ECO-WISE 2021)")
    plt.plot(df['Time'], df['Hum_out'], label = "Hum out (ECO-WISE 2021)")
    
    plt.title("Humidity")
    plt.xlabel("Time (min)")
    plt.ylabel("Humidity (%)")   #Distinction between y1 y2??
    plt.legend()
    plt.tight_layout()
    
    plt.show()
    pass

def centre_of_mass(Altitude, Concentration):
    #return plot-subplot
    pass

def O3_conc(df):
    plt.style.use('seaborn')
    
    plt.scatter(df['Altitude'], df['CO2_c'], s=10, 
                edgecolor='k', linewidth=0, label = "ECO-WISE 2021")
    
    plt.title("O3 concentration")
    plt.xlabel("O3 (ppb)")
    plt.ylabel("Altitude (m)")
    plt.legend()
    plt.tight_layout()
    
    #ERRORS
    p = 10/100 #error percentage in concentration
    
    y_errormin = df['flags']  #CHECK ERRORBARS BASED ON FLAGS (start-end of each circle)
    y_errormax = df['flags']  #CHECK ERRORBARS BASED ON FLAGS (start-end of each circle)
    y_error = [y_errormin,y_errormax]
    
    x_error= p*df['O3_c']
    
    plt.errorbar(df['Altitude'], 
                 df['O3_c'], 
                 yerr = y_error,
                 xerr = x_error, 
                 fmt=' ',
                 elinewidth=1,
                 capsize=5,
                 errorevery=100, 
                 capthick=1)  #ERROR EVERY για να φαίνεται στο γράφημα

    plt.show()
    pass


def CO2_conc(df):
    plt.style.use('seaborn')
    
    plt.scatter(df['Altitude'], df['CO2_c'], s=10, 
                edgecolor='k', linewidth=0, label = "ECO-WISE 2021")
    
    plt.title("CO2 concentration")
    plt.xlabel("CO2 (v/v %)")
    plt.ylabel("Altitude (m)")
    plt.legend()
    plt.tight_layout()
    
    #ERRORS
    p = 10/100 #error percentage in concentration
    
    y_errormin = df['flags']  #CHECK ERRORBARS BASED ON FLAGS (start-end of each circle)
    y_errormax = df['flags']  #CHECK ERRORBARS BASED ON FLAGS (start-end of each circle)
    y_error = [y_errormin,y_errormax]
    
    x_error= p*df['CO2_c']
    
    plt.errorbar(df['Altitude'], 
                 df['CO2_c'], 
                 yerr = y_error,
                 xerr = x_error, 
                 fmt=' ',
                 elinewidth=1,
                 capsize=5,
                 errorevery=100, 
                 capthick=1)  #ERROR EVERY για να φαίνεται στο γράφημα

    plt.show()
    pass

def altitude_time(df):
    
    plt.style.use('seaborn')
    
    colors=df['Temp out']
    
    plt.scatter(df['time'], df['Altitude'], s=10, c=colors, cmap='Reds', 
                edgecolor='k', linewidth=0, label = "ECO-WISE 2021")
    
    cbar = plt.colorbar()
    cbar.set_label('Temperature out(°C)')
    
    plt.title("Balloon altitude")
    plt.xlabel("Time (min)")
    plt.ylabel("Altitude (m)")
    plt.legend()
    plt.tight_layout()
    
    plt.show()
    pass

def temp_press_in_plot(df):
    plt.style.use('seaborn')
    
    colors=df['Temp in']
    
    plt.scatter(df['Sample press'], df['Time'], s=10, c=colors, cmap='Reds', 
                edgecolor='k', linewidth=0, label = "ECO-WISE 2021")
    
    cbar = plt.colorbar()
    cbar.set_label('Temperature in(°C)')
    
    plt.title("Sensor box variables")
    plt.xlabel("Pressure (mbar)")
    plt.ylabel("Time (min)")
    plt.legend()
    plt.tight_layout()
    
    plt.show()
    pass

def sample_plot():
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
    
    
# =============================================================================
#     Για την center of mass ΜΟΝΟ:
#     
#     t_start = 2
#     plt.fill_between(dev_x,dev_y, t_start, where = (dev_x > t_start), alpha = 0.25)
#
#     Γιατί δεν λειτουργεί το where??
# =============================================================================
    
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

# sample_plot()