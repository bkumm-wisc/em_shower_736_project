#-------------------------------------------------------------------------
#IMPORTS

#em_shower Imports (none)

#Other Imports
from math import sqrt, cos, sin, log, ceil, sqrt, pi
from random import getrandbits
import numpy as np

#-------------------------------------------------------------------------



#-------------------------------------------------------------------------
#CLASSES
class Particle:

	def __init__(self, name, energy, x_pos, y_pos, theta):

		name_to_mass = {'electron':0.510998946 , 'poistron':0.510998946, 'nitrogen':13047., 'gamma':0.0}


		self.name    = str(name)
		self.mass    = float(name_to_mass[name])
		self.energy  = float(energy)
		self.x_pos   = float(x_pos)
		self.y_pos   = float(y_pos)
		self.theta   = float(theta)

		if name == 'gamma':
			self.vel = 1
		else:
			self.vel = sqrt(1.0 - (float(self.mass) / float(self.energy)) ** 2.0)

		self.x_vel   = float(self.vel) * sin(theta)
		self.y_vel   = float(self.vel) * cos(theta)
		
#-------------------------------------------------------------------------