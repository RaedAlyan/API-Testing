import requests


def get_api_status(base_url: str, path_variable: str):
    """
    Fetches the status of the API from the specified endpoint.

    :param base_url: The base url of the API.
    :param path_variable: The path variable of the API.
    :return tuple: A tuple containing the status code and response JSON.
    :raises requests.exceptions.RequestException: For network-related errors.
    :raises KeyError: If the expected key is missing in the response.
    """
    url = f'{base_url}/{path_variable}'
    try:
        # Send the GET request
        response = requests.get(url)

        # Parse the JSON response
        response_json = response.json()
        if 'status' not in response_json:
            raise KeyError('Missing "status" key in the API response.')
        return response.status_code, response_json['status']

    except requests.exceptions.RequestException as e:
        raise RuntimeError(f'Error while accessing the API. Error: {e}')
    except KeyError as e:
        raise KeyError(f'The expected key is missing in the response. Error: {e}')


if __name__ == '__main__':
    BASE_URL = 'https://simple-grocery-store-api.glitch.me'
    PATH_VARIABLE = 'status'
    try:
        status_code, api_status = get_api_status(BASE_URL, PATH_VARIABLE)
        print(f'Status code: {status_code}')
        print(f'The API status is: {api_status}')
    except RuntimeError as error:
        print(f'An error occurred: {error}')
