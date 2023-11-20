# A Module for py.Aroma 3
# Create NICS input files

import numpy as np

def nics2Dxy(x_min, x_max, y_min, y_max, height, grid):
    bq_list = []

    x_position = x_min
    while x_position <= x_max + 0.5 * grid:
        y_position = y_min
        while y_position <= y_max + 0.5 * grid:
            bq_list.append(f'Bq      {x_position:.6f}      {y_position:.6f}      {height:.6f}\n')
            y_position += grid
        x_position += grid

    return bq_list


def nics2Dxz(x_min, x_max, z_min, z_max, height, grid):
    bq_list = []

    x_position = x_min
    while x_position <= x_max + 0.5 * grid:
        z_position = z_min
        while z_position <= z_max + 0.5 * grid:
            bq_list.append(f'Bq      {x_position:.6f}      {height:.6f}      {z_position:.6f}\n')
            z_position += grid
        x_position += grid

    return bq_list


def nics2Dyz(y_min, y_max, z_min, z_max, height, grid):
    bq_list = []

    y_position = y_min
    while y_position <= y_max + 0.5 * grid:
        z_position = z_min
        while z_position <= z_max + 0.5 * grid:
            bq_list.append(f'Bq      {height:.6f}      {y_position:.6f}      {z_position:.6f}\n')
            z_position += grid
        y_position += grid

    return bq_list


def nics3D(x_min, x_max, y_min, y_max, z_min, z_max, grid):
    bq_list = []

    x_position = x_min
    while x_position <= x_max + 0.5 * grid:
        y_position = y_min
        while y_position <= y_max + 0.5 * grid:
            z_position = z_min
            while z_position <= z_max + 0.5 * grid:
                bq_list.append(f'Bq      {x_position:.6f}      {y_position:.6f}      {z_position:.6f}\n')
                z_position += grid
            y_position += grid
        x_position += grid

    return bq_list

def projectOnPlane(a,b,c,d,x,y,z):
    #based on the Matlab function "projection" written by Neo Jing Ci, 11/7/18
    A = np.array([[1, 0, 0, -a], [0, 1, 0, -b], [0, 0, 1, -c], [a, b, c, 0]])
    B = [[x],[y],[z],[d]]
    C = np.linalg.lstsq(A, B, rcond=None)[0]
    px = C[0][0]
    py = C[1][0]
    pz = C[2][0]
    return [px, py, pz]

# projects a point on a plane
def projectOnPlane(a,b,c,d,x,y,z):
    #based on the Matlab function "projection" written by Neo Jing Ci, 11/7/18
    A = np.array([[1, 0, 0, -a], [0, 1, 0, -b], [0, 0, 1, -c], [a, b, c, 0]])
    B = [[x],[y],[z],[d]]
    C = np.linalg.lstsq(A, B, rcond=None)[0]
    px = C[0][0]
    py = C[1][0]
    pz = C[2][0]
    return [px, py, pz]

