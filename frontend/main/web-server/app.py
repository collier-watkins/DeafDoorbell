from flask import Flask, render_template, url_for, flash
from forms import MessageForm
from wtforms.widgets import html_params, HTMLString


app = Flask(__name__)

app.config['SECRET_KEY'] = '3985723043u208uj23022039rue'

posts = [
	{
		'author': 'Jim Beam',
		'title': 'Blog Post 1',
		'content': 'first post content',
		'date_posted': 'April 20, 2018'
	},

	{
		'author': 'Joey James',
		'title': 'Blog Post 2',
		'content': 'second post content',
		'date_posted': 'April 21, 2018'
	}

]




#Home Page
@app.route("/", methods=['GET', 'POST'])	#Related to website locations
def homePage():	#Returns data for the main home page, should be HTML data
	form = MessageForm()
	if form.validate_on_submit():
		flash(f'Message sent!', 'success')
	return render_template('home.html', posts=posts, title='Blog Posts', form=form)


#About Page
@app.route("/about")	
def aboutPage():
	return "<h1>About Page</h1>"









#Run Flask Application
if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=80)