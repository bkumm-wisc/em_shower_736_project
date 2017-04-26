#em_shower_main.py

#-------------------------------------------------------------------------
#IMPORTS

#em_shower imports
from em_shower_classes   import Particle
from em_shower_functions import BREMSSTRAHLUNG1, PAIR_PRODUCTION1


#Other imports
from math   import cos, log, ceil, sqrt, pi
from random import getrandbits
import numpy as np

#-------------------------------------------------------------------------




#-------------------------------------------------------------------------
#MODEL PARAMETERS

#Original Particle Parameters
Orig_type   = 'electron' # gamma, electron, or positron
Orig_energy = 500.
Orig_x_pos  = 0.
Orig_y_pos  = 0.
Orig_theta  = pi/4.


#Truth Values (Which assumptions to make for the model)
Const_scat_angle = True
Const_E_loss     = True
Const_scat_dist  = True

#Integers
## None for now ##

#Floats
Theta_scat  = 0.000000002
E_loss      = 2.0
E_crit      = 76.0
X_o         = 36.0
Density     = 0.00135

#Chosing which BREMSSTRAHLUNG and PAIR_PRODUCTION functions to from Truth Value Parameters
if Const_scat_dist and Const_scat_angle and Const_E_loss:
	BREMSSTRAHLUNG  = BREMSSTRAHLUNG1
	PAIR_PRODUCTION = PAIR_PRODUCTION1 

#-------------------------------------------------------------------------




#-------------------------------------------------------------------------
#ITERATING TO DEVELOP THE SHOWER

Original_Particle = Particle(Orig_type, Orig_energy, Orig_x_pos, Orig_y_pos, Orig_theta)
Shower_list       = [ [Original_Particle] ]
print Shower_list


N_crit = int( ceil( log(Original_Particle.energy/E_crit) / log(2.0) )) 

keep_going = False

#Before E < E_crit
while keep_going:
	previous_list = Shower_list[-1]
	new_list      = []
	for part in previous_list:
		if part.energy > E_crit:
			if part.name == 'gamma':
				PAIR_PRODUCTION(part,new_list)
			else:
				BREMSSTRAHLUNG(part,new_list)

		else:
			scatter electrons


#-------------------------------------------------------------------------




#-------------------------------------------------------------------------
#Testing

test_list = [1]
print "test list before is: %r" % test_list
BREMSSTRAHLUNG(Original_Particle,test_list,1,0)
print "test list after is: %r" % test_list


#-------------------------------------------------------------------------
