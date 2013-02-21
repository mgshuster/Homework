def reset_vars
	a = 0
	a_known = False
	b = 0
	b_known = False
	y = 0
	y_known = False
	z = 0
	z_known = False
	a_AND_y = 0
	a_AND_y_known = False
	a_AND_z = 0
	a_AND_z_known = False
	b_AND_y = 0
	b_AND_y_known = False
	b_AND_z = 0
	b_AND_z_known = False
	a_OR_y = 0
	a_OR_y_known = False
	a_OR_z = 0
	a_OR_z_known = False
	b_OR_y = 0
	b_OR_y_known = False
	b_OR_z = 0
	b_OR_z_known = False
	a_GIVEN_y = 0
	a_GIVEN_y_known = False
	a_GIVEN_z = 0
	a_GIVEN_z_known = False
	b_GIVEN_y = 0
	b_GIVEN_y_known = False
	b_GIVEN_z = 0
	b_GIVEN_z_known = False
	y_GIVEN_a = 0
	y_GIVEN_a_known = False
	y_GIVEN_b = 0
	y_GIVEN_b_known = False
	z_GIVEN_a = 0
	z_GIVEN_a_known = False
	z_GIVEN_b = 0
	z_GIVEN_b_known = False
	
def complement_solve
	if a_known == True and b_known == False
		b = 1 - a
		b_known = True
		
	if b_known == True and a_known == False
		a = 1 - b
		a_known = True
		
	if y_known == True and z_known == False
		z = 1 - y
		z_known = True
		
	if z_known == True and y_known == False
		y = 1 - z
		y_known = True
		
	if a_AND_y_known == True and b_OR_z_known == False
		b_OR_z = 1 - a_AND_y
		b_OR_z_known = True
		
	if b_OR_z_known == True and a_AND_y_known == False
		a_AND_y = 1 - b_OR_z
		a_AND_y_known = True
		
	if a_OR_y_known == True and b_AND_z_known == False
		b_AND_z = 1 - a_OR_y
		b_AND_z_known = True
		
	if b_AND_z_known == True and a_OR_y_known == False
		a_OR_y = 1 - b_AND_z
		a_OR_y_known = True
		
	if a_AND_z_known == True and b_OR_y_known == False
		b_OR_y = 1 - a_AND_z
		b_OR_y_known = True
		
	if b_OR_y_known == True and a_AND_z_known == False
		a_AND_z = 1 - b_OR_y
		a_AND_z_known = True
		
	if a_OR_z_known == True and b_AND_y_known == False
		b_AND_y = 1 - a_OR_z
		b_AND_y_known = True
		
	if b_AND_y_known == True and a_OR_z_known == False
		a_OR_z = 1 - b_AND_y
		a_OR_z_known = True
		
	if a_GIVEN_y_known == True and b_GIVEN_y_known == False
		b_GIVEN_y = 1 - a_GIVEN_y
		b_GIVEN_y_known = True
		
	if b_GIVEN_y_known == True and a_GIVEN_y_known == False
		a_GIVEN_y = 1 - b_GIVEN_Y
		a_GIVEN_y_known = True
		
	if a_GIVEN_z_known == True and b_GIVEN_z_known == False
		b_GIVEN_z = 1 - a_GIVEN_z
		b_GIVEN_z_known = True
		
	if b_GIVEN_z_known == True and a_GIVEN_z_known == False
		a_GIVEN_z = 1 - b_GIVEN_z
		a_GIVEN_z_known = True
		
	if y_GIVEN_a_known == True and z_GIVEN_a_known == False
		z_GIVEN_a = 1 - y_GIVEN_a
		z_GIVEN_a_known = True
		
	if z_GIVEN_a_known == True and y_GIVEN_a_known == False
		y_GIVEN_a = 1 - z_GIVEN_a
		y_GIVEN_a_known = True
		
	if y_GIVEN_b_known == True and z_GIVEN_b_known == False
		z_GIVEN_b = 1 - y_GIVEN_b
		z_GIVEN_b_known = True
		
	if z_GIVEN_b_known == True and y_GIVEN_b_known == False
		y_GIVEN_b = 1 - z_GIVEN_b
		y_GIVEN_b_known = True
	

