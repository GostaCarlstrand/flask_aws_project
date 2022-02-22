from flask import Flask, render_template, request, Response
from app.dynamo_access import get_all_readings

app = Flask(__name__)

alarm_activated = []

@app.get('/')
def index():
    readings = get_all_readings()
    return render_template('index.html', readings=readings)


@app.post('/api/v1.0/alarm')
def incoming_alarm():
    data = request.json
    alarm_activated.append(data)
    return Response('"Status":"Succeeded"', 200, content_type="application/json")

