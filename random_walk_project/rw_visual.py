import matplotlib.pyplot as plt

from random_walk import RandomWalk


# keep making new walks, as long as the program is active.
while True:
  # Make a random walk
  rw = RandomWalk()
  rw.fill_walk()

  # Plot the points in the walk.
  plt.style.use('classic')
  fig, ax = plt.subplots(figsize = (15,9))
  point_numbers = range(rw.num_points)
  # ax.plot(rw.x_values,rw.y_values,c=point_numbers,s=1)
  ax.plot(rw.x_values,rw.y_values,linewidth = 2)
  ax.set_aspect('equal')

  # emphasize the first and last points

  ax.get_xaxis().set_visible(False)
  ax.get_yaxis().set_visible(False)

  plt.show()

  keep_running = input("Make another walk? (y/n): ")
  if keep_running == 'n':
    break