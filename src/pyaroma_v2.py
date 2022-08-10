from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
import sys
from matplotlib import cm
from matplotlib.ticker import LinearLocator
from mpl_toolkits.mplot3d import axes3d
import webbrowser
import inpReader
import findMm
from const import *
from inpGen import *
from N1addBq import *
from N2out import *
from N3out import *

def import_file():
    global fName
    fTyp = [('All files', '*.*')]
    iDir = '/home/wangzhe/Desktop/mol_test/'         #iDir = '/home/'
    csvfilepath = filedialog.askopenfilename(filetypes = fTyp, initialdir = iDir, title = 'Choose file')
    fName.set(csvfilepath)
    global fileName
    fileName = fName.get()

def first_open():
	global fileName
	global xyzcoor
	global xmin
	global xmax
	global ymin
	global ymax
	global zmin
	global zmax
	global xcoor
	global ycoor
	global zcoor
	global colorList

	def nics1d():
		fig2 = plt.figure()
		ax2 = fig2.add_subplot(projection='3d')
		ax2.xaxis.pane.fill = False
		ax2.yaxis.pane.fill = False
		ax2.zaxis.pane.fill = False
		ax2.xaxis.pane.set_edgecolor('w')
		ax2.yaxis.pane.set_edgecolor('w')
		ax2.zaxis.pane.set_edgecolor('w')
		ax2.grid(False)
		if xmax == xmin:
			ax2.set_xlim(xmin - 1, xmin + 1)
			ax2.set_box_aspect([2, ymax-ymin, zmax-zmin])
		elif ymax == ymin:
			ax2.set_ylim(ymin - 1, ymin + 1)
			ax2.set_box_aspect([xmax-xmin, 2, zmax-zmin])
		elif zmax == zmin:
			ax2.set_zlim(zmin - 1, zmin + 1)
			ax2.set_box_aspect([xmax-xmin, ymax-ymin, 2])
		else:
			ax2.set_box_aspect([xmax-xmin, ymax-ymin, zmax-zmin])
		ax2.scatter(np.array([xcoor]), np.array([ycoor]), np.array([zcoor]), color = colorList, edgecolors = '0.0')
		for ino in range(len(xyzcoor)):
			ax2.text(xcoor[ino], ycoor[ino], zcoor[ino], str(ino+1))
		for j in range(len(xyzcoor)):
			for k in range(j + 1, len(xyzcoor)):
				dis = (xyzcoor[j][1] - xyzcoor[k][1]) * (xyzcoor[j][1] - xyzcoor[k][1]) + (xyzcoor[j][2] - xyzcoor[k][2]) * (xyzcoor[j][2] \
					- xyzcoor[k][2]) + (xyzcoor[j][3] - xyzcoor[k][3]) * (xyzcoor[j][3] - xyzcoor[k][3])
				if dis <= (ATOM_RADII[periodTable.index(xyzcoor[j][0].upper())] + ATOM_RADII[periodTable.index(xyzcoor[k][0].upper())]) * \
					(ATOM_RADII[periodTable.index(xyzcoor[j][0].upper())] + ATOM_RADII[periodTable.index(xyzcoor[k][0].upper())]):
					ax2.plot([xyzcoor[j][1], xyzcoor[k][1]] , [xyzcoor[j][2], xyzcoor[k][2]], [xyzcoor[j][3], xyzcoor[k][3]], '0.5')		

		ax2.set_xlabel('X')
		ax2.set_ylabel('Y')
		ax2.set_zlabel('Z')
		figWin2 = Toplevel()
		figWin2.title(fileName)
		canvas2 = FigureCanvasTkAgg(fig2, figWin2)
		canvas2.get_tk_widget().pack(expand = True, fill = 'both')

		frame_1d = LabelFrame(figWin2, text = '   1D NICS Parameters:   ', font = ('Helvetica', 16, 'bold'), padx = 10, pady = 10)
		frame_1d.pack(padx = 20, pady = 20, fill = 'x')

		global atm1, atm2, atm3, atm4, atm5, atm6, atm7, atm8, atm9, atm10
		atm1.set('0')
		atm2.set('0')
		atm3.set('0')
		atm4.set('0')
		atm5.set('0')
		atm6.set('0')
		atm7.set('0')
		atm8.set('0')
		atm9.set('0')
		atm10.set('0')
		Label(frame_1d, text = '   Atom No.: ', font = ('Helvetica',)).grid(row = 0, column = 0)
		Spinbox(frame_1d, textvariable = atm1, from_ = 0, to = len(xyzcoor), increment = 1, width = 3).grid(row = 0, column = 1)
		Spinbox(frame_1d, textvariable = atm2, from_ = 0, to = len(xyzcoor), increment = 1, width = 3).grid(row = 0, column = 2)
		Spinbox(frame_1d, textvariable = atm3, from_ = 0, to = len(xyzcoor), increment = 1, width = 3).grid(row = 0, column = 3)
		Spinbox(frame_1d, textvariable = atm4, from_ = 0, to = len(xyzcoor), increment = 1, width = 3).grid(row = 0, column = 4)
		Spinbox(frame_1d, textvariable = atm5, from_ = 0, to = len(xyzcoor), increment = 1, width = 3).grid(row = 0, column = 5)
		Spinbox(frame_1d, textvariable = atm6, from_ = 0, to = len(xyzcoor), increment = 1, width = 3).grid(row = 0, column = 6)
		Spinbox(frame_1d, textvariable = atm7, from_ = 0, to = len(xyzcoor), increment = 1, width = 3).grid(row = 0, column = 7)
		Spinbox(frame_1d, textvariable = atm8, from_ = 0, to = len(xyzcoor), increment = 1, width = 3).grid(row = 0, column = 8)
		Spinbox(frame_1d, textvariable = atm9, from_ = 0, to = len(xyzcoor), increment = 1, width = 3).grid(row = 0, column = 9)
		Spinbox(frame_1d, textvariable = atm10, from_ = 0, to = len(xyzcoor), increment = 1, width = 3).grid(row = 0, column = 10)

		global n1_hei
		n1_hei.set('0.0')
		Label(frame_1d, text = '   Altitude: ', font = ('Helvetica',)).grid(row = 0, column = 11)
		Spinbox(frame_1d, textvariable = n1_hei, from_ = -999.0, to = 999.9, increment = 0.1, width = 3).grid(row = 0, column = 12)

		def addBq():
			global atm1, atm2, atm3, atm4, atm5, atm6, atm7, atm8, atm9, atm10, n1_hei
			global n1bqlist
			usrList = [int(atm1.get()), int(atm2.get()), int(atm3.get()), int(atm4.get()), int(atm5.get()), int(atm6.get()), \
				int(atm7.get()), int(atm8.get()), int(atm9.get()), int(atm10.get())]
			if float(n1_hei.get()) == 0.0:
				bq0x, bq0y, bq0z = calCoor(usrList, n1_hei.get(), xyzcoor)
				n1bqlist.append([bq0x, bq0y, bq0z])
				ax2.scatter(np.array([bq0x]), np.array([bq0y]), np.array([bq0z]), color = [0.898, 0.2, 1.0], edgecolors = [0.898, 0.2, 1.0])
			else:
				bq0x1, bq0y1, bq0z1, bq0x2, bq0y2, bq0z2 = calCoor(usrList, n1_hei.get(), xyzcoor)
				n1bqlist.append([bq0x1, bq0y1, bq0z1])
				n1bqlist.append([bq0x2, bq0y2, bq0z2])
				ax2.scatter(np.array([bq0x1]), np.array([bq0y1]), np.array([bq0z1]), color = [0.898, 0.2, 1.0], edgecolors = [0.898, 0.2, 1.0])
				ax2.scatter(np.array([bq0x2]), np.array([bq0y2]), np.array([bq0z2]), color = [0.898, 0.2, 1.0], edgecolors = [0.898, 0.2, 1.0])

		frame_1d_g = LabelFrame(figWin2, text = '   Gaussian Calculation Setup: (Only valid when reading structure from .pdb/.xyz files)  ', font = ('Helvetica', 16, 'bold'), padx = 10, pady = 10)
		frame_1d_g.pack(padx = 20, pady = 20, fill = 'x')

		global nmr_type
		nmr_type.set('giao')
		Label(frame_1d_g, text = '   NMR Method:', font = ('Helvetica',)).grid(row = 0, column = 0)
		Radiobutton(frame_1d_g, text = 'GIAO', variable = nmr_type, value = 'giao').grid(row = 0, column = 1)
		Radiobutton(frame_1d_g, text = 'CSGT', variable = nmr_type, value = 'csgt').grid(row = 0, column = 2)
		Radiobutton(frame_1d_g, text = 'IGAIM', variable = nmr_type, value = 'igaim').grid(row = 0, column = 3)
		Radiobutton(frame_1d_g, text = 'CSGT, IGAGIM and Single Origin', variable = nmr_type, value = 'all').grid(row = 0, column = 4, columnspan = 3)

		global ru_method
		ru_method.set(' ')
		Label(frame_1d_g, text = '  Calculation:', font = ('Helvetica',)).grid(row = 1, column = 0)
		Radiobutton(frame_1d_g, text = 'Default', variable = ru_method, value = ' ').grid(row = 1, column = 1)
		Radiobutton(frame_1d_g, text = 'Restricted', variable = ru_method, value = 'r').grid(row = 1, column = 2)
		Radiobutton(frame_1d_g, text = 'Unrestricted', variable = ru_method, value = 'u').grid(row = 1, column = 3)
		Radiobutton(frame_1d_g, text = 'Restricted-open', variable = ru_method, value = 'ro').grid(row = 1, column = 4, columnspan = 2)

		global dft
		dft.set('B3LYP')
		Label(frame_1d_g, text = '   Functionals:', font = ('Helvetica',)).grid(row = 2, column = 0)
		Entry(frame_1d_g, textvariable = dft, width = 8).grid(row = 2, column = 1)

		global basis
		basis.set('6-311+G(d,p)')
		Label(frame_1d_g, text = '   Basis Set:', font = ('Helvetica',)).grid(row = 2, column = 2)
		Entry(frame_1d_g, textvariable = basis, width = 12).grid(row = 2, column = 3)

		Label(frame_1d_g, text = '   Charge:', font = ('Helvetica',)).grid(row = 2, column = 4)
		global charge
		charge.set('0')
		Spinbox(frame_1d_g, textvariable = charge, from_ = -99999, to = 99999, increment = 1, width = 5).grid(row = 2, column = 5)
		Label(frame_1d_g, text = '   Spin:', font = ('Helvetica',)).grid(row = 2, column = 6)
		global spin
		spin.set('1')
		Spinbox(frame_1d_g, textvariable = spin, from_ = 1, to = 99999, increment = 1, width = 5).grid(row = 2, column = 7)

		Label(frame_1d_g, text = '   Memory:', font = ('Helvetica',)).grid(row = 3, column = 0)
		global mem
		mem.set('Default')
		Entry(frame_1d_g, textvariable = mem, width = 8).grid(row = 3, column = 1)
		Label(frame_1d_g, text = '   Processors:', font = ('Helvetica',)).grid(row = 3, column = 2)
		global cpu
		cpu.set('Default')
		Entry(frame_1d_g, textvariable = cpu, width = 8).grid(row = 3, column = 3)

		Label(frame_1d_g, text = 'Addtional Keyword:', font = ('Helvetica',)).grid(row = 4, column = 0)
		global addkey
		addkey.set(' ')
		Entry(frame_1d_g, textvariable = addkey, width = 50).grid(row = 4, column = 1, columnspan = 5)

		def save_1d():
			global nmr_type, ru_method, fileName
			global dft, basis, charge, spin, mem, cpu
			global xyzcoor, n1bqlist
			n1inp(fileName, cpu.get(), mem.get(), nmr_type.get(), ru_method.get(), \
				dft.get(), basis.get(), addkey.get(), charge.get(), spin.get(), xyzcoor, n1bqlist)
			messagebox.showwarning("Finished", "Input file has been generated successfully.")

		Button(frame_1d, text = 'Add', command = addBq).grid(row = 0, column = 13)
		Button(frame_1d_g, text = 'Save Input File', command = save_1d).grid(row = 4, column = 6, columnspan = 2)

