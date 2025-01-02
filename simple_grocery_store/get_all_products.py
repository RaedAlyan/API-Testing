import requests


def get_all_products(base_url: str, path_variable: str):
    """
    Fetches all products.

    :param base_url: The base url of the API.
    :param path_variable: The path variable of the API.
    :return tuple: A tuple containing the status code and response JSON.
    :raises requests.exceptions.RequestException: For network-related errors.
    """
    url = f'{base_url}/{path_variable}'
    try:
        # Send the GET request
        response = requests.get(url)

        # Parse the JSON response
        response_json = response.json()
        return response.status_code, response_json

    except requests.exceptions.RequestException as e:
        raise RuntimeError(f'Error while accessing the API. Error: {e}')


if __name__ == '__main__':
    BASE_URL = 'https://simple-grocery-store-api.glitch.me'
    PATH_VARIABLE = 'products'
    try:
        status_code, products = get_all_products(BASE_URL, PATH_VARIABLE)
        print(f'Status code: {status_code}')
        print(f'Products are: {products}')
    except RuntimeError as error:
        print(f'An error occurred: {error}')
