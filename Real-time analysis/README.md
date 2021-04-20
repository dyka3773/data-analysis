# Real Time Analysis Documentation

### Table of Contents :
- [main.py](#mainpy)
- [data_line.py](#data_linepy)
	- [O3 Concentration](#O3Concentration-DataFrame-df-)
	- [CO2 Concentration](#CO2Concentration-DataFrame-df-)
- [methods.py](#methodspy)
	- [Flowrate](#flowrate-DataFrame-df-)
	- [Centre of Mass](#centre_of_mass-DataFrame-df-)
- [plot_handler.py](#plot_handlerpy)
	- [Flowrate Plot](#flow_rate_plot-DataFrame-df-)
	- [Pressure-Altitude-Temperature Outside The Gondola Plot](#temp_press_out_plot-DataFrame-df-)
	- [Humidity Plot](#humidity_plot-DataFrame-df-)
	- [O3 Concentration Plot](#O3_conc-DataFrame-df-)
	- [CO2 Concentration Plot](#CO2_conc-DataFrame-df-)
	- [Altitude-Time Plot](#altitude_time-DataFrame-df-)
	- [Pressure-Altitude-Temperature Inside The Gondola Plot](#temp_press_in_plot-DataFrame-df-)

## Clarifications

First of all, this program will be run in another program's GUI so everything you see will be implemented in a larger program

Τhe program, also, needs a given CSV file with 13 columns containing :
1. Time - which is declared as `time` inside the program
2. Pressure In - which is declared as `P_in` inside the program
3. Pressure In - which is declared as `P_in` inside the program
4. Pressure Out - which is declared as `P_out` inside the program
5. Temperature In - which is declared as `T_in` inside the program
6. Temperature Out - which is declared as `T_out` inside the program
7. Humidity Out - which is declared as `Hum_in` inside the program
8. Humidity In - which is declared as `Hum_out` inside the program
9. Carbon Dioxide Volume 1 - which is declared as `CO2_V1` inside the program
10. Carbon Dioxide Volume 2 - which is declared as `CO2_V2` inside the program
11. Ozone WE - which is declared as `O3_WE` inside the program
12. Ozone AE - which is declared as `O3_AE` inside the program
13. Flags **???** - which is declare as `flags` inside the program

## main.py
This module contains the `main` function and it's where the program has to be started

### `main()`
#### *Description*
This function opens a CSV file as a pandas' DataFrame. Sets its default columns to the above mentioned variable names, then creates new columns :
- `O3_ppm` using [O3 Concentration](#O3Concentration-DataFrame-df-) from the [data_line.py](#data_linepy) module
- `CO2_%v/v` using [CO2 Concentration](#CO2Concentration-DataFrame-df-) from the [data_line.py](#data_linepy) module
- `Flowrate` using [Flowrate](#flowrate-df-) from the [methods.py](#methodspy) module

After that, it passes the proper parameters in each of the plot functions of the [plot_handler.py](#plot_handlerpy) module and gets them returned into plot variables ready to be plotted in the GUI designed by _ECOWISE's Software Team_

#### *Parameters*
`None`

#### *Returns*
The plots that will be called in it

<p></br></p>

## data_line.py
This module contains functions to apply on each row of a given DataFrame.


### `O3Concentration( DataFrame df )`
#### *Description*
Calculates the O3 Concentration at any given time

#### *Parameters*
df - A DataFrame object with columns `OE_WE`, `O3_AE` and `T_in`

#### *Returns*
The O3 Concentration

<p></br></p>

### `CO2Concentration( DataFrame df )`
#### *Description*
Calculates the CO2 Concentration at any given time

#### *Parameters*
df - A DataFrame object with columns `CO2_V1`, `CO2_V2` and `T_in`

#### *Returns*
The CO2 Concentration

<p></br></p>

## methods.py
This module contains functions that are more general to the dataset or use the whole dataset in order to produce a result

### `flowrate( DataFrame df )`
#### *Description*
Calculates the flow rate of the pump at any given timeframe

#### *Parameters*
df - A DataFrame object with columns `time`, `P_in`, `P_out`, `T_in` and `T_out`

#### *Returns*
A `pd.Series` object where `dtype='float64'` and each row contains the flow rate at each moment

<p></br></p>

### `centre_of_mass( DataFrame df )`
#### *Description*
Calculates the centre of mass ???

#### *Parameters*
df - A DataFrame object with every column of the CSV + the ones we made in `main`.
*`Flowrate` has to be calculated before*

#### *Returns*
`h_cm` ???

<p></br></p>

## plot_handler.py
This module contains functions that will return `pyplot.subplot` objects and each function is dedicated to certain plots only.

### `flow_rate_plot( DataFrame df )`
#### *Description*
Plots how the flowrate changes over time

#### *Parameters*
df - A DataFrame object with columns `time`and `Flowrate`

#### *Returns*
`pyplot.subplot` object with the plot ready to be projected (`subplot.show()`)

<p></br></p>

### `temp_press_out_plot( DataFrame df )`
#### *Description*
Plots a graph with the pressure outside the gondola and altitude as its axes while also the color of each point in the plot changes according to the outside temperature. There are also errorbars showing what the divergence of the measurments can be.

#### *Parameters*
df - A DataFrame object with columns `T_out`, `Altitude` and `P_out`

#### *Returns*
`pyplot.subplot` object with the plot ready to be projected (`subplot.show()`)

<p></br></p>

### `humidity_plot( DataFrame df )`
#### *Description*
Plots humidity inside the gondola and humidity outside the gondola as the time passes to project the difference they can have

#### *Parameters*
df - A DataFrame object with columns `Hum_in`, `Hum_out` and `time`

#### *Returns*
`pyplot.subplot` object with the plot ready to be projected (`subplot.show()`)

<p></br></p>

### `O3_conc( DataFrame df )`
#### *Description*
Plots how the O3 Concentration changes over Altitude

#### *Parameters*
df - A DataFrame object with columns `Altitude`, `O3_ppm` and `flags`

#### *Returns*
`pyplot.subplot` object with the plot ready to be projected (`subplot.show()`)

<p></br></p>

### `CO2_conc( DataFrame df )`
#### *Description*
Plots how the CO2 Concentration changes over Altitude

#### *Parameters*
df - A DataFrame object with columns `Altitude`, `CO2_%v/v` and `flags`

#### *Returns*
`pyplot.subplot` object with the plot ready to be projected (`subplot.show()`)

<p></br></p>

### `altitude_time( DataFrame df )`
#### *Description*
Plots how the Temperature outside the gondola changes as the Altitude and Time change

#### *Parameters*
df - A DataFrame object with columns `Altitude`, `time` and `T_out`

#### *Returns*
`pyplot.subplot` object with the plot ready to be projected (`subplot.show()`)

<p></br></p>

### `temp_press_in_plot( DataFrame df )`
#### *Description*
Plots how the Temperature inside the gondola changes as the Pressure inside and Time change

#### *Parameters*
df - A DataFrame object with columns `time`, `T_in` and `P_in`

#### *Returns*
`pyplot.subplot` object with the plot ready to be projected (`subplot.show()`)

<p></br></p>
