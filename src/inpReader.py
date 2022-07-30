def readCoor(fileName):

	with open(fileName, 'r') as usrInp:
	    usrInpLine = usrInp.readlines()

# Define file type
	count = 0
	for char in range(len(fileName)):
		if fileName[char] == '.':
			count = char

	xyzCoor = []

# Read .pdb file
	if fileName[count+1:] == 'pdb':
		for usrInpLine_i in usrInpLine:
			if usrInpLine_i != '\n' and len(usrInpLine_i.split()) >= 6 and usrInpLine_i.count('.') == 3:
				xyzCoorEle = [usrInpLine_i.split()[2]]
				for usrInpLine_i_i in range(3, len(usrInpLine_i.split())):
					if '.' in usrInpLine_i.split()[usrInpLine_i_i]:
						xyzCoorEle.append(float(usrInpLine_i.split()[usrInpLine_i_i]))
				xyzCoor.append(xyzCoorEle)

# Read .xyz file
	elif fileName[count+1:] == 'xyz':
		for usrInpLine_i in usrInpLine:
			if usrInpLine_i != '\n' and len(usrInpLine_i.split()) == 4 and usrInpLine_i.count('.') == 3:
				xyzCoor.append([usrInpLine_i.split()[0], float(usrInpLine_i.split()[1]), \
					float(usrInpLine_i.split()[2]), float(usrInpLine_i.split()[3])])

# Read Gaussian input file (.gjf or .com)
	elif fileName[count+1:] == 'gjf' or fileName[count+1:] == 'com':
		for usrInpLine_i in usrInpLine:
			if usrInpLine_i != '\n' and len(usrInpLine_i.split()) >= 4 and usrInpLine_i.count('.') == 3:
				xyzCoorEle = []
				if len(usrInpLine_i.split()[0]) == 1 or len(usrInpLine_i.split()[0]) == 2:
					xyzCoorEle.append(usrInpLine_i.split()[0])
				elif usrInpLine_i.split()[0][1] == '(':
					xyzCoorEle.append(usrInpLine_i.split()[0][0])
				elif usrInpLine_i.split()[0][2] == '(':
					xyzCoorEle.append(usrInpLine_i.split()[0][:2])
				for usrInpLine_i_i in range(len(usrInpLine_i.split())):
					if '.' in usrInpLine_i.split()[usrInpLine_i_i]:
						xyzCoorEle.append(float(usrInpLine_i.split()[usrInpLine_i_i]))
				xyzCoor.append(xyzCoorEle)

	return xyzCoor
