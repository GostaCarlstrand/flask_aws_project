from flask import Flask, render_template, request, Response
from app.dynamo_access import get_all_readings
import json

app = Flask(__name__)

alarm_activated = []

@app.get('/')
def index():
    readings = get_all_readings()
    return render_template('index.html', readings=readings)


@app.post('/api/v1.0/alarm')
def incoming_alarm():
    data = request.json
    print(type(data))
    alarm_activated.append(data)
    print(type(alarm_activated))
    return Response('"Status":"Succeeded"', 200, content_type="application/json")


@app.get('/api/v1.0/alarm')
def get_alarm_client():
    print("Jag har lyckats skicka post request")
    return Response(json.dumps(alarm_activated), 200, content_type='application/json')
