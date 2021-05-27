import json
import math

import requests
from geopy.geocoders import Nominatim

API_URL = "https://dwp-techtest.herokuapp.com/"
EARTH_RADIUS = 3960.0
DEGREES_TO_RADIANS = math.pi/180.0
RADIANS_TO_DEGREES = 180.0/math.pi


def find_users(city, radius = 50):
    """
    Return a list of all users either living in or currently within the given
    radius of city.
    """
    # Get users listed as living in city
    exact = living_in(city)

    # Get users currently withing {radius} miles of city center
    nearby = currently_near(city, radius)

    # Join lists and remove duplicates
    unique = list({x['id']:x for x in exact + nearby}.values())

    return unique


def living_in(city):
    """
    Query the API for all users living in cityxs
    """
    endpoint = f"{API_URL}city/{city}/users"
    return _query(endpoint)


def currently_near(city, radius = 50):
    """
    Get all users that are currently based with the given radius from the
    geographical center of city
    """

    # Get coordinates for city
    geolocator = Nominatim(user_agent="OiNutter")
    location = geolocator.geocode(city)

    # Get upper and lower coordinate bounds
    lat_radius = _change_in_latitude(radius)
    min_lat = location.latitude - lat_radius
    max_lat = location.latitude + lat_radius

    lng_radius = _change_in_longitude(location.latitude, radius)
    min_lng = location.longitude - lng_radius
    max_lng = location.longitude + lng_radius

    # Get all users and filter out based on coordinates
    endpoint = f"{API_URL}/users"
    all_users = _query(endpoint)
    users = []
    for user in all_users:
        if _in_bounds(float(user["latitude"]), float(user["longitude"]), min_lat, max_lat, min_lng, max_lng):
            users.append(user)
    return users


def _query(url):
    """
    Perform the API request and return the JSON body
    """
    r = requests.get(url)
    r.raise_for_status()
    return r.json()


def _change_in_latitude(miles):
    """
    Given a distance north, return the change in latitude.
    """
    return (miles/EARTH_RADIUS) * RADIANS_TO_DEGREES


def _change_in_longitude(latitude, miles):
    """
    Given a latitude and a distance west, return the change in longitude.
    """

    # Find the radius of a circle around the earth at given latitude.
    r = EARTH_RADIUS * math.cos(latitude * DEGREES_TO_RADIANS)
    return (miles/r) * RADIANS_TO_DEGREES


def _in_bounds(lat, lng, min_lat, max_lat, min_lng, max_lng):
    """
    Check that both lat and lng are within their respective upper and lower bounds
    """
    return lat >= min_lat and lat <= max_lat and lng >= min_lng and lng <= max_lng
