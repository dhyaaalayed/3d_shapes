import matplotlib.pyplot as plt
from math import pi, cos, sin
from random import random
import itertools
import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D
from cycler import cycler

def get_angle_array(indeces, nb_points):
	return 2 * pi * indeces / nb_points

def get_shifted_points(indeces, nb_points, r, h, k):

	angels = get_angle_array(indeces, nb_points)
	v = np.cos(angels)
	X = np.array(h + np.cos(angels) * r).reshape(-1,1)

	Y = np.array(k + np.sin(angels) * r).reshape(-1,1)
	#return [h + cos(angels) * r , k + sin(angels) * r]
	return np.concatenate([X,Y], axis = 1)


def plot_points(xy):
	# plt.scatter(*zip( itertools.repeat(*xy) ))
	#plt.scatter(*zip( *xy ))
	#fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	ax.plot(xy[:,0], xy[:,1], 0, c = 'red')

def plot_sub_points(xy, fig, ax):
	#print('Triangle: ', xy)
	ax.plot(xy[:,0], xy[:,1], xy[:,2])
	# ax.plot(xy[:,0], xy[:,1], xy[:,2], c = 'red')

class Triangle:
	def __init__(self, point1, point2, point3, uv_point1 = 0, uv_point2 = 0, uv_point3 = 0):
		self.point1 = point1
		self.point2 = point2
		#self.point3 = np.array([0, 0, 1]) # the one is the index of the origin!!!!!
		self.point3 = point3
		self.uv_point1 = uv_point1
		self.uv_point2 = uv_point2
		self.uv_point3 = uv_point3
	def __repr__(self):
		uv_points = ' ___ uv_p1: ' + str(self.uv_point1) + ' ___ uv_p2: ' + str(self.uv_point2) + ' ___ uv_p3: ' + str(self.uv_point3)
		return 'point1: ' + str(self.point1) + '___ point2: ' + str(self.point2) + '___ point3: '+ str(self.point3) + uv_points
	def get_triangle_points(self):
		return np.array([self.point1, self.point2, self.point3])
	def get_3d_indices(self): # here should I add / then UV_MAP indices
		return 'f ' + str(self.point1[3]) + ' ' + str(self.point2[3]) + ' ' + str(self.point3[3])
	def get_3d_indices_with_uv(self): # here should I add / then UV_MAP indices
		return 'f ' + str(self.point1[3]) + '/' + str(self.uv_point1[2]) + ' ' + str(self.point2[3]) + '/' + str(self.uv_point2[2]) + ' ' + str(self.point3[3]) + '/' + str(self.uv_point3[2])
def get_points(h, k, r, points_number): # h and k are the origin axis
	points = []
	# items = 4
	items = points_number
	for i in range(items):
		points += [[h + cos((2 * pi * i / items)) * r, k + sin((2 * pi * i / items)) * r]]
	return np.array(points)

def plot_triangles(Triangles, fig, ax):
	# fig = plt.figure()
	# ax = fig.add_subplot(111, projection='3d')
	for i in range(len(Triangles)):
		points = Triangles[i].get_triangle_points()
		plot_sub_points(points, fig, ax)
def get_circle_Triangles(points, origin, uv_points, uv_origin):
	Triangles = []
	for i in range(1, len(points) - 1):
		Triangles.append(Triangle(points[i], points[i+1], origin, uv_points[i], uv_points[i+1], uv_origin))
	return np.array(Triangles)

def get_circle2_Triangles(points, origin, uv_points, uv_origin):
	Triangles = []
	print('points: ', points.shape)
	print('uv_points: ', uv_points.shape)
	print('points: ', points)
	print('uv_points: ', uv_points)

	for i in range(1, len(points) - 1):
		Triangles.append(Triangle(points[i], origin, points[i+1], uv_points[i], uv_origin, uv_points[i+1]))
	return np.array(Triangles)


