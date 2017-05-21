import requests

# The API key which I possess for this project
# Note that it is in a separate, non tracked file for security reasons.
api_key = open("api_key", "r").read()


def main():
    """ The main function of the program """

    # Getting the ID of the users to lookup
    first_id = get_account_id(input("enter the name of the first user \n"))
    second_id = get_account_id(input("enter name of second user \n"))

    # Getting the matchlists of the users
    first_matchlist = get_matchlist_ids(first_id)
    second_matchlist = get_matchlist_ids(second_id)

    # Checking for games that both users were in
    check_for_matches(first_matchlist, second_matchlist)

    exit(0)


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


def get_matchlist_ids(account_id: int) -> list:
    """ Grabs the matchlist for the player

     :param int account_id: the account id of the user who's matchlist is being requested
     :rtype: list
     :return: A list of match IDs for a player
     """

    # The endpoint for matchlists
    matchlistv3_url = "https://na1.api.riotgames.com/lol/match/v3/matchlists/by-account/" + str(account_id)
    # The parameters
    matchlistv3_parameters = {"api_key": api_key}
    # The request
    matchlist_response = requests.get(matchlistv3_url, params=matchlistv3_parameters)
    # Converting json
    data = matchlist_response.json()
    # Grabbing the value of 'gameId' from every dictionary in the list of dictionaries 'matches' and returning it
    return [d['gameId'] for d in data['matches']]


def check_for_matches(first_matchlist: list, second_matchlist:list) -> list:
    """ Checks for matching items between two lists

    :param list first_matchlist: The matchlist of one user
    :param list second_matchlist: The matchlist of another user
    :rtype: list
    :return: a list of all matching games
    """
    same_games = []
    for i in first_matchlist:
        for j in second_matchlist:
            if i == j:
                same_games.append(i)
    if len(same_games) != 0:
        print("overlapping games found \n")
        print("number of matching games: " + str(len(same_games))+ "\n")
    return same_games


if __name__ == "__main__":
    main()
