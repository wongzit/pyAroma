# A Module for py.Aroma 3
# Process NICS output files

import readFile
from PyQt6.QtWidgets import QApplication, QWidget, QProgressBar, QPushButton
import sys

def save_tensor(file_name, bq_numbers, icss_flag):
	with open(file_name, 'r') as usr_output_file:
		usr_output = usr_output_file.readlines()

	iso_ten = []
	ani_ten = []
	xx_ten = []
	yx_ten = []
	zx_ten = []
	xy_ten = []
	yy_ten = []
	zy_ten = []
	xz_ten = []
	yz_ten = []
	zz_ten = []

	bq_start_flag = 0
	for line_no in range(len(usr_output)):
		if 'Bq   Isotropic =' in usr_output[line_no] and 'Anisotropy =' in usr_output[line_no]:
			bq_start_flag = line_no
			break

	for bq_i in range(bq_numbers):
		iso_ten.append(icss_flag * float(usr_output[bq_start_flag + bq_i * 5].split()[4]))
		ani_ten.append(icss_flag * float(usr_output[bq_start_flag + bq_i * 5].split()[7]))
		xx_ten.append(icss_flag * float(usr_output[bq_start_flag + bq_i * 5 + 1].split()[1]))
		yx_ten.append(icss_flag * float(usr_output[bq_start_flag + bq_i * 5 + 1].split()[3]))
		zx_ten.append(icss_flag * float(usr_output[bq_start_flag + bq_i * 5 + 1].split()[5]))
		xy_ten.append(icss_flag * float(usr_output[bq_start_flag + bq_i * 5 + 2].split()[1]))
		yy_ten.append(icss_flag * float(usr_output[bq_start_flag + bq_i * 5 + 2].split()[3]))
		zy_ten.append(icss_flag * float(usr_output[bq_start_flag + bq_i * 5 + 2].split()[5]))
		xz_ten.append(icss_flag * float(usr_output[bq_start_flag + bq_i * 5 + 3].split()[1]))
		yz_ten.append(icss_flag * float(usr_output[bq_start_flag + bq_i * 5 + 3].split()[3]))
		zz_ten.append(icss_flag * float(usr_output[bq_start_flag + bq_i * 5 + 3].split()[5]))

	return iso_ten, ani_ten, xx_ten, yx_ten, zx_ten, xy_ten, yy_ten, zy_ten, xz_ten, yz_ten, zz_ten


def save_tensor_3d(file_name, icss_flag):
	file_name_list = []
	file_name_2 = file_name[:-8]
	for fname_i in range(1, 999999):
		fname_i_2 = '%04d' % fname_i
		if file_name[-3:].lower() == 'log':
			current_fname = file_name_2 + str(fname_i_2) + '.log'
		elif file_name[-3:].lower() == 'out':
			current_fname = file_name_2 + str(fname_i_2) + '.out'
		try:
			with open(current_fname, 'r') as output_test:
				file_name_list.append(current_fname)
		except FileNotFoundError:
			break
	
	iso_ten = []
	ani_ten = []
	xx_ten = []
	yx_ten = []
	zx_ten = []
	xy_ten = []
	yy_ten = []
	zy_ten = []
	xz_ten = []
	yz_ten = []
	zz_ten = []

	bq_3d_x_coor = []
	bq_3d_y_coor = []
	bq_3d_z_coor = []

	for fname_j in file_name_list:
		#print(f'({file_name_list.index(fname_j)+1}/{len(file_name_list)})')
		atom_list, geom_list = readFile.read_log(fname_j)

		bq_list = atom_list[len(geom_list) - len(atom_list):]
		for bq_j in bq_list:
			bq_3d_x_coor.append(bq_j[1])
			bq_3d_y_coor.append(bq_j[2])
			bq_3d_z_coor.append(bq_j[3])

		with open(fname_j, 'r') as out_file:
			out_line = out_file.readlines()

		bq_start_flag = 0
		for line_no in range(len(out_line)):
			if 'Bq   Isotropic =' in out_line[line_no] and 'Anisotropy =' in out_line[line_no]:
				bq_start_flag = line_no
				break
		
		for bq_i in range(len(bq_list)):
			iso_ten.append(icss_flag * float(out_line[bq_start_flag + bq_i * 5].split()[4]))
			ani_ten.append(icss_flag * float(out_line[bq_start_flag + bq_i * 5].split()[7]))
			xx_ten.append(icss_flag * float(out_line[bq_start_flag + bq_i * 5 + 1].split()[1]))
			yx_ten.append(icss_flag * float(out_line[bq_start_flag + bq_i * 5 + 1].split()[3]))
			zx_ten.append(icss_flag * float(out_line[bq_start_flag + bq_i * 5 + 1].split()[5]))
			xy_ten.append(icss_flag * float(out_line[bq_start_flag + bq_i * 5 + 2].split()[1]))
			yy_ten.append(icss_flag * float(out_line[bq_start_flag + bq_i * 5 + 2].split()[3]))
			zy_ten.append(icss_flag * float(out_line[bq_start_flag + bq_i * 5 + 2].split()[5]))
			xz_ten.append(icss_flag * float(out_line[bq_start_flag + bq_i * 5 + 3].split()[1]))
			yz_ten.append(icss_flag * float(out_line[bq_start_flag + bq_i * 5 + 3].split()[3]))
			zz_ten.append(icss_flag * float(out_line[bq_start_flag + bq_i * 5 + 3].split()[5]))
		
	return iso_ten, ani_ten, xx_ten, yx_ten, zx_ten, xy_ten, yy_ten, zy_ten, xz_ten, yz_ten, zz_ten, bq_3d_x_coor, bq_3d_y_coor, bq_3d_z_coor

def extract_2d(tensor, plane, height, x_set, y_set, z_set):
	converted_tensor = []
	if plane == 'XY':
		n_z = z_set.index(height)
		for n in range(len(x_set) * len(y_set)):
			converted_tensor.append(tensor[n * len(z_set) + n_z])
	elif plane == 'YZ':
		n_x = x_set.index(height)
		for n in range(len(y_set) * len(z_set)):
			converted_tensor.append(tensor[len(y_set) * len(z_set) * n_x + n])
	elif plane == 'XZ':
		n_y = y_set.index(height)
		for n_x in range(len(x_set)):
			for n in range(len(z_set)):
				converted_tensor.append(tensor[n + n_y * len(z_set) + n_x * len(y_set) * len(z_set)])

	return converted_tensor
