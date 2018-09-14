import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
from one_3d_func import *
from rotate import *


def curve_some_points(xy, step = 0.2, k = 1):
	x = xy[:,0]	
	y = xy[:,1]
	tck, u = interpolate.splprep([x, y], s=0, k = k)
	unew = np.arange(0, 1.01, step) # from 0 to 1.01 with step 0.01 [the number of points]
	out = interpolate.splev(unew, tck) # a circle of 101 points
	out = np.array(out).T
	return out	

def create_normal_square():
	xy = np.array([ [0, 0], [0, -1], [1, -1], [1, 0] ]).astype('float64')
	xy[:, 0] -= 0.5
	xy[:, 1] -= -0.5
	xy = np.append(xy, [xy[0]], axis = 0) # close the circle
	return xy

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

	# plt.plot(out[:, 0], out[:, 1])
	# plt.scatter(out[:, 0], out[:, 1], c = 'red')
	# plt.show()
	#create_single_3d(out, save_name = save_dir + 'row_' + str(5) + 'colmn_' + str(2) + '.obj')
	#create_single_3d(out, save_name = 'first_round_square.obj')
	return out

def get_splited_squares(nb_rows = 2, nb_colmns = 5, type = 'normal'): # later add type parameter: type = square, round_square, curve.....
	# one_shape = create_round_square()
	if type is 'normal':
		one_shape = create_normal_square()
	elif type is 'round':	
		one_shape = create_round_square()
	shape_list = [one_shape] * nb_colmns
	shape_list = np.array(shape_list)
	#print('new shape:', shape_list.shape)
	shape_list_matrix = nb_rows * [shape_list]
	shape_list_matrix = np.array(shape_list_matrix)
	#print('new shape matrix: ', shape_list_matrix.shape)
	return shape_list_matrix

def delete_squares(squares, start_x = 0, range_x = 2, start_y = 0, range_y = 2):
	for i in range(start_x, start_x + range_x):
		for j in range(start_y, start_y + range_y):
			squares[j][i] = None

def del_buttom_row(squares, start_x=0, range_x=0):
	rand_start_x = np.random.randint(0, squares.shape[0] - 1) # -1 we don't to start at the last element
	# print('rand_start_x: ', rand_start_x)
	if(2 < squares.shape[0] - rand_start_x - 2):
		rand_range_x = np.random.randint(2, squares.shape[0] - rand_start_x - 2)
	else:
		rand_range_x = 2
	# print('start: ', rand_start_x, ' _range: ', rand_range_x)
	rand_range_y = np.random.randint(1, 5)
	delete_squares(squares, start_x = rand_start_x, range_x = rand_range_x, range_y = rand_range_y)	

def del_upper_row(squares):
	rand_start_x = np.random.randint(0, squares.shape[0] - 1) # -1 we don't to start at the last element
	# print('rand_start_x: ', rand_start_x)
	if(2 < squares.shape[0] - rand_start_x - 2):
		rand_range_x = np.random.randint(2, squares.shape[0] - rand_start_x - 2)
	else:
		rand_range_x = 2
	# print('start: ', rand_start_x, ' _range: ', rand_range_x)
	rand_range_y = np.random.randint(1, 5)
	delete_squares(squares, start_y = squares.shape[0] - rand_range_y, start_x = rand_start_x, range_x = rand_range_x, range_y = rand_range_y)

def del_left_colmn(squares):
	rand_start_y = np.random.randint(0, squares.shape[0] - 1) # -1 we don't to start at the last element
	if(2 < squares.shape[0] - rand_start_y - 2):
		rand_range_y = np.random.randint(2, squares.shape[0] - rand_start_y - 2)
	else:
		rand_range_y = 2
	rand_range_x = np.random.randint(1, 5)
	delete_squares(squares, start_y = rand_start_y, range_y = rand_range_y, range_x = rand_range_x)
def del_right_colmn(squares):
	rand_start_y = np.random.randint(0, squares.shape[0] - 1) # -1 we don't to start at the last element
	if(2 < squares.shape[0] - rand_start_y - 2):
		rand_range_y = np.random.randint(2, squares.shape[0] - rand_start_y - 2)
	else:
		rand_range_y = 2
	rand_range_x = np.random.randint(1, 5)
	delete_squares(squares, start_x = squares.shape[0] - rand_range_x, start_y = rand_start_y, range_y = rand_range_y, range_x = rand_range_x)












