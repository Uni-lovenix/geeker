def safe_input():
	try:
		input_str = raw_input('>>> ')
	except StandardError:
		return None
	except SystemExit:
		return None
	return input_str

if __name__ == '__main__':
	while True:
		input_str = safe_input()
		print input_str
		if input_str == 'quit':
			break