from flask import Flask
from services import TravelEventService

app = Flask(__name__)


@app.route('/')
def status():
    return 'Status Ok!'


@app.route('/travel-event')
def travel_event():
    service = TravelEventService()
    data = service.get_travel_event()
    return data.title


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
