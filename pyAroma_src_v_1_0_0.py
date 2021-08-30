# MIT License

# Copyright (c) 2021 Zhe Wang

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import platform
import random
import matplotlib.pyplot as plt
import numpy as np

def elementDetermin (userInputted2):
	calcAtom2 = userInputted2[:]
	calcAtom2.append(userInputted2[0])
	userElements =[]
	for j in range(len(calcAtom2)):
		userElements.append(element[int(calcAtom2[j]) - 1])
	return userElements

def calcHOMA (userInputted, elementList):
	calcAtom = userInputted[:]
	calcAtom.append(userInputted[0])
	disMatrix = []
	for i in range(len(userInputted)):
		disABx = float(xCoors[int(calcAtom[i]) - 1]) - float(xCoors[int(calcAtom[i + 1]) - 1])
		disABy = float(yCoors[int(calcAtom[i]) - 1]) - float(yCoors[int(calcAtom[i + 1]) - 1])
		disABz = float(zCoors[int(calcAtom[i]) - 1]) - float(zCoors[int(calcAtom[i + 1]) - 1])
		disAB = pow(disABx * disABx + disABy * disABy + disABz * disABz, 0.5)
		disMatrix.append(format(disAB, '.3f'))
	sumDiff = 0.0000
	for j in range(len(disMatrix)):
		if elementList[j] == 'C' and elementList[j + 1] == 'C':
			Ropt = 1.388
			alpha = 257.7
		elif elementList[j] == 'C' and elementList[j + 1] == 'N':
			Ropt = 1.334
			alpha = 93.52
		elif elementList[j] == 'N' and elementList[j + 1] == 'C':
			Ropt = 1.334
			alpha = 93.52
		elif elementList[j] == 'C' and elementList[j + 1] == 'O':
			Ropt = 1.265
			alpha = 157.38
		elif elementList[j] == 'O' and elementList[j + 1] == 'C':
			Ropt = 1.265
			alpha = 157.38
		elif elementList[j] == 'C' and elementList[j + 1] == 'P':
			Ropt = 1.698
			alpha = 118.91
		elif elementList[j] == 'P' and elementList[j + 1] == 'C':
			Ropt = 1.698
			alpha = 118.91
		elif elementList[j] == 'C' and elementList[j + 1] == 'S':
			Ropt = 1.677
			alpha = 94.09
		elif elementList[j] == 'S' and elementList[j + 1] == 'C':
			Ropt = 1.677
			alpha = 94.09
		elif elementList[j] == 'N' and elementList[j + 1] == 'N':
			Ropt = 1.309
			alpha = 130.33
		elif elementList[j] == 'N' and elementList[j + 1] == 'O':
			Ropt = 1.248
			alpha = 57.21
		elif elementList[j] == 'O' and elementList[j + 1] == 'N':
			Ropt = 1.248
			alpha = 57.21
		diffRoptRi = (float(disMatrix[j]) - Ropt) * (float(disMatrix[j]) - Ropt) * alpha
		sumDiff += diffRoptRi
	valueHOMA = 1 - sumDiff / float(len(disMatrix))
	return valueHOMA

def elementNo (element):
	eleNumber = 6.000000
	periodTable = ['Bq', 'H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', \
					'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', \
					'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', \
					'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Ym', 'Yb', 'Lu', 'Ha', 'Ta', \
					'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', \
					'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', \
					'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og']
	eleNumber = periodTable.index(element)
	return eleNumber

# Program version
proVer = '1.0'
rlsDate = '2021-08-29'

# Platform determination
osVer = platform.system()

# Program information section
print("*******************************************************************************")
print("*                                                                             *")
print("*                               p y . A r o m a                               *")
print("*                                                                             *")
#print(f"*     =================== Version {proVer} for Source Code ===================     *")

if osVer == 'Darwin':
	print(f"*     ====================== Version {proVer} for macOS ======================     *")
elif osVer == 'Windows':
	print(f"*     ================ Version {proVer} for Microsoft Windows ================     *")
else:
	print(f"*     ====================== Version {proVer} for Linux ======================     *")

print(f"*                          Release date: {rlsDate}                           *")
print("*                                                                             *")
print("*      Aromaticity analysis tool, developed by Zhe Wang. Online document      *")
print("*    is available from GitHub (https://github.com/wongzit/pyAroma).           *")
print("*                                                                             *")
print("*                             -- Catch me with --                             *")
print("*                         E-mail  wongzit@yahoo.co.jp                         *")
print("*                       Homepage  https://wongzit.github.io                   *")
print("*                                                                             *")
print("*******************************************************************************")
print("\nPRESS Ctrl+c to exit the program.\n")

# Input file specification
print("Gaussian input/output file: support .gjf/.com/.log/.out")
if osVer == 'Windows':
	fileName = input("(e.g.: C:\\pyAroma\\examples\\benzene.gjf)\n")
	if fileName.strip()[0] == '\'' and fileName.strip()[-1] == '\'':
		fileName = fileName.strip()[1:-1]
	else:
		fileName = fileName.strip()
else:
	fileName = input("(e.g.: /pyAroma/examples/benzene.gjf)\n")
	if fileName.strip()[0] == '\"' and fileName.strip()[-1] == '\"':
		fileName = fileName.strip()[1:-1]
	else:
		fileName = fileName.strip()

# Check file type
if fileName[-3:] == 'gjf' or fileName[-3:] == 'com':
	fileType = 'inp'
elif fileName[-3:] == 'log' or fileName[-3:] == 'out':
	fileType = 'out'
else:
	usrFileTypeFlag = 1
	while usrFileTypeFlag:
		print("\nCould not determine the file type, please specify:")
		print("   1 - Gaussian input file")
		print("   2 - Gaussian output file.")
		usrFileType = input("Please input 1 or 2 and press ENTER: ")
		if usrFileType == '1':
			fileType = 'inp'
			usrFileTypeFlag = 0
		elif usrFileType == '2':
			fileType = 'out'
			usrFileTypeFlag = 0
		else:
			print("Input error, please input again.")

