import requests
from car_functions import RDW_ENDPOINT


def get_random_cars_brand(brand):

    # define the endpoint
    endpoint = f'{RDW_ENDPOINT}?merk={brand.upper()}'
    
    # execute the request
    resp = requests.get(endpoint)
    
    # get the data from the request
    resp_list = resp.json()
    
    return resp_list