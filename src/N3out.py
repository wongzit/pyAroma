from const import *

def n3out(fName, nicsTensor):
	fileNameList = []
	fName = fName[:-8]
	for i in range(1, 999999):
		i2 = '%04d' % i
		currentFileTest = fName + str(i2) + '.log'
		try:
			with open(currentFileTest, 'r') as icssOutTest:
				fileNameList.append(currentFileTest)
		except FileNotFoundError:
			break

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

		for line1 in outputLines:
			if ' Bq    ' in line1 and line1.count('.') == 3 and len(line1.split()) == 4:
				bqCoorsXList.append(line1.split()[1])
				bqCoorsYList.append(line1.split()[2])
				bqCoorsZList.append(line1.split()[3])
			elif 'NumDoF:  NAt= ' in line1:
				sysAtomNumbers1 = int(line1.split()[2])

		tensorCount = 0

		for outputLine in outputLines:
			if ' NumDoF:  NAt=' in outputLine or 'NUMDOF-- NAT=' in outputLine:
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

	with open(fName + '0001.log', 'r') as icssOut:
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

	if nicsTensor == 'isotropic':
		mapValue = shieldTensorIso
	elif nicsTensor == 'anisotropic':
		mapValue = shieldTensorAni
	elif nicsTensor == 'xx':
		mapValue = shieldTensorXX
	elif nicsTensor == 'yx':
		mapValue = shieldTensorYZ
	elif nicsTensor == 'zx':
		mapValue = shieldTensorZX
	elif nicsTensor == 'xy':
		mapValue = shieldTensorXY
	elif nicsTensor == 'yy':
		mapValue = shieldTensorYY
	elif nicsTensor == 'zy':
		mapValue = shieldTensorZY
	elif nicsTensor == 'xz':
		mapValue = shieldTensorXZ
	elif nicsTensor == 'yz':
		mapValue = shieldTensorYZ
	elif nicsTensor == 'zz':
		mapValue = shieldTensorZZ

	icssCubeFile = open(f"{fName}{nicsTensor.upper()}.cub", 'w')

	numCount = 0

	icssCubeFile.write("Generated by py.Aroma developed by Zhe Wang\n")
	icssCubeFile.write(f"Totally {len(mapValue)} grid points\n")

	icssCubeFile.write(f" {int(sysAtomNumbers)}  {format(min(bqCoorsXList3) * 1.88973, '.6f')}  {format(min(bqCoorsYList3) * 1.88973, '.6f')}  {format(min(bqCoorsZList3) * 1.88973, '.6f')}\n")
	icssCubeFile.write(f" {len(bqCoorsXList3)}    {format((bqCoorsXList3[1] - bqCoorsXList3[0]) * 1.88973, '.6f')}    0.000000    0.000000\n")
	icssCubeFile.write(f" {len(bqCoorsYList3)}    0.000000    {format((bqCoorsYList3[1] - bqCoorsYList3[0]) * 1.88973, '.6f')}    0.000000\n")
	icssCubeFile.write(f" {len(bqCoorsZList3)}    0.000000    0.000000    {format((bqCoorsZList3[1] - bqCoorsZList3[0]) * 1.88973, '.6f')}\n")

	for k in range(sysAtomNumbers):
		icssCubeFile.write(f" {periodTable.index(sysElemsList[k].upper())}    {format(periodTable.index(sysElemsList[k].upper()), '.6f')}    ")
		icssCubeFile.write(f" {format(float(sysCoorsXList[k]) * 1.88973, '.6f')}    {format(float(sysCoorsYList[k]) * 1.88973, '.6f')}    {format(float(sysCoorsZList[k]) * 1.88973, '.6f')}\n")

	for num in mapValue:
		icssCubeFile.write('%e' % num)
		icssCubeFile.write(' ')
		numCount += 1
		if numCount % 6 == 0:
			icssCubeFile.write('\n')

	icssCubeFile.close()

