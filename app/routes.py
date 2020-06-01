from app import app, mongo, models
from flask import render_template, flash, redirect, request, url_for
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
def index():
    team_names = []
    team_all = mongo.db.team.find()
    for team_x in team_all:
        team_names.append(team_x["team_name"])
    print(team_names)
    return render_template("index.html", title='Home Page', team_names=team_names)


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


@app.route('/player_name_change/<player_name>', methods=['GET', 'POST'])
def player_name_change(player_name):
    form = models.NameChangeForm()
    if form.validate_on_submit():
        result_0 = mongo.db.player.update_one({"player_name": player_name},
                                              {'$set': {"player_name": form.player_name_new.data}})
        flash("Success, player's new name is: ")
        flash(form.player_name_new.data)
        flash(result_0.matched_count)
        flash(result_0.modified_count)
    return render_template('player_name_change.html', player_name=player_name,form=form)