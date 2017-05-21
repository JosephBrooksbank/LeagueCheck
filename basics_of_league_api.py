import requests

# The API key which I possess for this project

api_key = open("api_key", "r").read()


def get_account_id(summoner_name: str) -> int:
    """
    Getting the Account ID

    :param string summoner_name: The username of the account to look up
    :rtype: long
    :return: Returns the account ID of the summoner, based on their plaintext name (as seen in game)
    """

    # Replacing spaces with %20, the percent coding for a space (required for valid path)
    summoner_name.replace(" ", "%20")
    # The url for a summoner lookup
    summonerv3_url = "https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/" + summoner_name
    # The parameters for this GET request
    summonerv3_parameters = {"api_key": api_key}
    # Getting the response from the server
    summoner_response = requests.get(summonerv3_url, params=summonerv3_parameters)
    # Converting the json string to its original form, a dict
    data = summoner_response.json()
    return data['accountId']


accountID = get_account_id("Bittah Dreamer")

