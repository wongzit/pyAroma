# Get Connectivity
# A Module for py.Aroma 3
# By Dr. Zhe Wang @Kyoto, 2022-02-08

import numpy as np
import networkx as nx
import CONSTANT

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

def find_monocycle(_bonded_atoms):
	nx_graph = nx.Graph(_bonded_atoms)
	monocycle_in_molecule = nx.cycle_basis(nx_graph)
	return monocycle_in_molecule

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