#!/usr/bin/env python
import time

db = {}

def newuser():
	prompt = 'login desired:'
	while True:
		name = raw_input(prompt)
		if db.has_key(name):
			prompt = 'name taken, try another:'
			continue
		else:
			break

	pwd = raw_input('passwd:')
	logintime = time.time()

	db[name] = [pwd,logintime]

def olduser():
	name = raw_input('login:')
	pwd = raw_input('passwd:')
	passwd = db.get(name)[0]
	lastlogintime = db.get(name)[1]
	curtime = time.time()
	if passwd == pwd:
		if curtime-lastlogintime < 14400:
			print 'You already logged in at: %s' % \
			time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(lastlogintime))
			return
		print 'welcome back', name
		db[name][1] = time.time()
	else:
		print 'login incorrect'

def deleteuser():
	name = raw_input('delete user name:')
	if db.has_key(name):
		del db[name]
		print 'deleted user:%s' % name
	else:
		print 'Don\'t has name:%s' % name

def allusershow():
	for k in db:
		print k, db[k][0]

def showmenu():
	prompt = """
(N)ew
(E)xisting User Login
(D)elete a user
(S)how all users
(Q)uit
Enter choice:"""

	done = False

	while not done:
		try:
			choice = raw_input(prompt).strip()[0].lower()
		except (EOFError, KeyboardInterrupt):
			choice = 'q'
		print '\nYou picked:[%s]' % choice
		if choice not in 'nedsq':
			print 'invailid option, try again'
		else:
			True

		if choice == 'q':done = True
		if choice == 'n':newuser()
		if choice == 'e':olduser()
		if choice == 'd':deleteuser()
		if choice == 's':allusershow()

if __name__ == '__main__':
	showmenu()