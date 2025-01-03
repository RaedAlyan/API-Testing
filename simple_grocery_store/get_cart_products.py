import requests

def get_cart_products(base_url: str, path_variable_1: str, path_variable_2: str, cart_id: str) -> tuple:
    """
    Gets a cart products.

    :param base_url: the base url of the API.
    :param path_variable_1: the first path variable.
    :param path_variable_2: the second path variable.
    :param cart_id: the cart id.
    :return: A tuple containing the status code and response body.
    :raises requests.exceptions.RequestException: For network-related errors.
    """
    url = f'{base_url}/{path_variable_1}/{cart_id}/{path_variable_2}'
    try:
        # Send the GET request
        response = requests.get(url)
        return response.status_code, response.json()
    except requests.exceptions.RequestException as e:
        raise requests.exceptions.RequestException(f'An error occurred while getting the cart products. Error: {e}')


if __name__ == '__main__':
    BASE_URL = 'https://simple-grocery-store-api.glitch.me'
    PATH_VARIABLE_1 = 'carts'
    CART_ID = 'tBdwEAmxj9WFlZgrXjjO8'
    PATH_VARIABLE_2 = 'items'
    status_code, body = get_cart_products(BASE_URL, PATH_VARIABLE_1, PATH_VARIABLE_2, CART_ID)
    print(f'Status code is: {status_code}')
    print(f'The products of this cart id {CART_ID} are: {body}')
