def findMaxMin(coorlist):
	x_min = coorlist[0][1]
	x_max = coorlist[0][1]
	y_min = coorlist[0][2]
	y_max = coorlist[0][2]
	z_min = coorlist[0][3]
	z_max = coorlist[0][3]

	for coorlist_i in coorlist:
	    if x_min > coorlist_i[1]:
	        x_min = coorlist_i[1]
	    if x_max < coorlist_i[1]:
	        x_max = coorlist_i[1]
	    if y_min > coorlist_i[2]:
	        y_min = coorlist_i[2]
	    if y_max < coorlist_i[2]:
	        y_max = coorlist_i[2]
	    if z_min > coorlist_i[3]:
	        z_min = coorlist_i[3]
	    if z_max < coorlist_i[3]:
	        z_max = coorlist_i[3]
	
	return x_min, x_max, y_min, y_max, z_min, z_max
	