# 2D NICS Section
	def nics2d():
		global fig3, ax3
		fig3 = plt.figure()
		ax3 = fig3.add_subplot(projection='3d')
		ax3.xaxis.pane.fill = False
		ax3.yaxis.pane.fill = False
		ax3.zaxis.pane.fill = False
		ax3.xaxis.pane.set_edgecolor('w')
		ax3.yaxis.pane.set_edgecolor('w')
		ax3.zaxis.pane.set_edgecolor('w')
		ax3.grid(False)
		if xmax == xmin:
			ax3.set_xlim(xmin - 1, xmin + 1)
			ax3.set_box_aspect([0.02, ymax-ymin, zmax-zmin])
		elif ymax == ymin:
			ax3.set_ylim(ymin - 1, ymin + 1)
			ax3.set_box_aspect([xmax-xmin, 0.02, zmax-zmin])
		elif zmax == zmin:
			ax3.set_zlim(zmin - 1, zmin + 1)
			ax3.set_box_aspect([xmax-xmin, ymax-ymin, 0.02])
		else:
			ax3.set_box_aspect([xmax-xmin, ymax-ymin, zmax-zmin])
		ax3.scatter(np.array([xcoor]), np.array([ycoor]), np.array([zcoor]), color = colorList, edgecolors = '0.0')
		for j in range(len(xyzcoor)):
			for k in range(j + 1, len(xyzcoor)):
				dis = (xyzcoor[j][1] - xyzcoor[k][1]) * (xyzcoor[j][1] - xyzcoor[k][1]) + (xyzcoor[j][2] - xyzcoor[k][2]) * (xyzcoor[j][2] \
					- xyzcoor[k][2]) + (xyzcoor[j][3] - xyzcoor[k][3]) * (xyzcoor[j][3] - xyzcoor[k][3])
				if dis <= (ATOM_RADII[periodTable.index(xyzcoor[j][0].upper())] + ATOM_RADII[periodTable.index(xyzcoor[k][0].upper())]) * \
					(ATOM_RADII[periodTable.index(xyzcoor[j][0].upper())] + ATOM_RADII[periodTable.index(xyzcoor[k][0].upper())]):
					ax3.plot([xyzcoor[j][1], xyzcoor[k][1]] , [xyzcoor[j][2], xyzcoor[k][2]], [xyzcoor[j][3], xyzcoor[k][3]], '0.5')		

		ax3.set_xlabel('X')
		ax3.set_ylabel('Y')
		ax3.set_zlabel('Z')
		figWin3 = Toplevel()
		figWin3.title(fileName)
		canvas3 = FigureCanvasTkAgg(fig3, figWin3)
		canvas3.get_tk_widget().pack(expand = True, fill = 'both')

		def renew2d():
			global fig3, ax3, nics_2d_plane
			plt.cla()

			ax3.xaxis.pane.fill = False
			ax3.yaxis.pane.fill = False
			ax3.zaxis.pane.fill = False
			ax3.xaxis.pane.set_edgecolor('w')
			ax3.yaxis.pane.set_edgecolor('w')
			ax3.zaxis.pane.set_edgecolor('w')
			ax3.grid(False)
			if xmax == xmin:
				ax3.set_xlim(xmin - 1, xmin + 1)
				ax3.set_box_aspect([2, ymax-ymin, zmax-zmin])
			elif ymax == ymin:
				ax3.set_ylim(ymin - 1, ymin + 1)
				ax3.set_box_aspect([xmax-xmin, 2, zmax-zmin])
			elif zmax == zmin:
				ax3.set_zlim(zmin - 1, zmin + 1)
				ax3.set_box_aspect([xmax-xmin, ymax-ymin, 2])
			else:
				ax3.set_box_aspect([xmax-xmin, ymax-ymin, zmax-zmin])
			ax3.scatter(np.array([xcoor]), np.array([ycoor]), np.array([zcoor]), color = colorList, edgecolors = '0.0')
			for j in range(len(xyzcoor)):
				for k in range(j + 1, len(xyzcoor)):
					dis = (xyzcoor[j][1] - xyzcoor[k][1]) * (xyzcoor[j][1] - xyzcoor[k][1]) + (xyzcoor[j][2] - xyzcoor[k][2]) * (xyzcoor[j][2] \
						- xyzcoor[k][2]) + (xyzcoor[j][3] - xyzcoor[k][3]) * (xyzcoor[j][3] - xyzcoor[k][3])
					if dis <= (ATOM_RADII[periodTable.index(xyzcoor[j][0].upper())] + ATOM_RADII[periodTable.index(xyzcoor[k][0].upper())]) * \
						(ATOM_RADII[periodTable.index(xyzcoor[j][0].upper())] + ATOM_RADII[periodTable.index(xyzcoor[k][0].upper())]):
						ax3.plot([xyzcoor[j][1], xyzcoor[k][1]] , [xyzcoor[j][2], xyzcoor[k][2]], [xyzcoor[j][3], xyzcoor[k][3]], '0.5')
			if str(nics_2d_plane.get()) == 'xy':
				x_poly = [float(x_left.get()), float(x_right.get()), float(x_right.get()), float(x_left.get())]
				y_poly = [float(y_left.get()), float(y_left.get()), float(y_right.get()), float(y_right.get())]
				z_poly = [float(plane_hei.get()), float(plane_hei.get()), float(plane_hei.get()), float(plane_hei.get())]
				poly = list(zip(x_poly, y_poly, z_poly))
				ax3.add_collection3d(Poly3DCollection([poly], facecolor = '#000080', alpha = 0.3))
			elif str(nics_2d_plane.get()) == 'yz':
				y_poly = [float(y_left.get()), float(y_right.get()), float(y_right.get()), float(y_left.get())]
				z_poly = [float(z_left.get()), float(z_left.get()), float(z_right.get()), float(z_right.get())]
				x_poly = [float(plane_hei.get()), float(plane_hei.get()), float(plane_hei.get()), float(plane_hei.get())]
				poly = list(zip(x_poly, y_poly, z_poly))
				ax3.add_collection3d(Poly3DCollection([poly], facecolor = '#000080', alpha = 0.3))
			elif str(nics_2d_plane.get()) == 'xz':
				x_poly = [float(x_left.get()), float(x_right.get()), float(x_right.get()), float(x_left.get())]
				z_poly = [float(z_left.get()), float(z_left.get()), float(z_right.get()), float(z_right.get())]
				y_poly = [float(plane_hei.get()), float(plane_hei.get()), float(plane_hei.get()), float(plane_hei.get())]
				poly = list(zip(x_poly, y_poly, z_poly))
				ax3.add_collection3d(Poly3DCollection([poly], facecolor = '#000080', alpha = 0.3))
			ax3.set_xlabel('X')
			ax3.set_ylabel('Y')
			ax3.set_zlabel('Z')

		frame_2d = LabelFrame(figWin3, text = '   2D NICS Parameters:   ', font = ('Helvetica', 16, 'bold'), padx = 10, pady = 10)
		frame_2d.pack(padx = 20, pady = 20, fill = 'x')

		global nics_2d_plane
		nics_2d_plane.set('xy')
		Label(frame_2d, text = '    Plane: ', font = ('Helvetica',)).grid(row = 0, column = 0)
		Radiobutton(frame_2d, text = 'XY', variable = nics_2d_plane, value = 'xy').grid(row = 0, column = 1)
		Radiobutton(frame_2d, text = 'YZ', variable = nics_2d_plane, value = 'yz').grid(row = 0, column = 2)
		Radiobutton(frame_2d, text = 'XZ', variable = nics_2d_plane, value = 'xz').grid(row = 0, column = 3)
		Label(frame_2d, text = '   Height: ', font = ('Helvetica',)).grid(row = 0, column = 4)
		global plane_hei
		plane_hei.set('0.0')
		Spinbox(frame_2d, textvariable = plane_hei, from_ = -99999.0, to = 99999.0, increment = 0.1, format = '%1.1f', width = 5, command = renew2d).grid(row = 0, column = 5)
		Label(frame_2d, text = '   Grid: ', font = ('Helvetica',)).grid(row = 0, column = 6)
		global grid
		grid.set('0.20')
		Spinbox(frame_2d, textvariable = grid, from_ = 0.05, to = 0.50, increment = 0.05, format = '%1.2f', width = 5).grid(row = 0, column = 7)

		global x_left
		x_left.set(f'{xmin - 1}')
		Label(frame_2d, text = '   x(min): ', font = ('Helvetica',)).grid(row = 1, column = 0)
		Spinbox(frame_2d, textvariable = x_left, from_ = -99999.0, to = 99999.0, increment = 0.1, format = '%1.1f', width = 5, command = renew2d).grid(row = 1, column = 1)

		global x_right
		x_right.set(f'{xmax + 1}')
		Label(frame_2d, text = '   x(max): ', font = ('Helvetica',)).grid(row = 1, column = 2)
		Spinbox(frame_2d, textvariable = x_right, from_ = -99999.0, to = 99999.0, increment = 0.1, format = '%1.1f', width = 5, command = renew2d).grid(row = 1, column = 3)

		global y_left
		y_left.set(f'{ymin - 1}')
		Label(frame_2d, text = '   y(min): ', font = ('Helvetica',)).grid(row = 1, column = 4)
		Spinbox(frame_2d, textvariable = y_left, from_ = -99999.0, to = 99999.0, increment = 0.1, format = '%1.1f', width = 5, command = renew2d).grid(row = 1, column = 5)

		global y_right
		y_right.set(f'{ymax + 1}')
		Label(frame_2d, text = '   y(max): ', font = ('Helvetica',)).grid(row = 1, column = 6)
		Spinbox(frame_2d, textvariable = y_right, from_ = -99999.0, to = 99999.0, increment = 0.1, format = '%1.1f', width = 5, command = renew2d).grid(row = 1, column = 7)

		global z_left
		z_left.set(f'{zmin - 1}')
		Label(frame_2d, text = '   z(min): ', font = ('Helvetica',)).grid(row = 1, column = 8)
		Spinbox(frame_2d, textvariable = z_left, from_ = -99999.0, to = 99999.0, increment = 0.1, format = '%1.1f', width = 5, command = renew2d).grid(row = 1, column = 9)

		global z_right
		z_right.set(f'{zmax + 1}')
		Label(frame_2d, text = '   z(max): ', font = ('Helvetica',)).grid(row = 1, column = 10)
		Spinbox(frame_2d, textvariable = z_right, from_ = -99999.0, to = 99999.0, increment = 0.1, format = '%1.1f', width = 5, command = renew2d).grid(row = 1, column = 11)

		def nics2d_ok():
			global fig3, ax3, nics_2d_plane
			plt.cla()

			ax3.xaxis.pane.fill = False
			ax3.yaxis.pane.fill = False
			ax3.zaxis.pane.fill = False
			ax3.xaxis.pane.set_edgecolor('w')
			ax3.yaxis.pane.set_edgecolor('w')
			ax3.zaxis.pane.set_edgecolor('w')
			ax3.grid(False)
			if xmax == xmin:
				ax3.set_xlim(xmin - 1, xmin + 1)
				ax3.set_box_aspect([2, ymax-ymin, zmax-zmin])
			elif ymax == ymin:
				ax3.set_ylim(ymin - 1, ymin + 1)
				ax3.set_box_aspect([xmax-xmin, 2, zmax-zmin])
			elif zmax == zmin:
				ax3.set_zlim(zmin - 1, zmin + 1)
				ax3.set_box_aspect([xmax-xmin, ymax-ymin, 2])
			else:
				ax3.set_box_aspect([xmax-xmin, ymax-ymin, zmax-zmin])
			ax3.scatter(np.array([xcoor]), np.array([ycoor]), np.array([zcoor]), color = colorList, edgecolors = '0.0')
			for j in range(len(xyzcoor)):
				for k in range(j + 1, len(xyzcoor)):
					dis = (xyzcoor[j][1] - xyzcoor[k][1]) * (xyzcoor[j][1] - xyzcoor[k][1]) + (xyzcoor[j][2] - xyzcoor[k][2]) * (xyzcoor[j][2] \
						- xyzcoor[k][2]) + (xyzcoor[j][3] - xyzcoor[k][3]) * (xyzcoor[j][3] - xyzcoor[k][3])
					if dis <= (ATOM_RADII[periodTable.index(xyzcoor[j][0].upper())] + ATOM_RADII[periodTable.index(xyzcoor[k][0].upper())]) * \
						(ATOM_RADII[periodTable.index(xyzcoor[j][0].upper())] + ATOM_RADII[periodTable.index(xyzcoor[k][0].upper())]):
						ax3.plot([xyzcoor[j][1], xyzcoor[k][1]] , [xyzcoor[j][2], xyzcoor[k][2]], [xyzcoor[j][3], xyzcoor[k][3]], '0.5')
			if str(nics_2d_plane.get()) == 'xy':
				x_poly = [float(x_left.get()), float(x_right.get()), float(x_right.get()), float(x_left.get())]
				y_poly = [float(y_left.get()), float(y_left.get()), float(y_right.get()), float(y_right.get())]
				z_poly = [float(plane_hei.get()), float(plane_hei.get()), float(plane_hei.get()), float(plane_hei.get())]
				poly = list(zip(x_poly, y_poly, z_poly))
				ax3.add_collection3d(Poly3DCollection([poly], facecolor = '#000080', alpha = 0.3))
			elif str(nics_2d_plane.get()) == 'yz':
				y_poly = [float(y_left.get()), float(y_right.get()), float(y_right.get()), float(y_left.get())]
				z_poly = [float(z_left.get()), float(z_left.get()), float(z_right.get()), float(z_right.get())]
				x_poly = [float(plane_hei.get()), float(plane_hei.get()), float(plane_hei.get()), float(plane_hei.get())]
				poly = list(zip(x_poly, y_poly, z_poly))
				ax3.add_collection3d(Poly3DCollection([poly], facecolor = '#000080', alpha = 0.3))
			elif str(nics_2d_plane.get()) == 'xz':
				x_poly = [float(x_left.get()), float(x_right.get()), float(x_right.get()), float(x_left.get())]
				z_poly = [float(z_left.get()), float(z_left.get()), float(z_right.get()), float(z_right.get())]
				y_poly = [float(plane_hei.get()), float(plane_hei.get()), float(plane_hei.get()), float(plane_hei.get())]
				poly = list(zip(x_poly, y_poly, z_poly))
				ax3.add_collection3d(Poly3DCollection([poly], facecolor = '#000080', alpha = 0.3))
			ax3.set_xlabel('X')
			ax3.set_ylabel('Y')
			ax3.set_zlabel('Z')

		Button(frame_2d, text = 'Update', command = nics2d_ok).grid(row = 0, column = 11)

		frame_2d_g = LabelFrame(figWin3, text = '   Gaussian Calculation Setup: (Only valid when reading structure from .pdb/.xyz files)  ', font = ('Helvetica', 16, 'bold'), padx = 10, pady = 10)
		frame_2d_g.pack(padx = 20, pady = 20, fill = 'x')

		global nmr_type
		nmr_type.set('giao')
		Label(frame_2d_g, text = '   NMR Method:', font = ('Helvetica',)).grid(row = 0, column = 0)
		Radiobutton(frame_2d_g, text = 'GIAO', variable = nmr_type, value = 'giao').grid(row = 0, column = 1)
		Radiobutton(frame_2d_g, text = 'CSGT', variable = nmr_type, value = 'csgt').grid(row = 0, column = 2)
		Radiobutton(frame_2d_g, text = 'IGAIM', variable = nmr_type, value = 'igaim').grid(row = 0, column = 3)
		Radiobutton(frame_2d_g, text = 'CSGT, IGAGIM and Single Origin', variable = nmr_type, value = 'all').grid(row = 0, column = 4, columnspan = 3)

		global ru_method
		ru_method.set(' ')
		Label(frame_2d_g, text = '  Calculation:', font = ('Helvetica',)).grid(row = 1, column = 0)
		Radiobutton(frame_2d_g, text = 'Default', variable = ru_method, value = ' ').grid(row = 1, column = 1)
		Radiobutton(frame_2d_g, text = 'Restricted', variable = ru_method, value = 'r').grid(row = 1, column = 2)
		Radiobutton(frame_2d_g, text = 'Unrestricted', variable = ru_method, value = 'u').grid(row = 1, column = 3)
		Radiobutton(frame_2d_g, text = 'Restricted-open', variable = ru_method, value = 'ro').grid(row = 1, column = 4, columnspan = 2)

		global dft
		dft.set('B3LYP')
		Label(frame_2d_g, text = '   Functionals:', font = ('Helvetica',)).grid(row = 2, column = 0)
		Entry(frame_2d_g, textvariable = dft, width = 8).grid(row = 2, column = 1)

		global basis
		basis.set('6-311+G(d,p)')
		Label(frame_2d_g, text = '   Basis Set:', font = ('Helvetica',)).grid(row = 2, column = 2)
		Entry(frame_2d_g, textvariable = basis, width = 12).grid(row = 2, column = 3)

		Label(frame_2d_g, text = '   Charge:', font = ('Helvetica',)).grid(row = 2, column = 4)
		global charge
		charge.set('0')
		Spinbox(frame_2d_g, textvariable = charge, from_ = -99999, to = 99999, increment = 1, width = 5).grid(row = 2, column = 5)
		Label(frame_2d_g, text = '   Spin:', font = ('Helvetica',)).grid(row = 2, column = 6)
		global spin
		spin.set('1')
		Spinbox(frame_2d_g, textvariable = spin, from_ = 1, to = 99999, increment = 1, width = 5).grid(row = 2, column = 7)

		Label(frame_2d_g, text = '   Memory:', font = ('Helvetica',)).grid(row = 3, column = 0)
		global mem
		mem.set('Default')
		Entry(frame_2d_g, textvariable = mem, width = 8).grid(row = 3, column = 1)
		Label(frame_2d_g, text = '   Processors:', font = ('Helvetica',)).grid(row = 3, column = 2)
		global cpu
		cpu.set('Default')
		Entry(frame_2d_g, textvariable = cpu, width = 8).grid(row = 3, column = 3)

		Label(frame_2d_g, text = 'Addtional Keyword:', font = ('Helvetica',)).grid(row = 4, column = 0)
		global addkey
		addkey.set(' ')
		Entry(frame_2d_g, textvariable = addkey, width = 50).grid(row = 4, column = 1, columnspan = 5)

		def save_2d():
			global nmr_type, ru_method, fileName
			global dft, basis, charge, spin, mem, cpu
			global xyzcoor, nics_2d_plane, plane_hei, grid
			global x_left, x_right, y_left, y_right, z_left, z_right
			atomNo = n2inp(fileName, cpu.get(), mem.get(), nmr_type.get(), ru_method.get(), \
				dft.get(), basis.get(), addkey.get(), charge.get(), spin.get(), xyzcoor, nics_2d_plane.get(), \
				x_left.get(), x_right.get(), y_left.get(), y_right.get(), z_left.get(), z_right.get(), plane_hei.get(), grid.get())
			if atomNo > 8000:
				messagebox.showwarning("WARNING", f"Total number of atoms ({atomNo}) in this input file exceed the limitation \
					of Gaussian, which was 8000. Thus, the calculation could not be normal terminated. Please try: (1) separate into \
					more input files; (2) use larger grid quality value; or (3) decrease the plotting region. Input file has been \
					generated successfully.")
			else:
				messagebox.showwarning("Finished", "Input file has been generated successfully.")
		Button(frame_2d_g, text = 'Save Input File', command = save_2d).grid(row = 4, column = 6, columnspan = 2)

