import requests


def create_cart(base_url: str, path_variable: str) -> tuple:
    """
    Creates a new cart.

    :param base_url: The base url of the API.
    :param path_variable: The path variable of the API.
    :return: A tuple containing the status code and response body.
    :raises requests.exceptions.RequestException: For network-related errors.
    """
    url = f'{base_url}/{path_variable}'
    try:
        # Send the POST request
        response = requests.post(url)

        # Parse the JSON response
        body = response.json()
        return response.status_code, body
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f'Error while accessing the API. Error: {e}')

if __name__ == '__main__':
    BASE_URL = 'https://simple-grocery-store-api.glitch.me/'
    PATH_VARIABLE = 'carts'
    status_code, response_body = create_cart(BASE_URL, PATH_VARIABLE)
    print(f'The status code is {status_code}')
    print(f'The cartId is {response_body["cartId"]}')
