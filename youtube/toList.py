#!/usr/bin/python3

def toList(self):
    '''
		This function tackes a object called data which really is a
		stream object
	'''
	l=[]
	data = str(data)	# Now data is a String
	data =data.split()	# Now data is a list of String
	for da in data:
		if da=="<Stream:":
			pass
		else:
			m=[]
			d=da.split('=')
			if d[0]=='mime_type':
				m.append(d[0])
				n=[]
				o=d[1].split('"')[1]
				o=o.split('/')
				for each in o:56
					n.append(each)
				m.append(n)
			else:
				m.append(d[0])
				m.append(d[1].split('"')[1])

			l.append(m)

	return l
