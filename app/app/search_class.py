from flask_wtf import FlaskForm 
from wtforms import StringField 
from wtforms.validators import DataRequired, Length 


class Search(FlaskForm): 
    state = StringField('state',
                        validators=[DataRequired(), 
                        Length(min=2,max=2)])


   