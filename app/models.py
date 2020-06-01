from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class NameChangeForm(FlaskForm):
    player_name_new = StringField('New Player Name', validators=[DataRequired()])
    submit = SubmitField("Submit")

#
# class Team():
#     team_name =
#
#     def __repr__(self):
#         return '<Team {}>'.format(self.teamname)
# #
# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     body = db.Column(db.String(140))
#     timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#
#     def __repr__(self):
#         return '<Post {}>'.format(self.body)

