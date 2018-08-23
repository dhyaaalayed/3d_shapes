import numpy as np
import matplotlib.pyplot as plt
from one_3d_func import *

class Square:
	def __init__(self, up_left, up_right, down_left, down_right, max_val): # uv_up_left, uv_up_right, uv_down_left, uv_down_right):
		self.up_left = up_left
		self.up_right = up_right
		self.down_right = down_right
		self.down_left = down_left
		self.uv_up_left = up_left * 1/max_val
		self.uv_up_right = up_right * 1/max_val
		self.uv_down_right = down_right * 1/max_val
		self.uv_down_left = down_left * 1/max_val
		self.triangle1 = Triangle(self.up_left, self.up_right, self.down_right, self.uv_up_left, self.uv_up_right, self.uv_down_right)
		self.triangle2 = Triangle(self.down_right, self.down_left, self.up_left, self.uv_down_right, self.uv_down_left, self.uv_up_left)
		self.flipped_triangle_1 = Triangle(self.down_right, self.up_right, self.up_left, self.uv_down_right, self.uv_up_right, self.uv_up_left)
		self.flipped_triangle_2 = Triangle(self.up_left, self.down_left, self.down_right, self.uv_up_left, self.uv_down_left, self.uv_down_right)
	def __repr__(self):
		return 'up_left: ' + str(self.up_left) + ' _up_right: ' + str(self.up_right) + ' _down_left: ' + str(self.down_left) + ' _down_right: ' + str(self.down_right)
	def get_square_points(self):
		return np.array([self.up_left, self.up_right, self.down_left, self.down_right])
	def get_triangles_points(self):
		return np.concatenate([self.triangle1.get_triangle_points(), self.triangle2.get_triangle_points()], axis = 0)
	def get_3d_indices(self):
		return self.triangle1.get_3d_indices() + '\n' +  self.triangle2.get_3d_indices() + '\n' + self.flipped_triangle_1.get_3d_indices() + '\n' + self.flipped_triangle_2.get_3d_indices()
	# def get_3d_indices_with_uv(self):
	# 	return self.

def get_splited_squares(nb_rows = 2, nb_colmns = 5):
	x_splite = np.arange(0, nb_rows + 1, 1).astype(float)
	print('x_splite: ', x_splite)
	# y_splite = np.copy(x_splite)
	y_splite = np.arange(0, nb_colmns + 1, 1).astype(float)
	# delete randomly choosen sub array for randomness later!
	if nb_rows > nb_colmns:
		max_val = np.amax(x_splite)
	else:
		max_val = np.amax(y_splite)
	all_squares = []
	index_counter = 1
	for i in range(len(x_splite) - 1): # each col loop
		row_squares = []
		for j in range(len(y_splite) - 1): # each row loop
			row_squares.append(Square([x_splite[i], y_splite[j + 1], 0, j + 1 + 1 + len(y_splite) * i], # Add zero dimention and index
				[x_splite[i + 1], y_splite[j + 1], 0, j + 1 + 1 + len(y_splite) * (i + 1)],
				[x_splite[i], y_splite[j], 0, j + 1 + len(y_splite)*i], # i + 1 + len(y_splite)*j
				[x_splite[i + 1], y_splite[j], 0, j + 1 + len(y_splite) * (i + 1) ],
				max_val))


		all_squares.append(np.array(row_squares))
	print('all_squares length: ', len(all_squares))
	print('shape: ', np.array(all_squares).shape)
	return np.array(all_squares)

def delete_squares(squares, start_x = 0, range_x = 2, start_y = 0, range_y = 2):
	for i in range(start_x, start_x + range_x):
		for j in range(start_y, start_y + range_y):
			squares[j][i] = None

# [len][i] --> upper row
# [i][len] --> last column [right column]
# [i][0]   --> first column [left column]
# [0][i]   --> first row [bottom row]

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

def plot_big_square(squares, axarr, jj = 0, ii = 0):
	for i in range(squares.shape[0]):
		for j in range(squares.shape[1]):
			if(squares[i][j] is not None):
				points = squares[i][j].get_triangles_points()
				print('squares :', i, ',',j,  '___', squares[i][j].get_square_points())
				#plt.plot(points[:, 0], points[:, 1])
				axarr[ii, jj].plot(points[:, 0], points[:, 1])
def get_square_vertices(big_square):
	squares = big_square
	vertices = []
	uv_vertices = []
	for i in range(squares.shape[0]):
		for j in range(squares.shape[1]):
			left_point = squares[i][j].down_left
			vertices.append(left_point)
			print(left_point)
			if(j == squares.shape[1] - 1):
				vertices.append(squares[i][j].up_left)
				print(squares[i][j].up_left)
		if(i == squares.shape[1] - 1):
			for j in range(squares.shape[1]):
				vertices.append(squares[i][j].down_right)
				if(j == squares.shape[1] - 1):
					vertices.append(squares[i][j].up_right)
	return np.array(vertices)
		

