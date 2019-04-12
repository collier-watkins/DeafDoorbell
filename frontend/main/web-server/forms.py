from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class MessageForm(FlaskForm):
	LCDMessage = TextAreaField('LCDMessage',
							validators=[DataRequired(), Length(min=1,max=32)])

	submit = SubmitField('Send')

