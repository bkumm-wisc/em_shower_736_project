#em_shower_main.py

#-------------------------------------------------------------------------
#IMPORTS

#em_shower imports
from em_shower_classes   import Particle
from em_shower_functions import TF_rand, delta_theta_calc
from em_shower_functions import get_Shower_tracks, name_Shower_list, energy_Shower_list, XY_Shower_list, electron_XY_Shower_list, positron_XY_Shower_list, gamma_XY_Shower_list, charged_XY_Shower_list
from em_shower_functions import BREMSSTRAHLUNG0, PAIR_PRODUCTION0, BREMSSTRAHLUNG1, PAIR_PRODUCTION1, BREMSSTRAHLUNG2, PAIR_PRODUCTION2, BREMSSTRAHLUNG3, PAIR_PRODUCTION3, BREMSSTRAHLUNG4, PAIR_PRODUCTION4
from em_shower_plotting  import plot_electron_position, plot_positron_position, plot_gamma_position, plot_charged_position, plot_all_position, plot_all_tracks, plot_charged_tracks, charged_density_histogram, electron_density_histogram, positron_density_histogram

#Other Imports
from math import sqrt, cos, sin, log, ceil, sqrt, pi
from random import getrandbits
import numpy as np
import pylab as pl

#-------------------------------------------------------------------------



#-------------------------------------------------------------------------
#MODEL PARAMETERS

#Integers
## None for now ##

#Original Particle Parameters
Orig_type   = 'gamma' # gamma, electron, or positron
Orig_energy = (2.**9*80. - 1) 		#Mev
Orig_x_pos  = 0.					#cm
Orig_y_pos  = 0.					#cm
Orig_theta  = 0.    				#radians
Orig_pid    = 0						#integer (leave as 0)


#Floats
E_crit      = 80.0					#MeV
X_o         = 36.0					#cm
#Density     = 0.00135				
print "\nNumber of interactions is approximately: %r\n" % (ceil( log(Orig_energy / E_crit) / log(2.)) )


#Truth Values (Which assumptions to make for the model)
Const_scat_dist  = True
Const_scat_angle = True
Const_E_loss     = True
All_travel_X_o   = True
Gaussian_X_o     = False
Gaussian_Angle   = False

#Preliminary Calculations
delta_theta = delta_theta_calc(Orig_energy,E_crit)


#Chosing which BREMSSTRAHLUNG and PAIR_PRODUCTION functions to use from Truth Value Parameters
if Const_scat_dist and Const_scat_angle and Const_E_loss and All_travel_X_o and not Gaussian_X_o and not Gaussian_Angle:
	print '\nUSING: BREMSSTRAHLUNG0 and PAIR_PRODUCTION0\n\n'
	BREMSSTRAHLUNG  = BREMSSTRAHLUNG0
	PAIR_PRODUCTION = PAIR_PRODUCTION0 
elif Const_scat_dist and Const_scat_angle and Const_E_loss and not All_travel_X_o and not Gaussian_X_o and not Gaussian_Angle:
	print 'using BREMSSTRAHLUNG1 and PAIR_PRODUCTION1'
	BREMSSTRAHLUNG  = BREMSSTRAHLUNG1
	PAIR_PRODUCTION = PAIR_PRODUCTION1 
elif not Const_scat_dist and Const_scat_angle and Const_E_loss and All_travel_X_o and not Gaussian_X_o and not Gaussian_Angle:
	print 'using BREMSSTRAHLUNG2 and PAIR_PRODUCTION2'
	BREMSSTRAHLUNG  = BREMSSTRAHLUNG2
	PAIR_PRODUCTION = PAIR_PRODUCTION2 
elif not Const_scat_dist and Const_scat_angle and Const_E_loss and not All_travel_X_o and Gaussian_X_o and not Gaussian_Angle:
	print 'using BREMSSTRAHLUNG3 and PAIR_PRODUCTION3'
	BREMSSTRAHLUNG  = BREMSSTRAHLUNG3
	PAIR_PRODUCTION = PAIR_PRODUCTION3 
elif not Const_scat_dist and Const_scat_angle and Const_E_loss and not All_travel_X_o and  Gaussian_X_o and Gaussian_Angle:
	print 'using BREMSSTRAHLUNG4 and PAIR_PRODUCTION4'
	BREMSSTRAHLUNG  = BREMSSTRAHLUNG4
	PAIR_PRODUCTION = PAIR_PRODUCTION4


#-------------------------------------------------------------------------




#-------------------------------------------------------------------------
#ITERATING TO DEVELOP THE SHOWER

#Defining various objects
Original_Particle = Particle(Orig_type, Orig_energy, Orig_x_pos, Orig_y_pos, Orig_theta, Orig_pid)
pid_list          = [0]
Shower_list       = [ [Original_Particle] ]

#Is E greater than E_crit?
E_gt_E_crit = True

if not Orig_energy > E_crit:
	print "\nORIGINAL PARTICLE ENERGY NOT GREATER THAN E_crit ... NO AIR SHOWER DEVELOPS\n"
	E_gt_E_crit = False


#Before E < E_crit
while E_gt_E_crit:
	print 'PERFORMING AN ITERATION'

	previous_list = Shower_list[-1]
	new_list      = []
	for part in previous_list:
		if part.energy > E_crit:
			if part.name == 'gamma':
				PAIR_PRODUCTION(part,new_list,delta_theta,X_o,pid_list)
			else:
				BREMSSTRAHLUNG(part,new_list,delta_theta,X_o,pid_list)

		#else:             #######################################################################
			#scatter electrons
		else:              
			new_list.append(part)
	print "Number of particles is now: %r" % (len(new_list))
	Shower_list.append(new_list)
	if all( Shower_list[-1][i].energy < E_crit for i in range(len(Shower_list[-1])) ):
		E_gt_E_crit = False

	


#-------------------------------------------------------------------------




#-------------------------------------------------------------------------
#OUTPUTS / TESTING

#print electron_XY_Shower_list(Shower_list)
#
#print electron_XY_Shower_list(Shower_list)[-1]
#
#plot_positron_position(Shower_list)
#plot_electron_position(Shower_list)
#plot_gamma_position(Shower_list)
#
#print pid_list

#print gamma_XY_Shower_list(Shower_list)

plot_charged_tracks(Shower_list,pid_list)

charged_density_histogram(Shower_list)




#-------------------------------------------------------------------------
