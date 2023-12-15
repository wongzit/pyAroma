# ===================================================================
#                         * readFile.py *
#                     A Module for py.Aroma 4
# -------------------------------------------------------------------
#
#    Extract geometric information from browsed files:
#         Cartesian Coordinates -> [atom_list] & [geom_list]
#    Read electronic energy from Gaussian output files.
#    Extract isotropic shielding tensors for NMR module.
#
#                          by Zhe Wang @iCeMS, updated on 2023-11-21
# ===================================================================

import CONSTANT

'''
*************************************************************************

              FOLLOWING CODES ARE USED TO READ .MOL2 FILES

*************************************************************************
'''
def read_mol2(file_name):
# Open .mol2 file
	with open(file_name, 'r') as mol2_f:
		mol2_file = mol2_f.readlines()

# Find '@<TRIPOS>ATOM' section
	mol2_start_flag = 0
	mol2_end_flag = 0
	for mol2_line_no in range(len(mol2_file)):
		if mol2_file[mol2_line_no].strip().upper() == '@<TRIPOS>ATOM':
			mol2_start_flag  = mol2_line_no + 1
			break
	for mol2_line_no_2 in range(mol2_start_flag, len(mol2_file)):
		if mol2_file[mol2_line_no_2].strip() == '' or mol2_file[mol2_line_no_2].strip()[0] == '@':
			mol2_end_flag = mol2_line_no_2 - 1
			break

# Save coordinates into 'atom_list' (including dummy atoms) and 'geom_list' (without dummy atoms)
	atom_list = []
	geom_list = []
	for mol2_atom_line_no in range(mol2_start_flag, mol2_end_flag + 1):
		coor_list = []
		if '.' not in mol2_file[mol2_atom_line_no].split()[5]:
			coor_list.append(mol2_file[mol2_atom_line_no].split()[5])
		else:
			for atom_dot_length in range(len(mol2_file[mol2_atom_line_no].split()[5])):
				if mol2_file[mol2_atom_line_no].split()[5][atom_dot_length] == '.':
					coor_list.append(mol2_file[mol2_atom_line_no].split()[5][:atom_dot_length])
					break
		coor_list.append(float(mol2_file[mol2_atom_line_no].split()[2]))
		coor_list.append(float(mol2_file[mol2_atom_line_no].split()[3]))
		coor_list.append(float(mol2_file[mol2_atom_line_no].split()[4]))
		atom_list.append(coor_list)
		if coor_list[0].upper() != 'BQ' and coor_list[0].upper() != 'DU':
			geom_list.append(coor_list)

	return atom_list, geom_list

'''
*************************************************************************

               FOLLOWING CODES ARE USED TO READ .CIF FILES

*************************************************************************

def read_cif(file_name):
	parser = CifParser(file_name)
	structure = parser.get_structures()[0]
	elements = [site.specie.name for site in structure.sites]
	cartesian_coordinates = structure.cart_coords.tolist()

	atom_list = []
	geom_list = []
	for ele in range(len(elements)):
		coor_list = []
		coor_list.append(elements[ele])
		coor_list.append(float(cartesian_coordinates[ele][0]))
		coor_list.append(float(cartesian_coordinates[ele][1]))
		coor_list.append(float(cartesian_coordinates[ele][2]))
		atom_list.append(coor_list)
		geom_list.append(coor_list)

	return atom_list, geom_list
'''
'''
*************************************************************************

               FOLLOWING CODES ARE USED TO READ .PDB FILES

*************************************************************************
'''
def read_pdb(file_name):
# Open .pdb file
	with open(file_name, 'r') as pdb_f:
		pdb_file = pdb_f.readlines()

# Find column number of coordinates in 'HETATM' lines
	atom_line_length = 0
	coor_start = 0
	for pdb_line in pdb_file:
		if pdb_line.strip().split()[0].upper() == 'HETATM':
			atom_line_length = len(pdb_line.strip().split())
			for atom_line_length_list_no in range(atom_line_length):
				if '.' in pdb_line.strip().split()[atom_line_length_list_no] \
				and '.' in pdb_line.strip().split()[atom_line_length_list_no + 1] \
				and '.' in pdb_line.strip().split()[atom_line_length_list_no + 2]:
					coor_start = atom_line_length_list_no
					break
			break

