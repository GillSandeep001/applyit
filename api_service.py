import requests
import os
import dotenv

dotenv.load_dotenv()


def get_company_info(company_name):
    """
    This function sends a request to a third-party API (API Ninjas)
    to retrieve company-related data such as logo.
    """

    # API endpoint for fetching company logo information
    url = "https://api.api-ninjas.com/v1/logo"

    # API key required to authenticate the request
    headers = {
    "X-Api-Key": os.getenv("API_KEY")
    }

    # Parameters sent with the request (company name entered by user)
    params = {
        "name": company_name
    }

    # Send GET request to the API
    response = requests.get(url, headers=headers, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Convert response to JSON format and return it
        return response.json()
    else:
        # Return error message if API call fails
        return "Error fetching data"