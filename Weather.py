#Get user input to lookup weather based on city  or zip-code using a main():, try, and api.

import requests


#function to search by city name
def cities():
    city = input("What city would you like to search? ")
    api = "https://api.openweathermap.org/data/2.5/weather?q={},us&appid=3647050e043499b28c280ce12add92bf&units=imperial".format(city)
    req = requests.get(api)
    info = req.json()
    report(info)
    
    again = input("Would you like to search another location? y/n ")
    if again.lower == "y":
        main()
    if again.lower == "n":
        print("Thank you for using our services, have a nice day!")
        quit()
#function to search by zipcode
def zipcode():
    code = int(input("What zip-code would you like to search? "))
    api = "https://api.openweathermap.org/data/2.5/weather?zip={},us&units=imperial&appid=3647050e043499b28c280ce12add92bf".format(code)
    req = requests.get(api)
    info = req.json()
    report(info)
    again = input("Would you like to search another location? y/n ")
    if again.lower == "y":
        main()
    if again.lower == "n":
        print("Thank you for using our services, have a nice day!")
        quit()
#function to display the gathered weather
def report(info):
    temp = info['main']['temp']
    hightemp = info['main']['temp_max']
    lowtemp = info['main']['temp_min']
    wind_speed = info['wind']['speed']
    humidity = info['main']['humidity']
    description = info['weather'][0]['description']

    print('Current Temperature : {} degree fahrenheit'.format(temp))
    print('High Temperature : {} degree fahrenheit'.format(hightemp))
    print('Low Temperature : {} degree fahrenheit'.format(lowtemp))
    print('Wind Speed : {} m/s'.format(wind_speed))
    print('Humidity : {} %'.format(humidity))
    print('Description : {}'.format(description))
#Required Main() as well as needed to actually run this program, I hope it was needed anyways.
def main():
    while True:
        lookup = input("Would you like to look up the weather by city or zip-code? ")

###wanted to add .upper/.lower, need to figure out why there is an issue.
        if lookup == 'city':
            try:
                print("Searching for city")
                cities()
            except:
                print("Error searching for city, please try again")
                cities()
###wanted to add .upper/.lower, need to figure out why there is an issue.
        if lookup == "zip-code":
            try:
                print("Searching for zip-code")
                zipcode()
            except:
                print("Error searching for zip-code, please try again")
                zipcode()
        else:
            print("There was an unforseen error with your selection, please try again.")
###3647050e043499b28c280ce12add92bf apicode
        
main()