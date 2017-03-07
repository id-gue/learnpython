def calc_area(length, width):
	if type(length) != int and type(length) != float:
		raise TypeError('length must be int or float')

	if type(width) != int and type(width) != float:
		raise TypeError('width must be int or float')

	if length <= 0:
		raise ValueError('lenght must be larger than 0')
	
	if width <= 0:
		raise ValueError('width must be larger than 0')

	return length * width