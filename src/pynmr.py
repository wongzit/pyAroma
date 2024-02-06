# ===================================================================
#                            * pynmr.py *
#                     A Module for py.Aroma 4
# -------------------------------------------------------------------
#
#     Functions for NMR module, based on py.NMR v2.1
#
#                          by Zhe Wang @iCeMS, updated on 2023-11-29
# ===================================================================

# Calculate chemical shifts based on referece shielding
def ref_peak(nmr_matrix, ref_shield):
	ref_matrix = []
	for i_nmr_mat in nmr_matrix:
		ref_matrix.append([i_nmr_mat[0], i_nmr_mat[1], ref_shield-i_nmr_mat[2]])

	return ref_matrix

# Calculate scaled chemical shifts based on inputted slope and intercept
def scale_peak(nmr_matrix, slope, intercept):
	scale_matrix = []
	for j_nmr_mat in nmr_matrix:
		scale_matrix.append([j_nmr_mat[0], j_nmr_mat[1], (j_nmr_mat[2]-intercept)/slope])

	return scale_matrix

# Determine the chemical shifts/shieldings for NMR plot
def plot_peak(element, matrix_type):
	peak_table = []
	for i_peak in matrix_type:
		if i_peak[1].lower() == element.lower():
			peak_table.append(i_peak[2])

	return peak_table

# Calculate the peak intensity in NMR plot
def nmr_intensity(peak_table, plot_min, plot_max, plot_split, plot_fwhm):
	y_axis_mat = []
	x_axis_mat = []
	x_axis = plot_min
	while x_axis <= plot_max:
		y_axis = 0.0
		for i_mat in range(len(peak_table)):
			y_axis += plot_fwhm / (6.283185306 * (x_axis - peak_table[i_mat]) * (x_axis - peak_table[i_mat])\
			 + 1.570796327 * plot_fwhm * plot_fwhm)
		y_axis_mat.append(y_axis)
		x_axis_mat.append(x_axis)
		x_axis += plot_split

	return x_axis_mat, y_axis_mat
