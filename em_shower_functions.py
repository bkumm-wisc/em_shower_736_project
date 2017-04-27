#em_shower_functions.py

#-------------------------------------------------------------------------
#IMPORTS

#em_shower imports
from em_shower_classes import Particle

#Other Imports
from math import sqrt, cos, sin, log, ceil, sqrt, pi
from random import getrandbits
import numpy as np

#-------------------------------------------------------------------------




#-------------------------------------------------------------------------
#Other functions
def delta_theta_calc(E,E_crit):
	N_o = ceil( log(E / E_crit) / log(2.) )
	return 2. / ( float(N_o) * (float(N_o) + 1) )

def TF_rand():
	return bool(getrandbits(1))

def Energy_Shower_list(Shower_list):
	master_list = []
	for part_list in Shower_list:
		new_e_list = []
		for part in part_list:
			new_e_list.append(part.energy)
		master_list.append(new_e_list)

	return master_list

def XY_Shower_list(Shower_list):
	master_list = []
	for part_list in Shower_list:
		new_xy_list = []
		for part in part_list:
			new_xy_list.append( (part.x_pos,part.y_pos) )
		master_list.append(new_xy_list)

	return master_list

def electron_XY_Shower_list(Shower_list):
	master_list = []
	for part_list in Shower_list:
		new_xy_list = []
		for part in part_list:
			if part.name == 'electron':
				new_xy_list.append( (part.x_pos,part.y_pos) )
		master_list.append(new_xy_list)

def positron_XY_Shower_list(Shower_list):
	master_list = []
	for part_list in Shower_list:
		new_xy_list = []
		for part in part_list:
			if part.name == 'positron':
				new_xy_list.append( (part.x_pos,part.y_pos) )
		master_list.append(new_xy_list)

	return master_list

def gamma_XY_Shower_list(Shower_list):
	master_list = []
	for part_list in Shower_list:
		new_xy_list = []
		for part in part_list:
			if part.name == 'gamma':
				new_xy_list.append( (part.x_pos,part.y_pos) )
		master_list.append(new_xy_list)

	return master_list

def e_and_p_XY_Shower_list(Shower_list):
	master_list = []
	for part_list in Shower_list:
		new_xy_list = []
		for part in part_list:
			if part.name in ['electron','positron']:
				new_xy_list.append( (part.x_pos,part.y_pos) )
		master_list.append(new_xy_list)

	return master_list


#-------------------------------------------------------------------------




#-------------------------------------------------------------------------
#Particle interactions

def PAIR_PRODUCTION0(Incident, input_list, delta_theta, X_o):
	new_energy  = Incident.energy *0.5

	if TF_rand:
		theta_e = Incident.theta + delta_theta
		theta_p = Incident.theta - delta_theta
	else:
		theta_e = Incident.theta - delta_theta
		theta_p = Incident.theta + delta_theta

	x_e_pos = Incident.x_pos + X_o * theta_e
	y_e_pos = Incident.y_pos + X_o * (1. - theta_e**2 / 2.)

	x_p_pos = Incident.x_pos + X_o * theta_p
	y_p_pos = Incident.y_pos + X_o * (1. - theta_p**2 / 2.)


	input_list.append(Particle('electron', new_energy, x_e_pos, y_e_pos, theta_e))
	input_list.append(Particle('positron', new_energy, x_p_pos, y_p_pos, theta_p))	

	return

def BREMSSTRAHLUNG0(Incident, input_list, delta_theta, X_o):
	new_energy  = Incident.energy *0.5

	if TF_rand:
		theta_e = Incident.theta + delta_theta
		theta_g = Incident.theta - delta_theta
	else:
		theta_e = Incident.theta - delta_theta
		theta_g = Incident.theta + delta_theta

	x_e_pos = Incident.x_pos + X_o * theta_e
	y_e_pos = Incident.y_pos + X_o * (1. - theta_e**2 / 2.)

	x_g_pos = Incident.x_pos + X_o * theta_g
	y_g_pos = Incident.y_pos + X_o * (1. - theta_g**2 / 2.)


	input_list.append(Particle(Incident.name, new_energy, x_e_pos, y_e_pos, theta_e))
	input_list.append(Particle('gamma', new_energy, x_g_pos, y_g_pos,  theta_g))
	return

def PAIR_PRODUCTION1(Incident, input_list, X_o):
	"""
	each particle gets half of incident energy and thetas calculated from small angle approx of conservation of momentum equations
	"""
	theta_i    = Incident.theta
	pc_old     = Incident.energy   
	new_energy = 0.5 * Incident.energy
	pc_new      = sqrt( (new_energy)**2 - 0.510998946 **2 ) 
	if TF_rand(): 
		theta_p =  ( (pc_old * theta_i) - (sqrt(8. * pc_new**2 - 4. * pc_old * pc_new - pc_old**2 * theta_i**2 + 2. * pc_old * pc_new * theta_i**2  ) ) / (2. * pc_new))
		theta_e = -( (pc_old * theta_i) - (sqrt(8. * pc_new**2 - 4. * pc_old * pc_new - pc_old**2 * theta_i**2 + 2. * pc_old * pc_new * theta_i**2  ) ) / (2. * pc_new))
	
	else:
		theta_p =  (pc_old * theta_i / ( 2.0 * pc_new )) - (sqrt(8. * pc_new**2 + -4. * pc_old * pc_new - pc_old**2 * theta_i**2 + 2. * pc_old * pc_new * theta_i**2  ) / (2. * pc_new))
		theta_e = -(pc_old * theta_i / ( 2.0 * pc_new )) - (sqrt(8. * pc_new**2 + -4. * pc_old * pc_new - pc_old**2 * theta_i**2 + 2. * pc_old * pc_new * theta_i**2  ) / (2. * pc_new))

	x_p_pos = Incident.x_pos + X_o * sin(theta_p)
	y_p_pos = Incident.y_pos + X_o * cos(theta_p)

	x_e_pos = Incident.x_pos - X_o * sin(theta_e)
	y_e_pos = Incident.y_pos + X_o * cos(theta_e)

	input_list.append(Particle('positron', new_energy, x_p_pos, y_p_pos,  theta_p))
	input_list.append(Particle('electron', new_energy, x_e_pos, y_e_pos, -theta_e))
	return

