from app import app
from flask import render_template, url_for, redirect, request
from models import *
import sqlite3


@app.route('/')
def index():
    return redirect(url_for('posts.index'), code=302)


@app.route('/index')
def index_():
    return redirect(url_for('posts.index'), code=302)


# Функция обратной связи
@app.route('/feedback', methods=['POST'])
def feedback():
    name = request.form['feedback_name']
    email = request.form['feedback_email']
    messages = request.form['feedback_message']

    if request.method == 'POST':
        try:
            feedback_message = Feedback(name=name, email=email, messages=messages)
            db.session.add(feedback_message)
            db.session.commit()
            print('Успешно')
        except:
            db.session.rollback()
            print('Ошибка добавления в БД')

    return redirect(url_for('posts.index'))


@app.route('/description')
def description():
    return render_template('description.html')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


# Отображение таблиц
@app.route('/allTable')
def allTable():
    con = sqlite3.connect('app.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute('select * from tablenso')
    rows = cur.fetchall()
    return render_template('allTable.html', rows=rows)


@app.route('/xozTable')
def xozTable():
    con = sqlite3.connect('app.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute('select * from xoz')
    rows = cur.fetchall()
    return render_template('xozTable.html', rows=rows)


@app.route('/aggregates')
def aggregates():
    con = sqlite3.connect('app.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute('select * from aggregates')
    rows = cur.fetchall()
    return render_template('aggregates.html', rows=rows)


@app.route('/bulkweight')
def bulkweight():
    con = sqlite3.connect('app.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute('select * from bulkweight')
    rows = cur.fetchall()
    return render_template('bulkweight.html', rows=rows)


@app.route('/deflation')
def deflation():
    con = sqlite3.connect('app.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute('select * from deflation')
    rows = cur.fetchall()
    return render_template('deflation.html', rows=rows)


@app.route('/erosion')
def erosion():
    con = sqlite3.connect('app.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute('select * from erosion')
    rows = cur.fetchall()
    return render_template('erosion.html', rows=rows)


@app.route('/granulometry')
def granulometry():
    con = sqlite3.connect('app.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute('select * from granulometry')
    rows = cur.fetchall()
    return render_template('granulometry.html', rows=rows)


@app.route('/humus')
def humus():
    con = sqlite3.connect('app.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute('select * from humus')
    rows = cur.fetchall()
    return render_template('humus.html', rows=rows)


@app.route('/moisture')
def moisture():
    con = sqlite3.connect('app.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute('select * from moisture')
    rows = cur.fetchall()
    return render_template('moisture.html', rows=rows)


@app.route('/pH')
def pH():
    con = sqlite3.connect('app.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute('select * from pH')
    rows = cur.fetchall()
    return render_template('pH.html', rows=rows)


@app.route('/phosphorus')
def phosphorus():
    con = sqlite3.connect('app.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute('select * from phosphorus')
    rows = cur.fetchall()
    return render_template('phosphorus.html', rows=rows)


@app.route('/potassium')
def potassium():
    con = sqlite3.connect('app.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute('select * from potassium')
    rows = cur.fetchall()
    return render_template('potassium.html', rows=rows)


@app.route('/power')
def power():
    con = sqlite3.connect('app.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute('select * from power')
    rows = cur.fetchall()
    return render_template('power.html', rows=rows)


@app.route('/salinization')
def salinization():
    con = sqlite3.connect('app.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute('select * from salinization')
    rows = cur.fetchall()
    return render_template('salinization.html', rows=rows)


@app.route('/solonetzes')
def solonetzes():
    con = sqlite3.connect('app.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute('select * from solonetzes')
    rows = cur.fetchall()
    return render_template('solonetzes.html', rows=rows)


@app.route('/water_resistant')
def water_resistant():
    con = sqlite3.connect('app.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute('select * from water_resistant')
    rows = cur.fetchall()
    return render_template('water_resistant.html', rows=rows)


@app.route('/maps')
def maps():
    return render_template('maps.html')


@app.route('/soil_description_nso')
def soil_description_nso():
    return render_template('soil_description_nso.html')


@app.route('/maps_xoz')
def maps_xoz():
    return render_template('maps_xoz.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