# 3D NICS Section
	def nics3d():
		global fig4, ax4
		fig4 = plt.figure()
		ax4 = fig4.add_subplot(projection='3d')
		ax4.xaxis.pane.fill = False
		ax4.yaxis.pane.fill = False
		ax4.zaxis.pane.fill = False
		ax4.xaxis.pane.set_edgecolor('w')
		ax4.yaxis.pane.set_edgecolor('w')
		ax4.zaxis.pane.set_edgecolor('w')
		ax4.grid(False)
		if xmax == xmin:
			ax4.set_xlim(xmin - 1, xmin + 1)
			ax4.set_box_aspect([2, ymax-ymin, zmax-zmin])
		elif ymax == ymin:
			ax4.set_ylim(ymin - 1, ymin + 1)
			ax4.set_box_aspect([xmax-xmin, 2, zmax-zmin])
		elif zmax == zmin:
			ax4.set_zlim(zmin - 1, zmin + 1)
			ax4.set_box_aspect([xmax-xmin, ymax-ymin, 2])
		else:
			ax4.set_box_aspect([xmax-xmin, ymax-ymin, zmax-zmin])
		ax4.scatter(np.array([xcoor]), np.array([ycoor]), np.array([zcoor]), color = colorList, edgecolors = '0.0')
		for j in range(len(xyzcoor)):
			for k in range(j + 1, len(xyzcoor)):
				dis = (xyzcoor[j][1] - xyzcoor[k][1]) * (xyzcoor[j][1] - xyzcoor[k][1]) + (xyzcoor[j][2] - xyzcoor[k][2]) * (xyzcoor[j][2] \
					- xyzcoor[k][2]) + (xyzcoor[j][3] - xyzcoor[k][3]) * (xyzcoor[j][3] - xyzcoor[k][3])
				if dis <= (ATOM_RADII[periodTable.index(xyzcoor[j][0].upper())] + ATOM_RADII[periodTable.index(xyzcoor[k][0].upper())]) * \
					(ATOM_RADII[periodTable.index(xyzcoor[j][0].upper())] + ATOM_RADII[periodTable.index(xyzcoor[k][0].upper())]):
					ax4.plot([xyzcoor[j][1], xyzcoor[k][1]] , [xyzcoor[j][2], xyzcoor[k][2]], [xyzcoor[j][3], xyzcoor[k][3]], '0.5')		

		ax4.set_xlabel('X')
		ax4.set_ylabel('Y')
		ax4.set_zlabel('Z')
		figWin4 = Toplevel()
		figWin4.title(fileName)
		canvas4 = FigureCanvasTkAgg(fig4, figWin4)
		canvas4.get_tk_widget().pack(expand = True, fill = 'both')

		def renew3d():
			global fig4, ax4
			plt.cla()

			ax4.xaxis.pane.fill = False
			ax4.yaxis.pane.fill = False
			ax4.zaxis.pane.fill = False
			ax4.xaxis.pane.set_edgecolor('w')
			ax4.yaxis.pane.set_edgecolor('w')
			ax4.zaxis.pane.set_edgecolor('w')
			ax4.grid(False)
			if xmax == xmin:
				ax4.set_xlim(xmin - 1, xmin + 1)
				ax4.set_box_aspect([2, ymax-ymin, zmax-zmin])
			elif ymax == ymin:
				ax4.set_ylim(ymin - 1, ymin + 1)
				ax4.set_box_aspect([xmax-xmin, 2, zmax-zmin])
			elif zmax == zmin:
				ax4.set_zlim(zmin - 1, zmin + 1)
				ax4.set_box_aspect([xmax-xmin, ymax-ymin, 2])
			else:
				ax4.set_box_aspect([xmax-xmin, ymax-ymin, zmax-zmin])
			ax4.scatter(np.array([xcoor]), np.array([ycoor]), np.array([zcoor]), color = colorList, edgecolors = '0.0')
			for j in range(len(xyzcoor)):
				for k in range(j + 1, len(xyzcoor)):
					dis = (xyzcoor[j][1] - xyzcoor[k][1]) * (xyzcoor[j][1] - xyzcoor[k][1]) + (xyzcoor[j][2] - xyzcoor[k][2]) * (xyzcoor[j][2] \
						- xyzcoor[k][2]) + (xyzcoor[j][3] - xyzcoor[k][3]) * (xyzcoor[j][3] - xyzcoor[k][3])
					if dis <= (ATOM_RADII[periodTable.index(xyzcoor[j][0].upper())] + ATOM_RADII[periodTable.index(xyzcoor[k][0].upper())]) * \
						(ATOM_RADII[periodTable.index(xyzcoor[j][0].upper())] + ATOM_RADII[periodTable.index(xyzcoor[k][0].upper())]):
						ax4.plot([xyzcoor[j][1], xyzcoor[k][1]] , [xyzcoor[j][2], xyzcoor[k][2]], [xyzcoor[j][3], xyzcoor[k][3]], '0.5')
			# Poly surface 1
			x_poly1 = [float(x_right.get()), float(x_right.get()), float(x_right.get()), float(x_right.get())]
			y_poly1 = [float(y_left.get()), float(y_right.get()), float(y_right.get()), float(y_left.get())]
			z_poly1 = [float(z_left.get()), float(z_left.get()), float(z_right.get()), float(z_right.get())]
			poly1 = list(zip(x_poly1, y_poly1, z_poly1))
			ax4.add_collection3d(Poly3DCollection([poly1], facecolor = '#000080', alpha = 0.3))
			# Poly surface 2
			x_poly2 = [float(x_right.get()), float(x_left.get()), float(x_left.get()), float(x_right.get())]
			y_poly2 = [float(y_right.get()), float(y_right.get()), float(y_right.get()), float(y_right.get())]
			z_poly2 = [float(z_left.get()), float(z_left.get()), float(z_right.get()), float(z_right.get())]
			poly2 = list(zip(x_poly2, y_poly2, z_poly2))
			ax4.add_collection3d(Poly3DCollection([poly2], facecolor = '#55559e', alpha = 0.3))
			# Poly surface 3
			x_poly3 = [float(x_left.get()), float(x_left.get()), float(x_left.get()), float(x_left.get())]
			y_poly3 = [float(y_left.get()), float(y_right.get()), float(y_right.get()), float(y_left.get())]
			z_poly3 = [float(z_left.get()), float(z_left.get()), float(z_right.get()), float(z_right.get())]
			poly3 = list(zip(x_poly3, y_poly3, z_poly3))
			ax4.add_collection3d(Poly3DCollection([poly3], facecolor = '#000080', alpha = 0.3))
			# Poly surface 4
			x_poly4 = [float(x_right.get()), float(x_left.get()), float(x_left.get()), float(x_right.get())]
			y_poly4 = [float(y_left.get()), float(y_left.get()), float(y_left.get()), float(y_left.get())]
			z_poly4 = [float(z_left.get()), float(z_left.get()), float(z_right.get()), float(z_right.get())]
			poly4 = list(zip(x_poly4, y_poly4, z_poly4))
			ax4.add_collection3d(Poly3DCollection([poly4], facecolor = '#55559e', alpha = 0.3))
			# Poly surface 5
			x_poly5 = [float(x_right.get()), float(x_right.get()), float(x_left.get()), float(x_left.get())]
			y_poly5 = [float(y_left.get()), float(y_right.get()), float(y_right.get()), float(y_left.get())]
			z_poly5 = [float(z_left.get()), float(z_left.get()), float(z_left.get()), float(z_left.get())]
			poly5 = list(zip(x_poly5, y_poly5, z_poly5))
			ax4.add_collection3d(Poly3DCollection([poly5], facecolor = '#3939e3', alpha = 0.3))
			# Poly surface 6
			x_poly6 = [float(x_right.get()), float(x_right.get()), float(x_left.get()), float(x_left.get())]
			y_poly6 = [float(y_left.get()), float(y_right.get()), float(y_right.get()), float(y_left.get())]
			z_poly6 = [float(z_right.get()), float(z_right.get()), float(z_right.get()), float(z_right.get())]
			poly6 = list(zip(x_poly6, y_poly6, z_poly6))
			ax4.add_collection3d(Poly3DCollection([poly6], facecolor = '#3939e3', alpha = 0.3))
			ax4.set_xlabel('X')
			ax4.set_ylabel('Y')
			ax4.set_zlabel('Z')

		frame_3d = LabelFrame(figWin4, text = '   3D NICS Parameters:   ', font = ('Helvetica', 16, 'bold'), padx = 10, pady = 10)
		frame_3d.pack(padx = 20, pady = 20, fill = 'x')

		global x_left
		x_left.set(f'{xmin - 1}')
		Label(frame_3d, text = '   x(min): ', font = ('Helvetica',)).grid(row = 1, column = 0)
		Spinbox(frame_3d, textvariable = x_left, from_ = -99999.0, to = 99999.0, increment = 0.1, format = '%1.1f', width = 5, command = renew3d).grid(row = 1, column = 1)

		global x_right
		x_right.set(f'{xmax + 1}')
		Label(frame_3d, text = '   x(max): ', font = ('Helvetica',)).grid(row = 1, column = 2)
		Spinbox(frame_3d, textvariable = x_right, from_ = -99999.0, to = 99999.0, increment = 0.1, format = '%1.1f', width = 5, command = renew3d).grid(row = 1, column = 3)

		global y_left
		y_left.set(f'{ymin - 1}')
		Label(frame_3d, text = '   y(min): ', font = ('Helvetica',)).grid(row = 1, column = 4)
		Spinbox(frame_3d, textvariable = y_left, from_ = -99999.0, to = 99999.0, increment = 0.1, format = '%1.1f', width = 5, command = renew3d).grid(row = 1, column = 5)

		global y_right
		y_right.set(f'{ymax + 1}')
		Label(frame_3d, text = '   y(max): ', font = ('Helvetica',)).grid(row = 1, column = 6)
		Spinbox(frame_3d, textvariable = y_right, from_ = -99999.0, to = 99999.0, increment = 0.1, format = '%1.1f', width = 5, command = renew3d).grid(row = 1, column = 7)

		global z_left
		z_left.set(f'{zmin - 1}')
		Label(frame_3d, text = '   z(min): ', font = ('Helvetica',)).grid(row = 1, column = 8)
		Spinbox(frame_3d, textvariable = z_left, from_ = -99999.0, to = 99999.0, increment = 0.1, format = '%1.1f', width = 5, command = renew3d).grid(row = 1, column = 9)

		global z_right
		z_right.set(f'{zmax + 1}')
		Label(frame_3d, text = '   z(max): ', font = ('Helvetica',)).grid(row = 1, column = 10)
		Spinbox(frame_3d, textvariable = z_right, from_ = -99999.0, to = 99999.0, increment = 0.1, format = '%1.1f', width = 5, command = renew3d).grid(row = 1, column = 11)

		def nics3d_ok():
			global fig4, ax4
			plt.cla()

			ax4.xaxis.pane.fill = False
			ax4.yaxis.pane.fill = False
			ax4.zaxis.pane.fill = False
			ax4.xaxis.pane.set_edgecolor('w')
			ax4.yaxis.pane.set_edgecolor('w')
			ax4.zaxis.pane.set_edgecolor('w')
			ax4.grid(False)
			if xmax == xmin:
				ax4.set_xlim(xmin - 1, xmin + 1)
				ax4.set_box_aspect([2, ymax-ymin, zmax-zmin])
			elif ymax == ymin:
				ax4.set_ylim(ymin - 1, ymin + 1)
				ax4.set_box_aspect([xmax-xmin, 2, zmax-zmin])
			elif zmax == zmin:
				ax4.set_zlim(zmin - 1, zmin + 1)
				ax4.set_box_aspect([xmax-xmin, ymax-ymin, 2])
			else:
				ax4.set_box_aspect([xmax-xmin, ymax-ymin, zmax-zmin])
			ax4.scatter(np.array([xcoor]), np.array([ycoor]), np.array([zcoor]), color = colorList, edgecolors = '0.0')
			for j in range(len(xyzcoor)):
				for k in range(j + 1, len(xyzcoor)):
					dis = (xyzcoor[j][1] - xyzcoor[k][1]) * (xyzcoor[j][1] - xyzcoor[k][1]) + (xyzcoor[j][2] - xyzcoor[k][2]) * (xyzcoor[j][2] \
						- xyzcoor[k][2]) + (xyzcoor[j][3] - xyzcoor[k][3]) * (xyzcoor[j][3] - xyzcoor[k][3])
					if dis <= (ATOM_RADII[periodTable.index(xyzcoor[j][0].upper())] + ATOM_RADII[periodTable.index(xyzcoor[k][0].upper())]) * \
						(ATOM_RADII[periodTable.index(xyzcoor[j][0].upper())] + ATOM_RADII[periodTable.index(xyzcoor[k][0].upper())]):
						ax4.plot([xyzcoor[j][1], xyzcoor[k][1]] , [xyzcoor[j][2], xyzcoor[k][2]], [xyzcoor[j][3], xyzcoor[k][3]], '0.5')
			# Poly surface 1
			x_poly1 = [float(x_right.get()), float(x_right.get()), float(x_right.get()), float(x_right.get())]
			y_poly1 = [float(y_left.get()), float(y_right.get()), float(y_right.get()), float(y_left.get())]
			z_poly1 = [float(z_left.get()), float(z_left.get()), float(z_right.get()), float(z_right.get())]
			poly1 = list(zip(x_poly1, y_poly1, z_poly1))
			ax4.add_collection3d(Poly3DCollection([poly1], facecolor = '#000080', alpha = 0.3))
			# Poly surface 2
			x_poly2 = [float(x_right.get()), float(x_left.get()), float(x_left.get()), float(x_right.get())]
			y_poly2 = [float(y_right.get()), float(y_right.get()), float(y_right.get()), float(y_right.get())]
			z_poly2 = [float(z_left.get()), float(z_left.get()), float(z_right.get()), float(z_right.get())]
			poly2 = list(zip(x_poly2, y_poly2, z_poly2))
			ax4.add_collection3d(Poly3DCollection([poly2], facecolor = '#55559e', alpha = 0.3))
			# Poly surface 3
			x_poly3 = [float(x_left.get()), float(x_left.get()), float(x_left.get()), float(x_left.get())]
			y_poly3 = [float(y_left.get()), float(y_right.get()), float(y_right.get()), float(y_left.get())]
			z_poly3 = [float(z_left.get()), float(z_left.get()), float(z_right.get()), float(z_right.get())]
			poly3 = list(zip(x_poly3, y_poly3, z_poly3))
			ax4.add_collection3d(Poly3DCollection([poly3], facecolor = '#000080', alpha = 0.3))
			# Poly surface 4
			x_poly4 = [float(x_right.get()), float(x_left.get()), float(x_left.get()), float(x_right.get())]
			y_poly4 = [float(y_left.get()), float(y_left.get()), float(y_left.get()), float(y_left.get())]
			z_poly4 = [float(z_left.get()), float(z_left.get()), float(z_right.get()), float(z_right.get())]
			poly4 = list(zip(x_poly4, y_poly4, z_poly4))
			ax4.add_collection3d(Poly3DCollection([poly4], facecolor = '#55559e', alpha = 0.3))
			# Poly surface 5
			x_poly5 = [float(x_right.get()), float(x_right.get()), float(x_left.get()), float(x_left.get())]
			y_poly5 = [float(y_left.get()), float(y_right.get()), float(y_right.get()), float(y_left.get())]
			z_poly5 = [float(z_left.get()), float(z_left.get()), float(z_left.get()), float(z_left.get())]
			poly5 = list(zip(x_poly5, y_poly5, z_poly5))
			ax4.add_collection3d(Poly3DCollection([poly5], facecolor = '#3939e3', alpha = 0.3))
			# Poly surface 6
			x_poly6 = [float(x_right.get()), float(x_right.get()), float(x_left.get()), float(x_left.get())]
			y_poly6 = [float(y_left.get()), float(y_right.get()), float(y_right.get()), float(y_left.get())]
			z_poly6 = [float(z_right.get()), float(z_right.get()), float(z_right.get()), float(z_right.get())]
			poly6 = list(zip(x_poly6, y_poly6, z_poly6))
			ax4.add_collection3d(Poly3DCollection([poly6], facecolor = '#3939e3', alpha = 0.3))
			ax4.set_xlabel('X')
			ax4.set_ylabel('Y')
			ax4.set_zlabel('Z')

		Label(frame_3d, text = '   Grid: ', font = ('Helvetica',)).grid(row = 0, column = 0)
		global grid
		grid.set('0.20')
		Spinbox(frame_3d, textvariable = grid, from_ = 0.05, to = 0.50, increment = 0.05, format = '%1.2f', width = 5).grid(row = 0, column = 1)

		Button(frame_3d, text = 'Update', command = nics3d_ok).grid(row = 0, column = 10, columnspan = 2)

		frame_3d_g = LabelFrame(figWin4, text = '   Gaussian Calculation Setup: (Only valid when reading structure from .pdb/.xyz files)  ', font = ('Helvetica', 16, 'bold'), padx = 10, pady = 10)
		frame_3d_g.pack(padx = 20, pady = 20, fill = 'x')

		global nmr_type
		nmr_type.set('giao')
		Label(frame_3d_g, text = '   NMR Method:', font = ('Helvetica',)).grid(row = 0, column = 0)
		Radiobutton(frame_3d_g, text = 'GIAO', variable = nmr_type, value = 'giao').grid(row = 0, column = 1)
		Radiobutton(frame_3d_g, text = 'CSGT', variable = nmr_type, value = 'csgt').grid(row = 0, column = 2)
		Radiobutton(frame_3d_g, text = 'IGAIM', variable = nmr_type, value = 'igaim').grid(row = 0, column = 3)
		Radiobutton(frame_3d_g, text = 'CSGT, IGAGIM and Single Origin', variable = nmr_type, value = 'all').grid(row = 0, column = 4, columnspan = 3)

		global ru_method
		ru_method.set(' ')
		Label(frame_3d_g, text = '  Calculation:', font = ('Helvetica',)).grid(row = 1, column = 0)
		Radiobutton(frame_3d_g, text = 'Default', variable = ru_method, value = ' ').grid(row = 1, column = 1)
		Radiobutton(frame_3d_g, text = 'Restricted', variable = ru_method, value = 'r').grid(row = 1, column = 2)
		Radiobutton(frame_3d_g, text = 'Unrestricted', variable = ru_method, value = 'u').grid(row = 1, column = 3)
		Radiobutton(frame_3d_g, text = 'Restricted-open', variable = ru_method, value = 'ro').grid(row = 1, column = 4, columnspan = 2)

		global dft
		dft.set('B3LYP')
		Label(frame_3d_g, text = '   Functionals:', font = ('Helvetica',)).grid(row = 2, column = 0)
		Entry(frame_3d_g, textvariable = dft, width = 8).grid(row = 2, column = 1)

		global basis
		basis.set('6-311+G(d,p)')
		Label(frame_3d_g, text = '   Basis Set:', font = ('Helvetica',)).grid(row = 2, column = 2)
		Entry(frame_3d_g, textvariable = basis, width = 12).grid(row = 2, column = 3)

		Label(frame_3d_g, text = '   Charge:', font = ('Helvetica',)).grid(row = 2, column = 4)
		global charge
		charge.set('0')
		Spinbox(frame_3d_g, textvariable = charge, from_ = -99999, to = 99999, increment = 1, width = 5).grid(row = 2, column = 5)
		Label(frame_3d_g, text = '   Spin:', font = ('Helvetica',)).grid(row = 2, column = 6)
		global spin
		spin.set('1')
		Spinbox(frame_3d_g, textvariable = spin, from_ = 1, to = 99999, increment = 1, width = 5).grid(row = 2, column = 7)

		Label(frame_3d_g, text = '   Memory:', font = ('Helvetica',)).grid(row = 3, column = 0)
		global mem
		mem.set('Default')
		Entry(frame_3d_g, textvariable = mem, width = 8).grid(row = 3, column = 1)
		Label(frame_3d_g, text = '   Processors:', font = ('Helvetica',)).grid(row = 3, column = 2)
		global cpu
		cpu.set('Default')
		Entry(frame_3d_g, textvariable = cpu, width = 8).grid(row = 3, column = 3)

		Label(frame_3d_g, text = 'Addtional Keyword:', font = ('Helvetica',)).grid(row = 4, column = 0)
		global addkey
		addkey.set(' ')
		Entry(frame_3d_g, textvariable = addkey, width = 50).grid(row = 4, column = 1, columnspan = 5)

		def save_3d():
			global nmr_type, ru_method, fileName
			global dft, basis, charge, spin, mem, cpu
			global xyzcoor, grid
			global x_left, x_right, y_left, y_right, z_left, z_right
			n3inp(fileName, cpu.get(), mem.get(), nmr_type.get(), ru_method.get(), \
				dft.get(), basis.get(), addkey.get(), charge.get(), spin.get(), xyzcoor, \
				x_left.get(), x_right.get(), y_left.get(), y_right.get(), z_left.get(), z_right.get(), grid.get())
			messagebox.showwarning("Finished", "Input file has been generated successfully.")
		Button(frame_3d_g, text = 'Save Input File', command = save_3d).grid(row = 4, column = 6, columnspan = 2)

	if fileName[-3:] != 'out' and fileName[-3:] != 'log':     # If an input file was detected
		xyzcoor = inpReader.readCoor(fileName)
		xmin, xmax, ymin, ymax, zmin, zmax = findMm.findMaxMin(xyzcoor)

		fig = plt.figure()
		ax = fig.add_subplot(projection='3d')
		ax.xaxis.pane.fill = False
		ax.yaxis.pane.fill = False
		ax.zaxis.pane.fill = False
		ax.xaxis.pane.set_edgecolor('w')
		ax.yaxis.pane.set_edgecolor('w')
		ax.zaxis.pane.set_edgecolor('w')
		ax.grid(False)
		if xmax == xmin:
			ax.set_xlim(xmin - 1, xmin + 1)
			ax.set_box_aspect([2, ymax-ymin, zmax-zmin])
		elif ymax == ymin:
			ax.set_ylim(ymin - 1, ymin + 1)
			ax.set_box_aspect([xmax-xmin, 2, zmax-zmin])
		elif zmax == zmin:
			ax.set_zlim(zmin - 1, zmin + 1)
			ax.set_box_aspect([xmax-xmin, ymax-ymin, 2])
		else:
			ax.set_box_aspect([xmax-xmin, ymax-ymin, zmax-zmin])
		#ax.set_aspect('equal','box')

		xcoor = []
		ycoor = []
		zcoor = []
		colorList = []
		for i in xyzcoor:
			xcoor.append(i[1])
			ycoor.append(i[2])
			zcoor.append(i[3])
			colorList.append(ATOM_COLORS[periodTable.index(i[0].upper())])
		
		# Draw atom scatter
		ax.scatter(np.array([xcoor]), np.array([ycoor]), np.array([zcoor]), color = colorList, edgecolors = '0.0')
		
		# Draw bond
		for j in range(len(xyzcoor)):
			for k in range(j + 1, len(xyzcoor)):
				dis = (xyzcoor[j][1] - xyzcoor[k][1]) * (xyzcoor[j][1] - xyzcoor[k][1]) + (xyzcoor[j][2] - xyzcoor[k][2]) * (xyzcoor[j][2] \
					- xyzcoor[k][2]) + (xyzcoor[j][3] - xyzcoor[k][3]) * (xyzcoor[j][3] - xyzcoor[k][3])
				if dis <= (ATOM_RADII[periodTable.index(xyzcoor[j][0].upper())] + ATOM_RADII[periodTable.index(xyzcoor[k][0].upper())]) * \
					(ATOM_RADII[periodTable.index(xyzcoor[j][0].upper())] + ATOM_RADII[periodTable.index(xyzcoor[k][0].upper())]):
					ax.plot([xyzcoor[j][1], xyzcoor[k][1]] , [xyzcoor[j][2], xyzcoor[k][2]], [xyzcoor[j][3], xyzcoor[k][3]], '0.5')		

		ax.set_xlabel('X')
		ax.set_ylabel('Y')
		ax.set_zlabel('Z')
		figWin = Toplevel()
		figWin.title(fileName)
		canvas = FigureCanvasTkAgg(fig, figWin)
		canvas.get_tk_widget().pack(expand = True, fill = 'both')
		#toolbar = NavigationToolbar2Tk(canvas, figWin, pack_toolbar = False).pack()
		btnFrame = LabelFrame(figWin, text = 'Create input files:', font = ('Helvetica', 16, 'bold'), padx = 10, pady = 10)
		btnFrame.pack(fill = 'x')

		global nics1d_icon
		global nics2d_icon
		global nics3d_icon
		nics1d_icon = PhotoImage(file = r'assets/1dnics_icon.png')
		nics1d_btn = Button(btnFrame, image = nics1d_icon, command = nics1d).grid(row = 0, column = 0)
		Label(btnFrame, text = '        ').grid(row = 0, column = 1)
		Label(btnFrame, text = '1D-NICS').grid(row = 1, column = 0)
		nics2d_icon = PhotoImage(file = r'assets/2dnics_icon.png')
		nics2d_btn = Button(btnFrame, image = nics2d_icon, command = nics2d).grid(row = 0, column = 2)
		Label(btnFrame, text = '        ').grid(row = 0, column = 3)
		Label(btnFrame, text = '2D-NICS').grid(row = 1, column = 2)
		nics3d_icon = PhotoImage(file = r'assets/3dnics_icon.png')
		nics3d_btn = Button(btnFrame, image = nics3d_icon, command = nics3d).grid(row = 0, column = 4)
		Label(btnFrame, text = '        ').grid(row = 0, column = 5)
		Label(btnFrame, text = '3D-NICS').grid(row = 1, column = 4)

	elif '2DNICS' in fileName or '2DICSS' in fileName:
		global tensor_type
		tensor_type.set('zz')
		figWin6 = Toplevel()
		figWin6.title(fileName + f' 2D-NICS: {tensor_type.get().upper()}')
		fig6, ax6 = n2outShow(fileName, tensor_type.get())
		canvas6 = FigureCanvasTkAgg(fig6, figWin6)
		canvas6.get_tk_widget().pack(expand = True, fill = 'both')

		def nics2d_update():
			global tensor_type
			#global fig6, ax6
			figWin_n = Toplevel()
			figWin_n.title(fileName + f' 2D-NICS: {tensor_type.get().upper()}')
			fig_n, ax_n = n2outShow(fileName, tensor_type.get())	
			canvas_n = FigureCanvasTkAgg(fig_n, figWin_n)
			canvas_n.get_tk_widget().pack(expand = True, fill = 'both')

		def nics2d_csv():
			global tensor_type
			n2outSave(fileName, tensor_type.get())

		n2Frame = LabelFrame(figWin6, text = ' Shielding Tensor Component: ', font = ('Helvetica', 16, 'bold'), padx = 10, pady = 10)
		n2Frame.pack(fill = 'x')

		Radiobutton(n2Frame, text = 'Isotropic', variable = tensor_type, value = 'isotropic').grid(row = 0, column = 0, columnspan = 2)
		Radiobutton(n2Frame, text = 'Anisotropic', variable = tensor_type, value = 'anisotropic').grid(row = 0, column = 2, columnspan = 2)
		Radiobutton(n2Frame, text = 'XX', variable = tensor_type, value = 'xx').grid(row = 0, column = 4)
		Radiobutton(n2Frame, text = 'YX', variable = tensor_type, value = 'yx').grid(row = 0, column = 5)
		Radiobutton(n2Frame, text = 'ZX', variable = tensor_type, value = 'zx').grid(row = 0, column = 6)
		Radiobutton(n2Frame, text = 'XY', variable = tensor_type, value = 'xy').grid(row = 1, column = 0)
		Radiobutton(n2Frame, text = 'YY', variable = tensor_type, value = 'yy').grid(row = 1, column = 1)
		Radiobutton(n2Frame, text = 'ZY', variable = tensor_type, value = 'zy').grid(row = 1, column = 2)
		Radiobutton(n2Frame, text = 'XZ', variable = tensor_type, value = 'xz').grid(row = 1, column = 3)
		Radiobutton(n2Frame, text = 'YZ', variable = tensor_type, value = 'yz').grid(row = 1, column = 4)
		Radiobutton(n2Frame, text = 'ZZ', variable = tensor_type, value = 'zz').grid(row = 1, column = 5)
		Button(n2Frame, text = 'Update', command = nics2d_update).grid(row = 2, column = 0, columnspan = 2)
		Button(n2Frame, text = 'Save', command = nics2d_csv).grid(row = 2, column = 2, columnspan = 2)

	elif '3DICSS' in fileName or '3DNICS' in fileName:
		figWin7 = Toplevel()
		figWin7.title(fileName + f' 3D-NICS: {tensor_type.get().upper()}')

		def nics3d_cub():
			n3out(fileName, tensor_type.get())
			messagebox.showwarning("Finished", "Shielding tensors have been saved in .cub file.")

		n3Frame = LabelFrame(figWin7, text = ' Shielding Tensor Component: ', font = ('Helvetica', 16, 'bold'), padx = 10, pady = 10)
		n3Frame.pack(fill = 'x')

		Radiobutton(n3Frame, text = 'Isotropic', variable = tensor_type, value = 'isotropic').grid(row = 0, column = 0, columnspan = 2)
		Radiobutton(n3Frame, text = 'Anisotropic', variable = tensor_type, value = 'anisotropic').grid(row = 0, column = 2, columnspan = 2)
		Radiobutton(n3Frame, text = 'XX', variable = tensor_type, value = 'xx').grid(row = 0, column = 4)
		Radiobutton(n3Frame, text = 'YX', variable = tensor_type, value = 'yx').grid(row = 0, column = 5)
		Radiobutton(n3Frame, text = 'ZX', variable = tensor_type, value = 'zx').grid(row = 0, column = 6)
		Radiobutton(n3Frame, text = 'XY', variable = tensor_type, value = 'xy').grid(row = 1, column = 0)
		Radiobutton(n3Frame, text = 'YY', variable = tensor_type, value = 'yy').grid(row = 1, column = 1)
		Radiobutton(n3Frame, text = 'ZY', variable = tensor_type, value = 'zy').grid(row = 1, column = 2)
		Radiobutton(n3Frame, text = 'XZ', variable = tensor_type, value = 'xz').grid(row = 1, column = 3)
		Radiobutton(n3Frame, text = 'YZ', variable = tensor_type, value = 'yz').grid(row = 1, column = 4)
		Radiobutton(n3Frame, text = 'ZZ', variable = tensor_type, value = 'zz').grid(row = 1, column = 5)
		Button(n3Frame, text = 'Save', command = nics3d_cub).grid(row = 2, column = 0, columnspan = 2)

