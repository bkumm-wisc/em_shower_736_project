#em_shower_functions.py

#-------------------------------------------------------------------------
#IMPORTS

#em_shower imports
from em_shower_classes import Particle

#Other Imports
from math import sqrt, cos, sin, log, ceil, sqrt, pi
from random import getrandbits
import numpy as np
import pylab as pl

#-------------------------------------------------------------------------




#-------------------------------------------------------------------------
#Initial functions
def delta_theta_calc(E,E_crit):
	N_max = ceil( log(E / E_crit) / log(2.) )
	return 2. / ( float(N_max) * (float(N_max) + 1) )

def TF_rand():
	return bool(getrandbits(1))
#-------------------------------------------------------------------------




#-------------------------------------------------------------------------
#Particle interactions

def PAIR_PRODUCTION0(Incident, input_list, delta_theta, X_o, pid_list):
	new_energy  = Incident.energy * 0.5

	if TF_rand():
		theta_e = Incident.theta + delta_theta
		theta_p = Incident.theta - delta_theta
	else:
		theta_e = Incident.theta - delta_theta
		theta_p = Incident.theta + delta_theta

	x_e_pos = Incident.x_pos + X_o * sin(theta_e)
	y_e_pos = Incident.y_pos + X_o * cos(theta_e)

	x_p_pos = Incident.x_pos + X_o * sin(theta_p)
	y_p_pos = Incident.y_pos + X_o * cos(theta_p)

	old_pid_max = max(pid_list)

	input_list.append(Particle('electron', new_energy, x_e_pos, y_e_pos, theta_e, old_pid_max + 1 ))
	input_list.append(Particle('positron', new_energy, x_p_pos, y_p_pos, theta_p, old_pid_max + 2 ))	

	pid_list.append( old_pid_max + 1 )
	pid_list.append( old_pid_max + 2)

	return

def BREMSSTRAHLUNG0(Incident, input_list, delta_theta, X_o, pid_list):
	new_energy  = Incident.energy *0.5

	if TF_rand():
		theta_e = Incident.theta + delta_theta
		theta_g = Incident.theta - delta_theta
	else:
		theta_e = Incident.theta - delta_theta
		theta_g = Incident.theta + delta_theta

	x_e_pos = Incident.x_pos + X_o * sin(theta_e)
	y_e_pos = Incident.y_pos + X_o * cos(theta_e)

	x_g_pos = Incident.x_pos + X_o * sin(theta_g)
	y_g_pos = Incident.y_pos + X_o * cos(theta_g)

	old_pid_max = max(pid_list)

	input_list.append(Particle(Incident.name, new_energy, x_e_pos, y_e_pos, theta_e, Incident.pid))
	input_list.append(Particle('gamma', new_energy, x_g_pos, y_g_pos, theta_g, old_pid_max + 1 ))

	pid_list.append(old_pid_max + 1)

	return

