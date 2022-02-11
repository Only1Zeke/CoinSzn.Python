#This program returns a users percise location

def get_formatted_location(city_location, country_location):
    """Return a full location, neatly formatted."""
    full_location = city_location + ' ' + country_location
    return full_location.title()

while True:
    print("\nPlease tell me your location:")
    c_ity = input("City: ")
    c_ountry = input("Country: ")

    formatted_location = get_formatted_location(city_location, country_location)
    print("\nYour loaction is " + formatted_location + "!")
