import numpy as np
import matplotlib.pyplot as plt

def n2out(fName, nicsTensor):
	with open(fName, 'r') as usrOutFile:
		gauOut = usrOutFile.readlines()

	coorBq = []
	shielTensor = []

	x_all = []
	y_all = []
	z_all = []

	ten_iso = []
	ten_ani = []
	ten_xx = []
	ten_xy = []
	ten_xz = []
	ten_yx = []
	ten_yy = []
	ten_yz = []
	ten_zx = []
	ten_zy = []
	ten_zz = []

	for outputLine in gauOut:
		if ' Bq    ' in outputLine and outputLine.count('.') == 3 and len(outputLine.split()) == 4:
			x_all.append(float(outputLine.rstrip().split()[1]))
			y_all.append(float(outputLine.rstrip().split()[2]))
			z_all.append(float(outputLine.rstrip().split()[3]))
			#coorBq.append(outputLine.rstrip())
		elif 'Isotropic =' in outputLine:
			ten_iso.append(-float(outputLine.rstrip().split()[4]))
			ten_ani.append(-float(outputLine.rstrip().split()[7]))
			#shielTensor.append(outputLine.rstrip())
		elif ('XX=  ' in outputLine) and ('YX=  ' in outputLine) and ('ZX=  ' in outputLine):
			ten_xx.append(-float(outputLine.rstrip().split()[1]))
			ten_yx.append(-float(outputLine.rstrip().split()[3]))
			ten_zx.append(-float(outputLine.rstrip().split()[5]))
			#shielTensor.append(outputLine.rstrip())
		elif ('XY=  ' in outputLine) and ('YY=  ' in outputLine) and ('ZY=  ' in outputLine):
			ten_xy.append(-float(outputLine.rstrip().split()[1]))
			ten_yy.append(-float(outputLine.rstrip().split()[3]))
			ten_zy.append(-float(outputLine.rstrip().split()[5]))
			#shielTensor.append(outputLine.rstrip())
		elif ('XZ=  ' in outputLine) and ('YZ=  ' in outputLine) and ('ZZ=  ' in outputLine):
			ten_xz.append(-float(outputLine.rstrip().split()[1]))
			ten_yz.append(-float(outputLine.rstrip().split()[3]))
			ten_zz.append(-float(outputLine.rstrip().split()[5]))
			#shielTensor.append(outputLine.rstrip())
	
	ten_iso = ten_iso[-len(x_all):]
	ten_ani = ten_ani[-len(x_all):]
	ten_xx = ten_xx[-len(x_all):]
	ten_xy = ten_xy[-len(x_all):]
	ten_xz = ten_xz[-len(x_all):]
	ten_yx = ten_yx[-len(x_all):]
	ten_yy = ten_yy[-len(x_all):]
	ten_yz = ten_yz[-len(x_all):]
	ten_zx = ten_zx[-len(x_all):]
	ten_zy = ten_zy[-len(x_all):]
	ten_zz = ten_zz[-len(x_all):]

	x_set = sorted(set(x_all))
	y_set = sorted(set(y_all))
	z_set = sorted(set(z_all))
	xo_max, xo_min = max(x_set), min(x_set)
	yo_max, yo_min = max(y_set), min(y_set)
	zo_max, zo_min = max(z_set), min(z_set)

	planeFlag = 0
	if len(x_set) == 1:
		planeFlag = 3
		y_step = y_set[1] - y_set[0]
		z_step = z_set[1] - z_set[0]
	elif len(y_set) == 1:
		planeFlag = 2
		x_step = x_set[1] - x_set[0]
		z_step = z_set[1] - z_set[0]
	elif len(z_set) == 1:
		planeFlag = 1
		x_step = x_set[1] - x_set[0]
		y_step = y_set[1] - y_set[0]

	if nicsTensor == 'isotropic':
		mapValue = ten_iso
	elif nicsTensor == 'anisotropic':
		mapValue = ten_ani
	elif nicsTensor == 'xx':
		mapValue = ten_xx
	elif nicsTensor == 'yx':
		mapValue = ten_yx
	elif nicsTensor == 'zx':
		mapValue = ten_zx
	elif nicsTensor == 'xy':
		mapValue = ten_xy
	elif nicsTensor == 'yy':
		mapValue = ten_yy
	elif nicsTensor == 'zy':
		mapValue = ten_zy
	elif nicsTensor == 'xz':
		mapValue = ten_xz
	elif nicsTensor == 'yz':
		mapValue = ten_yz
	elif nicsTensor == 'zz':
		mapValue = ten_zz

	return mapValue

