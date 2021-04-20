# Real Time Analysis Documentation

First of all the program needs a given CSV file with 13 columns containing :
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

### Table of Contents :
- [main.py](#mainpy)
- [data_line.py](#data_linepy)
	- [O3 Concentration](#O3Concentration-DataFrame-df-)
	- [CO2 Concentration](#CO2Concentration-DataFrame-df-)
- [methods.py](#methodspy)
- [plot_handler.py](#plot_handlerpy)


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

<p></br></p>

## plot_handler.py

