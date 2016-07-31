"""
Sample Controller File

"""
from system.core.controller import *

class Blanks(Controller):
	def __init__(self, action):
		super(Blanks, self).__init__(action)

		self.load_model('WelcomeModel')
		self.db = self._app.db

	def index(self):
		return self.load_view('index.html')

	def place_search(self):
		print "GOT HERE"
		lng = request.form['lng']
		lat = request.form['lat']
		
		what = request.form['what']
		url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location="+lat+","+lng+"&radius=10000&keyword="+what+"&key=AIzaSyBLgLT2H_qbHsAKH6L6Da_aLyz-aRGG34U"
		print url
		response = requests.get(url).content
		return response


