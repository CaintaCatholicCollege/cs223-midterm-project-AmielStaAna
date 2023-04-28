print('TEMPERATURE CONVERTER PROGRAM')
#Temperature Converter 
#StaAna Amiel Julius J.

# temperature conversion program from Celcius
celcius = float(input('Please input temperatur celcius : '))
print('Temperature celcius is :', celcius, '℃')

# celcius to other
ct_Fahrenheit = ((9/5) * celcius) + 32
print('Temperature from celcius to fahrenheit is :', ct_Fahrenheit, '°F')

ct_kelvin = celcius + 273.15
print('Temperature from celcius to kelvin is :', ct_kelvin, 'K')

ct_reamur = (4/5) * celcius
print('Temperature from celcius to reamur :', ct_reamur, 'R\n')


# temperature conversion program from Fahrenheit
Fahrenheit = float(input('Please input temperatur Fahrenheit : '))
print('Temperature Fahrenheit is :', Fahrenheit, '°F')

# Fahrenheit to other
ft_celcius = (Fahrenheit - 32) * 5/9
print('Temperature from Fahrenheit to celcius :', ft_celcius, '℃')

ft_kelvin = (Fahrenheit + 459.67) * 5/9
print('Temperature from Fahrenheit to kelvin :', ft_kelvin, 'K')

ft_reamur = 4/9 * (Fahrenheit - 32)
print('Temperature from Fahrenheit to reamur :', ft_reamur, 'R\n')


# temperature conversion program from Kelvin
kelvin = float(input('Please input temperatur kelvin : '))
print('Temperature kelvin is :', kelvin, 'K')

# Kelvin to other
kt_celcius = kelvin - 273.15
print('Temperature from kelvin to celcius :', kt_celcius, '℃')

kt_fahrenheit = (kelvin * 9/5) - 459.67
print('Temperature from kelvin to fahrenheit :', kt_fahrenheit, '°F')