def open_web():
    webbrowser.open('https://wongzit.github.io/program/pyaroma', new = 1)

proVer = '2.0.1'
rlsDate = '2022-08-04'

root = Tk()
root.title(f'py.Aroma v{proVer}')

wideLogo = ImageTk.PhotoImage(Image.open('assets/pyaroma_main.png'))
Label(image = wideLogo).grid(row = 0, column = 0, columnspan = 4)

proInfoFrame = LabelFrame(root, borderwidth = 0, highlightthickness = 0)
proInfoFrame.grid(row = 1, column = 0, columnspan = 4, sticky = W + E)
Label(proInfoFrame, text = f'\nVer. {proVer} ({rlsDate})', font = ('Helvetica', 16, 'bold')).pack()
Label(proInfoFrame, text = 'Creating input files for 1D/2D/3D-NICS \ncalculations and process 2D/3D-NICS outputs.\n').pack()
Label(proInfoFrame, text = 'Copyright © 2022 Zhe Wang\n(https://wongzit.github.io)\n').pack()
Label(proInfoFrame, text = 'Supported file types:\n(1) Gaussian input file: .gjf/.com\n(2) Gaussian output file: .log/.out\n(3) Chemical structure data: .pdb/.xyz\n\n').pack()

fName = StringVar()
fileName = ''
filePathStatus = Label(root, textvariable = fName, bd = 1, width = 25, relief = SUNKEN, anchor = E, fg = 'gray16', bg = 'old lace').grid(row = 4, column = 0, columnspan = 4, sticky = W + E)