# def get_triangle_mesh(big_square):
# 	triangle_list = []
# 	for i in range(len(big_square)):
# 		for j in range(len(big_square)):

def create_uvmap(vertices_3d):
	uv_vertices = np.copy(vertices_3d[:, [0, 1, 3]])
	uv_vertices = uv_vertices.astype(float)
	uv_vertices[:, :2] *= 1 / np.amax(uv_vertices[:, :2])
	print('uv_vertices: ', uv_vertices)
	return uv_vertices

def write_on_obj(vertices, uv_vertices ,big_square, save_name = 'first_square.obj'):
	vertices[:3] *= 1/30
	squares = big_square
	obj_format = 'o Mesh\n'
	for i in range(len(vertices)):
		obj_format += 'v ' + str(vertices[i][0]) + ' ' + str(vertices[i][1]) + ' ' + str(vertices[i][2]) + '\n'
	for i in range(len(uv_vertices)):
		obj_format += 'vt ' + str(uv_vertices[i][0]) + ' ' + str(uv_vertices[i][1]) + '\n'
	for i in range(squares.shape[0]):
		for j in range(squares.shape[1]):
			if(squares[i][j] is not None):
				obj_format += big_square[i][j].get_3d_indices() + '\n'
	file = open(save_name, 'w')
	file.write(obj_format)
	file.close()
save_dir = 'new_shapes/'
def get_squares_row(axarr, row_index):
	squares_list = []
	squares_vertices = []
	squares_uvs = []
	squares = get_splited_squares(7, 7)
	
	vertices = get_square_vertices(squares)
	del_upper_row(squares)
	
	del_upper_row(squares)
	plot_big_square(squares, axarr, 0, row_index)
	squares_list.append(squares)

	uv_vertices = create_uvmap(vertices)
	write_on_obj(vertices, uv_vertices, squares, save_dir + 'row_' + str(row_index + 1) + 'colmn_' + str(1) + '.obj')
	
	
	squares = get_splited_squares(10, 10)
	vertices = get_square_vertices(squares)
	del_upper_row(squares)
	del_upper_row(squares)
	plot_big_square(squares, axarr, 1, row_index)
	squares_list.append(squares)
	uv_vertices = create_uvmap(vertices)
	write_on_obj(vertices, uv_vertices, squares, save_dir + 'row_' + str(row_index + 1) + 'colmn_' + str(2) + '.obj')
	
	
	squares = get_splited_squares(10, 10)
	vertices = get_square_vertices(squares)
	del_upper_row(squares)
	del_buttom_row(squares)
	plot_big_square(squares, axarr, 2, row_index)
	squares_list.append(squares)
	uv_vertices = create_uvmap(vertices)
	write_on_obj(vertices, uv_vertices, squares, save_dir + 'row_' + str(row_index + 1) + 'colmn_' + str(3) + '.obj')


	squares = get_splited_squares(10, 10)
	vertices = get_square_vertices(squares)
	del_upper_row(squares)
	del_buttom_row(squares)
	del_buttom_row(squares)
	plot_big_square(squares, axarr, 3, row_index)
	squares_list.append(squares)
	uv_vertices = create_uvmap(vertices)
	write_on_obj(vertices, uv_vertices, squares, save_dir + 'row_' + str(row_index + 1) + 'colmn_' + str(4) + '.obj')

	
	squares = get_splited_squares(10, 10)
	vertices = get_square_vertices(squares)
	del_upper_row(squares)
	del_upper_row(squares)
	del_buttom_row(squares)
	del_buttom_row(squares)
	plot_big_square(squares, axarr, 4, row_index)
	squares_list.append(squares)
	uv_vertices = create_uvmap(vertices)
	write_on_obj(vertices, uv_vertices, squares, save_dir + 'row_' + str(row_index + 1) + 'colmn_' + str(5) + '.obj')


	return squares_list

