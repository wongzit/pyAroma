def n1inp(fileName, cpu, mem, nmrType, ruMethod, dft, basis, addKey, charge, spin, coordinate, bqcoor):

	nics1Input = open(f'{fileName.strip()[:-4]}_NICS.gjf', 'w')
	charNo = 0
	for nameChar in range(len(fileName)):
		if fileName[nameChar] == '/':
			charNo = nameChar
	fileNameShort = fileName[charNo+1:-4]
	
	if fileName[-3:] != 'gjf' and fileName[-3:] != 'com':
		if cpu != 'Default':
			nics1Input.write(f'%nprocshared={cpu}\n')
		if mem != 'Default':
			nics1Input.write(f'%mem={mem}\n')
		nics1Input.write(f'%chk={fileNameShort}.chk\n')
		if ruMethod != ' ':
			nics1Input.write(f'#p nmr={nmrType} {ruMethod}{dft}/{basis}')
		else:
			nics1Input.write(f'#p nmr={nmrType} {dft}/{basis}')
		if addKey != ' ':
			nics1Input.write(f' {addKey}\n')
		else:
			nics1Input.write('\n')
		nics1Input.write(f'\n{fileNameShort}_NICS // created by py.Aroma\n\n{charge} {spin}\n')

	else:
		with open(fileName, 'r') as gjfInp:
			gjfInpLine = gjfInp.readlines()
		for gjfLine in gjfInpLine:
			if gjfLine[0] == '%':
				nics1Input.write(gjfLine)
			elif gjfLine[0] == '#':
				nics1Input.write(gjfLine)
			elif len(gjfLine.split()) == 2 and len(''.join(gjfLine.rstrip())) < 6:
				nics1Input.write(f'\n{fileNameShort}_NICS // created by py.Aroma\n\n{gjfLine}')

	for i in range(len(coordinate)):
		nics1Input.write(f'{coordinate[i][0]}      {round(coordinate[i][1], 6)}      {round(coordinate[i][2], 6)}      {round(coordinate[i][3], 6)}\n')

	for j in range(len(bqcoor)):
		#nics1Input.write(f' Bq                 {'{:11f}'.format(bqcoor[j][0])}      {'{:11f}'.format(bqcoor[j][1])}      {'{:11f}'.format(bqcoor[j][2])}\n')
		nics1Input.write(f' Bq           {round(bqcoor[j][0], 6)}      {round(bqcoor[j][1], 6)}      {round(bqcoor[j][2], 6)}\n')

	nics1Input.write('\n\n')
	nics1Input.close()

