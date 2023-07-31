# 1D NICS Scan module for new version of py.Aroma
# This is currently a beta version, just used for testing.
# This function will be added into new version of py.Aroma 3.
# Wrote by Dr. Zhe Wang @Kyoto, Japan
# 2023-07-30
# Contact me via E-mail: wang.zhe.dr@gmail.com

import numpy as np

fName = "/Users/wangzhe/Desktop/test/mol.xyz"      # a .xyz file including your geometry

with open(fName) as xyzFile:
	xyzCoor = xyzFile.readlines()[2:]

xCoor = []
yCoor = []
zCoor = []

for i in xyzCoor:
	xCoor.append(float(i.split()[1]))
	yCoor.append(float(i.split()[2]))
	zCoor.append(float(i.strip().split()[3]))

# Following parameters need to be modified depends on your needs.
height = 0.0
dirct = [1.0, 0, 0]
knot = [[11, 14], [6, 8], [2, 4, 5, 6, 7, 8], [5, 7], [5, 7, 17, 18, 33], [17, 18], [17, 18, 19, 20, 21, 22], [20, 22], [27, 30]]  
#knot = [[22], [5], [19], [3, 8, 20, 13, 19], [8], [9], [9, 12, 14, 6, 17],[53],[53,56,59, 61, 64],[55],[55,50,66,60,67],[66],[52],[69]]
bqKnot = []
stepsize = 0.1

nicsInp = open("/Users/wangzhe/Desktop/nics_inp.gjf", "w")

nicsInp.write("# hf/sto-3g geom=connectivity\n\ntitle\n\n0 1\n")

bqCounter = 0

dirct_length = np.sqrt(dirct[0]*dirct[0] + dirct[1]*dirct[1] + dirct[2]*dirct[2])
if dirct_length != 0.0:
	dirct_unit = [dirct[0]/dirct_length, dirct[1]/dirct_length, dirct[2]/dirct_length]
else:
	dirct_unit = [0.0, 0.0, 0.0]

for j in xyzCoor:
	nicsInp.write(j)

for l in knot:
	sumX = 0.0
	sumY = 0.0
	sumZ = 0.0
	aveX = 0.0
	aveY = 0.0
	aveZ = 0.0
	for m in l:
		sumX += xCoor[m - 1]
		sumY += yCoor[m - 1]
		sumZ += zCoor[m - 1]
	aveX = sumX/len(l)
	aveY = sumY/len(l)
	aveZ = sumZ/len(l)
	bqKnot.append([aveX+dirct_unit[0]*height, aveY+dirct_unit[1]*height, aveZ+dirct_unit[2]*height])

start_dis = 0.0
for o in range(len(bqKnot) - 1):
	x_dire = bqKnot[o+1][0] - bqKnot[o][0]
	y_dire = bqKnot[o+1][1] - bqKnot[o][1]
	z_dire = bqKnot[o+1][2] - bqKnot[o][2]
	x_dire_unit = x_dire/np.sqrt(x_dire*x_dire+y_dire*y_dire+z_dire*z_dire)
	y_dire_unit = y_dire/np.sqrt(x_dire*x_dire+y_dire*y_dire+z_dire*z_dire)
	z_dire_unit = z_dire/np.sqrt(x_dire*x_dire+y_dire*y_dire+z_dire*z_dire)
	for p in range(8000):
		bq_x = bqKnot[o][0] + x_dire_unit * (start_dis + stepsize * p)
		bq_y = bqKnot[o][1] + y_dire_unit * (start_dis + stepsize * p)
		bq_z = bqKnot[o][2] + z_dire_unit * (start_dis + stepsize * p)
		if (bq_x - bqKnot[o][0])**2 + (bq_y - bqKnot[o][1])**2 + (bq_z - bqKnot[o][2])**2 < (bqKnot[o+1][0] - bqKnot[o][0])**2 + (bqKnot[o+1][1] - bqKnot[o][1])**2 + (bqKnot[o+1][2] - bqKnot[o][2])**2:
			nicsInp.write(f"Bq        {round(bq_x, 6)}        {round(bq_y, 6)}        {round(bq_z, 6)}\n")
			bqCounter += 1
		else:
			start_dis = np.sqrt((bq_x - bqKnot[o+1][0])**2 + (bq_y - bqKnot[o+1][1])**2 + (bq_z - bqKnot[o+1][2])**2)
			break

# *************************************************************************
nicsInp.write("\n")

with open("/Users/wangzhe/Desktop/test/mol_con.txt") as conFile:        # a .txt file including connectivity information is needed.
	con = conFile.readlines()

for k in con:
	if k !='\n':
		nicsInp.write(k)

for n in range(bqCounter):
	nicsInp.write(str(n + 36)+"\n")        # change the 36 to the number of atoms in your geometry

# *************************************************************************

nicsInp.write("\n")
nicsInp.close()
