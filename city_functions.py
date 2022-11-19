#TryItYourself
def city_and_country(city, country, population=''):
    """Return a neatly defined city and country."""
    if population:
        return f"{city.title()}, {country.title()} - population {population}"
    else:
        return f"{city.title()}, {country.title()}"

city_and_country('lagos', 'nigeria', 300)