#def PAIR_PRODUCTION10(Incident, input_list, X_o):     ##################### USELESS ##################### 
#	"""
#	each particle gets half of incident energy and thetas calculated from small angle approx of conservation of momentum equations
#	"""
#	theta_i    = Incident.theta
#	pc_old     = Incident.energy   
#	new_energy = 0.5 * Incident.energy
#	pc_new      = sqrt( (new_energy)**2 - 0.510998946 **2 ) 
#	if TF_rand(): 
#		theta_p =  ( (pc_old * theta_i) - (sqrt(8. * pc_new**2 - 4. * pc_old * pc_new - pc_old**2 * theta_i**2 + 2. * pc_old * pc_new * theta_i**2  ) ) / (2. * pc_new))
#		theta_e = -( (pc_old * theta_i) - (sqrt(8. * pc_new**2 - 4. * pc_old * pc_new - pc_old**2 * theta_i**2 + 2. * pc_old * pc_new * theta_i**2  ) ) / (2. * pc_new))
#	
#	else:
#		theta_p =  (pc_old * theta_i / ( 2.0 * pc_new )) - (sqrt(8. * pc_new**2 + -4. * pc_old * pc_new - pc_old**2 * theta_i**2 + 2. * pc_old * pc_new * theta_i**2  ) / (2. * pc_new))
#		theta_e = -(pc_old * theta_i / ( 2.0 * pc_new )) - (sqrt(8. * pc_new**2 + -4. * pc_old * pc_new - pc_old**2 * theta_i**2 + 2. * pc_old * pc_new * theta_i**2  ) / (2. * pc_new))
#
#	x_p_pos = Incident.x_pos + X_o * sin(theta_p)
#	y_p_pos = Incident.y_pos + X_o * cos(theta_p)
#
#	x_e_pos = Incident.x_pos - X_o * sin(theta_e)
#	y_e_pos = Incident.y_pos + X_o * cos(theta_e)
#
#	input_list.append(Particle('positron', new_energy, x_p_pos, y_p_pos,  theta_p))
#	input_list.append(Particle('electron', new_energy, x_e_pos, y_e_pos, -theta_e))
#	return
#
#def BREMSSTRAHLUNG10(Incident, input_list, delta_E_factor, X_o):   ##################### USELESS ##################### 
#	new_energy = 0.5 * Incident.energy 
#	theta_i    = Incident.theta
#	pc_old     = sqrt(  Incident.energy**2         - Incident.mass**2  )
#	pc_new     = sqrt( new_energy**2  - Incident.mass**2  )
#	pc_g       = Incident.energy / (2.0)
#	if TF_rand():
#		theta_e = (1./(2. * (pc_g * pc_new + pc_new**2))) * (2. * pc_new * pc_old * theta_i - sqrt(4. * pc_new**2 * pc_old**2 * theta_i**2 - 4. * (-pc_g * pc_new - pc_new**2) * (2. * pc_g**2 + 2. * pc_g * pc_new - 2. * pc_g * pc_old + pc_g * pc_old * theta_i**2 - pc_old**2 * theta_i**2)))
#		theta_g = -(1./pc_g) * (pc_old * theta_i - (pc_new**2 * pc_old * theta_i)/(pc_g * pc_new + pc_new**2) + (1./(2. * (pc_g * pc_new + pc_new**2))) * pc_new * sqrt(4. * pc_new**2 * pc_old**2 * theta_i**2 - 4. * (-pc_g * pc_new - pc_new**2) * (2. * pc_g**2 + 2. * pc_g * pc_new - 2. * pc_g * pc_old + pc_g * pc_old * theta_i**2 - pc_old**2 * theta_i**2)))
#
#	else:
#		theta_e = (1./(2. * (pc_g * pc_new + pc_new**2))) * (2. * pc_new * pc_old * theta_i + sqrt(4. * pc_new**2 * pc_old**2 * theta_i**2 - 4. * (-pc_g * pc_new - pc_new**2) * (2. * pc_g**2 + 2. * pc_g * pc_new - 2. * pc_g * pc_old + pc_g * pc_old * theta_i**2 - pc_old**2 * theta_i**2)))
#		theta_g = -(1./pc_g) * (pc_old * theta_i - (pc_new**2 * pc_old * theta_i)/(pc_g * pc_new + pc_new**2) - (1./(2. * (pc_g * pc_new + pc_new**2))) * pc_new * sqrt(4. * pc_new**2 * pc_old**2 * theta_i**2 - 4. * (-pc_g * pc_new - pc_new**2) * (2. * pc_g**2 + 2. * pc_g * pc_new - 2. * pc_g * pc_old + pc_g * pc_old * theta_i**2 - pc_old**2 * theta_i**2)))
#
#	x_e_pos = Incident.x_pos + X_o * sin(theta_e)
#	y_e_pos = Incident.y_pos + X_o * cos(theta_e)
#
#	x_g_pos = Incident.x_pos - X_o * sin(theta_g)
#	y_g_pos = Incident.y_pos + X_o * cos(theta_g)
#
#	input_list.append(Particle(Incident.name, new_energy, x_e_pos, y_e_pos, theta_p))
#	input_list.append(Particle('gamma', new_energy, x_g_pos, y_g_pos, -theta_g))
#	return
	
def PAIR_PRODUCTION1(Incident, input_list, delta_theta, X_o, pid_list):
	new_energy  = Incident.energy * 0.5

	if TF_rand():
		theta_e = Incident.theta + delta_theta
		theta_p = Incident.theta - delta_theta
	else:
		theta_e = Incident.theta - delta_theta
		theta_p = Incident.theta + delta_theta

	x_e_pos = Incident.x_pos + X_o * theta_e
	y_e_pos = Incident.y_pos + X_o * (1. - theta_e**2 / 2.)

	x_p_pos = Incident.x_pos + X_o * theta_p
	y_p_pos = Incident.y_pos + X_o * (1. - theta_p**2 / 2.)

	old_pid_max = max(pid_list)

	input_list.append(Particle('electron', new_energy, x_e_pos, y_e_pos, theta_e, old_pid_max + 1 ))
	input_list.append(Particle('positron', new_energy, x_p_pos, y_p_pos, theta_p, old_pid_max + 2 ))	

	pid_list.append( old_pid_max + 1 )
	pid_list.append( old_pid_max + 2)

	return