def n2outSave(fName, nicsTensor):
	with open(fName, 'r') as usrOutFile:
		gauOut = usrOutFile.readlines()

	coorBq = []
	shielTensor = []

	x_all = []
	y_all = []
	z_all = []

	ten_iso = []
	ten_ani = []
	ten_xx = []
	ten_xy = []
	ten_xz = []
	ten_yx = []
	ten_yy = []
	ten_yz = []
	ten_zx = []
	ten_zy = []
	ten_zz = []

	for outputLine in gauOut:
		if ' Bq    ' in outputLine and outputLine.count('.') == 3 and len(outputLine.split()) == 4:
			x_all.append(float(outputLine.rstrip().split()[1]))
			y_all.append(float(outputLine.rstrip().split()[2]))
			z_all.append(float(outputLine.rstrip().split()[3]))
			#coorBq.append(outputLine.rstrip())
		elif 'Isotropic =' in outputLine:
			ten_iso.append(-float(outputLine.rstrip().split()[4]))
			ten_ani.append(-float(outputLine.rstrip().split()[7]))
			#shielTensor.append(outputLine.rstrip())
		elif ('XX=  ' in outputLine) and ('YX=  ' in outputLine) and ('ZX=  ' in outputLine):
			ten_xx.append(-float(outputLine.rstrip().split()[1]))
			ten_yx.append(-float(outputLine.rstrip().split()[3]))
			ten_zx.append(-float(outputLine.rstrip().split()[5]))
			#shielTensor.append(outputLine.rstrip())
		elif ('XY=  ' in outputLine) and ('YY=  ' in outputLine) and ('ZY=  ' in outputLine):
			ten_xy.append(-float(outputLine.rstrip().split()[1]))
			ten_yy.append(-float(outputLine.rstrip().split()[3]))
			ten_zy.append(-float(outputLine.rstrip().split()[5]))
			#shielTensor.append(outputLine.rstrip())
		elif ('XZ=  ' in outputLine) and ('YZ=  ' in outputLine) and ('ZZ=  ' in outputLine):
			ten_xz.append(-float(outputLine.rstrip().split()[1]))
			ten_yz.append(-float(outputLine.rstrip().split()[3]))
			ten_zz.append(-float(outputLine.rstrip().split()[5]))
			#shielTensor.append(outputLine.rstrip())
	
	ten_iso = ten_iso[-len(x_all):]
	ten_ani = ten_ani[-len(x_all):]
	ten_xx = ten_xx[-len(x_all):]
	ten_xy = ten_xy[-len(x_all):]
	ten_xz = ten_xz[-len(x_all):]
	ten_yx = ten_yx[-len(x_all):]
	ten_yy = ten_yy[-len(x_all):]
	ten_yz = ten_yz[-len(x_all):]
	ten_zx = ten_zx[-len(x_all):]
	ten_zy = ten_zy[-len(x_all):]
	ten_zz = ten_zz[-len(x_all):]

	x_set = sorted(set(x_all))
	y_set = sorted(set(y_all))
	z_set = sorted(set(z_all))
	xo_max, xo_min = max(x_set), min(x_set)
	yo_max, yo_min = max(y_set), min(y_set)
	zo_max, zo_min = max(z_set), min(z_set)

	planeFlag = 0
	if len(x_set) == 1:
		planeFlag = 3
		y_step = y_set[1] - y_set[0]
		z_step = z_set[1] - z_set[0]
	elif len(y_set) == 1:
		planeFlag = 2
		x_step = x_set[1] - x_set[0]
		z_step = z_set[1] - z_set[0]
	elif len(z_set) == 1:
		planeFlag = 1
		x_step = x_set[1] - x_set[0]
		y_step = y_set[1] - y_set[0]

	if nicsTensor == 'isotropic':
		mapValue = ten_iso
	elif nicsTensor == 'anisotropic':
		mapValue = ten_ani
	elif nicsTensor == 'xx':
		mapValue = ten_xx
	elif nicsTensor == 'yx':
		mapValue = ten_yx
	elif nicsTensor == 'zx':
		mapValue = ten_zx
	elif nicsTensor == 'xy':
		mapValue = ten_xy
	elif nicsTensor == 'yy':
		mapValue = ten_yy
	elif nicsTensor == 'zy':
		mapValue = ten_zy
	elif nicsTensor == 'xz':
		mapValue = ten_xz
	elif nicsTensor == 'yz':
		mapValue = ten_yz
	elif nicsTensor == 'zz':
		mapValue = ten_zz

	icssOutput = open(f"{fName[:-4]}_2DNICS_output_{nicsTensor.upper()}.csv", 'w')

	icssOutput.write(f"# Data from {fName}.\n")
	icssOutput.write(f"# Shielding tensor data from {nicsTensor.upper()} component.\n")
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

	fig.savefig(f"{fName.strip()[:-4]}_2DNICS_output_{nicsTensor.upper()}.png")

