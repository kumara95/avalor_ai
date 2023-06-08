import json
import requests
import logging


def get(url):
    ''' 
    Fetches an url. Prints a warning if the call fails.

    Returns:
        result (str | False): Returns the returned string from the server. False if the call failed.
    '''
    try:
        response = requests.get(url)
        if response.status_code != 200:
            logging.warning(
                f'GET request to {url} failed with status code {response.status_code}')
            logging.warning(response.text)
            return False
    except:
        logging.error(f"Request to {url} failed. Url does not seem available.")
        return False
    return response.text


def post(url, data={}):
    ''' 
    Post data to an url. Prints a warning if the call fails.

    data : dict
        A dictionary that will be sent as json to the server    

    Returns:
        result (bool): Returns true if successful. False otherwise.
    '''
    try:
        response = requests.post(url, json=data)
        if response.status_code != 200:
            logging.warning(
                f'Post request to {url} failed with status code {response.status_code}')
            logging.warning(response.text)
            return False
    except:
        logging.error(f"Request to {url} failed. Url does not seem available.")
        return False
    return response.text
