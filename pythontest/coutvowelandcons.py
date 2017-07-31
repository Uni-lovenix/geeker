def countvowelandcons(word):
	ret = [0,0]
	for w in word.upper():
		if ord(w) >= ord('A') and ord(w) <= ord('Z'):
			if w in 'AEIOU':
				print w
				ret[0]+=1
				continue
			ret[1]+=1
	return ret

def timu_9_2():
	f = open('solve.py')
	
def safe_open(filename, mode='r'):
	try:
		file = open(filename, mode)
		return file
	except KeyboardInterrupt,e:
		file.close()
		print e
	except:
		return None

# print countvowelandcons('sdfdsfdsfwerwaaa')

