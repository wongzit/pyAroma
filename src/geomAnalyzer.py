# ===================================================================
#                       * geomAnalyzer.py *
#                     A Module for py.Aroma 4
# -------------------------------------------------------------------
#
#     Functions for analyzing input geometries.
#
#                          by Zhe Wang @iCeMS, updated on 2023-12-03
# ===================================================================

import numpy as np
import networkx as nx
import CONSTANT

# Get bond information
def get_connectivity(geom_list):
	connectivity_matrix = np.zeros((len(geom_list), len(geom_list)), dtype = int)
	bonded_atoms = []
	for atom_i in range(len(geom_list)):
		for atom_j in range(atom_i + 1, len(geom_list)):
			bond_length_cutoff = CONSTANT.atom_radii[CONSTANT.period_table.index(geom_list[atom_i][0].upper())] \
			+ CONSTANT.atom_radii[CONSTANT.period_table.index(geom_list[atom_j][0].upper())]
			bond_length = np.sqrt(
				(geom_list[atom_i][1] - geom_list[atom_j][1]) ** 2 +
				(geom_list[atom_i][2] - geom_list[atom_j][2]) ** 2 +
				(geom_list[atom_i][3] - geom_list[atom_j][3]) ** 2)
			if bond_length <= bond_length_cutoff:
				connectivity_matrix[atom_i, atom_j] = connectivity_matrix[atom_j, atom_i] = bond_length
				bonded_atoms.append((atom_i, atom_j))
	
	return connectivity_matrix, bonded_atoms

# Find chordless monocycles in molecule
def find_monocycle(_bonded_atoms):
	nx_graph = nx.Graph(_bonded_atoms)
	monocycle_in_molecule = list(nx.chordless_cycles(nx_graph))
	monocycle_smaller_than_10 = []
	for monocycle in monocycle_in_molecule:
		if len(monocycle) <= 10:
			monocycle_smaller_than_10.append(monocycle)
	
	return monocycle_smaller_than_10

# Find max and min coordinates on X, Y, Z axes
def find_max_min(geom_list):
	x_min = geom_list[0][1]
	x_max = geom_list[0][1]
	y_min = geom_list[0][2]
	y_max = geom_list[0][2]
	z_min = geom_list[0][3]
	z_max = geom_list[0][3]

	for coor_i in geom_list:
		if x_min > coor_i[1]:
			x_min = coor_i[1]
		if x_max < coor_i[1]:
			x_max = coor_i[1]
		if y_min > coor_i[2]:
			y_min = coor_i[2]
		if y_max < coor_i[2]:
			y_max = coor_i[2]
		if z_min > coor_i[3]:
			z_min = coor_i[3]
		if z_max < coor_i[3]:
			z_max = coor_i[3]

	return x_min, x_max, y_min, y_max, z_min, z_max

# Save Cartesian coordinates and atom color
def save_coor_list(geom_list):
	x_coor = []
	y_coor = []
	z_coor = []
	color_list = []

	for coor_j in geom_list:
		x_coor.append(coor_j[1])
		y_coor.append(coor_j[2])
		z_coor.append(coor_j[3])
		color_list.append(CONSTANT.atom_colors[CONSTANT.period_table.index(coor_j[0].upper())])

	return x_coor, y_coor, z_coor, color_list

# Calculate unit normal vector of a fitted plane defined by more than 3 atoms
def normal_vector(atom_list, xyz_coor):
	usr_x = []
	usr_y = []
	usr_z = []
	for atom_i in atom_list:
		usr_x.append(xyz_coor[atom_i][1])
		usr_y.append(xyz_coor[atom_i][2])
		usr_z.append(xyz_coor[atom_i][3])

	x_set = sorted(set(usr_x))
	y_set = sorted(set(usr_y))
	z_set = sorted(set(usr_z))

	if len(x_set) == 1:
		c_1_norm = 1.0
		c_2_norm = 0.0
		c_3_norm = 0.0

	elif len(y_set) == 1:
		c_1_norm = 0.0
		c_2_norm = 1.0
		c_3_norm = 0.0

	elif len(z_set) == 1:
		c_1_norm = 0.0
		c_2_norm = 0.0
		c_3_norm = 1.0
		
	else:
		a_1 = np.column_stack([usr_x, usr_y, np.ones(len(atom_list))])
		a_2 = np.column_stack([usr_z])
		a_3 = np.linalg.lstsq(a_1, a_2, rcond=None)[0]

		c_1 = a_3[0][0]     # x_norm
		c_2 = a_3[1][0]     # y_norm

		norm = np.sqrt(c_1*c_1+c_2*c_2+1)
		c_1_norm = c_1 / norm
		c_2_norm = c_2 / norm
		c_3_norm = -1 / norm

	return c_1_norm, c_2_norm, c_3_norm
