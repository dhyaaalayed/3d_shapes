from complete_daniel import *
from rotate import *

star1 = create_one_small_star()
# star1 = rotate_polygon(star1, 40)
star2 = create_one_small_star()
# star2 = rotate_polygon(star2, 70)
star3 = create_one_small_star()
# star3 = rotate_polygon(star3, 60)
star4 = create_one_small_star()
# star4 = rotate_polygon(star4, 90)
star5 = create_one_small_star()


# the rotation should also be applied on the final vertices like what I did now

# f, axarr = plt.subplots(1,3, figsize=(20,2.4 * 1))


# star1[:, 0] += 
# star2[:, 0] += 2.5
# star3[:, 0] += 1.0
# star4[:, 0] += 1.5
# star5[:, 0] += 2.0
# star = np.concatenate([star1, star2, star3, star4], axis = 0) # this concatenating for plotting 2d
star = star1

# The last plot
# axarr[2].plot(star[:, 0], star[:, 1])

stars_list = []
stars_list.append(star1)
stars_list.append(star2)
stars_list.append(star3)
stars_list.append(star4)
stars_list.append(star5)

create_3d_for_list(stars_list)

plt.show()