# Save coordinates into 'atom_list' (including dummy atoms) and 'geom_list' (without dummy atoms)
	atom_list = []
	geom_list = []
	for pdb_line_2 in pdb_file:
		coor_list = []
		if pdb_line_2.strip().split()[0].upper() == 'HETATM':
			if len(pdb_line_2.strip().split()[2]) == 1:
				coor_list.append(pdb_line_2.strip().split()[2])
			else:
				atom_name = ''
				for atom_char in pdb_line_2.strip().split()[2]:
					if atom_char.isalpha():
						atom_name += atom_char
					else:
						break
				coor_list.append(atom_name)

			coor_list.append(float(pdb_line_2.strip().split()[coor_start]))
			coor_list.append(float(pdb_line_2.strip().split()[coor_start + 1]))
			coor_list.append(float(pdb_line_2.strip().split()[coor_start + 2]))
			atom_list.append(coor_list)
			if coor_list[0].upper() != 'BQ':
				geom_list.append(coor_list)

	return atom_list, geom_list

'''
*************************************************************************

               FOLLOWING CODES ARE USED TO READ .XYZ FILES

*************************************************************************
'''
def read_xyz(file_name):
# Open .xyz file
	with open(file_name, 'r') as xyz_f:
		xyz_file = xyz_f.readlines()

# Save coordinates into 'atom_list' (including dummy atoms) and 'geom_list' (without dummy atoms)
	atom_list = []
	geom_list = []
	for xyz_line in xyz_file:
		coor_list = []
		if len(xyz_line.strip().split()) == 4 and xyz_line.count('.') == 3:
			coor_list.append(xyz_line.strip().split()[0])
			coor_list.append(float(xyz_line.strip().split()[1]))
			coor_list.append(float(xyz_line.strip().split()[2]))
			coor_list.append(float(xyz_line.strip().split()[3]))
			atom_list.append(coor_list)
			if coor_list[0].upper() != 'BQ':
				geom_list.append(coor_list)

	return atom_list, geom_list

'''
*************************************************************************

       FOLLOWING CODES ARE USED TO READ GAUSSIAN-TYPE INPUT FILES

*************************************************************************
'''
def read_gjf(file_name):
# Open .gjf file, also support .com file
	with open(file_name, 'r') as gjf_f:
		gjf_file = gjf_f.readlines()

# Save coordinates into 'atom_list' (including dummy atoms) and 'geom_list' (without dummy atoms)
# For atom symbol, only read character before '(' if there is.
	atom_list = []
	geom_list = []

	start_line = 0
	end_line = 0

	for line_no in range(len(gjf_file)):
		#print(line_no)
		if len(gjf_file[line_no].strip()) > 4 and gjf_file[line_no].strip()[0] != '%' and gjf_file[line_no].strip()[0] != '#' and gjf_file[line_no].count('.') == 3:
			start_line = line_no
			break
	for line_no_2 in range(start_line, len(gjf_file)):
		if gjf_file[line_no_2].strip() == '':
			end_line = line_no_2
			break
	
	for line_no_3 in range(start_line, end_line):
		coor_list = []
		if len(gjf_file[line_no_3].strip().split()[0]) > 3:
			atom_name = ''
			for atom_char in gjf_file[line_no_3].strip().split()[0]:
				if atom_char != '(':
					atom_name += atom_char
				else:
					break
			coor_list.append(atom_name)
		else:
			coor_list.append(gjf_file[line_no_3].strip().split()[0])
		coor_list.append(float(gjf_file[line_no_3].strip().split()[-3]))
		coor_list.append(float(gjf_file[line_no_3].strip().split()[-2]))
		coor_list.append(float(gjf_file[line_no_3].strip().split()[-1]))
		atom_list.append(coor_list)
		if coor_list[0].upper() != 'BQ':
			geom_list.append(coor_list)
	
	return atom_list, geom_list

'''
*************************************************************************

       FOLLOWING CODES ARE USED TO READ GAUSSIAN-TYPE OUTPUT FILES

*************************************************************************
'''
def read_log(file_name):
# Open .log file, also support .com file
	with open(file_name, 'r') as log_f:
		log_file = log_f.readlines()

# Find geometry section in files
	geom_start_line = 0
	geom_end_line = 0
	for log_line_no in range(len(log_file)):
		if 'Standard orientation:' in log_file[log_line_no]:
			geom_start_line = log_line_no + 5
	if geom_start_line == 0:
		for log_line_no_2 in range(len(log_file)):
			if 'Input orientation:' in log_file[log_line_no_2]:
				geom_start_line = log_line_no_2 + 5

	for log_line_no_3 in range(geom_start_line, len(log_file)):
		if '------' in log_file[log_line_no_3]:
			geom_end_line = log_line_no_3 - 1
			break

