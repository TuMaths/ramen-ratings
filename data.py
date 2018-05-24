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
five_star_ratio_country = {} #Ratio of 5star vs country submitted ramen
five_star_ratio_overall = {} #Ratio of 5star vs overall submitted ramen total
overall_ratio = {}           #Ratio of Country submitted ramen vs overall total
overall_points = {}

total_reviews = countries.sum()
total_5_reviews = countries_5_stars.sum()

for each in country_list:
    total_count = countries[each]
    five_count = countries_5_stars[each]
    ratio_country = five_count / total_count
    ratio_overall = total_count / total_reviews
    ratio_five_overall = five_count / total_reviews
    five_star_ratio_country[each] = ratio_country
    five_star_ratio_overall[each] = ratio_five_overall
    overall_ratio[each] = ratio_overall
    overall_points[each] = ratio_country + ratio_five_overall + ratio_overall

#Plot those dictionaries, get a visual representation of the five_star_ratio
#define a function to display our dictionaries as barplots
def barplot(input_dictionary):
    plt.bar(range(len(input_dictionary)),list(input_dictionary.values()), align='center')
    plt.xticks(range(len(input_dictionary)),list(input_dictionary.keys()))
    plt.show()
    #credit: stack exchange
#Comparison 1
barplot(five_star_ratio_country)
#This is the ratio of 5 star reviews out of the total number of ramen reviews in that country

#It looks like Cambodia, Malaysia, Sarawak, and Singapore, and Myanmar are the top 6.
#But that's not the whole picture.
barplot(five_star_ratio_overall)
#This is the ratio of five star ramens from that country to the total number of submitted ramen in total
#Japan shows a clear lead here.

barplot(overall_ratio)
#Here's the overall numer of ramen submitted per country vs the total number of ramen reviews available
#Again, Japan with a good lead.

barplot(overall_points)
#Now the Highest is Malaysia!
