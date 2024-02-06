# ===================================================================
#                        * pathCreator.py *
#                     A Module for py.Aroma 4
# -------------------------------------------------------------------
#
#     Functions for 1D NICS scan module.
#
#                          by Zhe Wang @iCeMS, updated on 2023-02-15
# ===================================================================

import numpy as np

# Calculate Cartesian coordinates of ghost atoms and save them into a list
def creat_path(knot_coor, stepsize, height, plane_flag):
	start_dis = 0.0
	bq_list = []

	for knot in range(len(knot_coor) - 1):
		x1 = knot_coor[knot][0]
		x2 = knot_coor[knot + 1][0]
		y1 = knot_coor[knot][1]
		y2 = knot_coor[knot + 1][1]

		if x1 != x2:
			for n in range(8000):
				x3 = (x1*x2*x2 - 2*x1*x1*x2 + x1*y1*y1 + x1*y2*y2 + x1*x1*x1 - \
					2*x1*y1*y2 - (start_dis+n*stepsize)*x1*np.sqrt(x1*x1 - 2*x1*x2 + x2*x2 + y1*y1 \
					- 2*y1*y2 + y2*y2) + (start_dis+n*stepsize)*x2*np.sqrt(x1*x1 - 2*x1*x2 + x2*x2 \
					+ y1*y1 - 2*y1*y2 + y2*y2))/(x1*x1 - 2*x1*x2 + x2*x2 + y1*y1 - \
					2*y1*y2 + y2*y2)
				y3 = (x3 - x1) * (y2 - y1) / (x2 - x1) + y1
				if ((x3-x1)**2+(y3-y1)**2) < ((x2-x1)**2+(y2-y1)**2):
					if plane_flag.upper() == 'XY':
						bq_list.append(f'Bq     {float(x3):.6f}    {float(y3):.6f}     {float(height):.6f}\n')
					elif plane_flag.upper() == 'XZ':
						bq_list.append(f'Bq     {float(x3):.6f}     {float(height):.6f}    {float(y3):.6f}\n')
					elif plane_flag.upper() == 'YZ':
						bq_list.append(f'Bq     {float(height):.6f}     {float(x3):.6f}    {float(y3):.6f}\n')
				else:
					start_dis = np.sqrt((x3-x2)**2+(y3-y2)**2)
					break
		else:
			x3 = x1
			if y2 > y1:
				sign_flag = 1
			else:
				sign_flag = -1
			for m in range(8000):
				y3 = sign_flag*(start_dis+m*stepsize)+y1
				if (y3-y1)**2 < (y2-y1)**2:
					if plane_flag.upper() == 'XY':
						bq_list.append(f'Bq     {float(x3):.6f}    {float(y3):.6f}     {float(height):.6f}\n')
					elif plane_flag.upper() == 'XZ':
						bq_list.append(f'Bq     {float(x3):.6f}     {float(height):.6f}    {float(y3):.6f}\n')
					elif plane_flag.upper() == 'YZ':
						bq_list.append(f'Bq     {float(height):.6f}     {float(x3):.6f}    {float(y3):.6f}\n')
					else:
						start_dis = np.sqrt((y3 - y2)**2)
						break
	
	return bq_list

# Define the knots based on selected plane
def define_knot(knot_list, plane_flag):
	if plane_flag.upper() == 'XY':
		for knot in knot_list:
			del knot[-1]
	elif plane_flag.upper() == 'YZ':
		for knot in knot_list:
			del knot[0]
	elif plane_flag.upper() == 'XZ':
		for knot in knot_list:
			del knot[1]

	return knot_list
