def fibonacci_calculator(_value, option):
	
	def _get_nth_value(_value):
		a, b = 0, 1
		fib_values = [a]
		while len(fib_values) <= _value:
			a, b = b, b + a
			fib_values.append(a)

		return float(a)

	def _get_sequence_less_than(_value):
		a, b = 0, 1
		fib_values = [a]
		while a < _value:
			a, b = b, b + a
			if a < _value:
				fib_values.append(a)

		return fib_values

	def _get_sequence_length(_value):
		a, b = 0, 1
		fib_values = [a]
		while len(fib_values) <= _value:
			a, b = b, b + a
			fib_values.append(a)

		return fib_values

	options = {'nth-value': _get_nth_value(_value),
	           'less-than': _get_sequence_less_than(_value),
	           'sequence-of-length': _get_sequence_length(_value)}

	try:
		_return = options[option]
	except KeyError, e:
		_return = e
	else:
		return _return


n = 100
print fibonacci_calculator(n, 'nth-value')
print fibonacci_calculator(n, 'less-than')
print fibonacci_calculator(n, 'sequence-of-length')