# Calculate coordinates of Bq atoms.
def calCoor(atmcList, heigh, xyzCoors):
    aveX = 0.0
    aveY = 0.0
    aveZ = 0.0
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
        aveX += xyzCoors[atm][1] / len(atmcList)
        aveY += xyzCoors[atm][2] / len(atmcList)
        aveZ += xyzCoors[atm][3] / len(atmcList)
        userX.append(xyzCoors[atm][1])
        userY.append(xyzCoors[atm][2])
        userZ.append(xyzCoors[atm][3])

    # Additional code: calculate plane and project points on plane
    a1 = np.column_stack([userX, userY, np.ones(len(atmcList))])
    a2 = np.column_stack([userZ])
    a3 = np.linalg.lstsq(a1, a2, rcond=None)[0]  # coefficients for the equation of the plane: z=c1*x+c2*y+c3

    c1 = a3[0][0]
    c2 = a3[1][0]
    c3 = a3[2][0]

    #overwrites the atom coordinates stored in userX, userY, userZ with the coordinates of the atoms projected on the projectOnPlane
    for ii in range(len(userX)):
        projected_xyz = projectOnPlane(c1, c2, -1, -c3, userX[ii], userY[ii], userZ[ii])
        userX[ii] = projected_xyz[0]
        userY[ii] = projected_xyz[1]
        userZ[ii] = projected_xyz[2]

    if float(heigh) == 0.0:
        return aveX, aveY, aveZ

    else:
        para_a = (userY[1] - userY[0]) * (userZ[2] - userZ[0]) - (userY[2] - userY[0]) * (userZ[1] - userZ[0])
        para_b = (userZ[1] - userZ[0]) * (userX[2] - userX[0]) - (userZ[2] - userZ[0]) * (userX[1] - userX[0])
        para_c = (userX[1] - userX[0]) * (userY[2] - userY[0]) - (userX[2] - userX[0]) * (userY[1] - userY[0])
        if para_a != 0.0:
            para_A3 = 1 + para_b * para_b / para_a / para_a + para_c * para_c / para_a / para_a
            para_B3 = - 2 * aveX - 2 * para_b * para_b * aveX / para_a / para_a - 2 * para_c * para_c * aveX / para_a / para_a
            para_C3 = aveX * aveX + para_b * para_b * aveX * aveX / para_a / para_a + para_c * para_c * aveX * aveX / para_a / para_a - float(
                heigh) * float(heigh)
            deltaValue = para_B3 * para_B3 - 4 * para_A3 * para_C3
            if deltaValue != 0:
                bqN1X = (- para_B3 + pow(deltaValue, 1.0 / 2)) / 2 / para_A3
                bqN2X = (- para_B3 - pow(deltaValue, 1.0 / 2)) / 2 / para_A3
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

	aveX = 0.0
	aveY = 0.0
	aveZ = 0.0
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
		aveX += xyzCoors[atm][1] / len(atmcList)
		aveY += xyzCoors[atm][2] / len(atmcList)
		aveZ += xyzCoors[atm][3] / len(atmcList)
		userX.append(xyzCoors[atm][1])
		userY.append(xyzCoors[atm][2])
		userZ.append(xyzCoors[atm][3])

    	#!!!!!!!!!!!!!! Additional code: calculate plane and project points on plane
	# Since the position of the NICS(n) points are calculated, in the original code, via the cross product of two vectors (defined by three atoms),
	# the result is unreliable when rings are not perfectly planar.
	# For instance, attempting the calculation of NICS(1) on boat cyclohexane leads to different results depending
	# On wether the selected atoms are "1,2,3,4,5,6" or "2,3,4,5,6,1". The same problem is seen in distorted aromatic systems, i.e. nonplanar nanoribbons.
	# The additional code finds the plane that best fits the selected atoms, and then projects the selected atoms on the plane.
	# Vector operations and calculation of the normal vector are done as before, but on projected positions instead of atomic positions, hence leading to the same result as before
	# in the case of planar rings, and to a univocal result in the case of nonplanar rings
	
    	a1 = np.column_stack([userX, userY, np.ones(len(atmcList))])
	a2 = np.column_stack([userZ])
	a3 = np.linalg.lstsq(a1, a2, rcond=None)[0] # Finds the plane that best fits the selected atoms

	# coefficients for the equation of the plane: z=c1*x+c2*y+c3
	c1 = a3[0][0]
	c2 = a3[1][0]
	c3 = a3[2][0]
	
	#overwrites the atom coordinates stored in userX, userY, userZ with the coordinates of the atoms projected on the plane
	for ii in range(len(userX)):
	        projected_xyz = projectOnPlane(c1, c2, -1, -c3, userX[ii], userY[ii], userZ[ii])
	        userX[ii] = projected_xyz[0]
	        userY[ii] = projected_xyz[1]
	        userZ[ii] = projected_xyz[2]
	
	#!!!!!!!!!!!!!! End of additional code

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

