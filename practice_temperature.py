#check if user is using Celsius or Fahrenheit
unit = input('What unit are you using?')
if unit == 'C':
	temp_c = input('Temperature')
	temp_c = float(temp_c)
	temp_f = temp_c * 9 / 5 + 32
	print (temp_f, 'F')

if unit == 'F':
	temp_f = input('Temperature')
	temp_f = float(temp_f)
	temp_c = (temp_f - 32) * 5 / 9
	print (temp_c, 'C')