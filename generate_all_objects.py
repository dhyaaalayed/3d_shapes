import matplotlib.pyplot as plt
from math import pi, cos, sin
from random import random
import itertools
import numpy as np
import math
from random import randint
from scipy import interpolate
from one_3d_func import *
from big_square import *
from rotate import *

all_shapes_global = [] # list of all shapes

def get_points(h, k, r, nb_points): # h and k are the origin axis
	points = []
	# items = 4
	items = nb_points
	for i in range(items):
		points += [[h + cos((2 * pi * i / items)) * r, k + sin((2 * pi * i / items)) * r]]
	return points
def get_angle(index, nb_points):
	return (2 * pi * index / nb_points)

def get_one_point(index, nb_points, r, h, k):
	angle = get_angle(index, nb_points)
	return [h + cos(angle) * r, k + sin(angle) * r]

def get_angle_array(indeces, nb_points):
	return 2 * pi * indeces / nb_points


def get_shifted_points(indeces, nb_points, r, h, k):

	angels = get_angle_array(indeces, nb_points)
	v = np.cos(angels)
	X = np.array(h + np.cos(angels) * r).reshape(-1,1)

	Y = np.array(k + np.sin(angels) * r).reshape(-1,1)
	#return [h + cos(angels) * r , k + sin(angels) * r]
	return np.concatenate([X,Y], axis = 1)


