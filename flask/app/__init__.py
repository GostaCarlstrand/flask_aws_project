from flask import Flask, render_template, request, Response
from app.dynamo_access import get_all_readings
import json

app = Flask(__name__)

alarm_activated = []
alarm_state = False


# Not always correct value on alarm_state
#
#
#
#


@app.post('/alarm_activate')
def activate_alarm():
    activate_msg = '{"Alarm":"Activated"}'
    deactivate_msg = '{"Alarm":"Deactivated"}'
    global alarm_state
    if not alarm_state:
        alarm_state = True
        print("sant")
        return Response(activate_msg, 200, content_type="application/json")
    if alarm_state:
        alarm_state = False
        print("falskt")
        return Response(deactivate_msg, 200, content_type="application/json")


@app.get('/')
def index():
    readings = get_all_readings()
    return render_template('index.html', readings=readings, alarm=alarm_state)


@app.post('/api/v1.0/alarm')
def incoming_alarm():
    data = request.json
    print(type(data))
    alarm_activated.append(data)
    print(type(alarm_activated))
    return Response('"Status":"Succeeded"', 200, content_type="application/json")


@app.get('/api/v1.0/alarm')
def get_alarm_client():
    return Response(json.dumps(alarm_activated), 200, content_type='application/json')
