class Rep:
	S="'"; D='"'; E=';'; C=','
	G='''print "class Rep:"; print "	S="+Rep.D+Rep.S+Rep.D+Rep.E, "D="+Rep.S+Rep.D+Rep.S+Rep.E, "E="+Rep.S+Rep.E+Rep.S+Rep.E, "C="+Rep.S+Rep.C+Rep.S; print "	G="+Rep.S+Rep.S+Rep.S+Rep.G+Rep.S+Rep.S+Rep.S; print """	def __init__(self):
		"""+Rep.G; print "Rep()"'''
	def __init__(self):
		print "class Rep:"; print "	S="+Rep.D+Rep.S+Rep.D+Rep.E, "D="+Rep.S+Rep.D+Rep.S+Rep.E, "E="+Rep.S+Rep.E+Rep.S+Rep.E, "C="+Rep.S+Rep.C+Rep.S; print "	G="+Rep.S+Rep.S+Rep.S+Rep.G+Rep.S+Rep.S+Rep.S; print """	def __init__(self):
		"""+Rep.G; print "Rep()"
Rep()