# Save coordinates into 'atom_list' (including dummy atoms) and 'geom_list' (without dummy atoms)
	atom_list = []
	geom_list = []
	for geom_line in range(geom_start_line, geom_end_line + 1):
		coor_list = []
		coor_list.append(CONSTANT.period_table[int(log_file[geom_line].strip().split()[1])].title())
		coor_list.append(float(log_file[geom_line].strip().split()[3]))
		coor_list.append(float(log_file[geom_line].strip().split()[4]))
		coor_list.append(float(log_file[geom_line].strip().split()[5]))
		atom_list.append(coor_list)
		if coor_list[0].upper() != 'BQ':
			geom_list.append(coor_list)

	return atom_list, geom_list

'''
*************************************************************************

  FOLLOWING CODES ARE USED TO READ ELECTRONIC ENERGY FROM OUTPUT FILES

*************************************************************************
'''
def read_energy(route_line, file_name):
	ele_energy = 0
	with open(file_name, 'r') as output_file:
		output = output_file.readlines()

	if 'uff' in route_line or 'dreiding' in route_line or 'amber' in route_line:
		for output_i in output:
			if  'Predicted change in' not in output_i and 'Energy=' in output_i:
				ele_energy = float(output_i.split()[1])

	elif 'cas' in route_line:
		marker = 0
		for i in range(len(output)):
			if 'EIGENVALUES AND  EIGENVECTORS OF CI MATRIX' in output[i]:
				marker = i
		for j in range(marker+1, len(output)):
			if output[j].strip() != '' and 'EIGENVALUE' in output[j]:
				ele_energy = float(output[j].split()[-1])
			if output[j].strip() != '' and 'EIGENVALUE' not in output[j]:
				break

	elif 'mp2' in route_line:
		for output_j in output:
			if 'EUMP2 =' in output_j:
				mp2Str = output_j.split()[5]
				if 'D' in mp2Str:
					ele_energy = float(mp2Str[:mp2Str.index('D')]) * 10**(int(mp2Str[mp2Str.index('D') + 2:]))
				else:
					ele_energy = float(mp2Str)

	elif 'ccsd' in route_line:
		archive = ''
		for output_k in output:
			if '\\' in output_k:
				archive += output_k.strip()
		if 'ccsd(t' in route_line or 'ccsd=(t' in route_line:
			start_flag = 0
			end_flag = 0
			for char_i in range(len(archive)):
				if archive[char_i:char_i+9] == '\\CCSD(T)=':
					start_flag = char_i + 9
					break
			for char_j in range(start_flag, len(archive)):
				if archive[char_j] == '\\':
					end_flag = char_j
					break
			ele_energy = float(archive[start_flag:end_flag])
		else:
			start_flag = 0
			end_flag = 0
			for char_i in range(len(archive)):
				if archive[char_i:char_i+6] == '\\CCSD=':
					start_flag = char_i + 6
					break
			for char_j in range(start_flag, len(archive)):
				if archive[char_j] == '\\':
					end_flag = char_j
					break
			ele_energy = float(archive[start_flag:end_flag])

	elif 'td' in route_line:
		for output_l in output:
			if 'Total Energy, E(TD-HF/TD-DFT) =' in output_l:
				ele_energy = float(output_l.split()[4])

	else:
		archive = ''
		for output_n in output:
			if '\\' in output_n:
				archive += output_n.strip()
		if '\\MP2=' in archive:
			start_flag = 0
			end_flag = 0
			for char_k in range(len(archive)):
				if archive[char_k:char_k+5] == '\\MP2=':
					start_flag = char_k + 5
					break
			for char_j in range(start_flag, len(archive)):
				if archive[char_j] == '\\':
					end_flag = char_j
					break
			ele_energy = float(archive[start_flag:end_flag])
		else:
			for output_m in output:
				if 'SCF Done:' in output_m:
					ele_energy = float(output_m.split()[4])

	return ele_energy

'''
*************************************************************************************

  FOLLOWING CODES ARE USED TO EXTRACT ISOTROPIC SHIELDING TENSORS FROM OUTPUT FILES

*************************************************************************************
'''
def nmr_isotropy(file_name):
	
	with open(file_name, 'r') as nmr_f:
		nmr_file = nmr_f.readlines()

	nmr_matrix = []
	for nmr_line_i in nmr_file:
		nmr_tensor = []
		if 'Isotropic =' in nmr_line_i and 'Anisotropy =' in nmr_line_i:
			if nmr_line_i.split()[1].lower() != 'bq':
				nmr_tensor.append(nmr_line_i.split()[0])
				nmr_tensor.append(nmr_line_i.split()[1].lower())
				nmr_tensor.append(float(nmr_line_i.split()[4]))
				nmr_matrix.append(nmr_tensor)

	return nmr_matrix