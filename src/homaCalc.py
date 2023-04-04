# Module for Compute HOMA Value of Specified Monocycle
# Dr. Zhe Wang @Kyoto, 2023-02-09

import numpy as np
import CONSTANT
import configparser, os
from pathlib import Path

def mono_homa(monocycle, geom_list):
	engeo_dict = []

	# Calculate bond length, determine the bond type and find the HOMA parameters
	# Then, compute engeo(=alpha*(Ropt-Ri)**2), and add them to a list
	for atom in range(len(monocycle) - 1):
		bond_length = get_bond_length(monocycle[atom], monocycle[atom + 1], geom_list)
		r_o, homa_al, bnd_type = find_parameters(monocycle[atom], monocycle[atom + 1], geom_list)
		engeo_dict.append([bnd_type, calc_engeo(bond_length, r_o, homa_al)])

	bond_length = get_bond_length(monocycle[0], monocycle[-1], geom_list)
	r_o, homa_al, bnd_type = find_parameters(monocycle[0], monocycle[-1], geom_list)
	engeo_dict.append([bnd_type, calc_engeo(bond_length, r_o, homa_al)])
	
	valid_flag = 1      # Find whether unsupported atoms are contained
	for engeo_value in engeo_dict:
		if engeo_value[1] == 0.0:
			valid_flag = 0

	if valid_flag:
		homa = 1 - calc_homa(engeo_dict)
	else:
		homa = -9999999999      # If contain unsupported atom, export HOMA

	return homa

def get_bond_length(atom_i, atom_j, geom_list):
	length_i_j = float(np.sqrt(
			(geom_list[atom_i][1] - geom_list[atom_j][1]) ** 2 +
			(geom_list[atom_i][2] - geom_list[atom_j][2]) ** 2 +
			(geom_list[atom_i][3] - geom_list[atom_j][3]) ** 2))
	return length_i_j

def find_parameters(atom_i, atom_j, geom_list):
	# Load config.ini
	config_file = configparser.ConfigParser()
	config_file_path = os.path.join(os.path.dirname(__file__), 'config.ini')
	config_file.read(config_file_path)

	# Load homa from config.ini
	homa_para = {
	    'CC':[float(config_file.get('homa', 'cc').split(',')[0]), \
	    float(config_file.get('homa', 'cc').split(',')[1])],
	    'CN':[float(config_file.get('homa', 'cn').split(',')[0]), \
	    float(config_file.get('homa', 'cn').split(',')[1])],
	    'NC':[float(config_file.get('homa', 'cn').split(',')[0]), \
	    float(config_file.get('homa', 'cn').split(',')[1])],
	    'CO':[float(config_file.get('homa', 'co').split(',')[0]), \
	    float(config_file.get('homa', 'co').split(',')[1])],
	    'OC':[float(config_file.get('homa', 'co').split(',')[0]), \
	    float(config_file.get('homa', 'co').split(',')[1])],
	    'CP':[float(config_file.get('homa', 'cp').split(',')[0]), \
	    float(config_file.get('homa', 'cp').split(',')[1])],
	    'PC':[float(config_file.get('homa', 'cp').split(',')[0]), \
	    float(config_file.get('homa', 'cp').split(',')[1])],
	    'CS':[float(config_file.get('homa', 'cs').split(',')[0]), \
	    float(config_file.get('homa', 'cs').split(',')[1])],
	    'SC':[float(config_file.get('homa', 'cs').split(',')[0]), \
	    float(config_file.get('homa', 'cs').split(',')[1])],
	    'NN':[float(config_file.get('homa', 'nn').split(',')[0]), \
	    float(config_file.get('homa', 'nn').split(',')[1])],
	    'NO':[float(config_file.get('homa', 'no').split(',')[0]), \
	    float(config_file.get('homa', 'no').split(',')[1])],
	    'ON':[float(config_file.get('homa', 'no').split(',')[0]), \
	    float(config_file.get('homa', 'no').split(',')[1])],
	    'BN':[float(config_file.get('homa', 'bn').split(',')[0]), \
	    float(config_file.get('homa', 'bn').split(',')[1])],
	    'NB':[float(config_file.get('homa', 'bn').split(',')[0]), \
	    float(config_file.get('homa', 'bn').split(',')[1])],
	    'CSE':[float(config_file.get('homa', 'cse').split(',')[0]), \
	    float(config_file.get('homa', 'cse').split(',')[1])],
	    'SEC':[float(config_file.get('homa', 'cse').split(',')[0]), \
	    float(config_file.get('homa', 'cse').split(',')[1])]
	}

	bond_type = geom_list[atom_i][0].upper() + geom_list[atom_j][0].upper()
	if bond_type in homa_para.keys():
		r_opt = homa_para[bond_type][0]
		homa_alpha = homa_para[bond_type][1]
	else:
		r_opt = 0.0
		homa_alpha = 0.0
	return r_opt, homa_alpha, bond_type

def calc_engeo(bond_length_2, r_opt_2, homa_alpha_2):
	engeo_value = homa_alpha_2 * (bond_length_2 - r_opt_2) ** 2
	return engeo_value

def calc_homa(engeo_dictionary):
	count_cc = []
	count_cn = []
	count_co = []
	count_cp = []
	count_cs = []
	count_nn = []
	count_no = []
	count_bn = []
	count_cse = []

	for engeo_num in range(len(engeo_dictionary)):
		if engeo_dictionary[engeo_num][0].upper() == 'CC':
			count_cc.append(engeo_dictionary[engeo_num][1])
		elif engeo_dictionary[engeo_num][0].upper() == 'CN' or engeo_dictionary[engeo_num][0].upper() == 'NC':
			count_cn.append(engeo_dictionary[engeo_num][1])
		elif engeo_dictionary[engeo_num][0].upper() == 'CO' or engeo_dictionary[engeo_num][0].upper() == 'OC':
			count_co.append(engeo_dictionary[engeo_num][1])
		elif engeo_dictionary[engeo_num][0].upper() == 'CP' or engeo_dictionary[engeo_num][0].upper() == 'PC':
			count_cp.append(engeo_dictionary[engeo_num][1])
		elif engeo_dictionary[engeo_num][0].upper() == 'CS' or engeo_dictionary[engeo_num][0].upper() == 'SC':
			count_cs.append(engeo_dictionary[engeo_num][1])
		elif engeo_dictionary[engeo_num][0].upper() == 'NN':
			count_nn.append(engeo_dictionary[engeo_num][1])
		elif engeo_dictionary[engeo_num][0].upper() == 'NO' or engeo_dictionary[engeo_num][0].upper() == 'ON':
			count_no.append(engeo_dictionary[engeo_num][1])
		elif engeo_dictionary[engeo_num][0].upper() == 'BN' or engeo_dictionary[engeo_num][0].upper() == 'NB':
			count_bn.append(engeo_dictionary[engeo_num][1])
		elif engeo_dictionary[engeo_num][0].upper() == 'CSe' or engeo_dictionary[engeo_num][0].upper() == 'SeC':
			count_cse.append(engeo_dictionary[engeo_num][1])

	pro_homa = count_ave(count_cc) + count_ave(count_cn) + count_ave(count_co) \
	+ count_ave(count_cp) + count_ave(count_cs) + count_ave(count_nn) \
	+ count_ave(count_no) + count_ave(count_bn) + count_ave(count_cse)

	return pro_homa

def count_ave(usr_list):
	ave = 0.0
	if len(usr_list) != 0:
		for usr_element in usr_list:
			ave += usr_element
		ave = ave / len(usr_list)
	return ave