def curve_lines_array(arr, nb_lines):
	half = len(arr) // 2
	if(nb_lines % 2 == 0):
		random_lines = np.arange(half-nb_lines // 2, half +nb_lines // 2, 1)
	else:
		random_lines = np.arange(half-nb_lines // 2, half +nb_lines // 2 + 1, 1)
	first_array = arr[:random_lines[0]]
	lines_array = arr[random_lines[0]:random_lines[-1]]
	second_array = arr[random_lines[-1]:]

	curves_array = np.concatenate((first_array, second_array), axis = 0)
	print('curves_array: ', curves_array.shape)
	tck, u = interpolate.splprep([curves_array[:, 0], curves_array[:, 1]], s=0)
	unew = np.arange(0, 1.01, 0.01)
	out = interpolate.splev(unew, tck)
	curves_array = np.array(out).T
	merged_arrays = curves_array
	#merged_arrays = np.concatenate((curves_array, lines_array), axis = 0)
	return merged_arrays

def new_add_random_lines(arr, nb_lines):
	half = len(arr) // 2
	if(nb_lines % 2 == 0):
		random_lines = np.arange(half-nb_lines // 2, half +nb_lines // 2, 1)
	else:
		random_lines = np.arange(half-nb_lines // 2, half +nb_lines // 2 + 1, 1)

	print('random lines: ', random_lines)
	merged_arrays = []
	if(len(random_lines) > 0):
		first_array = arr[:random_lines[0]]
		lines_array = arr[random_lines[0]:random_lines[-1]]
		second_array = arr[random_lines[-1]:]
		print('first array length: ', first_array.shape)
		print('second_array length: ', second_array.shape)
		print('lines_array length: ', lines_array.shape)

		# interploation for first array:
		k = 3
		if len(first_array) <= 3:
			k = len(first_array) - 1

		tck, u = interpolate.splprep([first_array[:, 0], first_array[:, 1]], s=0, k = k)
		unew = np.arange(0, 1.01, 0.01)
		out = interpolate.splev(unew, tck)
		first_array = np.array(out).T

		# interploation for second array:
		k = 3
		if len(second_array) <= 3:
			k = len(second_array) - 1
		tck, u = interpolate.splprep([second_array[:, 0], second_array[:, 1]], s=0, k = k)
		unew = np.arange(0, 1.01, 0.01)
		out = interpolate.splev(unew, tck)
		second_array = np.array(out).T


		merged_arrays = np.concatenate((first_array, lines_array), axis = 0)
		merged_arrays = np.concatenate((merged_arrays, second_array), axis = 0)
	return merged_arrays

def add_random_lines(arr, nb_lines): # splite and combine


	#random_lines = np.random.randint(len(arr) // 2 - nb_lines, len(arr) // 2 + nb_lines, nb_lines) # this is good just for one random line!
	random_lines = [4]
	## getting the middle points of the array:
	half = len(arr) // 2
	if(nb_lines % 2 == 0):
		random_lines = np.arange(half-nb_lines // 2, half +nb_lines // 2, 1)
	else:
		random_lines = np.arange(half-nb_lines // 2, half +nb_lines // 2 + 1, 1)
	random_lines = random_lines
	print('random_lines: ', random_lines)
	splitet_arrays = np.split(arr, random_lines)
	plt.scatter(arr[random_lines, 0], arr[random_lines, 1])
	# merged_arrays = np.empty([len(splitet_arrays), 2])
	print('length of all: ', len(splitet_arrays))

	merged_arrays = []

	for i in range(len(splitet_arrays)):		
		print('plotting splitted array: ', i)
		tmp_plot = np.array(splitet_arrays[i])
		# if(i > 0):
		# 	tmp_plot = tmp_plot[:-1]
		#plt.plot(tmp_plot[:, 0], tmp_plot[:, 1])
		# plt.show()
		tck, u = interpolate.splprep([tmp_plot[:, 0], tmp_plot[:, 1]], s=0)
		unew = np.arange(0, 1.01, 0.01)
		out = interpolate.splev(unew, tck)
		
		out = np.array(out).T
		if(i == 0):
			merged_arrays = out
		else:
			merged_arrays = np.concatenate((merged_arrays, out), axis = 0)
		
	# plt.plot(merged_arrays[:, 0], merged_arrays[:, 1])
	# plt.show()
	return merged_arrays

def create_stars():
	nb_points = 6
	nb_shifts = 3
	shift_parameter = 3
	shift_value = 3
	r = 1
	for j in range(nb_colmns):
		xy = get_points(0, 0, r, nb_points)
		xy = np.array(xy)
		# shift even points for starts
		shifts_indices = np.arange(0, nb_points - 1, 2) # np.array([0, 2, 4]) 
		print('shifts_indices: ', shifts_indices)
		if(nb_shifts > 0):
			xy[shifts_indices] = get_shifted_points(shifts_indices, nb_points, r + shift_parameter, 0, 0) + np.random.uniform(low=-1.0, high=+1.0, size=(len(shifts_indices),)).reshape(-1, 1)
		xy = np.append(xy, [xy[0]], axis = 0) # close the circle


		x = xy[:,0]
		y = xy[:,1]
		if i == nb_rows - 1: # just lines
			# shift_value = 0.2
			out = xy
		axarr[i + 1,j].plot(out[:, 0], out[:, 1])
		#axarr[i + 1,j].scatter(out[:, 0], out[:, 1], c = 'green')
		axarr[i + 1,j].scatter(xy[shifts_indices, 0], xy[shifts_indices, 1], c = 'red')


		out *= 1/5 # to scall it like  others
		out *= 2 # for the merged object
		#create_3d(out, save_dir + 'row_' + str(i + 2) + 'colmn_' + str(j + 1) + '.obj')
		all_shapes_global.append(out)
		create_single_3d(out, save_name = save_dir + 'row_' + str(i + 2) + 'colmn_' + str(j + 1) + '.obj')
		#print('out: ', out)
		#axarr[i,j].scatter(out[0], out[1])
		

		nb_points += 2
		nb_shifts += 1 # this should has a random range
		# if(np.random.randint(0, 1 ,1) == 0):
		# 	signal = -1
		# 	shift_parameter -= signal * shift_value # this should be smaller than rs
		# elif(np.absolute(shift_parameter) < r):
		# 	#signal = 1
		# 	if(np.random.randint(0, 1 ,1) == 0):
		# 		signal = -1
		# 	shift_parameter -= signal * shift_value # this should be smaller than rs

def create_small_stars():
	nb_points = 4
	nb_shifts = 1
	shift_parameter = 1
	shift_value = 3
	r = 1
	for j in range(nb_colmns):
		if j == 1:
			continue
		xy = get_points(0, 0, r, nb_points)
		xy = np.array(xy)
		shifts_indices = np.array([3])
		print('shifts_indices: ', shifts_indices)
		if(j == 0):
			xy[shifts_indices, 1] += shift_parameter
			xy[shifts_indices, 0] += np.random.uniform(low= - 0.2, high=+0.2, size=(1,))
		elif j == 1:
			shift_parameter += np.random.uniform(low=0.2, high=+0.3, size=(1,))
			xy[shifts_indices, 1] += shift_parameter
			xy[shifts_indices, 0] += np.random.uniform(low= - 0.2, high=+0.2, size=(1,))
		elif j == 2:
			shift_parameter = 1
			shift_parameter += np.random.uniform(low=0.2, high=+0.8, size=(1,))
			xy[shifts_indices, 0] += np.random.uniform(low= - 0.4, high=+0.4, size=(1,))
			xy[shifts_indices, 1] -= shift_parameter
		else:
			shift_parameter += np.random.uniform(low=0.2, high=+0.8, size=(1,))
			xy[shifts_indices, 0] += np.random.uniform(low= - 0.4, high=+0.4, size=(1,))
			xy[shifts_indices, 1] -= shift_parameter

		xy = np.append(xy, [xy[0]], axis = 0) # close the circle
		out = xy

		x = xy[:,0]
		y = xy[:,1]
		axarr[i + 2,j].plot(xy[:, 0], xy[:, 1], c = 'black')
		axarr[i + 2,j].scatter(xy[:, 0], xy[:, 1], c = 'green')
		axarr[i + 2,j].scatter(xy[shifts_indices, 0], xy[shifts_indices, 1], c = 'red')
		#out *= 1/5 # to scall it like  others
		create_single_3d(out, save_name = save_dir + 'row_' + str(5) + 'colmn_' + str(j + 1) + '.obj')

		#nb_points += 2
		#nb_shifts += 1 # this should has a random range
def create_one_small_star():
	nb_points = 3
	nb_shifts = 0
	shift_parameter = 3
	shift_value = 3
	r = 1
	for j in range(1):
		xy = get_points(0, 0, r, nb_points)
		xy = np.array(xy)
		# shift even points for starts
		shifts_indices = np.arange(0, nb_points - 1, 2) # np.array([0, 2, 4]) 
		print('shifts_indices: ', shifts_indices)
		if(nb_shifts > 0):
			xy[shifts_indices] = get_shifted_points(shifts_indices, nb_points, r + shift_parameter, 0, 0) + np.random.uniform(low=-1.0, high=+1.0, size=(len(shifts_indices),)).reshape(-1, 1)
		xy = np.append(xy, [xy[0]], axis = 0) # close the circle
		average_point = (xy[2] + xy[3]) / 2
		average_point[1] += 0.3
		average_point[0] -= 0.15
		xy = np.array([xy[0], xy[1] , xy[2], average_point ,xy[3]])
		x = xy[:,0]	
		y = xy[:,1]		
		out = xy
		axarr[4, 1].plot(out[:, 0], out[:, 1])
		axarr[4, 1].scatter(average_point[0], average_point[1], c = 'red')
	create_single_3d(out, save_name = save_dir + 'row_' + str(5) + 'colmn_' + str(2) + '.obj')
	return out

def create_one_complex_object(all_shapes, number_of_objects = 0):
	# convert all_shapes to numpy:
	print('before conversion: ', len(all_shapes))
	all_shapes = np.array(all_shapes) # maybe it needs to be reshaped (-1, +1)
	print('after conversion: ', all_shapes.shape)
	print('one shape: ', all_shapes[0])
	create_3d_for_list(all_shapes[14:19], save_name = 'complex_daniel.obj', shift_x_between = 1.9)

def curve_some_points(xy, step = 0.2, k = 1):
	x = xy[:,0]	
	y = xy[:,1]
	tck, u = interpolate.splprep([x, y], s=0, k = k)
	unew = np.arange(0, 1.01, step) # from 0 to 1.01 with step 0.01 [the number of points]
	out = interpolate.splev(unew, tck) # a circle of 101 points
	out = np.array(out).T
	return out	

def create_round_square():
	upper_left_round = np.array([[0.4, 0], [0, 0], [0, -0.4]])
	upper_left_round = curve_some_points(upper_left_round)
	upper_left_round = curve_some_points(upper_left_round, step = 0.04, k = 1)
	# shifting the shape origin to the (0, 0)
	upper_left_round[:, 0] -= 0.5 
	upper_left_round[:, 1] -= -0.5
	# creating other corners
	upper_right_round = rotate_polygon(upper_left_round, -90)
	buttom_left_round = rotate_polygon(upper_left_round, +90)
	buttom_right_round = rotate_polygon(upper_left_round, +180)
	xy = np.concatenate([upper_left_round, buttom_left_round,
		buttom_right_round, upper_right_round], axis = 0)
	xy = np.append(xy, [xy[0]], axis = 0) # close the circle
	out = xy
	print('out.shape: ', out.shape)
	# plt.plot(out[:, 0], out[:, 1])
	# plt.scatter(out[:, 0], out[:, 1], c = 'red')
	# plt.show()
	#create_single_3d(out, save_name = save_dir + 'row_' + str(5) + 'colmn_' + str(2) + '.obj')
	#create_single_3d(out, save_name = 'first_round_square.obj')
	return out


one_shape = create_round_square()
create_round_matrix(one_shape)
main = False
if main == True:
	nb_colmns = 5
	nb_rows = 3
	nb_lines = 0
	f, axarr = plt.subplots(nb_rows + 4,nb_colmns, figsize=(20,2.4 * (nb_rows + 4)    ))
	shift_value = 0.1
	save_dir = 'new_shapes/'
	
	for i in range(nb_rows):
		
		nb_points = 6
		nb_shifts = 1
		shift_parameter = 0.2
		r = 1
		for j in range(nb_colmns):
			xy = get_points(0, 0, r, nb_points)
			xy = np.array(xy)
			# choose random of shifts satrting with 0
			shifts_indices = np.random.randint(0, nb_points ,nb_shifts) # choose random points
			if(nb_shifts > 0):
				xy[shifts_indices] = get_shifted_points(shifts_indices, nb_points, r + shift_parameter, 0, 0)
			xy = np.append(xy, [xy[0]], axis = 0) # close the circle
	
	
			x = xy[:,0]
			y = xy[:,1]
			if i == nb_rows - 1: # just lines
				# shift_value = 0.2
				out = xy
			else:
				if(nb_lines < 1): # normal circles
					tck, u = interpolate.splprep([x, y], s=0)
					unew = np.arange(0, 1.01, 0.01) # from 0 to 1.01 with step 0.01 [the number of points]
					out = interpolate.splev(unew, tck) # a circle of 101 points
					out = np.array(out).T
					# print('last out: ', out)
				else: # lines and curves
					#out = add_random_lines(xy, nb_lines)
					#out = curve_lines_array(xy, nb_lines)
					out = new_add_random_lines(xy, nb_lines)
					# out_np = np.array(out[0]).T # transpose
					# for k in range(1, len(out)):
					# 	out_np = np.concatenate((out_np, np.array(out[k]).T), axis = 0)
					# out = out_np
			#axarr[i,j].plot(x, y, 'x', out[:, 0], out[:, 1])
			axarr[i,j].plot(out[:, 0], out[:, 1])
			axarr[i,j].scatter(xy[shifts_indices, 0], xy[shifts_indices, 1], c = 'red')
			
			all_shapes_global.append(out)
			create_single_3d(out, save_name = save_dir + 'row_' + str(i + 1) + 'colmn_' + str(j + 1) + '.obj')
			#print('out: ', out)
			#axarr[i,j].scatter(out[0], out[1])
			
	
			nb_points += 1
			if j < 3:
				nb_shifts += 1
			if i == nb_rows - 1:
				nb_shifts += 1
				signal = 1
				if(np.random.randint(0, 1 ,1) == 0):
					signal = -1
				shift_parameter -= signal * shift_value # this should be smaller than rs
			elif(np.absolute(shift_parameter) < r):
				signal = 1
				if(np.random.randint(0, 1 ,1) == 0):
					signal = -1
				shift_parameter -= signal * shift_value # this should be smaller than rs
		nb_lines += 1
	## stars code:

	create_stars()
	create_small_stars()
	# get_squares_row(axarr, 5)
	# get_moreno_row(axarr, 6)
	create_one_small_star()
	# create_one_complex_object(all_shapes)
	create_objects_matrix(all_shapes_global, shift_x_between = 2, shift_y_between = 2)
	plt.savefig('shapes.jpg')
	plt.show()










