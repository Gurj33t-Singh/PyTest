# Helper functions for API calls
import logging
import requests

def make_request(method, url, headers=None, params=None, payload=None, is_json=True):
    """
    Make an HTTP request.

    Args:
        method (str): HTTP method (GET, POST, PUT, etc.).
        url (str): The URL for the request.
        headers (dict): Optional headers for the request.
        params (dict): Optional query parameters for the request.
        payload (dict, str, bytes, or file-like object): The request payload.
        use_json (bool): If True, send payload as JSON; otherwise, send as form-encoded or raw data.

    Returns:
        requests.Response: The HTTP response object.
    """
    if is_json:
        response = requests.request(method, url, headers=headers, params=params, json=payload)
    else:
        response = requests.request(method, url, headers=headers, params=params, data=payload)
    return response

def log_response(response):
    
    """
    Log response details to a file.
    Params: response obj
    """

    # Configure logging
    logging.basicConfig(
                        filename='response_log.txt',  # Log file name
                        level=logging.DEBUG,           # Set logging level to INFO (or DEBUG for more detailed logs)
                        format='%(asctime)s - %(message)s',  # Log format with timestamp
                        )
    try:
        # Extract response details
        url = response.url
        status_code = response.status_code
        request_body = response.request.body
        response_content = response.json()

        # Log the details
        logging.info(f"URL: {url}\n")
        logging.info(f"Status Code: {status_code}\n")
        logging.info(f"Request Body: {request_body}\n")
        logging.info(f"Response: {response_content}\n")

    except Exception as e:
        # Log any exceptions while logging the response
        logging.error(f"Failed to log response: {e}")

