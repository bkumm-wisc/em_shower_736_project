#em_shower_functions.py

#-------------------------------------------------------------------------
#IMPORTS

#em_shower imports
from em_shower_classes import Particle

#Other imports
from random import getrandbits
import numpy as np

#-------------------------------------------------------------------------




#-------------------------------------------------------------------------
#Other functions
def TF_rand():
	return bool(getrandbits(1))

#-------------------------------------------------------------------------




#-------------------------------------------------------------------------
#Particle interactions

def PAIR_PRODUCTION1(Incident, input_list, delta_E_factor, X_o):
	"""
	each particle gets half of incident energy and thetas calculated from small angle approx of conservation of momentum equations
	"""
	new_energy = Incident.energy * delta_E_factor
	theta_i    = Incident.theta
	p_new      = sqrt( (new_energy) **2 - 0.510998946 **2 )
	a          = new_energy * theta_i / ( 2.0 * p_new ) 
	b          = sqrt(8.0 * p_new**2 + -4.0 * new_energy * p_new - new_energy**2 * theta_i**2 + 2 * new_energy *p_new * theta_i**2  ) / (2.0 * p_new)
	if TF_rand: 
		theta_p = a - b
		theta_e = -a - b
	
	else:
		theta_p = a + b
		theta_e = -a + b

	x_p_pos = Incident.x_pos + X_o * sin(theta_p)
	y_p_pos = Incident.y_pos + X_o * cos(theta_p)
	x_e_pos = Incident.x_pos - X_o * sin(theta_e)
	y_e_pos = Incident.y_pos + X_o * cos(theta_e)


	inputlist.append(Particle('positron', new_energy, x_p_pos, y_p_pos, theta_p), Particle('electron', new_energy, x_e_pos, y_e_pos, theta_e))
	return

def BREMSSTRAHLUNG1(Incident, input_list, delta_E_factor, X_o):
	new_energy = Incident.energy
	theta_i    = Incident.theta
	p_new_e    =
	


#-------------------------------------------------------------------------




#-------------------------------------------------------------------------
#TESTING
for i in range(50):
	print bool(getrandbits(1))


#-------------------------------------------------------------------------