def get_side_surface_triangles(s1, s2, side_upper_points, side_lower_points):
	Triangles = []
	for i in range(1, len(s1) - 1):
		j = i-1
		t1 = Triangle(s1[i], s1[i+1], s2[i+1]
			, side_upper_points[j], side_upper_points[j+1], side_lower_points[j+1])
		# t2 = Triangle(s2[i], s2[i+1], s1[i])
		t2 = Triangle(s2[i], s1[i], s2[i+1]
			, side_lower_points[j], side_upper_points[j], side_lower_points[j+1])
		t3 = Triangle(s2[i], s2[i+1], s1[i]
			, side_lower_points[j], side_lower_points[j+1], side_upper_points[j])
		t4 = Triangle(s1[i], s2[i+1], s1[i+1]
			, side_upper_points[j], side_lower_points[j+1], side_upper_points[j+1])
		Triangles.append(t1)
		Triangles.append(t2)
		Triangles.append(t3)
		Triangles.append(t4)

	return np.array(Triangles)

def write_on_obj(vertices, triangles_mesh, uv_vertices, save_name = 'first_3d.obj'): #, uv_vertices # no need, because they are already exist with each triangle
	obj_format = 'o Mesh\n'
	for i in range(len(vertices)):
		obj_format += 'v ' + str(vertices[i][0]) + ' ' + str(vertices[i][1]) + ' ' + str(vertices[i][2]) + '\n'
	for i in range(len(uv_vertices)):
		obj_format += 'vt ' + str(uv_vertices[i][0]) + ' ' + str(uv_vertices[i][1]) + '\n'
	for i in range(len(triangles_mesh)):
		obj_format += triangles_mesh[i].get_3d_indices_with_uv() + '\n'
	file = open(save_name, 'w')
	file.write(obj_format)
	file.close()
def create_uvmap(surface): # make this one for the whole side surface!
	# 1- plot the side surfac
	start_upper_point = [0, 0.5] # change just the x-axis later!
	# for each tow points in the first surface
	upper_points = np.array([start_upper_point])
	for i in range(1, len(surface) - 1):
		# 1- calculate the distance
		distance = surface[i] - surface[i + 1]
		distance = np.linalg.norm(distance)
		# print('distance: ', distance)
		next_upper_point = np.copy(upper_points[-1])
		next_upper_point[0] += distance
		upper_points = np.append(upper_points, [next_upper_point], axis = 0)
	lower_points = np.copy(upper_points)
	lower_points[:,1] += 0.2 # here to reduce the height of the side surface
	normal_surface1 = np.copy(surface[:, :2])
	normal_surface1[:,1] -= 0.7
	normal_surface1[:,0] += 1
	normal_surface2 = np.copy(normal_surface1)
	normal_surface1 *= 0.85 # make the upper surface smaller than the buttom one
	normal_surface2[:,0] += 2.2
	side_surface = np.concatenate((upper_points, lower_points), axis = 0)
	# plt.scatter(points[:, 0], points[:, 1])
	# scaling between 0 and 1
	side_surface *= 0.15
	normal_surface1 *= 0.15
	normal_surface2 *= 0.15 ### here to make it bigger maybe
	# shift between 0 and 1
	side_surface[:, 1] += 0.35
	normal_surface1[:, 1] += 0.35
	normal_surface2[:, 1] += 0.35
	#### to try
	side_surface[:, 0] *= 0.7
	#### end to try
	return side_surface, normal_surface1, normal_surface2 # delete the closing circle point