# Read from user input file
if fileType == 'inp':
	print("\nGaussian input file detected.\n")
	with open(fileName, 'r') as usrInpFile:
		gauInp = usrInpFile.readlines()
elif fileType == 'out' and '_3DICSS_' not in fileName:
	print("\nGaussian output file detected.\n")
elif fileType == 'out' and '_3DICSS_' in fileName:
	print("\n3D-ICSS calculation output detected. For process 3D-ICSS data, please select\nfunction 3 (3D-ICSS map).\n")

# Choose functions
if fileType == 'inp':
	print("Please select calculation type:")
	print("  1 - NICS(n)\n  2 - 2D-ICSS map\n  3 - 3D-ICSS map")
	usrFunc = input("Input menu number and press ENTER: ")
else:
	print("Please select calculation type:")
	print("  1 - HOMA\n  2 - 2D-ICSS map\n  3 - 3D-ICSS map")
	usrFunc = input("Input menu number and press ENTER: ")

# ICSSgen part
if fileType == 'inp' and usrFunc == '2':
	plane = input("\nPlease specify the plane for ICSS map (XY, XZ, YZ):\n")
	plane = plane.lower()
	while plane != 'xy' and plane != 'xz' and plane != 'yz':
	    print("\nInput error, please input again.\n")
	    plane = input("Please specify the plane for ICSS map (XY, XZ, YZ):\n")
	    plane = plane.lower()

	if plane == 'xy':
	    planeFlag = 1
	elif plane == 'xz':
	    planeFlag = 2
	else:
	    planeFlag = 3

	while True:
	    try:
	        altitude = float(input("\nPlease input the altitude over the plane (in angstrom):\n"))
	        break
	    except ValueError:
	        print("\nInput error, please input a number!")
	        continue

	if planeFlag == 1:
	    z = altitude
	    while True:
	        try:
	            x_min, x_max = input("\nPlease specify the range of X axis (in angstrom, e.g., -10 10):\n").split()
	            x_min = float(x_min)
	            x_max = float(x_max)
	            break
	        except ValueError:
	            print("\nInput error, please input 2 numbers:")
	            continue
	    while True:
	        try:
	            y_min, y_max = input("\nPlease specify the range of Y axis (in angstrom, e.g., -8 8):\n").split()
	            y_min = float(y_min)
	            y_max = float(y_max)
	            break
	        except ValueError:
	            print("\nInput error, please input 2 numbers!")
	            continue
	    print(f"\n2D-ICSS({plane.upper()},{altitude}) map in [X: {x_min} to {x_max}, Y: {y_min} to {y_max}].\n")
	elif planeFlag == 2:
	    y = altitude
	    while True:
	        try:
	            x_min, x_max = input("\nPlease specify the range of X axis (in angstrom, e.g., -10 10):\n").split()
	            x_min = float(x_min)
	            x_max = float(x_max)
	            break
	        except ValueError:
	            print("\nInput error, please input 2 numbers!")
	            continue
	    while True:
	        try:
	            z_min, z_max = input("\nPlease specify the range of Z axis (in angstrom, e.g., -8 8):\n").split()
	            z_min = float(z_min)
	            z_max = float(z_max)
	            break
	        except ValueError:
	            print("\nInput error, please input 2 numbers!")
	            continue
	    print(f"\n2D-ICSS({plane.upper()},{altitude}) map in [X: {x_min} to {x_max}, Z: {z_min} to {z_max}].\n")
	else:
	    x = altitude
	    while True:
	        try:
	            y_min, y_max = input("\nPlease specify the range of Y axis (in angstrom, e.g., -10 10):\n").split()
	            y_min = float(y_min)
	            y_max = float(y_max)
	            break
	        except ValueError:
	            print("\nInput error, please input 2 numbers:")
	            continue
	    while True:
	        try:
	            z_min, z_max = input("\nPlease specify the range of Z axis (in angstrom, e.g., -8 8):\n").split()
	            z_min = float(z_min)
	            z_max = float(z_max)
	            break
	        except ValueError:
	            print("\nInput error, please input 2 numbers:")
	            continue
	    print(f"\n2D-ICSS({plane.upper()},{altitude}) map in [Y: {y_min} to {y_max}, Z: {z_min} to {z_max}].\n")

	print("Please specify the grid quality (value smaller than 0.25 is recommended):")
	userGrid = input("(press Enter to use default value 0.2)\n")
	if userGrid:
	    grid = float(userGrid)
	    if grid < 0:
	    	grid = 0 - grid
	    elif grid == 0:
	    	print("Input error, default grid value 0.2 will be used.\n")
	    	grid = 0.2
	else:
	    grid = 0.2
	print(f"A grid quality of {grid} will be used.\n")

	routeLine = []
	coordinatesLine = []
	chargeSpin = ''

	for line in gauInp:
	    if line[0] == '%':
	        routeLine.append(line)
	    elif line[0] == '#':
	        if 'geom=connectivity' in line.lower():
	            routeLine.append(line)
	        else:
	            routeLine.append(f"{line.rstrip()} geom=connectivity\n")
	    elif len(line.split()) == 2 and len(''.join(line.rstrip())) < 6:
	        chargeSpin = line
	    elif ( line[0].isalpha or line[1].isalpha ) and line.count('.') == 3:
	        coordinatesLine.append(f"{line.rstrip()}\n")

	icssInput = open(f"{fileName.strip()[:-4]}_ICSS_{plane.upper()}_{int(altitude)}.gjf", "w")

	for route in routeLine:
	    icssInput.write(route)

	icssInput.write(f"\n{fileName.strip()[:-4]}_ICSS_{plane.upper()}_{int(altitude)}//Created_by_py.Aroma\n\n")
	icssInput.write(chargeSpin)

	for i in range(len(coordinatesLine)):
	    icssInput.write(coordinatesLine[i])

	if planeFlag == 1:
	    x_position = x_min
	    bqFlag = 0     # Total Bq atom: 10*(max-min)+1
	    while x_position <= (x_max + 0.5 * grid):
	        y_position = y_min
	        while y_position <= (y_max + 0.5 * grid):
	            icssInput.write(f" Bq      {round(x_position, 2)}      {round(y_position, 2)}      {round(z, 2)}\n")
	            bqFlag += 1
	            y_position += grid
	        x_position += grid
	    for bqNumber in list(range(1, bqFlag + len(coordinatesLine) + 1)):
	        icssInput.write(f"\n{bqNumber}")
	elif planeFlag == 2:
	    x_position = x_min
	    bqFlag = 0
	    while x_position <= (x_max + 0.5 * grid):
	        z_position = z_min
	        while z_position <= (z_max + 0.5 * grid):
	            icssInput.write(f" Bq      {round(x_position, 2)}      {round(y, 2)}      {round(z_position, 2)}\n")
	            bqFlag += 1
	            z_position += grid
	        x_position += grid
	    for bqNumber in list(range(1, bqFlag + len(coordinatesLine) + 1)):
	        icssInput.write(f"\n{bqNumber}")
	else:
	    y_position = y_min
	    bqFlag = 0
	    while y_position <= (y_max + 0.5 * grid):
	        z_position = z_min
	        while z_position <= (z_max + 0.5 * grid):
	            icssInput.write(f" Bq      {round(x, 2)}      {round(y_position, 2)}      {round(z_position, 2)}\n")
	            bqFlag += 1
	            z_position += grid
	        y_position += grid
	    for bqNumber in list(range(1, bqFlag + len(coordinatesLine) + 1)):
	        icssInput.write(f"\n{bqNumber}")

	totalAtom = bqFlag + len(coordinatesLine)
	icssInput.write("\n\n")
	icssInput.close()

	print("\n*******************************************************************************")
	print("")
	if totalAtom > 8000:
	    print("                          ------ W A R N I N G ------")
	    print(f"   Total number of atoms ({totalAtom}) in this input file exceed the limitation")
	    print("  of Gaussian (8000), the calculation could not be normal terminated. Please ")
	    print("  try: (1) separate into more input files; (2) use larger grid quality ")
	    print("  value; or (3) decrease the plotting region.")
	    print("")
	print("                     Input file is successfully generated.")
	print("                        Normal termination of py.Aroma.")
	print("")
	print("*******************************************************************************\n")

