#!/usr/bin/env python

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

	db[name] = pwd

def olduser():
	name = raw_input('login:')
	pwd = raw_input('passwd:')
	passwd = db.get(name)
	if passwd == pwd:
		print 'welcome back', name