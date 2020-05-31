from app import app, mongo
from flask import render_template, flash, redirect, request, url_for
from werkzeug.urls import url_parse

# TODO make a form for replacing player's names
# TODO update mongodb based on new names

@app.route('/')
@app.route('/index')
def index():
    team_names = []
    team_all = mongo.db.team.find()
    for team_x in team_all:
        team_names.append(team_x["team_name"])
    print(team_names)
    return render_template("index.html", title='Home Page', team_names=team_names)


# TODO make team page with players per team
@app.route('/team/<team_name>')
def team(team_name):
    team_x = mongo.db.team.find_one_or_404({"team_name": team_name})
    player_list = team_x["players_on_team"]
    player_names = []
    for player in player_list:
        player_x = mongo.db.player.find_one_or_404({"id": player})
        player_names.append(player_x["player_name"])
    return render_template('team.html', team_name=team_x["team_name"], team_color=team_x["team_color"],
                           player_names=player_names)