def create_3d_for_list(surface1_list, save_name = 'first_complex.obj'):
	# get all vertices, uv_map vertices and all triangles, then concatenate them together
	surface1 = surface1_list[0]
	surfaces_vertices, surfaces_all_triangles, surfaces_uv_vertices = create_single_3d(surface1)
	last_vertices_index = len(surfaces_vertices) # not sure for +1 or +2 or +0...
	last_uv_index = len(surfaces_uv_vertices)
	# print('first object vertices: ', surfaces_vertices)
	print('uv vertices of object: 0 :', surfaces_uv_vertices)
	for i in range(1, len(surface1_list)):
		print('I am in the loop')
		surface1 = surface1_list[i]
		print('last_vertices_index: ', last_vertices_index)
		# vertices, all_triangles, uv_vertices = create_single_3d(surface1, origin = np.array([[i*0.5, 0]]), start_index = last_vertices_index, start_uv_index = last_uv_index)
		vertices, all_triangles, uv_vertices = create_single_3d(surface1, origin = np.array([[i*0.5, 0]]), start_index = last_vertices_index, start_uv_index = last_uv_index)
		print('uv vertices of object: ',i ,':', uv_vertices)
		surfaces_vertices = np.concatenate([surfaces_vertices, vertices], axis = 0)
		surfaces_all_triangles = np.concatenate([surfaces_all_triangles, all_triangles], axis = 0)
		surfaces_uv_vertices = np.concatenate([surfaces_uv_vertices, uv_vertices], axis = 0)
		last_vertices_index += len(vertices)
		last_uv_index += len(uv_vertices)
	write_on_obj(surfaces_vertices, surfaces_all_triangles, surfaces_uv_vertices, save_name)
	plt.figure()
	plt.scatter(surfaces_uv_vertices[:, 0], surfaces_uv_vertices[:, 1])
	plt.show()

def create_3d(surface1, save_name = 'first_3d.obj'): # this function should return only what we need for creating 3d
	third_dimension_bias = 0.9 # must stay less than 1
	surface2 = np.copy(surface1)
	surface1 *= 0.85
	# print(surface1) # for uvmap later
	# plt.plot(surface1[:, 0], surface1[:, 1])
	surface1 = np.append(surface1, [surface1[0]], axis = 0) # to close the circle: still important for the last triangle!
	surface1 = np.append(np.array([[0, 0]]), surface1, axis = 0) # add the origin as the first vertex
	surface1_for_uvmap = np.copy(surface1)
	
	## UV_MAP Call
	#

	# fig = plt.figure()
	uv_side_surface, uv_surface1, uv_surface2 = create_uvmap(surface1_for_uvmap)
	# plt.scatter(uv_side_surface[:, 0], uv_side_surface[:, 1])
	# plt.scatter(uv_surface1[:, 0], uv_surface1[:, 1])
	# print('before uv_surface1: ', uv_surface1)
	# plt.scatter(uv_surface2[:, 0], uv_surface2[:, 1])
	split_side_index = len(uv_side_surface) // 2
	uv_upper_side_points = np.copy(uv_side_surface[:split_side_index])
	uv_lower_side_points = np.copy(uv_side_surface[split_side_index:])
	
	#
	## End UV_MAP Call
	
	### Some UV_MAP code will be added in parallel with the 3d code
	#uv_surface1 = np.append(np.array([[-1, -1]]), uv_surface1, axis = 0) # add -1 instead of the origin
	# add the z (third) dimension
	surface1 = np.append(surface1, np.ones((len(surface1), 1)) - third_dimension_bias, axis = 1) # adding the third dimension
	indices = np.arange(1, len(surface1) + 1).reshape(-1, +1)
	surface1 = np.append(surface1, indices, axis = 1) # add the indices
	surface1[len(surface1) - 1][3] = 2 # Set the same index for the repeated vertex; the repeated vertex is the closing circle point
	# uv_map
	uv_map_indices = np.arange(1, len(uv_surface1) + 1).reshape(-1, +1)
	uv_surface1 = np.append(uv_surface1, uv_map_indices, axis = 1)
	uv_surface1[-1][2] = 2 # the repeated vertex in the uv map
	# end uv_map
	# print('uv_surface1: ', uv_surface1)
	surface1_triangles = get_circle_Triangles(surface1, surface1[0], uv_surface1, uv_surface1[0])
	
	# plot_triangles(surface1_triangles, fig, ax)
	
	#
	# End Creating The First Surface
	
	# Creating The Second Surface
	#
		## 2d Phase
	# surface2 = get_points(0, 0, 1, surface_points)
	
	# surface2 = np.append(surface2, [surface2[0]], axis = 0)
	print('___surface2: ', surface2)
	surface2 = np.append(np.array([[0, 0]]), surface2, axis = 0)
		## End 2d Phase
	surface2 = np.append(surface2, -np.ones((len(surface2), 1)) + third_dimension_bias, axis = 1)
	first_index = surface1[-2][3] + 1 # start counting from the last index of the first surface
	print('first_index of the surface2 [the buttom surface]: ', first_index)
	indices = np.arange(first_index, first_index + len(surface2)).reshape(-1, +1)
	surface2 = np.append(surface2, indices, axis = 1) # add the indices
	surface2[len(surface2) - 1][3] = first_index + 1 # the repeated vertex
	# print('surface2 after all: ', surface2 )
	
	# uv_map
	#
	uv_map_indices = np.copy(indices) # this indices should be done as the indices of the first surface
	uv_surface2 = np.append(uv_surface2, uv_map_indices, axis = 1)
	uv_surface2[-1][2] = first_index + 1
	# print('uv_surface2: ', uv_surface2)
	#
	# end uv_map
	
	surface2_triangles = get_circle2_Triangles(surface2, surface2[0], uv_surface2, uv_surface2[0])
	# plot_triangles(Triangles, fig, ax)
	
	
	# indices = np.arange(surface1[-1][4], len(xy) + 1).reshape(-1, +1)
	#
	# End Creating The Second Surface
	
	# Adding The Side Surface
	#
		## uv_map: indexing the upper side points
	# first_index = uv_map_indices[-1] + 1
	first_index = uv_map_indices[-1]
	uv_map_indices = np.arange(first_index, first_index + len(uv_upper_side_points)).reshape(-1, +1)
	uv_upper_side_points = np.append(uv_upper_side_points, uv_map_indices, axis = 1)
		## uv_map: end indexing the upper side points
	
		## uv_map: indexing the lower side points
	first_index = uv_map_indices[-1] + 1
	uv_map_indices = np.arange(first_index, first_index + len(uv_lower_side_points)).reshape(-1, +1)
	uv_lower_side_points = np.append(uv_lower_side_points, uv_map_indices, axis = 1)
		## uv_map: end indexing the lower side points
	#print('uv upper: ', uv_upper_side_points, 'uv lower: ', uv_lower_side_points)
	side_surface_triangles = get_side_surface_triangles(surface1, surface2, 
		uv_upper_side_points, uv_lower_side_points)
	# plot_triangles(side_surface_triangles, fig, ax)
	#
	# End Adding The Side Surface
	
	## Vertex list
	#
	Vertices = np.concatenate([surface1[:-1], surface2[:-1]], axis = 0) # plot all the vertices
	all_triangles = np.concatenate([surface1_triangles, surface2_triangles, side_surface_triangles],
		axis = 0)
	# print('uv_surface1: ',uv_surface1, 'uv_surface2: ', uv_surface2, 'uv_upper_side_points: ', uv_upper_side_points, 'uv_lower_side_points: ', uv_lower_side_points)
	#uv_vertices = np.concatenate([uv_surface1[:-1], uv_surface2[:-1], uv_upper_side_points, uv_lower_side_points], axis = 0)
	uv_vertices = np.concatenate([uv_surface1[:-1], uv_surface2[:-1], uv_upper_side_points, uv_lower_side_points], axis = 0)
	# plot_triangles(all_triangles, fig, ax)
	write_on_obj(Vertices, all_triangles, uv_vertices, save_name)


