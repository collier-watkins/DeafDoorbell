from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length
from wtforms.widgets import html_params, HTMLString

class ButtonWidget(object):
    """
    Renders a multi-line text area.
    `rows` and `cols` ought to be passed as keyword args when rendering.
    """
    input_type = 'submit'

    html_params = staticmethod(html_params)

    def __call__(self, field, **kwargs):
        kwargs.setdefault('id', field.id)
        kwargs.setdefault('type', self.input_type)
        if 'value' not in kwargs:
            kwargs['value'] = field._value()

        return HTMLString('<button {params}>{label}</button>'.format(
            params=self.html_params(name=field.name, **kwargs),
            label=field.label.text)
        )

class ButtonField(StringField):
    widget = ButtonWidget()

class MessageForm(FlaskForm):
	LCDMessage = TextAreaField('LCDMessage',
							validators=[DataRequired(), Length(min=1,max=32)])

	client1 = ButtonField('Joy\'s Bedroom') 
	client2 = ButtonField('Upstairs Bathroon')

	submit = SubmitField('Send')

