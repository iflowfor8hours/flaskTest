from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView
from flask.ext.mongoengine.wtf import model_form
from housing.models import Rent, Maintenance, Taxes, Bills

pages = Blueprint('pages', __name__, template_folder='templates')

'''
HTML Components Found in Templates
  Header
  Footer
  Graph
  UI (Base) {Interaction + Add Query, etc Buttons}
  Comments
'''
'''
python classes to describe each view
  We will add these as we go, for now just one type
'''
class BaseView(MethodView):
	def get(self):
		return render_template('base.html')

class MaintenanceView(MethodView):
	def get(self):
		return render_template('maintenance.html')

pages.add_url_rule('/',view_func=BaseView.as_view('pages'))
pages.add_url_rule('/maintenance/',view_func=MaintenanceView.as_view('maintenance'))