# ICSSgen3D part
elif fileType == 'inp' and usrFunc == '3':
	while True:
	    try:
	        x_min, x_max = input("\nPlease specify the range of X axis (in angstrom, e.g., -10 10):\n").split()
	        x_min = float(x_min)
	        x_max = float(x_max)
	        break
	    except ValueError:
	        print("\nInput error, please input 2 numbers:")
	        continue
	while True:
	    try:
	        y_min, y_max = input("\nPlease specify the range of Y axis (in angstrom, e.g., -8 8):\n").split()
	        y_min = float(y_min)
	        y_max = float(y_max)
	        break
	    except ValueError:
	        print("\nInput error, please input 2 numbers!")
	        continue
	while True:
	    try:
	        z_min, z_max = input("\nPlease specify the range of Z axis (in angstrom, e.g., -8 8):\n").split()
	        z_min = float(z_min)
	        z_max = float(z_max)
	        break
	    except ValueError:
	        print("\nInput error, please input 2 numbers!")
	        continue
	print(f"\n3D-ICSS map in [X: {x_min} to {x_max}, Y: {y_min} to {y_max}, Z: {z_min} to {z_max}].\n")
	print("Please specify the grid quality (value smaller than 0.25 is recommended):")
	userGrid = input("(press Enter to use default value 0.2)\n")
	if userGrid:
	    grid = float(userGrid)
	    if grid < 0:
	    	grid = 0 - grid
	    elif grid == 0:
	    	print("Input error, default grid value 0.2 will be used.\n")
	    	grid = 0.2
	else:
	    grid = 0.2
	print(f"A grid quality of {grid} will be used.\n")

	allBqCoors = []
	oneBqCoor =[]
	x_position = x_min
	while x_position <= (x_max + 0.5 * grid):
	    y_position = y_min
	    while y_position <= (y_max + 0.5 * grid):
	        z_position = z_min
	        while z_position <= (z_max + 0.5 * grid):
	            oneBqCoor = [format(x_position, '.6f'), format(y_position, '.6f'), format(z_position, '.6f')]
	            allBqCoors.append(oneBqCoor)
	            oneBqCoor = []
	            z_position += grid
	        y_position += grid
	    x_position += grid

	routeLine = []
	coordinatesLine = []
	chargeSpin = ''

	for line in gauInp:
	    if line[0] == '%':
	        routeLine.append(line)
	    elif line[0] == '#':
	        if 'geom=connectivity' in line.lower():
	            routeLine.append(line)
	        else:
	            routeLine.append(f"{line.rstrip()} geom=connectivity\n")
	    elif len(line.split()) == 2 and len(''.join(line.rstrip())) < 6:
	        chargeSpin = line
	    elif ( line[0].isalpha or line[1].isalpha ) and line.count('.') == 3:
	        coordinatesLine.append(f"{line.rstrip()}\n")

	fileNumbers = 1
	if len(allBqCoors) <= 7000 - len(coordinatesLine):
	    fileNumbers = 1
	elif len(allBqCoors) % 7000 == 0:
	    fileNumbers = int(len(allBqCoors) / 7000)
	else:
	    fileNumbers = int(len(allBqCoors) / 7000 + 1)
	icssInput = open(f"{fileName.strip()[:-4]}_3DICSS_0001.gjf", "w")
	for route in routeLine:
	    icssInput.write(route)
	icssInput.write(f"\n{fileName.strip()[:-4]}_3DICSS//Created_by_py.Aroma\n\n")
	icssInput.write(chargeSpin)
	for coorLine in coordinatesLine:
	    icssInput.write(coorLine)
	if fileNumbers == 1:
	    for i in range(len(allBqCoors)):
	        icssInput.write(f" Bq      {allBqCoors[i][0]}      {allBqCoors[i][1]}      {allBqCoors[i][2]}\n")
	    for bqNumber1 in list(range(1, len(coordinatesLine) + len(allBqCoors) + 1)):
	        icssInput.write(f"\n{bqNumber1}")
	else:
	    bqCounter1 = 0
	    for i in range(7000):
	        icssInput.write(f" Bq      {allBqCoors[i][0]}      {allBqCoors[i][1]}      {allBqCoors[i][2]}\n")
	        bqCounter1 += 1
	    for bqNumber1 in list(range(7000 + len(coordinatesLine))):
	        icssInput.write(f"\n{bqNumber1 + 1}")

	icssInput.write("\n\n")
	print(f"{fileName.strip()[:-4]}_3DICSS_0001.gjf has been saved.")
	icssInput.close()
	routeLine[-1] = f"{routeLine[-1].rstrip()} guess=read\n"
	if fileNumbers > 1:
	    for fileNumber in range(2, fileNumbers + 1):
	        fileNameNumber = '%04d' % fileNumber
	        icssInput = open(f"{fileName.strip()[:-4]}_3DICSS_{fileNameNumber}.gjf", "w")
	        for route in routeLine:
	            icssInput.write(route)

	        icssInput.write(f"\n{fileName.strip()[:-4]}_3DICSS//Created_by_py.Aroma\n\n")
	        icssInput.write(chargeSpin)
	        for coorLine in coordinatesLine:
	            icssInput.write(coorLine)
	        bqCounter2 = 0
	        while (bqCounter2 < 7000) and bqCounter1 < len(allBqCoors):
	            icssInput.write(f" Bq      {allBqCoors[bqCounter1][0]}      {allBqCoors[bqCounter1][1]}      {allBqCoors[bqCounter1][2]}\n")
	            bqCounter1 += 1
	            bqCounter2 += 1
	        for bqNumber2 in list(range(1, len(coordinatesLine) + bqCounter2 + 1)):
	            icssInput.write(f"\n{bqNumber2}")
	        icssInput.write("\n\n")
	        print(f"{fileName.strip()[:-4]}_3DICSS_{fileNameNumber}.gjf has been saved.")
	        icssInput.close()

	print("\n*******************************************************************************")
	print("")
	print("                    Input files are successfully generated.")
	print("                       Normal termination of py.Aroma.")
	print("")
	print("*******************************************************************************\n")

