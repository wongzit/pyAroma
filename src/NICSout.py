# ===================================================================
#                         * NICSout.py *
#                     A Module for py.Aroma 4
# -------------------------------------------------------------------
#
#     Functions for extracting shielding tensors from Gaussian
#  output files and saving into lists.
#
#                          by Zhe Wang @iCeMS, updated on 2023-11-30
# ===================================================================

import readFile
from PyQt6.QtWidgets import QApplication, QWidget, QProgressBar, QPushButton
import sys

# Save tensors into 11 lists, with different compounents
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

# For 3D-NICS/ICSS outputs: Save tensors into 11 lists, with different compounents
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

# Use for 2D-NICS plot in 3D-NICS module
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

# For INICS outputs: Save tensors into 11 lists, with different compounents
def cal_inics(file_name, num_bq, num_rings, split, num_dots):
	isoTen, aniTen, xxTen, yxTen, zxTen, xyTen, yyTen, zyTen, xzTen, yzTen, zzTen = save_tensor(file_name, num_bq, -1)
	all_int_iso = []
	all_int_ani = []
	all_int_xx = []
	all_int_yx = []
	all_int_zx = []
	all_int_xy = []
	all_int_yy = []
	all_int_zy = []
	all_int_xz = []
	all_int_yz = []
	all_int_zz = []

	for n_ring in range(num_rings):
		mono_iso_tensor = isoTen[n_ring*num_dots:n_ring*num_dots+num_dots]
		mono_ani_tensor = aniTen[n_ring*num_dots:n_ring*num_dots+num_dots]
		mono_xx_tensor = xxTen[n_ring*num_dots:n_ring*num_dots+num_dots]
		mono_yx_tensor = yxTen[n_ring*num_dots:n_ring*num_dots+num_dots]
		mono_zx_tensor = zxTen[n_ring*num_dots:n_ring*num_dots+num_dots]
		mono_xy_tensor = xyTen[n_ring*num_dots:n_ring*num_dots+num_dots]
		mono_yy_tensor = yyTen[n_ring*num_dots:n_ring*num_dots+num_dots]
		mono_zy_tensor = zyTen[n_ring*num_dots:n_ring*num_dots+num_dots]
		mono_xz_tensor = xzTen[n_ring*num_dots:n_ring*num_dots+num_dots]
		mono_yz_tensor = yzTen[n_ring*num_dots:n_ring*num_dots+num_dots]
		mono_zz_tensor = zzTen[n_ring*num_dots:n_ring*num_dots+num_dots]
		int_iso = 0.0
		int_ani = 0.0
		int_xx = 0.0
		int_yx = 0.0
		int_zx = 0.0
		int_xy = 0.0
		int_yy = 0.0
		int_zy = 0.0
		int_xz = 0.0
		int_yz = 0.0
		int_zz = 0.0

		for iso_i in range(len(mono_iso_tensor)-1):
			int_iso += mono_iso_tensor[iso_i]*split
		for ani_i in range(len(mono_ani_tensor)-1):
			int_ani += mono_ani_tensor[ani_i]*split
		for xx_i in range(len(mono_xx_tensor)-1):
			int_xx += mono_xx_tensor[xx_i]*split
		for yx_i in range(len(mono_yx_tensor)-1):
			int_yx += mono_yx_tensor[yx_i]*split
		for zx_i in range(len(mono_zx_tensor)-1):
			int_zx += mono_zx_tensor[zx_i]*split
		for xy_i in range(len(mono_xy_tensor)-1):
			int_xy += mono_xy_tensor[xy_i]*split
		for yy_i in range(len(mono_yy_tensor)-1):
			int_yy += mono_yy_tensor[yy_i]*split
		for zy_i in range(len(mono_zy_tensor)-1):
			int_zy += mono_zy_tensor[zy_i]*split
		for xz_i in range(len(mono_xz_tensor)-1):
			int_xz += mono_xz_tensor[xz_i]*split
		for yz_i in range(len(mono_yz_tensor)-1):
			int_yz += mono_yz_tensor[yz_i]*split
		for zz_i in range(len(mono_zz_tensor)-1):
			int_zz += mono_zz_tensor[zz_i]*split

		all_int_iso.append(int_iso)
		all_int_ani.append(int_ani)
		all_int_xx.append(int_xx)
		all_int_yx.append(int_yx)
		all_int_zx.append(int_zx)
		all_int_xy.append(int_xy)
		all_int_yy.append(int_yy)
		all_int_zy.append(int_zy)
		all_int_xz.append(int_xz)
		all_int_yz.append(int_yz)
		all_int_zz.append(int_zz)

	return all_int_iso, all_int_ani, all_int_xx, all_int_yx, all_int_zx, all_int_xy, all_int_yy, all_int_zy, all_int_xz, all_int_yz, all_int_zz
