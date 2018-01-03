import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine


API_TOKEN = '529140540:AAG2MAQY99taAjOPj0hSYLMd7nW9MjtaCpE'
WEBHOOK_URL = 'https://d9d5e6d9.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
        'user',
        'state1',
        'state2',
	'state3',
	'state4',
	'statedoge1',
	'statedoge2',
	'statedoge3',
	'statedoge4',
	'statedogehelp',
	'statehelp',
	'staterest'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state1',
            'conditions': 'hello'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state2',
            'conditions': 'nice_to_meet_you'
        },
	{	
            'trigger': 'advance',
	    'source': 'user',
	    'dest': 'state3',
	    'conditions': 'bye'
	},
	{
	    'trigger': 'advance',
	    'source': 'user',
	    'dest': 'state4',
	    'conditions': 'doge_mode'
	},
	{
	    'trigger': 'advance',
	    'source': 'user',
	    'dest': 'statehelp',
	    'conditions': 'help'
	},
	{
	    'trigger': 'advance',
	    'source': 'state4',
	    'dest': 'statedoge1',
	    'conditions': 'hello'
	},
	{
	    'trigger': 'advance',
	    'source': 'state4',
	    'dest': 'statedoge2',
	    'conditions': 'nice_to_meet_you'
	},
	{
	    'trigger': 'advance',
	    'source': 'state4',
	    'dest': 'statedoge3',
	    'conditions': 'bye'
	},
	{
	    'trigger': 'advance',
	    'source': 'state4',
	    'dest': 'statedoge4',
	    'conditions': 'turn_on_the_light'
	},
	{
	    'trigger': 'advance',
	    'source': 'state4',
	    'dest': 'statedogehelp',
	    'conditions': 'help'
	},
        {
            'trigger': 'go_back',
            'source': [
                'state1',
                'state2',
		'state3',
		'state4',
		'statehelp',
		'statedoge3'
            ],
            'dest': 'user'
        },
	{
	    'trigger': 'go_back',
	    'source': [
		'statedoge1',
		'statedoge2',
		'statedoge4',
		'statedogehelp'
	    ],
	    'dest': 'state4'
	}
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
	update = telegram.Update.de_json(request.get_json(force=True), bot)
	machine.advance(update)
	return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
	byte_io = BytesIO()
	machine.graph.draw(byte_io, prog='dot', format='png')
	byte_io.seek(0)
	return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__":
    _set_webhook()
    app.run()

