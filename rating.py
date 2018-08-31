# import libraries
import urllib.request
import urllib.error
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import time
import csv


now = time.strftime("%m-%d-%Y")
filename = "Ratings-Report-"+now+".csv"
print("Ratings report being generated and will output to: ")
print(filename)
f = open(filename,'a')

# specify the url
yelpURLs = {
# Orlando Stores
"Altamonte Springs": "https://www.yelp.com/biz/ifixyouri-iphone-ipad-and-ipod-repair-altamonte-springs-2",
"East Orlando": "https://www.yelp.com/biz/ifixyouri-iphone-ipad-and-ipod-repair-orlando-6",
"Downtown Orlando": "https://www.yelp.com/biz/i-fix-your-i-orlando-9",
"Longwood": "https://www.yelp.com/biz/ifixyouri-iphone-ipad-and-ipod-repair-longwood",
"Millenia": "https://www.yelp.com/biz/ifixyouri-iphone-ipad-and-ipod-repair-orlando-14",
"Oviedo": "https://www.yelp.com/biz/ifixyouri-iphone-ipad-and-ipod-repair-oviedo",
"Winter Park": "https://www.yelp.com/biz/ifixyouri-iphone-ipad-and-ipod-repair-winter-park",

#Palm Beach Stores
"Donald Ross": "https://www.yelp.com/biz/ifixyouri-iphone-ipad-and-ipod-repair-jupiter",
"Indiantown": "https://www.yelp.com/biz/i-fix-your-i-smart-device-repair-jupiter-6",
"Northlake": "https://www.yelp.com/biz/i-fix-your-i-palm-beach-gardens-5",
"PGA": "https://www.yelp.com/biz/ifixyouri-iphone-ipad-and-ipod-repair-palm-beach-gardens-3",
"West Palm": "https://www.yelp.com/biz/ifixyouri-iphone-ipad-and-ipod-repair-west-palm-beach-5",

#Boston Stores
"Brookline": "https://www.yelp.com/biz/ifixyouri-brookline-10",
"Newbury": "https://www.yelp.com/biz/ifixyouri-iphone-ipad-and-ipod-repair-boston"
}

# specify the url
googURLs = {
#Orlando Stores
"Altamonte Springs": "https://www.google.com/search?q=iFixYouri+Altamonte+Springs",
"East Orlando": "https://www.google.com/search?q=iFixYouri+Alafaya",
"Downtown Orlando": "https://www.google.com/search?q=iFixYouri+Colonial+Dr",
"Longwood": "https://www.google.com/search?q=iFixYouri+Longwood",
"Millenia": "https://www.google.com/search?q=iFixYouri+Millenia",
"Oviedo": "https://www.google.com/search?q=iFixYouri+Oviedo",
"Winter Park": "https://www.google.com/search?q=iFixYouri+Winter+Park",

#Palm Beach Stores
"Donald Ross": "https://www.google.com/search?q=iFixYouri+Donald+Ross",
"Indiantown": "https://www.google.com/search?q=iFixYouri+Indiantown+Road",
"Northlake": "https://www.google.com/search?q=iFixYouri+Northlake",
"PGA": "https://www.google.com/search?q=iFixYouri+PGA",
"West Palm": "https://www.google.com/search?q=iFixYouri+West+Palm",

#Boston Stores
"Brookline": "https://www.google.com/search?q=iFixYouri+Brookline",
"Newbury": "https://www.google.com/search?q=iFixYouri+Newbury"
}

a = [["LOCATION", 'YELP RATING', 'YELP REVIEWS','GOOGLE RATING','GOOGLE REVIEWS']]

print("\n")
print("Yelp Ratings")
print("------------")

for key in yelpURLs:
    # query the website and return the html to the variable ‘page’
    quote_page = yelpURLs[key]
    page = urllib.request.urlopen(quote_page)
    
    # parse the html using beautiful soup and store in variable `soup`
    soup = BeautifulSoup(page, 'html.parser')
    
    # get the rating
    rating_box = soup.find('div', attrs={'class':'i-stars'})    
    rating = str(rating_box) #convert the bs4 to class str  
    review_count_box = soup.find('span', attrs={'itemprop':'reviewCount'})    
    review_count = str(review_count_box) #convert the bs4 to class str   
    
    reviewCount = review_count[(review_count.find('Count')+ 7) : (review_count.find('Count')+ 7) + 3]
    reviewCount = reviewCount.replace("<", "")
    reviewCount = reviewCount.replace("/", "")
    print(key + ", " + rating[(rating.find('title')+7) : (rating.find('title')+7) + 3] + ", " + reviewCount)
    b=[key, rating[(rating.find('title')+7) : (rating.find('title')+7) + 3], reviewCount]
    
    a.append(b)


print("\n")
print("Google Ratings")
print("--------------")

c = 1
for key in googURLs:
    # query the website and return the html to the variable ‘page’
    quote_page = googURLs[key]
    req = Request(quote_page, headers={'User-Agent': 'Mozilla/5.0'}) #adds a user agent to not get blocked
    page = urlopen(req).read()
    #page = pager.decode('utf-8')

    # parse the html using beautiful soup and store in variable `soup`
    soup = BeautifulSoup(page, 'html.parser')
    
    # get the rating
    rating = str(soup) #convert the bs4 to string
       
    #since google changes div names, it takes two slices to get to the rating 
    firstSlice = rating[(rating.find('reviews</span>')-105) : (rating.find('reviews</span>')-105) + 10]
    rate = firstSlice[(firstSlice.find('.')-1) : (firstSlice.find('.')-1) + 3]
    #since google changes div names, it takes two slices to get to the rating 
    secondSlice = rating[(rating.find('reviews</span>')-4) : (rating.find('reviews</span>')-4) + 3]
    
    reviewCount = reviewCount.replace(" ", "")
    print(key + ", " + rate + ", " + secondSlice)
    #time.sleep(1) #add a pause to not get blocked  
    
    a[c].append(rate)
    a[c].append(secondSlice)
    c = c+1


print(' ')

#file output
for s in a:
    for b in s:
        f.write(b)
        f.write(", ")
    f.write("\n")

f.close()