openIcon = PhotoImage(file = r'assets/open_icon.png')
readIcon = PhotoImage(file = r'assets/read_icon.png')
webIcon = PhotoImage(file = r'assets/web_icon.png')
quitIcon = PhotoImage(file = r'assets/quit_icon.png')

openButton = Button(root, image = openIcon, padx = 20, pady = 6, command = import_file).grid(row = 2, column = 0)
readButton = Button(root, image = readIcon, padx = 20, pady = 6, command = first_open).grid(row = 2, column = 1)
webButton = Button(root, image = webIcon, padx = 20, pady = 6, command = open_web).grid(row = 2, column = 2)
quitButton = Button(root, image = quitIcon, padx = 20, pady = 8, command = sys.exit).grid(row = 2, column = 3)

atm1 = StringVar()
atm2 = StringVar()
atm3 = StringVar()
atm4 = StringVar()
atm5 = StringVar()
atm6 = StringVar()
atm7 = StringVar()
atm8 = StringVar()
atm9 = StringVar()
atm10 = StringVar()
atm1.set('0')
atm2.set('0')
atm3.set('0')
atm4.set('0')
atm5.set('0')
atm6.set('0')
atm7.set('0')
atm8.set('0')
atm9.set('0')
atm10.set('0')

n1_hei = StringVar()
n1_hei.set('0.0')

