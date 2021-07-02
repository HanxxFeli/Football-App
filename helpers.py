import requests


payload = {}
headers = {
    'x-rapidapi-key': '1e86c6ff26e12c84cee9c25bf1e5c697',
    'x-rapidapi-host': 'v3.football.api-sports.io'
}

base_url = "https://v3.football.api-sports.io"

def get_live_data():
    """
    Retrieve all live fixture data from API
    """
    url = base_url + "/fixtures?live=all"
    response = requests.request("GET", url, headers=headers, data=payload)
    r = response.json()
    matches = r["response"]
    return matches


def get_live_matchdata(match_id):
    """
    Retrieve specific fixture statistics
    """
    url =  base_url + f"/fixtures/statistics?fixture={match_id}"
    response = requests.request("GET", url, headers=headers, data=payload)
    r = response.json()
    match_data = r["response"]
    return match_data


def get_team_id(team_name):
    """
    Retrieve team id from API
    """
    url = base_url + f"/teams?name={team_name}"
    response = requests.request("GET", url, headers=headers, data=payload)
    r = response.json()
    team_id = r["response"][0]["team"]["id"]
    return team_id


def get_team_leagueid(team_id):
    """
    Retrieve league where teams belong to by passing in team_id
    """
    url = base_url + f"/leagues?team={team_id}"
    response = requests.request("GET", url, headers=headers, data=payload)
    r = response.json()
    league_id = r["response"][0]["league"]["id"]
    return league_id


def get_team_seasons(team_id):
    """
    Retrieve all list of seasons available for a team by passing in team_id
    """
    url = base_url + f"/teams/seasons?team={team_id}"
    response = requests.request("GET", url, headers=headers, data=payload)
    r = response.json()
    available_seasons = r["response"]
    return available_seasons


def get_team_statistics(team_id, league_id, team_season):
    """
    Retrieve season statistics of a specific team
    """
    url = base_url + f"/teams/statistics?season={team_season}&team={team_id}&league={league_id}"
    response = requests.request("GET", url, headers=headers, data=payload)
    r = response.json()
    team_data = r["response"]
    return team_data