# NICSgen part
elif fileType == 'inp' and usrFunc == '1':
	continueFlag = 'y'
	routeLine = []
	coordinatesLine = []
	chargeSpin = ''
	for line in gauInp:
	    if line[0] == '%':
	        routeLine.append(line)
	    elif line[0] == '#':
	        routeLine.append(line)
	    elif len(line.split()) == 2 and len(''.join(line.rstrip())) < 6:
	        chargeSpin = line
	    elif ( line[0].isalpha or line[1].isalpha ) and line.count('.') == 3:
	        coordinatesLine.append(f"{line.rstrip()}\n")

	nicsInput = open(f"{fileName.strip()[:-4]}_NICS.gjf", "w")
	for route in routeLine:
	    nicsInput.write(route)
	nicsInput.write(f"\nNICSinput//Created_by_NICSgen\n\n")
	nicsInput.write(chargeSpin)

	for i in range(len(coordinatesLine)):
	    nicsInput.write(coordinatesLine[i])

	while continueFlag == 'y':
	    userX = []
	    userY = []
	    userZ = []
	    userAtomsInput = input("\nPlease specify the target atoms number:\n")
	    userAtomsNumber = []
	    userAltitudeInput = input("\nPlease specify the altitude n of NICS(n):\n")
	    userAltitude = float(userAltitudeInput)
	    for userAtomInput in userAtomsInput.split():
	    	userAtomsNumber.append(int(userAtomInput))
	    for userAtomNumber in userAtomsNumber:
	    	userX.append(float(coordinatesLine[userAtomNumber - 1].split()[1]))
	    	userY.append(float(coordinatesLine[userAtomNumber - 1].split()[2]))
	    	userZ.append(float(coordinatesLine[userAtomNumber - 1].split()[3]))

	    allX = 0.0000000
	    allY = 0.0000000
	    allZ = 0.0000000

	    for x in userX:
	    	allX += x
	    for y in userY:
	    	allY += y
	    for z in userZ:
	    	allZ += z

	    bqZeroCenterX = allX / float(len(userAtomsNumber))
	    bqZeroCenterY = allY / float(len(userAtomsNumber))
	    bqZeroCenterZ = allZ / float(len(userAtomsNumber))

	    if userAltitude == 0.00000:
	        nicsInput.write(f" Bq                 {'{:11f}'.format(bqZeroCenterX)}    {'{:11f}'.format(bqZeroCenterY)}    {'{:11f}'.format(bqZeroCenterZ)}\n")

	    if userAltitude != 0.00000:
	        para_a = (userY[1] - userY[0]) * (userZ[2] - userZ[0]) - (userY[2] - userY[0]) * (userZ[1] - userZ[0])
	        para_b = (userZ[1] - userZ[0]) * (userX[2] - userX[0]) - (userZ[2] - userZ[0]) * (userX[1] - userX[0])
	        para_c = (userX[1] - userX[0]) * (userY[2] - userY[0]) - (userX[2] - userX[0]) * (userY[1] - userY[0])
	        if para_a != 0.00000000:
	            para_A3 = 1 + para_b * para_b / para_a / para_a + para_c * para_c / para_a / para_a
	            para_B3 = - 2 * bqZeroCenterX - 2 * para_b * para_b * bqZeroCenterX / para_a / para_a - 2 * para_c * para_c * bqZeroCenterX / para_a / para_a
	            para_C3 = bqZeroCenterX * bqZeroCenterX + para_b * para_b * bqZeroCenterX * bqZeroCenterX / para_a / para_a + para_c * para_c * bqZeroCenterX * bqZeroCenterX / para_a / para_a - userAltitude * userAltitude
	            deltaValue = para_B3 * para_B3 - 4 * para_A3 * para_C3
	            if deltaValue != 0:
	                bqN1X = (- para_B3 + pow(deltaValue, 1.0/2)) / 2 / para_A3
	                bqN2X = (- para_B3 - pow(deltaValue, 1.0/2)) / 2 / para_A3
	                bqN1Y = para_b / para_a * (bqN1X - bqZeroCenterX) + bqZeroCenterY
	                bqN2Y = para_b / para_a * (bqN2X - bqZeroCenterX) + bqZeroCenterY
	                bqN1Z = para_c / para_a * (bqN1X - bqZeroCenterX) + bqZeroCenterZ
	                bqN2Z = para_c / para_a * (bqN2X - bqZeroCenterX) + bqZeroCenterZ
	                nicsInput.write(f" Bq                 {'{:11f}'.format(bqN1X)}    {'{:11f}'.format(bqN1Y)}    {'{:11f}'.format(bqN1Z)}\n")
	                nicsInput.write(f" Bq                 {'{:11f}'.format(bqN2X)}    {'{:11f}'.format(bqN2Y)}    {'{:11f}'.format(bqN2Z)}\n")
	            else:
	                bqNX = - para_B3 / 2 / para_A3
	                bqNY = para_b / para_a * (bqNX - bqZeroCenterX) + bqZeroCenterY
	                bqNZ = para_c / para_a * (bqNX - bqZeroCenterX) + bqZeroCenterZ
	                nicsInput.write(f" Bq                 {'{:11f}'.format(bqNX)}    {'{:11f}'.format(bqNY)}    {'{:11f}'.format(bqNZ)}\n")
	        elif userX[0] == userX[1] and userX[1] == userX[2]:
	        	nicsInput.write(f" Bq                 {userAltitude}    {'{:11f}'.format(bqZeroCenterY)}    {'{:11f}'.format(bqZeroCenterZ)}\n")
	        	nicsInput.write(f" Bq                 {- userAltitude}    {'{:11f}'.format(bqZeroCenterY)}    {'{:11f}'.format(bqZeroCenterZ)}\n")
	        elif userY[0] == userY[1] and userY[1] == userY[2]:
	        	nicsInput.write(f" Bq                 {'{:11f}'.format(bqZeroCenterX)}    {userAltitude}    {'{:11f}'.format(bqZeroCenterZ)}\n")
	        	nicsInput.write(f" Bq                 {'{:11f}'.format(bqZeroCenterX)}    {- userAltitude}    {'{:11f}'.format(bqZeroCenterZ)}\n")
	        elif userZ[0] == userZ[1] and userZ[1] == userZ[2]:
	        	nicsInput.write(f" Bq                 {'{:11f}'.format(bqZeroCenterX)}    {'{:11f}'.format(bqZeroCenterY)}    {userAltitude}\n")
	        	nicsInput.write(f" Bq                 {'{:11f}'.format(bqZeroCenterX)}    {'{:11f}'.format(bqZeroCenterY)}    {- userAltitude}\n")
	    continueFlag = input("\nContinue to add other Bq atoms? (y/n):\n")

	nicsInput.write("\n\n")
	nicsInput.close()

	print("\n*******************************************************************************")
	print("")
	print("                     Input file is successfully generated.")
	print("                        Normal termination of py.Aroma.")
	print("")
	print("*******************************************************************************\n")