def n2inp(fileName, cpu, mem, nmrType, ruMethod, dft, basis, addKey, charge, spin, coordinate, planeFlag, \
	x_min, x_max, y_min, y_max, z_min, z_max, height, grid):

	nicsInput = open(f'{fileName.strip()[:-4]}_2DNICS_{planeFlag.upper()}.gjf', 'w')
	charNo = 0
	for nameChar in range(len(fileName)):
		if fileName[nameChar] == '/':
			charNo = nameChar
	fileNameShort = fileName[charNo+1:-4]
	
	if fileName[-3:] != 'gjf' and fileName[-3:] != 'com':
		if cpu != 'Default':
			nicsInput.write(f'%nprocshared={cpu}\n')
		if mem != 'Default':
			nicsInput.write(f'%mem={mem}\n')
		nicsInput.write(f'%chk={fileNameShort}.chk\n')
		if ruMethod != ' ':
			nicsInput.write(f'#p nmr={nmrType} {ruMethod}{dft}/{basis} geom=connectivity')
		else:
			nicsInput.write(f'#p nmr={nmrType} {dft}/{basis} geom=connectivity')
		if addKey != ' ':
			nicsInput.write(f' {addKey}\n')
		else:
			nicsInput.write('\n')
		nicsInput.write(f'\n{fileNameShort}_2DNICS // created by py.Aroma\n\n{charge} {spin}\n')

	else:
		with open(fileName, 'r') as gjfInp:
			gjfInpLine = gjfInp.readlines()
		for gjfLine in gjfInpLine:
			if gjfLine[0] == '%':
				nicsInput.write(gjfLine)
			elif gjfLine[0] == '#':
				if 'geom=connectivity' in gjfLine.lower():
					nicsInput.write(gjfLine)
				else:
					nicsInput.write(f'{gjfLine.rstrip()} geom=connectivity\n')
			elif len(gjfLine.split()) == 2 and len(''.join(gjfLine.rstrip())) < 6:
				nicsInput.write(f'\n{fileNameShort}_2DNICS // created by py.Aroma\n\n{gjfLine}')

	for i in range(len(coordinate)):
		nicsInput.write(f'{coordinate[i][0]}      {round(coordinate[i][1], 6)}      {round(coordinate[i][2], 6)}      {round(coordinate[i][3], 6)}\n')

	if planeFlag == 'xy':
		x_position = float(x_min)
		bqFlag = 0
		while x_position <= (float(x_max) + 0.5 * float(grid)):
			y_position = float(y_min)
			while y_position <= (float(y_max) + 0.5 * float(grid)):
				nicsInput.write(f" Bq      {round(x_position, 2)}      {round(y_position, 2)}      {round(float(height), 2)}\n")
				bqFlag += 1
				y_position += float(grid)
			x_position += float(grid)
		for bqNumber in list(range(1, bqFlag + len(coordinate) + 1)):
			nicsInput.write(f"\n{bqNumber}")
	
	elif planeFlag == 'yz':
		y_position = float(y_min)
		bqFlag = 0
		while y_position <= (float(y_max) + 0.5 * float(grid)):
			z_position = float(z_min)
			while z_position <= (float(z_max) + 0.5 * float(grid)):
				nicsInput.write(f" Bq      {round(float(height), 2)}      {round(y_position, 2)}      {round(z_position, 2)}\n")
				bqFlag += 1
				z_position += float(grid)
			y_position += float(grid)
		for bqNumber in list(range(1, bqFlag + len(coordinate) + 1)):
			nicsInput.write(f"\n{bqNumber}")

	else:
		x_position = float(x_min)
		bqFlag = 0
		while x_position <= (float(x_max) + 0.5 * float(grid)):
			z_position = float(z_min)
			while z_position <= (float(z_max) + 0.5 * float(grid)):
				nicsInput.write(f" Bq      {round(x_position, 2)}      {round(float(height), 2)}      {round(z_position, 2)}\n")
				bqFlag += 1
				z_position += float(grid)
			x_position += float(grid)
		for bqNumber in list(range(1, bqFlag + len(coordinate) + 1)):
			nicsInput.write(f"\n{bqNumber}")

	nicsInput.write('\n\n')
	nicsInput.close()

	return bqNumber

