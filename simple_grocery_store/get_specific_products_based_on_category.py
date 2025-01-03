import requests


def get_specific_products_based_on_category(base_url: str, path_variable: str, query_parameters: dir) -> tuple:
    """
    Fetches specific products based on a category.

    :param base_url: The base url of the API.
    :param path_variable: The path variable of the API.
    :param query_parameters: The query parameters of the API.
    :return tuple: A tuple containing the status code and response JSON.
    :raises requests.exceptions.RequestException: For network-related errors.
    """
    url = f'{base_url}/{path_variable}'
    try:
        # Send the GET request
        response = requests.get(url, params=query_parameters)

        # Parse the JSON response
        response_json = response.json()
        return response.status_code, response_json

    except requests.exceptions.RequestException as e:
        raise RuntimeError(f'Error while accessing the API. Error: {e}')

if __name__ == '__main__':
    BASE_URL = 'https://simple-grocery-store-api.glitch.me'
    PATH_VARIABLE = 'products'
    QUERY_PARAMS = {
        "category": "candy"
    }
    try:
        status_code, products = get_specific_products_based_on_category(BASE_URL, PATH_VARIABLE, QUERY_PARAMS)
        print(f'Status code: {status_code}')
        print(f'Products are: {products}')
    except RuntimeError as error:
        print(f'An error occurred: {error}')
