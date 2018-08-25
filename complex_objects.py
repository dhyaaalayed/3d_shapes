from complete_daniel import *


star1 = create_one_small_star()
star2 = create_one_small_star()
star3 = create_one_small_star()
star4 = create_one_small_star()

f, axarr = plt.subplots(1,3, figsize=(20,2.4 * 1))



star2[:, 0] += 0.5
star3[:, 0] += 1.5
star4[:, 0] += 2.5
star = np.concatenate([star1, star2, star3, star4], axis = 0) # this concatenating for plotting 2d
axarr[2].plot(star[:, 0], star[:, 1])

stars_list = []
stars_list.append(star1)
stars_list.append(star2)
stars_list.append(star3)
stars_list.append(star4)

create_3d_for_list(stars_list)

plt.show()