def get_moreno_row(axarr, row_index):
	squares_list = []
	squares = get_splited_squares(13, 13)
	vertices = get_square_vertices(squares)
	del_upper_row(squares)
	del_left_colmn(squares)
	# del_buttom_row(squares)
	del_buttom_row(squares)
	plot_big_square(squares, axarr, 0, row_index)
	squares_list.append(squares)
	uv_vertices = create_uvmap(vertices)
	write_on_obj(vertices, uv_vertices, squares, save_dir + 'row_' + str(row_index + 1) + 'colmn_' + str(1) + '.obj')
	
	
	squares = get_splited_squares(13, 13)
	vertices = get_square_vertices(squares)
	del_upper_row(squares)
	del_left_colmn(squares)
	del_right_colmn(squares)
	del_buttom_row(squares)
	plot_big_square(squares, axarr, 1, row_index)
	squares_list.append(squares)
	uv_vertices = create_uvmap(vertices)
	write_on_obj(vertices, uv_vertices, squares, save_dir + 'row_' + str(row_index + 1) + 'colmn_' + str(2) + '.obj')


	squares = get_splited_squares(13, 13)
	vertices = get_square_vertices(squares)
	del_upper_row(squares)
	del_upper_row(squares)
	del_left_colmn(squares)
	del_left_colmn(squares)
	del_right_colmn(squares)
	del_buttom_row(squares)
	plot_big_square(squares, axarr, 2, row_index)
	squares_list.append(squares)
	uv_vertices = create_uvmap(vertices)
	write_on_obj(vertices, uv_vertices, squares, save_dir + 'row_' + str(row_index + 1) + 'colmn_' + str(3) + '.obj')

	
	squares = get_splited_squares(13, 13)
	vertices = get_square_vertices(squares)
	del_upper_row(squares)
	del_upper_row(squares)
	del_left_colmn(squares)
	del_left_colmn(squares)
	del_right_colmn(squares)
	del_right_colmn(squares)
	del_buttom_row(squares)
	plot_big_square(squares, axarr, 3, row_index)
	squares_list.append(squares)
	uv_vertices = create_uvmap(vertices)
	write_on_obj(vertices, uv_vertices, squares, save_dir + 'row_' + str(row_index + 1) + 'colmn_' + str(4) + '.obj')


	squares = get_splited_squares(13, 13)
	vertices = get_square_vertices(squares)
	del_upper_row(squares)
	del_upper_row(squares)
	del_left_colmn(squares)
	del_left_colmn(squares)
	del_right_colmn(squares)
	del_right_colmn(squares)
	del_buttom_row(squares)
	del_buttom_row(squares)
	plot_big_square(squares, axarr, 4, row_index)
	squares_list.append(squares)
	
	uv_vertices = create_uvmap(vertices)
	write_on_obj(vertices, uv_vertices, squares, save_dir + 'row_' + str(row_index + 1) + 'colmn_' + str(5) + '.obj')


	return squares_list

###### void main
main = False
if main == True:
	f, axarr = plt.subplots(2,5, figsize=(20,2.4 * 2))
	
	squares_list = []
	
	squares = get_splited_squares(7, 7)
	
	vertices = get_square_vertices(squares)
	del_upper_row(squares)
	
	del_upper_row(squares)
	plot_big_square(squares, axarr, 0)
	squares_list.append(squares)
	
	uv_vertices = create_uvmap(vertices)
	write_on_obj(vertices, uv_vertices, squares)
	
	
	squares = get_splited_squares(10, 10)
	del_upper_row(squares)
	del_upper_row(squares)
	plot_big_square(squares, axarr, 1)
	squares_list.append(squares)
	
	
	squares = get_splited_squares(10, 10)
	del_upper_row(squares)
	del_buttom_row(squares)
	plot_big_square(squares, axarr, 2)
	squares_list.append(squares)
	
	squares = get_splited_squares(10, 10)
	del_upper_row(squares)
	del_buttom_row(squares)
	del_buttom_row(squares)
	plot_big_square(squares, axarr, 3)
	squares_list.append(squares)
	
	squares = get_splited_squares(10, 10)
	del_upper_row(squares)
	del_upper_row(squares)
	del_buttom_row(squares)
	del_buttom_row(squares)
	plot_big_square(squares, axarr, 4)
	squares_list.append(squares)
	
	### second row:
	
	squares = get_splited_squares(13, 13)
	del_upper_row(squares)
	del_left_colmn(squares)
	# del_buttom_row(squares)
	del_buttom_row(squares)
	plot_big_square(squares, axarr, 0, 1)
	squares_list.append(squares)
	
	
	squares = get_splited_squares(13, 13)
	del_upper_row(squares)
	del_left_colmn(squares)
	del_right_colmn(squares)
	del_buttom_row(squares)
	plot_big_square(squares, axarr, 1, 1)
	squares_list.append(squares)
	
	squares = get_splited_squares(13, 13)
	del_upper_row(squares)
	del_upper_row(squares)
	del_left_colmn(squares)
	del_left_colmn(squares)
	del_right_colmn(squares)
	del_buttom_row(squares)
	plot_big_square(squares, axarr, 2, 1)
	squares_list.append(squares)
	
	
	squares = get_splited_squares(13, 13)
	del_upper_row(squares)
	del_upper_row(squares)
	del_left_colmn(squares)
	del_left_colmn(squares)
	del_right_colmn(squares)
	del_right_colmn(squares)
	del_buttom_row(squares)
	plot_big_square(squares, axarr, 3, 1)
	squares_list.append(squares)
	
	squares = get_splited_squares(13, 13)
	del_upper_row(squares)
	del_upper_row(squares)
	del_left_colmn(squares)
	del_left_colmn(squares)
	del_right_colmn(squares)
	del_right_colmn(squares)
	del_buttom_row(squares)
	del_buttom_row(squares)
	plot_big_square(squares, axarr, 4, 1)
	squares_list.append(squares)
	
	# squares_list = np.array(squares_list).reshape(2, 5)
	# for i in range(squares_list.shape[0]):
	# 	for j in range(squares_list.shape[1]):
	# 		### write on obj
	
	
	
	plt.show()


