def n2outShow(fName, nicsTensor):
	with open(fName, 'r') as usrOutFile:
		gauOut = usrOutFile.readlines()

	coorBq = []
	shielTensor = []

	x_all = []
	y_all = []
	z_all = []

	ten_iso = []
	ten_ani = []
	ten_xx = []
	ten_xy = []
	ten_xz = []
	ten_yx = []
	ten_yy = []
	ten_yz = []
	ten_zx = []
	ten_zy = []
	ten_zz = []

	for outputLine in gauOut:
		if ' Bq    ' in outputLine and outputLine.count('.') == 3 and len(outputLine.split()) == 4:
			x_all.append(float(outputLine.rstrip().split()[1]))
			y_all.append(float(outputLine.rstrip().split()[2]))
			z_all.append(float(outputLine.rstrip().split()[3]))
		elif 'Isotropic =' in outputLine:
			ten_iso.append(-float(outputLine.rstrip().split()[4]))
			ten_ani.append(-float(outputLine.rstrip().split()[7]))
		elif ('XX=  ' in outputLine) and ('YX=  ' in outputLine) and ('ZX=  ' in outputLine):
			ten_xx.append(-float(outputLine.rstrip().split()[1]))
			ten_yx.append(-float(outputLine.rstrip().split()[3]))
			ten_zx.append(-float(outputLine.rstrip().split()[5]))
		elif ('XY=  ' in outputLine) and ('YY=  ' in outputLine) and ('ZY=  ' in outputLine):
			ten_xy.append(-float(outputLine.rstrip().split()[1]))
			ten_yy.append(-float(outputLine.rstrip().split()[3]))
			ten_zy.append(-float(outputLine.rstrip().split()[5]))
		elif ('XZ=  ' in outputLine) and ('YZ=  ' in outputLine) and ('ZZ=  ' in outputLine):
			ten_xz.append(-float(outputLine.rstrip().split()[1]))
			ten_yz.append(-float(outputLine.rstrip().split()[3]))
			ten_zz.append(-float(outputLine.rstrip().split()[5]))

	ten_iso = ten_iso[-len(x_all):]
	ten_ani = ten_ani[-len(x_all):]
	ten_xx = ten_xx[-len(x_all):]
	ten_xy = ten_xy[-len(x_all):]
	ten_xz = ten_xz[-len(x_all):]
	ten_yx = ten_yx[-len(x_all):]
	ten_yy = ten_yy[-len(x_all):]
	ten_yz = ten_yz[-len(x_all):]
	ten_zx = ten_zx[-len(x_all):]
	ten_zy = ten_zy[-len(x_all):]
	ten_zz = ten_zz[-len(x_all):]

	x_set = sorted(set(x_all))
	y_set = sorted(set(y_all))
	z_set = sorted(set(z_all))
	xo_max, xo_min = max(x_set), min(x_set)
	yo_max, yo_min = max(y_set), min(y_set)
	zo_max, zo_min = max(z_set), min(z_set)

	planeFlag = 0
	if len(x_set) == 1:
		planeFlag = 3
		y_step = y_set[1] - y_set[0]
		z_step = z_set[1] - z_set[0]
	elif len(y_set) == 1:
		planeFlag = 2
		x_step = x_set[1] - x_set[0]
		z_step = z_set[1] - z_set[0]
	elif len(z_set) == 1:
		planeFlag = 1
		x_step = x_set[1] - x_set[0]
		y_step = y_set[1] - y_set[0]

	if nicsTensor == 'isotropic':
		mapValue = ten_iso
	elif nicsTensor == 'anisotropic':
		mapValue = ten_ani
	elif nicsTensor == 'xx':
		mapValue = ten_xx
	elif nicsTensor == 'yx':
		mapValue = ten_yx
	elif nicsTensor == 'zx':
		mapValue = ten_zx
	elif nicsTensor == 'xy':
		mapValue = ten_xy
	elif nicsTensor == 'yy':
		mapValue = ten_yy
	elif nicsTensor == 'zy':
		mapValue = ten_zy
	elif nicsTensor == 'xz':
		mapValue = ten_xz
	elif nicsTensor == 'yz':
		mapValue = ten_yz
	elif nicsTensor == 'zz':
		mapValue = ten_zz

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

	return fig, ax