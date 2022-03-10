from flask import Flask, render_template, request, Response
from app.dynamo_access import get_all_readings
import json

app = Flask(__name__)

alarm_activated = []
alarm_state = False


@app.post('/alarm_activate')
def activate_alarm():
    activate_msg = '{"Alarm":"Activated"}'
    deactivate_msg = '{"Alarm":"Deactivated"}'
    global alarm_state
    if not alarm_state:
        alarm_state = True
        return Response(activate_msg, 200, content_type="application/json")
    if alarm_state:
        alarm_state = False
        return Response(deactivate_msg, 200, content_type="application/json")


@app.get('/')
def index():
    readings = get_all_readings()
    print()
    positions = []
    datatime = []
    device = []
    for reading in readings:
        positions.append(reading['pos'])
        datatime.append(reading['datatime'])
        device.append(reading['device'])

    return render_template('index.html', readings=readings, alarm=alarm_state)


@app.post('/api/v1.0/alarm')
def incoming_alarm():
    data = request.json
    print(type(data))
    alarm_activated.append(data)
    print(type(alarm_activated))
    return Response('"Status":"Succeeded"', 200, content_type="application/json")


@app.get('/clear_history')
def clear_history_entries():
    alarm_activated.clear()
    return Response('"Status":"HistoryDeleted"', 200, content_type="application/json")


@app.get('/api/v1.0/alarm')
def get_alarm_client():
    if alarm_state and alarm_activated:
        return Response("'Status':'Deactivated'", 200, content_type='application/json')
    else:
        return Response(json.dumps(alarm_activated), 200, content_type='application/json')
