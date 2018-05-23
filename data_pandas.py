#Ramen-Ratings !!now with Pandas!!

#Initialize modules
import pandas
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (25, 10)

#Import data
ramen_ratings = pandas.read_csv("ramen-ratings.csv", index_col="review")
ramen_ratings = ramen_ratings.sort_values(by=['review']) #Because the list was unsorted
ramen_ratings['stars'] = pandas.to_numeric(ramen_ratings['stars'], errors='coerce') #Convert strings to floats for the stars rating

#Work with the data

#Working with totals for each country
countries = ramen_ratings["country"].value_counts()     #gives us a DF with country name and number of reviews

#Look at it
print(countries)
countries[:20].plot(kind='bar')     #plot the first 20 most reviewed countries

#Now lets get 5 star ratings
is_5_star = ramen_ratings['stars'] == 5     #Create an array of truth values
five_stars = ramen_ratings[is_5_star]   #Return just the 5 star rated ramens
countries_5_stars = five_stars['country'].value_counts()    #Create a list like the first, with Country and number of 5 star reviews

#Look at them too
countries_5_stars[:10].plot(kind='bar')     #Plot the first 10 countries number of 5 star reviews

#Create a unique list of all countries producing 5 star ramen
country_list = five_stars['country'].unique()

#Find the ratio between 5 star ramens over all ramens reviewed from that country
five_star_ratio = {}
for each in country_list:
    total_count = countries[each]
    five_count = countries_5_stars[each]
    five_star_ratio[each] = five_count / total_count

#Plot that dictionary, get a visual representation of the five_star_ratio
plt.bar(range(len(five_star_ratio)),list(five_star_ratio.values()), align='center')
plt.xticks(range(len(five_star_ratio)),list(five_star_ratio.keys()))
plt.show()
