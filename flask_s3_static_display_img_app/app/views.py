from app import app
from flask import Flask, render_template, redirect
import boto3
from datetime import datetime
from dateutil import tz

S3_BUCKET='myflaskassets'

@app.route('/homersimpson')
def homersimpson():
    s3=boto3.client('s3')
    url = s3.generate_presigned_url('get_object', Params = {'Bucket': S3_BUCKET, 'Key': 'simpson.png'}, ExpiresIn = 100)
    return redirect(url, code=302)

@app.route('/covilha')
def covilha():
    from_zone = tz.gettz('UTC')
    to_zone = tz.gettz('Europe/Lisbon')
    utc = datetime.utcnow()
    utc = utc.replace(tzinfo=from_zone)
    Lisbon_time = utc.astimezone(to_zone)
    lisstr= Lisbon_time.strftime("%H:%M:%S")
    return render_template('covilha.html', lisstr=lisstr)

@app.route('/')
def home():
    return "flask app test"

