from matplotlib import pyplot as plt


def flow_rate_plot(df):    
    flow_rate_figure, ax1 = plt.subplots()
    
    plt.style.use('seaborn')
    ax1.scatter(df['time'], df['Flowrate'], s=20, 
                marker= '.', label = "ECO-WISE 2021")
    
    ax1.set_title("Pump's flowrate")
    ax1.set_xlabel("Time (min)")
    ax1.set_ylabel("Flowrate (L/min)")
    ax1.legend()
    plt.tight_layout()
    
    return flow_rate_figure


def temp_press_out_plot(df):
    
    temp_press_out_figure, ax3 = plt.subplots()
    
    plt.style.use('seaborn')
    
    colors=df['T_out']
    
    plot = ax3.scatter(df['P_out'], df['Altitude'], s=20, c=colors, cmap='jet', 
                  label = "ECO-WISE 2021",marker= '.')
    temp_press_out_figure.colorbar(plot, ax=ax3,label = 'Temperature out (°C)')
    
    
    ax3.set_title("Environmental variables")
    ax3.set_xlabel("Pressure (mbar)")
    ax3.set_ylabel("Altitude (m)")
    ax3.legend()
    plt.tight_layout()
    
    #ERRORS
    
    p = 1/100 #ποσοστό σφάλματος στην πίεση
    
    y_errormin = p*df['P_out']
    y_errormax = p*df['P_out']
    y_error = [y_errormin,y_errormax]
    
    x_error= 0
    
    ax3.errorbar(df['P_out'], 
                 df['Altitude'], 
                 yerr = y_error,
                 xerr = x_error, 
                 fmt=' ',
                 elinewidth=1,
                 capsize=5,
                 errorevery=100, 
                 capthick=1)  #ERROR EVERY για να φαίνεται στο γράφημα


    return temp_press_out_figure

def humidity_plot(df):
    humidity_figure, (hum_in,hum_out) = plt.subplots(nrows=2, ncols=1, sharex=True)
    
    #hum_in.grid(linewidth= 0.5, linestyle= '--', color= '#262626', alpha= 0.2)
    #hum_out.grid(linewidth= 0.5, linestyle= '--', color= '#262626', alpha= 0.2)
    #plt.rcParams['axes.facecolor'] = '#ccccff'
    plt.style.use('seaborn')
    
    hum_in.plot(df['time'], df['Hum_in'], label = "Hum in (ECO-WISE 2021)")
    hum_out.plot(df['time'], df['Hum_out'], label = "Hum out (ECO-WISE 2021)")
    
    hum_in.set_title("Humidity")
    hum_in.set_ylabel("Humidity Inside (%)")  
    hum_in.legend()
    
    hum_out.set_xlabel("Time (min)")
    hum_out.set_ylabel("Humidity Outside (%)")   
    hum_out.legend()
    
    plt.tight_layout()
    
    return humidity_figure

def O3_conc(df):
    
    O3_conc_figure, ax5 = plt.subplots()
    
    plt.style.use('seaborn')
    #ax5.grid(linewidth= 0.5, linestyle= '--', color= '#262626', alpha= 0.2)
    #plt.rcParams['axes.facecolor'] = '#ccccff'
    ax5.scatter(df['Altitude'], df['O3_ppm'], s=20,marker= '.', 
                  label = "ECO-WISE 2021")
    
    ax5.set_title("O3 concentration")
    ax5.set_xlabel("O3 (ppb)")
    ax5.set_ylabel("Altitude (m)")
    ax5.legend()
    plt.tight_layout()
    
# =============================================================================
#     #ERRORS
#     p = 10/100 #error percentage in concentration
#     
#     y_errormin = df['flags']  #CHECK ERRORBARS BASED ON FLAGS (start-end of each circle)
#     y_errormax = df['flags']  #CHECK ERRORBARS BASED ON FLAGS (start-end of each circle)
#     y_error = [y_errormin,y_errormax]
#     
#     x_error= p*df['O3_ppm']
#     
#     ax5.errorbar(df['Altitude'], 
#                  df['O3_ppm'], 
#                  yerr = y_error,
#                  xerr = x_error, 
#                  fmt=' ',
#                  elinewidth=1,
#                  capsize=5,
#                  errorevery=100, 
#                  capthick=1)  #ERROR EVERY για να φαίνεται στο γράφημα
# =============================================================================

    return O3_conc_figure


def CO2_conc(df):
    
    CO2_conc_figure, ax6 = plt.subplots()
    
    plt.style.use('seaborn')
    ax6.scatter(df['Altitude'], df['CO2_C'], s=20, 
                marker= '.', label = "ECO-WISE 2021")
    
    ax6.set_title("CO2 concentration")
    ax6.set_xlabel("CO2 (v/v %)")
    ax6.set_ylabel("Altitude (m)")
    ax6.legend()
    plt.tight_layout()
    
# =============================================================================
#     #ERRORS
#     p = 10/100 #error percentage in concentration
#     
#     y_errormin = df['flags']  #CHECK ERRORBARS BASED ON FLAGS (start-end of each circle)
#     y_errormax = df['flags']  #CHECK ERRORBARS BASED ON FLAGS (start-end of each circle)
#     y_error = [y_errormin,y_errormax]
#     
#     x_error= p*df['CO2_C']
#     
#     ax6.errorbar(df['Altitude'], 
#                  df['CO2_C'], 
#                  yerr = y_error,
#                  xerr = x_error, 
#                  fmt=' ',
#                  elinewidth=1,
#                  capsize=5,
#                  errorevery=100, 
#                  capthick=1)  #ERROR EVERY για να φαίνεται στο γράφημα
# =============================================================================

    return CO2_conc_figure

def altitude_time(df):
    
    altitude_time_figure, ax7 = plt.subplots()
    
    colors=df['T_out']
    
    plt.style.use('seaborn')
    plot = ax7.scatter(df['time'], df['Altitude'], s=20, c=colors, cmap='jet', 
                marker= '.', label = "ECO-WISE 2021")
    
    altitude_time_figure.colorbar(plot, ax=ax7,label = 'Temperature out (°C)')
    
    ax7.set_title("Balloon altitude (Altitude Over Time)")
    ax7.set_xlabel("Time (min)")
    ax7.set_ylabel("Altitude (m)")
    ax7.legend()
    plt.tight_layout()
    
    return altitude_time_figure

def temp_press_in_plot(df):
    
    temp_press_in_figure, ax8 = plt.subplots()
    
    colors=df['T_in']
    
    plt.style.use('seaborn')
    plot = ax8.scatter(df['time'],df['P_in'], s=20, c=colors, cmap='jet', 
                marker= '.', label = "ECO-WISE 2021")
    
    temp_press_in_figure.colorbar(plot, ax=ax8,label = 'Temperature in (°C)')
    
    ax8.set_title("Sensor box variables")
    ax8.set_xlabel("Time (min)")
    ax8.set_ylabel("Pressure (mbar)")
    ax8.legend()
    plt.tight_layout()

    return temp_press_in_figure

def sample_plot():
    """ Sample"""
    plt.style.use('seaborn')
        
    dev_x = [25, 26, 27, 28]  
    dev_y = [1, 2, 3, 4]
    
    
    colors=[300, 315, 270, 305]
    
    plt.scatter(dev_x, dev_y, s=100, c=colors, cmap='Reds', edgecolor='k', linewidth=1, label = "sample variables")
    
    cbar = plt.colorbar()
    cbar.set_label('Temperature')
    
    plt.set_title("Sample Plot")
    plt.set_xlabel("x")
    plt.set_ylabel("y")
    
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