def create_single_3d(surface1, origin = np.array([[0, 0]]), start_index = 0, start_uv_index = 0): # this function should return only what we need for creating 3d
	third_dimension_bias = 0.9 # must stay less than 1
	print('first state of surface1: ', surface1)
	surface2 = np.copy(surface1)
	surface1 *= 0.85
	# surface1 = np.append(surface1, [surface1[0]], axis = 0) # to close the circle: still important for the last triangle!
	print('shape surface1 after: ', surface1.shape)
	surface1 = np.append(origin, surface1, axis = 0) # add the origin as the first vertex
	surface1_for_uvmap = np.copy(surface1)
	print('surface1_for_uvmap: ', surface1_for_uvmap)
	
	## UV_MAP Call
	#
	uv_side_surface, uv_surface1, uv_surface2 = create_uvmap(surface1_for_uvmap)
	split_side_index = len(uv_side_surface) // 2
	uv_upper_side_points = np.copy(uv_side_surface[:split_side_index])
	uv_lower_side_points = np.copy(uv_side_surface[split_side_index:])
	#
	## End UV_MAP Call
	
	surface1 = np.append(surface1, np.ones((len(surface1), 1)) - third_dimension_bias, axis = 1) # adding the third dimension
	indices = np.arange(1, len(surface1) + 1).reshape(-1, +1)
	surface1 = np.append(surface1, indices, axis = 1) # add the indices
	surface1[len(surface1) - 1][3] = 2 # Set the same index for the repeated vertex; the repeated vertex is the closing circle point
	surface1[:, 3] += start_index
	# uv_map
	uv_map_indices = np.arange(1, len(uv_surface1) + 1).reshape(-1, +1)
	uv_surface1 = np.append(uv_surface1, uv_map_indices, axis = 1)
	uv_surface1[-1][2] = 2 # the repeated vertex in the uv map
	uv_surface1[:, 2] += start_uv_index
	# end uv_map
	surface1_triangles = get_circle_Triangles(surface1, surface1[0], uv_surface1, uv_surface1[0])	
	#
	# End Creating The First Surface
	
	# Creating The Second Surface
	#
		## 2d Phase
	# surface2 = get_points(0, 0, 1, surface_points)
	# surface2 = np.append(surface2, [surface2[0]], axis = 0)
	surface2 = np.append(origin, surface2, axis = 0)
		## End 2d Phase
	surface2 = np.append(surface2, -np.ones((len(surface2), 1)) + third_dimension_bias, axis = 1)
	first_index = surface1[-2][3] + 1 # start counting from the last index of the first surface
	indices = np.arange(first_index, first_index + len(surface2)).reshape(-1, +1)
	surface2 = np.append(surface2, indices, axis = 1) # add the indices
	surface2[len(surface2) - 1][3] = first_index + 1 # the repeated vertex
	#surface2[:, 3] += start_index
	
	# uv_map
	#
	first_uv_index = uv_surface1[-2][2] + 1 # the last uv_vertex index 29.08.2018
	print('first_uv_index: ', first_uv_index)
	uv_map_indices = np.arange(first_uv_index, first_uv_index + len(uv_surface2)).reshape(-1, +1)
	print('uv indeices for surface2: ', uv_map_indices.shape)
	print('uv_surface2: ', uv_surface2.shape)
	uv_surface2 = np.append(uv_surface2, uv_map_indices, axis = 1)
	uv_surface2[-1][2] = first_index + 1
	#
	# end uv_map
	
	surface2_triangles = get_circle2_Triangles(surface2, surface2[0], uv_surface2, uv_surface2[0])	
	#
	# End Creating The Second Surface
	
	# Adding The Side Surface
	#
	## uv_map: indexing the upper side points
	first_index = uv_map_indices[-1]
	uv_map_indices = np.arange(first_index, first_index + len(uv_upper_side_points)).reshape(-1, +1)
	uv_upper_side_points = np.append(uv_upper_side_points, uv_map_indices, axis = 1)
		## uv_map: end indexing the upper side points
	
		## uv_map: indexing the lower side points
	first_index = uv_map_indices[-1] + 1
	uv_map_indices = np.arange(first_index, first_index + len(uv_lower_side_points)).reshape(-1, +1)
	uv_lower_side_points = np.append(uv_lower_side_points, uv_map_indices, axis = 1)
		## uv_map: end indexing the lower side points
	side_surface_triangles = get_side_surface_triangles(surface1, surface2, 
		uv_upper_side_points, uv_lower_side_points)
	#
	# End Adding The Side Surface
	
	## Vertex list
	#
	Vertices = np.concatenate([surface1[:-1], surface2[:-1]], axis = 0) # plot all the vertices
	all_triangles = np.concatenate([surface1_triangles, surface2_triangles, side_surface_triangles],
		axis = 0)
	#uv_vertices = np.concatenate([uv_surface1[:-1], uv_surface2[:-1], uv_upper_side_points, uv_lower_side_points], axis = 0)
	uv_vertices = np.concatenate([uv_surface1[:-1], uv_surface2[:-1], uv_upper_side_points, uv_lower_side_points], axis = 0)
	return Vertices, all_triangles, uv_vertices



















