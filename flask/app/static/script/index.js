let alarmText;
let alarmState;
const api_url = "http://13.48.57.227/api/v1.0/alarm"
const local_api = "http://127.0.0.1"
const http_url = "http://127.0.0.1:5000"
setInterval(getAlarm, 2000)
setInterval(clearAlarmHistory, 15000)
function activateAlarm(){
        const xhttp = new XMLHttpRequest();
        xhttp.onload = function () {
            alarmState = JSON.parse(this.responseText);
            let button = document.getElementById("alarm_button")
            console.log(button)
            if (alarmState.Alarm === "Activated") {
                document.getElementById("alarm_button").innerHTML = "Deactivate alarm"
                document.getElementById("alarm_button").classList.remove('buttonGreen');
                document.getElementById("alarm_button").classList.add('buttonRed');

            }
            else {
                document.getElementById("alarm_button").innerHTML = "Activate alarm"
                document.getElementById("alarm_button").classList.remove('buttonRed');
                document.getElementById("alarm_button").classList.add('buttonGreen');
            }
            console.log(JSON.stringify((alarmState)))
            //document.getElementById("alarmState").innerText = alarmState.Alarm

        }

        //xhttp.open('POST', (local_api + "/alarm_activate"))
        xhttp.open('POST', (local_api + "/alarm_activate"))
        xhttp.send()

    }
function getAlarm() {
        const xhttp = new XMLHttpRequest();
        xhttp.onload = function () {
            alarmText = this.responseText;
            if (alarmText === "'Status':'Deactivated'") {
                console.log("Alarm is deactivated")
            }
            else {
                console.log(alarmText)
                document.getElementById("alarm").innerText = alarmText
            }
        }


        xhttp.open('GET', (local_api + "/api/v1.0/alarm"))
        xhttp.send()
    }
function clearAlarmHistory() {
    const xhttp = new XMLHttpRequest();
    xhttp.onload = function () {
        const serverResponse = this.responseText;
        console.log(serverResponse)
    }

    xhttp.open('GET', (local_api + "/clear_history"))
    xhttp.send()
}