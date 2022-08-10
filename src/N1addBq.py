def calCoor(atmcList, heigh, xyzCoors):
	allX = 0.0
	allY = 0.0
	allZ = 0.0
	count = 0
	userX = []
	userY = []
	userZ = []
	bqN1X = 0.0
	bqN2X = 0.0
	bqN1Y = 0.0
	bqN2Y = 0.0
	bqN1Z = 0.0
	bqN2Z = 0.0
	for atm in atmcList:
		if atm != 0:
			count += 1
			allX += xyzCoors[int(atm) - 1][1]
			allY += xyzCoors[int(atm) - 1][2]
			allZ += xyzCoors[int(atm) - 1][3]
			userX.append(xyzCoors[int(atm) - 1][1])
			userY.append(xyzCoors[int(atm) - 1][2])
			userZ.append(xyzCoors[int(atm) - 1][3])

	aveX = allX / float(count)
	aveY = allY / float(count)
	aveZ = allZ / float(count)

	if float(heigh) == 0.0:
		return aveX, aveY, aveZ

	else:
		para_a = (userY[1] - userY[0]) * (userZ[2] - userZ[0]) - (userY[2] - userY[0]) * (userZ[1] - userZ[0])
		para_b = (userZ[1] - userZ[0]) * (userX[2] - userX[0]) - (userZ[2] - userZ[0]) * (userX[1] - userX[0])
		para_c = (userX[1] - userX[0]) * (userY[2] - userY[0]) - (userX[2] - userX[0]) * (userY[1] - userY[0])
		if para_a != 0.0:
			para_A3 = 1 + para_b * para_b / para_a / para_a + para_c * para_c / para_a / para_a
			para_B3 = - 2 * aveX - 2 * para_b * para_b * aveX / para_a / para_a - 2 * para_c * para_c * aveX / para_a / para_a
			para_C3 = aveX * aveX + para_b * para_b * aveX * aveX / para_a / para_a + para_c * para_c * aveX * aveX / para_a / para_a - float(heigh) * float(heigh)
			deltaValue = para_B3 * para_B3 - 4 * para_A3 * para_C3
			if deltaValue != 0:
				bqN1X = (- para_B3 + pow(deltaValue, 1.0/2)) / 2 / para_A3
				bqN2X = (- para_B3 - pow(deltaValue, 1.0/2)) / 2 / para_A3
				bqN1Y = para_b / para_a * (bqN1X - aveX) + aveY
				bqN2Y = para_b / para_a * (bqN2X - aveX) + aveY
				bqN1Z = para_c / para_a * (bqN1X - aveX) + aveZ
				bqN2Z = para_c / para_a * (bqN2X - aveX) + aveZ
		elif userX[0] == userX[1] and userX[1] == userX[2]:
			bqN1X = float(heigh)
			bqN1Y = aveY
			bqN1Z = aveZ
			bqN2X = -float(heigh)
			bqN2Y = aveY
			bqN2Z = aveZ
		elif userY[0] == userY[1] and userY[1] == userY[2]:
			bqN1X = aveX
			bqN1Y = float(heigh)
			bqN1Z = aveZ
			bqN2X = aveX
			bqN2Y = -float(heigh)
			bqN2Z = aveZ
		elif userZ[0] == userZ[1] and userZ[1] == userZ[2]:
			bqN1X = aveX
			bqN1Y = aveY
			bqN1Z = float(heigh)
			bqN2X = aveX
			bqN2Y = aveY
			bqN2Z = -float(heigh)
		return bqN1X, bqN1Y, bqN1Z, bqN2X, bqN2Y, bqN2Z