# ICSScsv part
elif fileType == 'out' and usrFunc == '2':
	with open(fileName, 'r') as usrOutFile:
		gauOut = usrOutFile.readlines()

	coorBq = []
	shielTensor = []
	for outputLine in gauOut:
		if ' Bq    ' in outputLine and outputLine.count('.') == 3:
			coorBq.append(outputLine.rstrip())
		elif 'Isotropic =' in outputLine:
			shielTensor.append(outputLine.rstrip())
		elif ('XX=  ' in outputLine) and ('YX=  ' in outputLine) and ('ZX=  ' in outputLine):
			shielTensor.append(outputLine.rstrip())
		elif ('XY=  ' in outputLine) and ('YY=  ' in outputLine) and ('ZY=  ' in outputLine):
			shielTensor.append(outputLine.rstrip())
		elif ('XZ=  ' in outputLine) and ('YZ=  ' in outputLine) and ('ZZ=  ' in outputLine):
			shielTensor.append(outputLine.rstrip())
	x_all = []
	y_all = []
	z_all = []

	for atomNum in range(len(coorBq)):
		x_all.append(float(coorBq[atomNum].split()[1]))
		y_all.append(float(coorBq[atomNum].split()[2]))
		z_all.append(float(coorBq[atomNum].split()[3]))
	x_set = sorted(set(x_all))
	y_set = sorted(set(y_all))
	z_set = sorted(set(z_all))
	x_max, x_min = max(x_set), min(x_set)
	y_max, y_min = max(y_set), min(y_set)
	z_max, z_min = max(z_set), min(z_set)

	planeFlag = 0
	if len(x_set) == 1:
		planeFlag = 3
		y_step = y_set[1] - y_set[0]
		z_step = z_set[1] - z_set[0]
		print(f"\n2D-ICSS will be mapped on YZ plane in Y[{y_min} {y_max}, {round(y_step, 2)}], Z[{z_min} {z_max}, {round(z_step, 2)}].\n")
	elif len(y_set) == 1:
		planeFlag = 2
		x_step = x_set[1] - x_set[0]
		z_step = z_set[1] - z_set[0]
		print(f"\n2D-ICSS will be mapped on XZ plane in X[{x_min} {x_max}, {round(x_step, 2)}], Z[{z_min} {z_max}, {round(z_step, 2)}].\n")
	elif len(z_set) == 1:
		planeFlag = 1
		x_step = x_set[1] - x_set[0]
		y_step = y_set[1] - y_set[0]
		print(f"\n2D-ICSS will be mapped on XY plane in X[{x_min} {x_max}, {round(x_step, 2)}], Y[{y_min} {y_max}, {round(y_step, 2)}].\n")

	totalNum = int(len(shielTensor) / 4)
	tarMolNum = int(totalNum - len(coorBq))

	isotropicValue = []
	for isotropicLine in shielTensor:
		if 'Isotropic =' in isotropicLine:
			isotropicValue.append(- float(isotropicLine.split()[4]))
	del isotropicValue[:tarMolNum]

	anisotropyValue = []
	for anisotropyLine in shielTensor:
		if 'Anisotropy =' in anisotropyLine:
			anisotropyValue.append(- float(anisotropyLine.split()[7]))
	del anisotropyValue[:tarMolNum]

	xxValue = []
	yxValue = []
	zxValue = []
	for xxLine in shielTensor:
		if 'XX=' in xxLine:
			xxValue.append(- float(xxLine.split()[1]))
			yxValue.append(- float(xxLine.split()[3]))
			zxValue.append(- float(xxLine.split()[5]))

	del xxValue[:tarMolNum]
	del yxValue[:tarMolNum]
	del zxValue[:tarMolNum]

	xyValue = []
	yyValue = []
	zyValue = []
	for yyLine in shielTensor:
		if 'YY=' in yyLine:
			xyValue.append(- float(yyLine.split()[1]))
			yyValue.append(- float(yyLine.split()[3]))
			zyValue.append(- float(yyLine.split()[5]))

	del xyValue[:tarMolNum]
	del yyValue[:tarMolNum]
	del zyValue[:tarMolNum]

	xzValue = []
	yzValue = []
	zzValue = []
	for zzLine in shielTensor:
		if 'ZZ=' in zzLine:
			xzValue.append(- float(zzLine.split()[1]))
			yzValue.append(- float(zzLine.split()[3]))
			zzValue.append(- float(zzLine.split()[5]))

	del xzValue[:tarMolNum]
	del yzValue[:tarMolNum]
	del zzValue[:tarMolNum]

	print("Choose shielding tensor for ICSS map:")
	print("      1 - Isoptropic       2 - Anisotropy")
	print("      3 - XX component     4 - YX component     5 - ZX component")
	print("      6 - XY component     7 - YY component     8 - ZY component")
	print("      9 - XZ component    10 - YZ component    11 - ZZ component")
	nicsTensor = input('Please input the No.: ')
	tensorType = ''

	if nicsTensor == '1':
		mapValue = isotropicValue
		tensorType = 'iso'
	elif nicsTensor == '2':
		mapValue = anisotropyValue
		tensorType = 'ani'
	elif nicsTensor == '3':
		mapValue = xxValue
		tensorType = 'xx'
	elif nicsTensor == '4':
		mapValue = yxValue
		tensorType = 'yx'
	elif nicsTensor == '5':
		mapValue = zxValue
		tensorType = 'zx'
	elif nicsTensor == '6':
		mapValue = xyValue
		tensorType = 'xy'
	elif nicsTensor == '7':
		mapValue = yyValue
		tensorType = 'yy'
	elif nicsTensor == '8':
		mapValue = zyValue
		tensorType = 'zy'
	elif nicsTensor == '9':
		mapValue = xzValue
		tensorType = 'xz'
	elif nicsTensor == '10':
		mapValue = yzValue
		tensorType = 'yz'
	elif nicsTensor == '11':
		mapValue = zzValue
		tensorType = 'zz'

	icssOutput = open(f"{fileName.strip()[:-4]}_ICSS_output_{tensorType}.csv", 'w')

	icssOutput.write(f"# Data from {fileName.strip()}.\n")
	icssOutput.write(f"# Shielding tensor data from {tensorType.upper()} component.\n")
	icssOutput.write("# Processed with py.Aroma.\n")
	icssOutput.write("# Author: Zhe Wang\n")
	icssOutput.write("# Homepage: https://wongzit.github.io\n\n\n")

	if planeFlag == 1:
		icssOutput.write("XY,")
		for x_axis in x_set:
			icssOutput.write(f"{x_axis},")
		icssOutput.write("\n")
		y_count = 0
		for n_y in range(len(y_set)):
			if y_count < len(y_set):
				icssOutput.write(f"{y_set[y_count]},")
			for n_x in range(len(x_set)):
				icssOutput.write(f"{mapValue[n_y + len(y_set) * n_x]},")
			y_count += 1
			icssOutput.write("\n")

	elif planeFlag == 2:
		icssOutput.write("XZ,")
		for x_axis in x_set:
			icssOutput.write(f"{x_axis},")
		icssOutput.write("\n")
		z_count = 0
		for n_z in range(len(z_set)):
			if z_count < len(z_set):
				icssOutput.write(f"{z_set[z_count]},")
			for n_x in range(len(x_set)):
				icssOutput.write(f"{mapValue[n_z + len(z_set) * n_x]},")
			z_count += 1
			icssOutput.write("\n")

	elif planeFlag == 3:
		icssOutput.write("YZ,")
		for y_axis in y_set:
			icssOutput.write(f"{y_axis},")
		icssOutput.write("\n")
		z_count = 0
		for n_z in range(len(z_set)):
			if z_count < len(z_set):
				icssOutput.write(f"{z_set[z_count]},")
			for n_y in range(len(y_set)):
				icssOutput.write(f"{mapValue[n_z + len(z_set) * n_y]},")
			z_count += 1
			icssOutput.write("\n")

	icssOutput.close()
	icssArray = []

	if planeFlag == 1:
		for n_y2 in range(len(y_set)):
			icssArrayLine = []
			for n_x2 in range(len(x_set)):
				icssArrayLine.append(mapValue[n_y2 + len(y_set) * n_x2])
			icssArray.append(icssArrayLine)
		X, Y = np.meshgrid(x_set,y_set)
		iCss = np.array(icssArray)
		fig, ax = plt.subplots()
		icssFig = ax.pcolormesh(X, Y, iCss, shading='gouraud')
		fig.colorbar(icssFig)
		plt.xlabel("X (Angstrom)")
		plt.ylabel("Y (Angstrom)")
	elif planeFlag == 2:
		for n_z2 in range(len(z_set)):
			icssArrayLine = []
			for n_x2 in range(len(x_set)):
				icssArrayLine.append(mapValue[n_z2 + len(z_set) * n_x2])
			icssArray.append(icssArrayLine)
		X, Z = np.meshgrid(x_set,z_set)
		iCss = np.array(icssArray)
		fig, ax = plt.subplots()
		icssFig = ax.pcolormesh(X, Z, iCss, shading='gouraud')
		fig.colorbar(icssFig)
		plt.xlabel("X (Angstrom)")
		plt.ylabel("Z (Angstrom)")
	elif planeFlag == 3:
		for n_z2 in range(len(z_set)):
			icssArrayLine = []
			for n_y2 in range(len(y_set)):
				icssArrayLine.append(mapValue[n_z2 + len(z_set) * n_y2])
			icssArray.append(icssArrayLine)
		Y, Z = np.meshgrid(y_set,z_set)
		iCss = np.array(icssArray)
		fig, ax = plt.subplots()
		icssFig = ax.pcolormesh(Y, Z, iCss, shading='gouraud')
		fig.colorbar(icssFig)
		plt.xlabel("Y (Angstrom)")
		plt.ylabel("Z (Angstrom)")

	plt.show()
	fig.savefig(f"{fileName.strip()[:-4]}_ICSS_output_{tensorType}.png")

	print("\n*******************************************************************************")
	print("")
	print("                    2D-ICSS results are saved successfully.")
	print("                        Normal termination of py.Aroma.")
	print("")
	print("*******************************************************************************\n")

