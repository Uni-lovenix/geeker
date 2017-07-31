
def a(b):
	print 'a'

def b(c):
	print 'b'

@a
@b
def t():
	print n
	return 1
	

if __name__ == '__main__':
	t()