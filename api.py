from flask import Flask
from services import TravelEventService

app = Flask(__name__)


@app.route('/')
def status():
    return 'Status Ok!'


@app.route('/travel-event')
def travel_event():
    service = TravelEventService()
    response_data = service.get_travel_events()
    return {
        'morning': {
            'title': response_data['morning'].title,
            'description': response_data['morning'].description
        },
        'afternoon': {
            'title': response_data['afternoon'].title,
            'description': response_data['afternoon'].description
        },
        'night': {
            'title': response_data['night'].title,
            'description': response_data['night'].description
        }
    }


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