# ICSScub3D part
elif fileType == 'out' and usrFunc == '3':
	maxFileNumber = 999999
	fileNameList = []
	fileName = fileName[:-8]
	for i in range(1, maxFileNumber):
		i2 = '%04d' % i
		currentFileTest = fileName + str(i2) + '.log'
		try:
			with open(currentFileTest, 'r') as icssOutTest:
				fileNameList.append(currentFileTest)
		except FileNotFoundError:
			break

	totalFiles = len(fileNameList)
	if totalFiles == 1:
		print("\npy.Aroma found 1 output file.")
	elif totalFiles > 1:
		print(f"\npy.Aroma found {totalFiles} output files.")

	print("\nPlease wait...")
	print("py.Aroma is extracting magnetic shielding tensor from the output files...\n")

	shieldTensorIso = []
	shieldTensorAni = []
	shieldTensorXX = []
	shieldTensorYX = []
	shieldTensorZX = []
	shieldTensorXY = []
	shieldTensorYY = []
	shieldTensorZY = []
	shieldTensorXZ = []
	shieldTensorYZ = []
	shieldTensorZZ = []
	bqCoorsXList = []
	bqCoorsYList = []
	bqCoorsZList = []

	for j in range(len(fileNameList)):
		with open(fileNameList[j], 'r') as icssOut:
			outputLines = icssOut.readlines()

		print(f"Processing {fileNameList[j]}...")

		for line1 in outputLines:
			if 'Bq              ' in line1:
				bqCoorsXList.append(line1.split()[1])
				bqCoorsYList.append(line1.split()[2])
				bqCoorsZList.append(line1.split()[3])
			elif 'NumDoF:  NAt= ' in line1:
				sysAtomNumbers1 = int(line1.split()[2])

		tensorCount = 0

		for outputLine in outputLines:
			if ' NumDoF:  NAt=' in outputLine:
				sysAtomNumbers = int(outputLine.split()[2])
				bqAtomNumbers = int(outputLine.split()[4]) - int(outputLine.split()[2])
			elif 'Isotropic =' in outputLine:
				tensorCount += 1
				if tensorCount > sysAtomNumbers:
					shieldTensorIso.append(- float(outputLine.split()[4]))
					shieldTensorAni.append(- float(outputLine.split()[7]))
			elif ('XX=  ' in outputLine) and ('YX=  ' in outputLine) and ('ZX=  ' in outputLine) and (tensorCount > sysAtomNumbers):
				shieldTensorXX.append(- float(outputLine.split()[1]))
				shieldTensorYX.append(- float(outputLine.split()[3]))
				shieldTensorZX.append(- float(outputLine.split()[5]))
			elif ('XY=  ' in outputLine) and ('YY=  ' in outputLine) and ('ZY=  ' in outputLine) and (tensorCount > sysAtomNumbers):
				shieldTensorXY.append(- float(outputLine.split()[1]))
				shieldTensorYY.append(- float(outputLine.split()[3]))
				shieldTensorZY.append(- float(outputLine.split()[5]))
			elif ('XZ=  ' in outputLine) and ('YZ=  ' in outputLine) and ('ZZ=  ' in outputLine) and (tensorCount > sysAtomNumbers):
				shieldTensorXZ.append(- float(outputLine.split()[1]))
				shieldTensorYZ.append(- float(outputLine.split()[3]))
				shieldTensorZZ.append(- float(outputLine.split()[5]))

	sysCoorCount = 0
	sysElemsList = []
	sysCoorsXList = []
	sysCoorsYList = []
	sysCoorsZList = []

	with open(fileName + '0001.log', 'r') as icssOut:
		outLines2 = icssOut.readlines()

	for line2 in outLines2:
		if line2.strip() and line2.count('.') == 3 and line2.strip()[0].isalpha():
			sysElemsList.append(line2.split()[0])
			sysCoorsXList.append(line2.split()[1])
			sysCoorsYList.append(line2.split()[2])
			sysCoorsZList.append(line2.split()[3])
			sysCoorCount += 1
		if sysCoorCount == sysAtomNumbers:
			break

	bqCoorsXList2 = []
	bqCoorsYList2 = []
	bqCoorsZList2 = []

	for bqCoorX in bqCoorsXList:
		bqCoorsXList2.append(round(float(bqCoorX), 5))

	for bqCoorY in bqCoorsYList:
		bqCoorsYList2.append(round(float(bqCoorY), 5))

	for bqCoorZ in bqCoorsZList:
		bqCoorsZList2.append(round(float(bqCoorZ), 5))

	bqCoorsXList3 = list(set(bqCoorsXList2))
	bqCoorsXList3.sort()
	bqCoorsYList3 = list(set(bqCoorsYList2))
	bqCoorsYList3.sort()
	bqCoorsZList3 = list(set(bqCoorsZList2))
	bqCoorsZList3.sort()

	print("Processing finished!\n")

	print("Choose shielding tensor for 3D-ICSS map:")
	print("      1 - Isoptropic       2 - Anisotropy")
	print("      3 - XX component     4 - YX component     5 - ZX component")
	print("      6 - XY component     7 - YY component     8 - ZY component")
	print("      9 - XZ component    10 - YZ component    11 - ZZ component")
	nicsTensor = input('Please input the No.: ')
	tensorType = ''

	if nicsTensor == '1':
		mapValue = shieldTensorIso
		tensorType = 'iso'
	elif nicsTensor == '2':
		mapValue = shieldTensorAni
		tensorType = 'ani'
	elif nicsTensor == '3':
		mapValue = shieldTensorXX
		tensorType = 'xx'
	elif nicsTensor == '4':
		mapValue = shieldTensorYX
		tensorType = 'yx'
	elif nicsTensor == '5':
		mapValue = shieldTensorZX
		tensorType = 'zx'
	elif nicsTensor == '6':
		mapValue = shieldTensorXY
		tensorType = 'xy'
	elif nicsTensor == '7':
		mapValue = shieldTensorYY
		tensorType = 'yy'
	elif nicsTensor == '8':
		mapValue = shieldTensorZY
		tensorType = 'zy'
	elif nicsTensor == '9':
		mapValue = shieldTensorXZ
		tensorType = 'xz'
	elif nicsTensor == '10':
		mapValue = shieldTensorYZ
		tensorType = 'yz'
	elif nicsTensor == '11':
		mapValue = shieldTensorZZ
		tensorType = 'zz'

	icssCubeFile = open(f"{fileName}{tensorType}.cub", 'w')

	numCount = 0

	icssCubeFile.write("Generated by py.Aroma developed by Zhe Wang\n")
	icssCubeFile.write(f"Totally {len(mapValue)} grid points\n")

	icssCubeFile.write(f" {int(sysAtomNumbers)}  {format(min(bqCoorsXList3) * 1.88973, '.6f')}  {format(min(bqCoorsYList3) * 1.88973, '.6f')}  {format(min(bqCoorsZList3) * 1.88973, '.6f')}\n")
	icssCubeFile.write(f" {len(bqCoorsXList3)}    {format((bqCoorsXList3[1] - bqCoorsXList3[0]) * 1.88973, '.6f')}    0.000000    0.000000\n")
	icssCubeFile.write(f" {len(bqCoorsYList3)}    0.000000    {format((bqCoorsYList3[1] - bqCoorsYList3[0]) * 1.88973, '.6f')}    0.000000\n")
	icssCubeFile.write(f" {len(bqCoorsZList3)}    0.000000    0.000000    {format((bqCoorsZList3[1] - bqCoorsZList3[0]) * 1.88973, '.6f')}\n")

	for k in range(sysAtomNumbers):
		icssCubeFile.write(f" {elementNo(sysElemsList[k])}    {format(elementNo(sysElemsList[k]), '.6f')}    ")
		icssCubeFile.write(f" {format(float(sysCoorsXList[k]) * 1.88973, '.6f')}    {format(float(sysCoorsYList[k]) * 1.88973, '.6f')}    {format(float(sysCoorsZList[k]) * 1.88973, '.6f')}\n")

	for num in mapValue:
		icssCubeFile.write('%e' % num)
		icssCubeFile.write(' ')
		numCount += 1
		if numCount % 6 == 0:
			icssCubeFile.write('\n')

	icssCubeFile.close()

	print("\n*******************************************************************************")
	print("")
	print("                The cube file has been saved at current folder.")
	print("                        Normal termination of py.Aroma.")
	print("")
	print("*******************************************************************************\n")

