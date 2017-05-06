#em_shower_plotting.py

#-------------------------------------------------------------------------
#IMPORTS

#em_shower imports
from em_shower_classes import Particle
from em_shower_functions import get_Shower_tracks

#Other Imports
from math import sqrt, cos, sin, log, ceil, sqrt, pi
from random import getrandbits
import matplotlib.patches as mpatches
import numpy as np
import pylab as pl

#-------------------------------------------------------------------------




#-------------------------------------------------------------------------
#Position Scatter Plots Funtions

def plot_all_position(Shower_list):
	x_list = []
	y_list = []
	for part_list in Shower_list:
		for part in part_list:
			x_list.append(part.x_pos)
			y_list.append(-part.y_pos)
	pl.scatter(x_list,y_list)
	pl.show()

	return

def plot_electron_position(Shower_list):
	x_list = []
	y_list = []
	for part_list in Shower_list:
		for part in part_list:
			if part.name == 'electron':
				x_list.append(part.x_pos)
				y_list.append(-part.y_pos)
	pl.scatter(x_list,y_list, color = 'r')
	pl.title('X and Y Positions of Electrons Durring Shower Developement')
	pl.xlabel('x position (cm)')
	pl.ylabel('y position (cm)')
	pl.show()

	return

def plot_positron_position(Shower_list):
	x_list = []
	y_list = []
	for part_list in Shower_list:
		for part in part_list:
			if part.name == 'positron':
				x_list.append(part.x_pos)
				y_list.append(-part.y_pos)
	pl.scatter(x_list,y_list, color = 'b')
	pl.title('X and Y Positions of Positrons Durring Shower Developement')
	pl.xlabel('x position (cm)')
	pl.ylabel('y position (cm)')
	pl.show()

	return

def plot_gamma_position(Shower_list):
	x_list = []
	y_list = []
	for part_list in Shower_list:
		for part in part_list:
			if part.name == 'gamma':
				x_list.append(part.x_pos)
				y_list.append(-part.y_pos)
	pl.scatter(x_list,y_list, color = 'g')
	pl.title('X and Y Positions of Gammas Durring Shower Developement')
	pl.xlabel('x position (cm)')
	pl.ylabel('y position (cm)')
	pl.show()

	return

def plot_charged_position(Shower_list):
	x_list = []
	y_list = []
	for part_list in Shower_list:
		for part in part_list:
			if part.name in ['electron','positron']:
				x_list.append(part.x_pos)
				y_list.append(-part.y_pos)
	pl.scatter(x_list,y_list)
	pl.show()

	return

def plot_all_tracks(Shower_list,pid_list):
	Shower_tracks = get_Shower_tracks(Shower_list,pid_list)
	Plotted_electron = False
	Plotted_positron = False
	Plotted_gamma    = False
	for pid in pid_list:
		if Shower_tracks[pid][0] == 'electron' and not Plotted_electron:
			pl.plot(Shower_tracks[pid][1],Shower_tracks[pid][2], 'ro' , linestyle = '-', label = 'electron')
			Plotted_electron = True

		elif Shower_tracks[pid][0] == 'electron'and Plotted_electron:
			pl.plot(Shower_tracks[pid][1],Shower_tracks[pid][2], 'ro' , linestyle = '-')

		elif Shower_tracks[pid][0] == 'positron' and not Plotted_positron:
			pl.plot(Shower_tracks[pid][1],Shower_tracks[pid][2], 'bo' , linestyle = '-', label = 'positron')
			Plotted_positron = True

		elif Shower_tracks[pid][0] == 'positron' and Plotted_positron:
			pl.plot(Shower_tracks[pid][1],Shower_tracks[pid][2], 'bo' , linestyle = '-')

		elif Shower_tracks[pid][0] == 'gamma' and not Plotted_gamma:
			pl.plot(Shower_tracks[pid][1],Shower_tracks[pid][2], 'go' , linestyle = '-', label = 'gamma')
			Plotted_gamma = True

		elif Shower_tracks[pid][0] == 'gamma' and Plotted_gamma:
			pl.plot(Shower_tracks[pid][1],Shower_tracks[pid][2], 'go' , linestyle = '-')

	pl.title('Tracks of Particles Durring Shower developement')
	pl.xlabel('x position (cm)')
	pl.ylabel('y position (cm)')
	pl.legend()
	pl.show()
	return


def plot_charged_tracks(Shower_list,pid_list):
	Shower_tracks = get_Shower_tracks(Shower_list,pid_list)
	Plotted_electron = False
	Plotted_positron = False
	for pid in pid_list:
		if Shower_tracks[pid][0] == 'electron' and not Plotted_electron:
			pl.plot(Shower_tracks[pid][1],Shower_tracks[pid][2], 'ro' , linestyle = '-', label = 'electron')
			Plotted_electron = True
		elif Shower_tracks[pid][0] == 'electron' and Plotted_electron:
			pl.plot(Shower_tracks[pid][1],Shower_tracks[pid][2], 'ro' , linestyle = '-')

		elif Shower_tracks[pid][0] == 'positron' and not Plotted_positron:
			pl.plot(Shower_tracks[pid][1],Shower_tracks[pid][2], 'bo' , linestyle = '-', label = 'positron')
			Plotted_positron = True
		elif Shower_tracks[pid][0] == 'positron' and Plotted_positron:
			pl.plot(Shower_tracks[pid][1],Shower_tracks[pid][2], 'bo' , linestyle = '-')

	pl.title('Tracks of Charged Particles Durring Shower developement')
	pl.xlabel('x position (cm)')
	pl.ylabel('y position (cm)')
	pl.legend()
	pl.show()
	return

def charged_density_histogram(Shower_list):
	x_list = []
	for part in Shower_list[-1]:
		if part.name in ['electron','positron']:
			x_list.append(part.x_pos)
	pl.hist(x_list)
	pl.ylabel('Number of charged particles')
	pl.xlabel('Spatial Bins (cm)')
	pl.title('Histogram plot of Number of Charged particles per spatial bin')
	pl.show()

	return

def electron_density_histogram(Shower_list):
	x_list = []
	for part in Shower_list[-1]:
		if part.name == 'electron':
			x_list.append(part.x_pos)
	pl.hist(x_list)
	pl.ylabel('Number of charged particles')
	pl.xlabel('Spatial Bins (cm)')
	pl.title('Histogram plot of Number of electrons per spatial bin')
	pl.show()

	return

def positron_density_histogram(Shower_list):
	x_list = []
	for part in Shower_list[-1]:
		if part.name == 'positron':
			x_list.append(part.x_pos)
	pl.hist(x_list)
	pl.ylabel('Number of charged particles')
	pl.xlabel('Spatial Bins (cm)')
	pl.title('Histogram plot of Number of positrons per spatial bin')
	pl.show()

	return


#-------------------------------------------------------------------------