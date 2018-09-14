from new_big_square import *

def plot_big_square(squares, axarr, jj = 0, ii = 0, shift_x_between = 1, shift_y_between = 1):
	#axarr[ii, jj].plot(squares[:, 0], squares[:, 1])
	print('squares: ', squares)
	for i in range(squares.shape[0]):
		for j in range(squares.shape[1]):
			# plt.plot(plot_shape[:, 0], plot_shape[:, 1])
			if squares[i, j].all() != None:
				plot_shape = squares[i][j]
				#vertices[:, 0] += i * shift_x_between
				#print('one surface1: ', plot_shape)
				axarr[ii, jj].plot(plot_shape[:, 0] + i * shift_x_between, plot_shape[:, 1] + j * shift_y_between)
def new_plot(vertices, axarr, jj = 0, ii = 0):
	axarr[ii, jj].plot(vertices[:, 0], vertices[:, 1])


def get_squares_row(axarr, row_index, type = 'round', shift_x_between = 1, shift_y_between = 1, save_dir = ''):
	squares_list = []
	squares_vertices = []
	squares_uvs = []


# result = get_splited_squares(7, 7, type = 'round')
# del_upper_row(result)
# del_upper_row(result)
# print('result.shape: ', result.shape)
# print('after reshape: ', result.reshape(-1, 2).shape)
# create_round_squares_matrix_3d(result, save_name = 'merged_code.obj', shift_x_between = 1, shift_y_between = 1)

	squares = get_splited_squares(10, 10, type)	
	del_upper_row(squares)
	del_upper_row(squares)
	
	# squares_list.append(squares)
	create_round_squares_matrix_3d(squares, save_name = save_dir + 'row_' + str(row_index + 1) + 'colmn_' + str(1) + '.obj',
		shift_x_between = shift_x_between, shift_y_between = shift_y_between)
	plot_big_square(squares, axarr, 0, row_index, shift_x_between, shift_y_between)

	squares = get_splited_squares(10, 10, type)	
	del_upper_row(squares)
	del_upper_row(squares)
	plot_big_square(squares, axarr, 1, row_index, shift_x_between, shift_y_between)
	# squares_list.append(squares)
	create_round_squares_matrix_3d(squares, save_name = save_dir + 'row_' + str(row_index + 1) + 'colmn_' + str(2) + '.obj',
		shift_x_between = shift_x_between, shift_y_between = shift_y_between)
	
	
	
	squares = get_splited_squares(10, 10, type)	
	del_upper_row(squares)
	del_buttom_row(squares)
	plot_big_square(squares, axarr, 2, row_index, shift_x_between, shift_y_between)
	# squares_list.append(squares)
	create_round_squares_matrix_3d(squares, save_name = save_dir + 'row_' + str(row_index + 1) + 'colmn_' + str(3) + '.obj',
		shift_x_between = shift_x_between, shift_y_between = shift_y_between)


	squares = get_splited_squares(10, 10, type)	
	del_upper_row(squares)
	del_buttom_row(squares)
	del_buttom_row(squares)
	plot_big_square(squares, axarr, 3, row_index, shift_x_between, shift_y_between)
	# squares_list.append(squares)
	create_round_squares_matrix_3d(squares, save_name = save_dir + 'row_' + str(row_index + 1) + 'colmn_' + str(4) + '.obj',
		shift_x_between = shift_x_between, shift_y_between = shift_y_between)


	
	squares = get_splited_squares(10, 10, type)	
	del_upper_row(squares)
	del_upper_row(squares)
	del_buttom_row(squares)
	del_buttom_row(squares)
	plot_big_square(squares, axarr, 4, row_index, shift_x_between, shift_y_between)
	# squares_list.append(squares)
	create_round_squares_matrix_3d(squares, save_name = save_dir + 'row_' + str(row_index + 1) + 'colmn_' + str(5) + '.obj',
		shift_x_between = shift_x_between, shift_y_between = shift_y_between)


	return squares_list