def BREMSSTRAHLUNG1(Incident, input_list, delta_theta, X_o, pid_list):
	new_energy  = Incident.energy * 0.5

	if TF_rand():
		theta_e = Incident.theta + delta_theta
		theta_p = Incident.theta - delta_theta
	else:
		theta_e = Incident.theta - delta_theta
		theta_p = Incident.theta + delta_theta

	x_e_pos = Incident.x_pos + X_o * theta_e
	y_e_pos = Incident.y_pos + X_o * (1. - theta_e**2 / 2.)

	x_g_pos = Incident.x_pos + (9./7.) * X_o * theta_p
	y_g_pos = Incident.y_pos + (9./7.) * X_o * (1. - theta_p**2 / 2.)

	old_pid_max = max(pid_list)

	input_list.append(Particle(Incident.name, new_energy, x_e_pos, y_e_pos, theta_e, Incident.pid ))
	input_list.append(Particle('gamma', new_energy, x_g_pos, y_g_pos, theta_p, old_pid_max + 1 ))	

	pid_list.append( old_pid_max + 1 )

	return

def PAIR_PRODUCTION2(Incident, input_list, delta_theta, X_o, pid_list):
	new_energy  = Incident.energy * 0.5

	if TF_rand():
		theta_e = Incident.theta + delta_theta
		theta_p = Incident.theta - delta_theta
	else:
		theta_e = Incident.theta - delta_theta
		theta_p = Incident.theta + delta_theta

	x_e_pos = Incident.x_pos + np.random.normal(X_o, X_o) * theta_e
	y_e_pos = Incident.y_pos + np.random.normal(X_o, X_o) * (1. - theta_e**2 / 2.)

	x_p_pos = Incident.x_pos + np.random.normal(X_o, X_o) * theta_p
	y_p_pos = Incident.y_pos + np.random.normal(X_o, X_o) * (1. - theta_p**2 / 2.)

	old_pid_max = max(pid_list)

	input_list.append(Particle('electron', new_energy, x_e_pos, y_e_pos, theta_e, old_pid_max + 1 ))
	input_list.append(Particle('positron', new_energy, x_p_pos, y_p_pos, theta_p, old_pid_max + 2 ))	

	pid_list.append( old_pid_max + 1 )
	pid_list.append( old_pid_max + 2)

	return

def BREMSSTRAHLUNG2(Incident, input_list, delta_theta, X_o, pid_list):
	new_energy  = Incident.energy * 0.5

	if TF_rand():
		theta_e = Incident.theta + delta_theta
		theta_p = Incident.theta - delta_theta
	else:
		theta_e = Incident.theta - delta_theta
		theta_p = Incident.theta + delta_theta

	x_e_pos = Incident.x_pos + np.random.normal(X_o, X_o) * theta_e
	y_e_pos = Incident.y_pos + np.random.normal(X_o, X_o) * (1. - theta_e**2 / 2.)

	x_g_pos = Incident.x_pos + np.random.normal(X_o, X_o) * theta_p
	y_g_pos = Incident.y_pos + np.random.normal(X_o, X_o) * (1. - theta_p**2 / 2.)

	old_pid_max = max(pid_list)

	input_list.append(Particle(Incident.name, new_energy, x_e_pos, y_e_pos, theta_e, Incident.pid ))
	input_list.append(Particle('gamma', new_energy, x_g_pos, y_g_pos, theta_p, old_pid_max + 1 ))	

	pid_list.append( old_pid_max + 1 )
	
	return


def PAIR_PRODUCTION3(Incident, input_list, delta_theta, X_o, pid_list):
	new_energy  = Incident.energy * 0.5

	if TF_rand():
		theta_e = Incident.theta + delta_theta
		theta_p = Incident.theta - delta_theta
	else:
		theta_e = Incident.theta - delta_theta
		theta_p = Incident.theta + delta_theta

	x_e_pos = Incident.x_pos + np.random.normal(X_o, X_o / 10.) * sin(theta_e)
	y_e_pos = Incident.y_pos + np.random.normal(X_o, X_o / 10.) * cos(theta_e)

	x_p_pos = Incident.x_pos + np.random.normal(X_o, X_o / 10.) * sin(theta_p)
	y_p_pos = Incident.y_pos + np.random.normal(X_o, X_o / 10.) * cos(theta_p)

	old_pid_max = max(pid_list)

	input_list.append(Particle('electron', new_energy, x_e_pos, y_e_pos, theta_e, old_pid_max + 1 ))
	input_list.append(Particle('positron', new_energy, x_p_pos, y_p_pos, theta_p, old_pid_max + 2 ))	

	pid_list.append( old_pid_max + 1 )
	pid_list.append( old_pid_max + 2)

	return

