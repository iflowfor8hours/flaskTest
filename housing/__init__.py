import os, csv, pymongo
from flask import Flask, render_template, request, redirect, url_for, send_from_directory,jsonify
from werkzeug import secure_filename
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__, static_url_path='')
app.config["MONGODB_SETTINGS"] = {'DB':"housing"}
app.config["SECRET_KEY"] = "littleBooahHousingDatabase"
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS']=set(['csv'])

db = MongoEngine(app)

def allowed_file(filename):
    return '.' in filename and \
      filename.rsplit('.',1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/',methods=['POST'])
def upload():
    file = request.files['file']
    
    selectValues = request.form.items(True)
    year = selectValues[1][1]
    month = selectValues[0][1]

    if file and allowed_file(file.filename):
      filename = secure_filename(file.filename)
      file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
      completionMessage = addToMongo(month,year,filename)

      return render_template('base.html', reloadVals = {'type':'Entry','msg':completionMessage})
    else:
      return render_template('base.html', reloadVals = {'type':'Entry','msg':'File Upload Failed'})

def addToMongo(month, year, filename):
	with open(os.path.join(app.config['UPLOAD_FOLDER'],filename), 'r') as fh:
	    data = [row for row in csv.reader(fh.read().splitlines())]
	if(data[0] == ['Nickname','PropID','Amount','Type','Due','Paid','Notes']):
		msg = parseBills(month, year, data)
	
	elif (data[0] == ['PropertyID','Nickname','Amount','DueDate','PaidDate']):
		msg = parseTaxes(month, year, data)
	
	elif (data[0] == ['Date','PropID','Nickname','Contractor','LaborCost','MaterialCost','Paid','Comments']):
		msg = parseMaint(month, year, data)

	elif (data[0] == ['PropID','Nickname','Unit','Tenant','Rent','Paid','Owes','DueDate','PaidDate','Comments']):
		msg = parseRent(month, year, data)
	else:
		msg = "FAILED"
	
	return msg

def parseBills(month, year, data):
	from housing.models import Bills;
	oldBills = Bills.objects.all()
	billList = ()
    #remove old bills from same month/year
	for bills in oldBills:
		if(bills.year == year and bills.month == month):
			billList.append(bills)
			bills.remove()
    
	#replace the old documents with the new ones
	try:
		for x in range(1,len(data)):
		    newBills = Bills(
			    year = year,
			    month = month,
			    nickname = data[x][0],
			    prop_id = data[x][1],
			    amount = data[x][2],
			    bill_type = data[x][3],
			    due_date = data[x][4],
			    paid = data[x][5],
			    comments = data[x][6]
		    )
		    newBills.save()
	except:
	    partials = Bills.objects.all()
	    #remove any documents that have been saved before exception
	    for bills in partials:
		    if(bills.year == year and bills.month == month):
		        bills.remove()
	    
	    for ob in billList:
	    	ob.save()
	    #TODO delete uploaded CSV file
	    return "Upload Failed, reverted back to old list"
	#TODO move CSV file to uploads/*year*/*month*/blah.timestamp
	return 'Updated Bills!'
def parseTaxes(month, year, data):
	return 'Made it to parseTaxes'
def parseMaint(month, year, data):
	return 'Made it to parseMaint'
def parseRent(month, year, data):
	return 'Made it to parseRent'

if __name__ == 'main':
	app.run()

def register_blueprints(app):
	from housing.views import pages
	
	app.register_blueprint(pages)

register_blueprints(app)