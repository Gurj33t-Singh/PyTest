# Helper functions for API calls
import logging
import requests
from requests.exceptions import RequestException, HTTPError, Timeout, ConnectionError

def make_request(method, url, headers=None, params=None, payload=None, is_json=True, timeout=10):
    """
    Helper function to make API requests.

    Args:
        method (str): HTTP method (GET, POST, PUT, DELETE).
        url (str): The API endpoint.
        payload (dict): Request body data.
        headers (dict): Request headers.
        params (dict): Query parameters.
        is_json (bool): Whether to send the payload as JSON.
        timeout (int): Request timeout in seconds.

    Returns:
        dict: Parsed JSON response or error details.

    Raises:
        Exception: If an error occurs during the request.
    """
    if headers is None:
        headers = {"Content-Type": "application/json"} if is_json else {}

    try:
        response = requests.request(
            method=method,
            url=url,
            json=payload if is_json else None,
            data=None if is_json else payload,
            headers=headers,
            params=params,
            timeout=timeout,
        )

        # Attempt to parse JSON response
        try:
            return response.json()
        except ValueError:
            return {
                "error": "Invalid JSON response",
                "status_code": response.status_code,
                "content": response.text,
            }

    except ConnectionError:
        return {"error": "Connection error. Unable to reach the server.", "url": url}

    except Timeout:
        return {"error": f"Request timed out after {timeout} seconds.", "url": url}

    except HTTPError as http_err:
        return {
            "error": "HTTP error occurred.",
            "status_code": response.status_code if 'response' in locals() else None,
            "details": str(http_err),
            "url": url,
        }

    except RequestException as req_err:
        return {
            "error": "An error occurred during the request.",
            "details": str(req_err),
            "url": url,
        }

    except Exception as e:
        return {
            "error": "An unexpected error occurred.",
            "details": str(e),
            "url": url,
        }

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

