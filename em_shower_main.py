#em_shower_main.py

#-------------------------------------------------------------------------
#IMPORTS

#em_shower imports
from em_shower_classes   import Particle
from em_shower_functions import TF_rand, delta_theta_calc, Energy_Shower_list, XY_Shower_list
from em_shower_functions import BREMSSTRAHLUNG0, PAIR_PRODUCTION0, BREMSSTRAHLUNG1, PAIR_PRODUCTION1


#Other Imports
from math import sqrt, cos, sin, log, ceil, sqrt, pi
from random import getrandbits
import numpy as np

#-------------------------------------------------------------------------




#-------------------------------------------------------------------------
#MODEL PARAMETERS

#Original Particle Parameters
Orig_type   = 'gamma' # gamma, electron, or positron
Orig_energy = 800.
Orig_x_pos  = 0.
Orig_y_pos  = 0.
Orig_theta  = 0.



#Truth Values (Which assumptions to make for the model)
Const_scat_angle = True
Const_E_loss     = True
Const_scat_dist  = True

#Integers
## None for now ##

#Floats
E_crit      = 76.0
X_o         = 36.0
Density     = 0.00135
print "N is: %r" % (log(Orig_energy / E_crit) / log(2.))

#Chosing which BREMSSTRAHLUNG and PAIR_PRODUCTION functions to use from Truth Value Parameters
if Const_scat_dist and Const_scat_angle and Const_E_loss:
	BREMSSTRAHLUNG  = BREMSSTRAHLUNG0
	PAIR_PRODUCTION = PAIR_PRODUCTION0 

#Preliminary Calculations
delta_theta = delta_theta_calc(Orig_energy,E_crit)

#-------------------------------------------------------------------------




#-------------------------------------------------------------------------
#ITERATING TO DEVELOP THE SHOWER

Original_Particle = Particle(Orig_type, Orig_energy, Orig_x_pos, Orig_y_pos, Orig_theta)
Shower_list       = [ [Original_Particle] ]
print Shower_list


N_crit = int( ceil( log(Original_Particle.energy/E_crit) / log(2.0) )) 

E_gt_E_crit = True

#Before E < E_crit
while E_gt_E_crit:
	print 'PERFORMING ANTOHER ITERATION'

	previous_list = Shower_list[-1]
	new_list      = []
	for part in previous_list:
		if part.energy > E_crit:
			if part.name == 'gamma':
				PAIR_PRODUCTION(part,new_list,delta_theta,X_o)
			else:
				BREMSSTRAHLUNG(part,new_list,delta_theta,X_o)

		#else:             #######################################################################
			#scatter electrons
		else:              #######################################################################
			new_list.append(part)
	print "length of new_list is: %r" % (len(new_list))
	Shower_list.append(new_list)
	if all( Shower_list[-1][i].energy < E_crit for i in range(len(Shower_list[-1])) ):
		E_gt_E_crit = False

	


#-------------------------------------------------------------------------




#-------------------------------------------------------------------------
#Testing

print XY_Shower_list(Shower_list)


#-------------------------------------------------------------------------
