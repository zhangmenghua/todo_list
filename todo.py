#coding=utf-8
from flask import Flask, g, request, redirect, render_template,url_for
from pymongo import Connection
from bson.objectid import ObjectId

app=Flask(__name__)
app.debug=True

@app.before_request
def before_request():
	conn=Connection()
	g.db=conn.test

def get_lists():
	return g.db.list.find()

@app.route('/',methods=['POST','GET'])
def index():
	lit=get_lists()
	if request.method=='POST':
		if request.form['context']:
			con=request.form['context']
		 	g.db.list.insert({'context':con})
			return redirect(url_for('index'))
		else:
			return "不能为空"
	return render_template('todo.html',lists=lit)
@app.route('/delete/<idd>')
def delete(idd):
	g.db.list.remove({'_id':ObjectId(idd)})
	return redirect(url_for('index'))

if __name__=='__main__':
	app.run()