nics_2d_plane = StringVar()
nics_2d_plane.set('xy')
plane_hei = StringVar()
plane_hei.set('0.0')

grid = StringVar()
grid.set('0.20')
x_left = StringVar()
x_left.set('0')
x_right = StringVar()
x_right.set('0')
y_left = StringVar()
y_left.set('0')
y_right = StringVar()
y_right.set('0')
z_left = StringVar()
z_left.set('0')
z_right = StringVar()
z_right.set('0')

nmr_type = StringVar()
nmr_type.set('giao')
ru_method = StringVar()
ru_method.set(' ')

dft = StringVar()
dft.set('B3LYP')
basis = StringVar()
basis.set('6-311+G(d,p)')

charge = StringVar()
charge.set('0')
spin = StringVar()
spin.set('1')

mem = StringVar()
mem.set('Default')
cpu = StringVar()
cpu.set('Default')

addkey = StringVar()
addkey.set('')

n1bqlist = []

tensor_type = StringVar()
tensor_type.set('zz')

Label(root, text = '1. Open', font = ('Helvetica', 13, 'bold')).grid(row = 3, column = 0)
Label(root, text = '2. Read', font = ('Helvetica', 13, 'bold')).grid(row = 3, column = 1)
Label(root, text = 'Help', font = ('Helvetica', 13, 'bold')).grid(row = 3, column = 2)
Label(root, text = 'Quit', font = ('Helvetica', 13, 'bold')).grid(row = 3, column = 3)

root.mainloop()
