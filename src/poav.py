# A Module for py.Aroma 3
# Compute POAV

import numpy as np

pi = 3.14159265358979

def find_connect_atom(target_atom, bonded_atoms):
	connected = []
	error_connected = []
	for b_atom in bonded_atoms:
		if target_atom == b_atom[0]:
			connected.append(b_atom[1])
		elif target_atom == b_atom[1]:
			connected.append(b_atom[0])
	if len(connected) == 3:
		return connected
	else:
		return error_connected



def calc_angle(x1, y1, z1, x2, y2, z2, x3, y3, z3):
	num = (x2 - x1) * (x3 - x1) + (y2 - y1) * (y3 - y1) + (z2 - z1) * (z3 - z1)
	den = np.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2-z1)**2) * np.sqrt((x3 - x1)**2 + (y3 - y1)**2 + (z3 - z1)**2)
	angle = np.arccos(num / den) * 180 / pi

	return angle

def calc_poav(theta_12, theta_23, theta_13):
	cos_12, cos_23, cos_13 = np.cos(theta_12*pi/180), np.cos(theta_23*pi/180), np.cos(theta_13*pi/180)
	sin_12 = np.sin(theta_12*pi/180)
	x1 = -1
	x2 = -cos_12
	x3 = -cos_13
	y2 = sin_12
	y3 = (cos_23 - cos_12 * cos_13) / sin_12
	x4 = np.sqrt(1 - x3**2 - y3**2)
	x1y2z3 = x1 * y2 * x4
	D1 = y2*y2*x4*x4
	D2 = ((x2 - x1) * x4)**2
	D3 = ((x2 - x1) * y3 - (y2 * (x3 - x1)))**2
	cos_theta_sigma_pi = x1y2z3 / np.sqrt(D1 + D2 + D3)
	theta_sigma_pi = np.arccos(cos_theta_sigma_pi) * 180 / pi
	if theta_sigma_pi >= 90:
		theta_p = theta_sigma_pi - 90
	else:
		theta_p = 90 - theta_sigma_pi
	smp_m = 2 * cos_theta_sigma_pi**2 / (1 - 3 * cos_theta_sigma_pi**2)
	spn_n = 3 * smp_m + 2

	# Following code for POAV2
	n1 = -cos_23 / (cos_12 * cos_13)
	n2 = -cos_13 / (cos_12 * cos_23)
	n3 = -cos_12 / (cos_23 * cos_13)
	s_sigma = (1/(1 + n1)) + (1/(1 + n2)) + (1/(1 + n3))
	spn = s_sigma / (1 - s_sigma)
	smp = 1 / spn
	lambda_1 = np.sqrt(n1)
	lambda_2 = np.sqrt(n2)
	lambda_3 = np.sqrt(n3)
	lambda_pi = np.sqrt(spn)
	theta_1pi = np.arccos(-1/(lambda_1*lambda_pi))*180/pi
	theta_2pi = np.arccos(-1/(lambda_2*lambda_pi))*180/pi
	theta_3pi = np.arccos(-1/(lambda_3*lambda_pi))*180/pi
	#print(theta_sigma_pi, theta_p, spn_n, smp_m, theta_1pi, theta_2pi, theta_3pi, n1, n2, n3, smp)
	return theta_sigma_pi, theta_p, spn_n, smp_m, theta_1pi, theta_2pi, theta_3pi, n1, n2, n3, smp