def get_moreno_row(axarr, row_index, type = 'round', shift_x_between = 1, shift_y_between = 1, save_dir = ''):

	squares_list = []



	
	squares = get_splited_squares(13, 13, type)
	del_upper_row(squares)
	del_left_colmn(squares)
	del_buttom_row(squares)
	plot_big_square(squares, axarr, 0, row_index, shift_x_between, shift_y_between)
	# squares_list.append(squares)
	create_round_squares_matrix_3d(squares, save_name = save_dir + 'row_' + str(row_index + 1) + 'colmn_' + str(1) + '.obj',
		shift_x_between = shift_x_between, shift_y_between = shift_y_between)
	
	squares = get_splited_squares(13, 13, type)	
	del_upper_row(squares)
	del_left_colmn(squares)
	del_right_colmn(squares)
	del_buttom_row(squares)
	plot_big_square(squares, axarr, 1, row_index, shift_x_between, shift_y_between)
	# squares_list.append(squares)
	create_round_squares_matrix_3d(squares, save_name = save_dir + 'row_' + str(row_index + 1) + 'colmn_' + str(2) + '.obj',
		shift_x_between = shift_x_between, shift_y_between = shift_y_between)


	squares = get_splited_squares(13, 13, type)
	del_upper_row(squares)
	del_upper_row(squares)
	del_left_colmn(squares)
	del_left_colmn(squares)
	del_right_colmn(squares)
	del_buttom_row(squares)
	plot_big_square(squares, axarr, 2, row_index, shift_x_between, shift_y_between)
	# squares_list.append(squares)
	create_round_squares_matrix_3d(squares, save_name = save_dir + 'row_' + str(row_index + 1) + 'colmn_' + str(3) + '.obj',
		shift_x_between = shift_x_between, shift_y_between = shift_y_between)

	
	squares = get_splited_squares(13, 13, type)
	del_upper_row(squares)
	del_upper_row(squares)
	del_left_colmn(squares)
	del_left_colmn(squares)
	del_right_colmn(squares)
	del_right_colmn(squares)
	del_buttom_row(squares)
	plot_big_square(squares, axarr, 3, row_index, shift_x_between, shift_y_between)
	# squares_list.append(squares)
	create_round_squares_matrix_3d(squares, save_name = save_dir + 'row_' + str(row_index + 1) + 'colmn_' + str(4) + '.obj',
		shift_x_between = shift_x_between, shift_y_between = shift_y_between)

	squares = get_splited_squares(13, 13, type)
	del_upper_row(squares)
	del_upper_row(squares)
	del_left_colmn(squares)
	del_left_colmn(squares)
	del_right_colmn(squares)
	del_right_colmn(squares)
	del_buttom_row(squares)
	del_buttom_row(squares)
	plot_big_square(squares, axarr, 4, row_index, shift_x_between, shift_y_between)
	# squares_list.append(squares)
	create_round_squares_matrix_3d(squares, save_name = save_dir + 'row_' + str(row_index + 1) + 'colmn_' + str(5) + '.obj',
		shift_x_between = shift_x_between, shift_y_between = shift_y_between)


	return squares_list


def get_normal_squares_row(axarr):
	get_squares_row(axarr, row_index = 0, type = 'normal', shift_x_between = 1, shift_y_between = 1, save_dir = 'test_merged_code/')
	get_moreno_row(axarr, row_index = 1, type = 'normal', shift_x_between = 1, shift_y_between = 1, save_dir = 'test_merged_code/')

def get_round_squares_row(axarr):
	get_squares_row(axarr, row_index = 0, type = 'round', shift_x_between = 0.8, shift_y_between = 0.8, save_dir = 'test_merged_code/')
	get_moreno_row(axarr, row_index = 1, type = 'round', shift_x_between = 0.8, shift_y_between = 0.8, save_dir = 'test_merged_code/')

f, axarr = plt.subplots(2, 5, figsize=(20,2.4 * 2 ))
get_normal_squares_row(axarr)
plt.show()

# f, axarr = plt.subplots(2, 5, figsize=(20,2.4 * 2 ))
# get_round_squares_row(axarr)
# plt.show()


