def BREMSSTRAHLUNG3(Incident, input_list, delta_theta, X_o, pid_list):
	new_energy  = Incident.energy * 0.5

	if TF_rand():
		theta_e = Incident.theta + delta_theta
		theta_p = Incident.theta - delta_theta
	else:
		theta_e = Incident.theta - delta_theta
		theta_p = Incident.theta + delta_theta

	x_e_pos = Incident.x_pos + np.random.normal(X_o, X_o / 10.) * sin(theta_e)
	y_e_pos = Incident.y_pos + np.random.normal(X_o, X_o / 10.) * cos(theta_e)

	x_g_pos = Incident.x_pos + np.random.normal((9./7.) * X_o, (9./7.) * X_o / 10. ) * sin(theta_p)
	y_g_pos = Incident.y_pos + np.random.normal((9./7.) * X_o, (9./7.) * X_o / 10. ) * cos(theta_p)

	old_pid_max = max(pid_list)

	input_list.append(Particle(Incident.name, new_energy, x_e_pos, y_e_pos, theta_e, Incident.pid ))
	input_list.append(Particle('gamma', new_energy, x_g_pos, y_g_pos, theta_p, old_pid_max + 1 ))	

	pid_list.append( old_pid_max + 1 )
	
	return


def PAIR_PRODUCTION4(Incident, input_list, delta_theta, X_o, pid_list):
	new_energy  = Incident.energy * 0.5
	rand_delta_theta = np.random.normal(0,pi/100.)

	if TF_rand():
		theta_e = Incident.theta + rand_delta_theta
		theta_p = Incident.theta - rand_delta_theta
	else:
		theta_e = Incident.theta - rand_delta_theta
		theta_p = Incident.theta + rand_delta_theta

	x_e_pos = Incident.x_pos + np.random.normal(X_o,X_o / 4) * sin(theta_e)
	y_e_pos = Incident.y_pos + np.random.normal(X_o,X_o / 4) * cos(theta_e)

	x_p_pos = Incident.x_pos + np.random.normal(X_o,X_o / 4) * sin(theta_p)
	y_p_pos = Incident.y_pos + np.random.normal(X_o,X_o / 4) * cos(theta_p)

	old_pid_max = max(pid_list)

	input_list.append(Particle('electron', new_energy, x_e_pos, y_e_pos, theta_e, old_pid_max + 1 ))
	input_list.append(Particle('positron', new_energy, x_p_pos, y_p_pos, theta_p, old_pid_max + 2 ))	

	pid_list.append( old_pid_max + 1 )
	pid_list.append( old_pid_max + 2)

	return

def BREMSSTRAHLUNG4(Incident, input_list, delta_theta, X_o, pid_list):
	new_energy  = Incident.energy * 0.5
	rand_delta_theta = np.random.normal(0,pi/10000.)

	if TF_rand():
		theta_e = Incident.theta + rand_delta_theta
		theta_p = Incident.theta - rand_delta_theta
	else:
		theta_e = Incident.theta - rand_delta_theta
		theta_p = Incident.theta + rand_delta_theta

	x_e_pos = Incident.x_pos + np.random.normal(X_o,X_o / 4) * sin(theta_e)	
	y_e_pos = Incident.y_pos + np.random.normal(X_o,X_o / 4) * cos(theta_e)

	x_g_pos = Incident.x_pos + np.random.normal((9./7.) * X_o, (9./7.) * X_o / 4) * sin(theta_p)	
	y_g_pos = Incident.y_pos + np.random.normal((9./7.) * X_o, (9./7.) * X_o / 4) * cos(theta_p)

	old_pid_max = max(pid_list)

	input_list.append(Particle(Incident.name, new_energy, x_e_pos, y_e_pos, theta_e, Incident.pid ))
	input_list.append(Particle('gamma', new_energy, x_g_pos, y_g_pos, theta_p, old_pid_max + 1 ))	

	pid_list.append( old_pid_max + 1 )

	
	return


#-------------------------------------------------------------------------



#-------------------------------------------------------------------------
#Shower_list data manipulation functions 

def get_Shower_tracks(Shower_list,pid_list):

	Shower_tracks = [['',[],[]] for pid in pid_list]
	for part_list in Shower_list:
		for part in part_list:
			if Shower_tracks[part.pid][0] == '':
				Shower_tracks[part.pid][0] = part.name
			Shower_tracks[part.pid][1].append(part.x_pos)
			Shower_tracks[part.pid][2].append(-part.y_pos)

	return Shower_tracks

def name_Shower_list(Shower_list):
	master_list = []
	for part_list in Shower_list:
		new_name_list = []
		for part in part_list:
			new_name_list.append(part.name)
		master_list.append(new_name_list)

	return master_list

def energy_Shower_list(Shower_list):
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

	return master_list

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

def charged_XY_Shower_list(Shower_list):
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


