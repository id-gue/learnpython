def calc_area(length, width):
	size = length * width

	if type(length) is str or type(width) is str:
		raise TypeError('Please use numbers instead of letters.')
	elif size < 0:
		raise ValueError('Please use positive numbers.')
	elif size == 0:
		raise NameError('Please use numbers bigger than 0.')
	elif size > 0:
		return size