# HOMAcalc part
elif fileType == 'out' and usrFunc == '1':
	with open(fileName, 'r') as usrOutFile:
		gauOut = usrOutFile.readlines()
	
	print("\n------ Parameters used in HOMAcalc ------")
	print("")
	print(" J. Chem. Inf. Comput. Sci. 1993, 33, 70 ")
	print("")
	print("-----------------------------------------\n")	

	alpha = 98.89
	Ropt = 1.397	

	geoFlagStart = 0
	for j in range(len(gauOut)):
		if 'Standard orientation:' in gauOut[j]:
			geoFlagStart = j
	if geoFlagStart == 0:
		for k in range(len(gauOut)):
			if 'Input orientation:' in gauOut[k]:
				geoFlagStart = k
	for m in range(geoFlagStart + 5, len(gauOut)):
		if '------' in gauOut[m]:
			geoFlagEnd = m
			break	

	geoLines = []
	for geoLine in gauOut[geoFlagStart + 5 : geoFlagEnd]:
		if geoLine.split()[1] != '0':
			geoLines.append(geoLine.strip())	

	periodTable2 = ['Bq', 'H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', \
					'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', \
					'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', \
					'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Ym', 'Yb', 'Lu', 'Ha', 'Ta', \
					'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', \
					'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', \
					'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og']	

	xCoors = []
	yCoors = []
	zCoors = []
	element = []	

	for i in range(len(geoLines)):
		element.append(periodTable2[int(geoLines[i].split()[1])])
		xCoors.append(format(float(geoLines[i].split()[3]), '.6f'))
		yCoors.append(format(float(geoLines[i].split()[4]), '.6f'))
		zCoors.append(format(float(geoLines[i].split()[5]), '.6f'))	

	print("Please input the atom numbers, separated by space:")
	userInput = input("(e.g.: 1 2 3 4 5 6)\n")	

	while userInput != 'q':
		while True:
			try:
				userInputList = userInput.split()
				break
			except ValueError:
				print("\nInput error, py.Aroma termination.")
		userElementList = elementDetermin(userInputList)
		print(f"\nHOMA value of ring [{userInput}] is {format(calcHOMA(userInputList, userElementList), '.4f')}.")
		userInput = input("\nInput atom numbers to calculate for other ring, or input \'q\' to quit.\n")	

	print("\n*******************************************************************************")
	print("")
	print("                       Normal termination of py.Aroma.")
	print("")
	print("*******************************************************************************\n")