def n3inp(fileName, cpu, mem, nmrType, ruMethod, dft, basis, addKey, charge, spin, coordinate, \
	x_min, x_max, y_min, y_max, z_min, z_max, grid):

	charNo = 0
	for nameChar in range(len(fileName)):
		if fileName[nameChar] == '/':
			charNo = nameChar
	fileNameShort = fileName[charNo+1:-4]
	
	routeLine = []
	routeLine2 = []

	if fileName[-3:] != 'gjf' and fileName[-3:] != 'com':
		if cpu != 'Default':
			routeLine.append(f'%nprocshared={cpu}\n')
			routeLine2.append(f'%nprocshared={cpu}\n')
		if mem != 'Default':
			routeLine.append(f'%mem={mem}\n')
			routeLine2.append(f'%mem={mem}\n')
		routeLine.append(f'%chk={fileNameShort}.chk\n')
		routeLine2.append(f'%chk={fileNameShort}.chk\n')
		if ruMethod != ' ':
			routeLine.append(f'#p nmr={nmrType} {ruMethod}{dft}/{basis} geom=connectivity')
			routeLine2.append(f'#p nmr={nmrType} {ruMethod}{dft}/{basis} geom=connectivity guess=read')
		else:
			routeLine.append(f'#p nmr={nmrType} {dft}/{basis} geom=connectivity')
			routeLine2.append(f'#p nmr={nmrType} {dft}/{basis} geom=connectivity guess=read')
		if addKey != ' ':
			routeLine.append(f' {addKey}\n')
			routeLine2.append(f' {addKey}\n')
		else:
			routeLine.append('\n')
			routeLine2.append('\n')
		routeLine.append(f'\n{fileNameShort}_3DNICS // created by py.Aroma\n\n{charge} {spin}\n')
		routeLine2.append(f'\n{fileNameShort}_3DNICS // created by py.Aroma\n\n{charge} {spin}\n')

	else:
		with open(fileName, 'r') as gjfInp:
			gjfInpLine = gjfInp.readlines()
		for gjfLine in gjfInpLine:
			if gjfLine[0] == '%':
				routeLine.append(gjfLine)
				routeLine2.append(gjfLine)
			elif gjfLine[0] == '#':
				if 'geom=connectivity' in gjfLine.lower():
					routeLine.append(gjfLine)
					routeLine2.append(f'{gjfLine.strip()} guess=read\n')
				else:
					routeLine.append(f'{gjfLine.rstrip()} geom=connectivity\n')
					routeLine2.append(f'{gjfLine.rstrip()} geom=connectivity guess=read\n')
			elif len(gjfLine.split()) == 2 and len(''.join(gjfLine.rstrip())) < 6:
				routeLine.append(f'\n{fileNameShort}_3DNICS // created by py.Aroma\n\n{gjfLine}')
				routeLine2.append(f'\n{fileNameShort}_3DNICS // created by py.Aroma\n\n{gjfLine}')

	allBqCoors = []
	oneBqCoor =[]
	x_position = float(x_min)
	while x_position <= (float(x_max) + 0.5 * float(grid)):
		y_position = float(y_min)
		while y_position <= (float(y_max) + 0.5 * float(grid)):
			z_position = float(z_min)
			while z_position <= (float(z_max) + 0.5 * float(grid)):
				oneBqCoor = [format(x_position, '.6f'), format(y_position, '.6f'), format(z_position, '.6f')]
				allBqCoors.append(oneBqCoor)
				oneBqCoor = []
				z_position += float(grid)
			y_position += float(grid)
		x_position += float(grid)

	fileNumbers = 1
	if len(allBqCoors) <= 7000 - len(coordinate):
		fileNumbers = 1
	elif len(allBqCoors) % 7000 == 0:
		fileNumbers = int(len(allBqCoors) / 7000)
	else:
		fileNumbers = int(len(allBqCoors) / 7000 + 1)
	
	nics3Input = open(f"{fileName[:-4]}_3DNICS_0001.gjf", "w")

	for route_i in routeLine:
		nics3Input.write(route_i)

	for j in range(len(coordinate)):
		nics3Input.write(f'{coordinate[j][0]}      {round(coordinate[j][1], 6)}      {round(coordinate[j][2], 6)}      {round(coordinate[j][3], 6)}\n')
	if fileNumbers == 1:
		for i in range(len(allBqCoors)):
			nics3Input.write(f" Bq      {allBqCoors[i][0]}      {allBqCoors[i][1]}      {allBqCoors[i][2]}\n")
		for bqNumber1 in list(range(1, len(coordinate) + len(allBqCoors) + 1)):
			nics3Input.write(f"\n{bqNumber1}")
	else:
		bqCounter1 = 0
		for i in range(7000):
			nics3Input.write(f" Bq      {allBqCoors[i][0]}      {allBqCoors[i][1]}      {allBqCoors[i][2]}\n")
			bqCounter1 += 1
		for bqNumber1 in list(range(7000 + len(coordinate))):
			nics3Input.write(f"\n{bqNumber1 + 1}")

	nics3Input.write("\n\n")
	nics3Input.close()

	if fileNumbers > 1:
		for fileNumber in range(2, fileNumbers + 1):
			fileNameNumber = '%04d' % fileNumber
			nics3Input = open(f"{fileName[:-4]}_3DNICS_{fileNameNumber}.gjf", "w")

			for route_j in routeLine2:
				nics3Input.write(route_j)

			for k in range(len(coordinate)):
				nics3Input.write(f'{coordinate[k][0]}      {round(coordinate[k][1], 6)}      {round(coordinate[k][2], 6)}      {round(coordinate[k][3], 6)}\n')
			bqCounter2 = 0
			while (bqCounter2 < 7000) and bqCounter1 < len(allBqCoors):
				nics3Input.write(f" Bq      {allBqCoors[bqCounter1][0]}      {allBqCoors[bqCounter1][1]}      {allBqCoors[bqCounter1][2]}\n")
				bqCounter1 += 1
				bqCounter2 += 1
			for bqNumber2 in list(range(1, len(coordinate) + bqCounter2 + 1)):
				nics3Input.write(f"\n{bqNumber2}")
			nics3Input.write("\n\n")
			nics3Input.close()