def BREMSSTRAHLUNG1(Incident, input_list, delta_E_factor, X_o):
	new_energy = 0.5 * Incident.energy 
	theta_i    = Incident.theta
	pc_old     = sqrt(  Incident.energy**2         - Incident.mass**2  )
	pc_new     = sqrt( new_energy**2  - Incident.mass**2  )
	pc_g       = Incident.energy / (2.0)
	if TF_rand():
		theta_e = (1./(2. * (pc_g * pc_new + pc_new**2))) * (2. * pc_new * pc_old * theta_i - sqrt(4. * pc_new**2 * pc_old**2 * theta_i**2 - 4. * (-pc_g * pc_new - pc_new**2) * (2. * pc_g**2 + 2. * pc_g * pc_new - 2. * pc_g * pc_old + pc_g * pc_old * theta_i**2 - pc_old**2 * theta_i**2)))
		theta_g = -(1./pc_g) * (pc_old * theta_i - (pc_new**2 * pc_old * theta_i)/(pc_g * pc_new + pc_new**2) + (1./(2. * (pc_g * pc_new + pc_new**2))) * pc_new * sqrt(4. * pc_new**2 * pc_old**2 * theta_i**2 - 4. * (-pc_g * pc_new - pc_new**2) * (2. * pc_g**2 + 2. * pc_g * pc_new - 2. * pc_g * pc_old + pc_g * pc_old * theta_i**2 - pc_old**2 * theta_i**2)))

	else:
		theta_e = (1./(2. * (pc_g * pc_new + pc_new**2))) * (2. * pc_new * pc_old * theta_i + sqrt(4. * pc_new**2 * pc_old**2 * theta_i**2 - 4. * (-pc_g * pc_new - pc_new**2) * (2. * pc_g**2 + 2. * pc_g * pc_new - 2. * pc_g * pc_old + pc_g * pc_old * theta_i**2 - pc_old**2 * theta_i**2)))
		theta_g = -(1./pc_g) * (pc_old * theta_i - (pc_new**2 * pc_old * theta_i)/(pc_g * pc_new + pc_new**2) - (1./(2. * (pc_g * pc_new + pc_new**2))) * pc_new * sqrt(4. * pc_new**2 * pc_old**2 * theta_i**2 - 4. * (-pc_g * pc_new - pc_new**2) * (2. * pc_g**2 + 2. * pc_g * pc_new - 2. * pc_g * pc_old + pc_g * pc_old * theta_i**2 - pc_old**2 * theta_i**2)))

	x_e_pos = Incident.x_pos + X_o * sin(theta_e)
	y_e_pos = Incident.y_pos + X_o * cos(theta_e)

	x_g_pos = Incident.x_pos - X_o * sin(theta_g)
	y_g_pos = Incident.y_pos + X_o * cos(theta_g)

	input_list.append(Particle(Incident.name, new_energy, x_e_pos, y_e_pos, theta_p))
	input_list.append(Particle('gamma', new_energy, x_g_pos, y_g_pos, -theta_g))
	return
	
	


#-------------------------------------------------------------------------




#-------------------------------------------------------------------------
#TESTING

#pc_new  = 3.44
#pc_old  = 4.55
#theta_i = 5.66
#
#theta_p = (pc_old * theta_i / ( 2.0 * pc_new )) + (sqrt(8. * pc_new**2 + -4. * pc_old * pc_new - pc_old**2 * theta_i**2 + 2. * pc_old * pc_new * theta_i**2  ) / (2. * pc_new))
#theta_e = -(pc_old * theta_i / ( 2.0 * pc_new )) + (sqrt(8. * pc_new**2 + -4. * pc_old * pc_new - pc_old**2 * theta_i**2 + 2. * pc_old * pc_new * theta_i**2  ) / (2. * pc_new))
#
#print 'theta_p is: %r' % theta_p
#print 'theta_e is: %r' % theta_e
#
#theta_p = (pc_old * theta_i / ( 2.0 * pc_new )) - (sqrt(8. * pc_new**2 + -4. * pc_old * pc_new - pc_old**2 * theta_i**2 + 2. * pc_old * pc_new * theta_i**2  ) / (2. * pc_new))
#theta_e = -(pc_old * theta_i / ( 2.0 * pc_new )) - (sqrt(8. * pc_new**2 + -4. * pc_old * pc_new - pc_old**2 * theta_i**2 + 2. * pc_old * pc_new * theta_i**2  ) / (2. * pc_new))
#
#print 'theta_p is: %r' % theta_p
#print 'theta_e is: %r' % theta_e

#-------------------------------------------------------------------------


