#Ramen-Ratings

#Initialize modules
import numpy as np

#Import data
data = np.genfromtxt("ramen-ratings.csv", dtype = 'U75', encoding = 'utf-8', skip_header = 1, delimiter = ",")
ramen_ratings = np.array(data)

#Define Common functs
#Compare a string against a column, return the vector of BOOL values
def comparison_vector(input_array,string,col):
    is_it = input_array[:,col] == string
    return is_it

#Practice creating data catagories
#Numpy uses keyed matrices as something like a truth mapping, then combining two truth mappings produces an output.
rating_4 = comparison_vector(ramen_ratings,"4",5)
rating_5 = comparison_vector(ramen_ratings,"5",5)
country_japan = comparison_vector(ramen_ratings,"Japan",4)
country_china = comparison_vector(ramen_ratings,"China",4)

#This is printing the combined 'truth mapping' over the array of data, only printing where a TRUE comes from both maps.
print(ramen_ratings[(rating_5)&(country_japan)])

#While its easy to print all exactly 5 star or 4 star, doing ranges of 1-3 or 3-5
# becomes increasingly difficult when treating the numbers as strings instead of floats.

#While looking into what to do, a Numpy solution seems increasingly complex, and Pandas makes this a lot easier. Shifting to Pandas. 
