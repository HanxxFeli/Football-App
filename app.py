import re
from flask import Flask, render_template, request, flash
from helpers import *


app = Flask(__name__)
app.config["SECRET_KEY"] = "58FCD97C86EF2692498D597D1F223"


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/live', methods=["GET","POST"])
def live_matches():
    fixtures = get_live_data()
    fixtures_data = []

    for match in fixtures:
        match_details = {
        "match_id": match["fixture"]["id"],
        "elapsed_time": match["fixture"]["status"]["elapsed"],
        "league_name": match["league"]["name"],
        "home_name": match["teams"]["home"]["name"],
        "home_logo": match["teams"]["home"]["logo"],
        "home_score": match["goals"]["home"],
        "away_name": match["teams"]["away"]["name"],
        "away_logo": match["teams"]["away"]["logo"],
        "away_score": match["goals"]["away"],
        }
        fixtures_data.append(match_details)

    if len(fixtures_data) == 0:
        flash("There are currently no ongoing matches! Please check again at a latter time.")
        return render_template("livematches.html")
    else :
        return render_template("livematches.html", fixtures_data=fixtures_data)


# @app.route('/livematchstat')
# def match_stat():
#     match_id = request.args.get('match_id','')
#     #match_data = get_live_matchdata(int(match_id))
#     #print(match_data)
#     return render_template("matchstat.html")

@app.route('/searchteam')
def search_team():
    return render_template("teamstat.html")

@app.route('/teamstat', methods=["GET","POST"])
def team_stat():
    team_name = request.form.get('team-name') # User input of what team to find
    team_id = get_team_id(team_name) 
    team_leagueid = get_team_leagueid(team_id) # id of league where team belongs to
    
    available_team_seasons = get_team_seasons(team_id) # list of all available seasons of a team
    chosen_season = request.form.get('season-year') # chosen year by user

    team_statistics = get_team_statistics(team_id, team_leagueid, int(chosen_season))
    print(team_statistics)
    return render_template("teamstat.html", seasons=available_team_seasons, team_statistics=team_statistics)




if __name__=='__main__':
    app.run(debug=True)
