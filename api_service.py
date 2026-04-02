import requests

def get_company_info(company_name):

    url = "https://api.api-ninjas.com/v1/logo"

    headers = {
         "X-Api-Key": "JYlXrHonvN3zU7RFzmAjCeTiPTlAyQaxfvQxoamD"
    }

    params = {
        "name": company_name
    }

    response = requests.get(url, headers=headers, params=params)

    print("Status Code:", response.status_code)
    print("Response Text:", response.text)

    if response.status_code == 200:
        return response.json()
    else:
        return "Error fetching data"