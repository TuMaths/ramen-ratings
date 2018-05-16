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
rating_4 = comparison_vector(ramen_ratings,"4",5)
rating_5 = comparison_vector(ramen_ratings,"5",5)
country_japan = comparison_vector(ramen_ratings,"Japan",4)
country_china = comparison_vector(ramen_ratings,"China",4)

print(ramen_ratings[(rating_5)&(country_japan)])
