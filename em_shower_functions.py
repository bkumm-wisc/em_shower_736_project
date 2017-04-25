#em_shower_functions.py

#-------------------------------------------------------------------------
#IMPORTS

#em_shower imports

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

def BREMSSTRAHLUNG1(Incident,input_list,delta_E_factor):
	new_energy = Incident.energy * delta_E_factor
	theta_i    = Incident.theta
	p_new      = sqrt( (new_energy) **2 - Incident.mass **2)
	a          = new_energy * theta_i / ( 2.0 * p_new ) 
	b          = sqrt(8.0 * p_new**4 + -4.0 * new_energy * p_new**3 - new_energy**2 * p_new**2 * theta_i**2 + 2 * new_energy *p_new**3 * theta_i**2  ) / (2.0 * p_new**2)
	if TF_rand: 
		theta_p = 

		theta_e = 
	
	else:
		theta_p = 

		theta_e = 

	return

def PAIR_PRODUCTION1(Particle,input_list):
	return 1


#-------------------------------------------------------------------------




#-------------------------------------------------------------------------
#TESTING
for i in range(50):
	print bool(getrandbits(1))


#-------------------------------------------------------------------------


