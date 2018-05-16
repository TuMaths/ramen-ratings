#Ramen-Ratings

import numpy as np
data = np.genfromtxt("ramen-ratings.csv", encoding = 'utf-8', skip_header = 1, delimiter = ",")
ramen_ratings = np.array(data)
print(ramen_ratings)