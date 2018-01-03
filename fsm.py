
from transitions.extensions import GraphMachine


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def hello(self, update):
        text = update.message.text
        return text.lower() == 'hello'

    def nice_to_meet_you(self, update):
        text = update.message.text
        return text.lower() == 'nice to meet you'
    
    def bye(self, update):
        text = update.message.text
        return text.lower() == 'bye'

    def doge_mode(self, update):
	text = update.message.text
	return text.lower() == 'doge mode'

    def help(self, update):
	text = update.message.text
	return text.lower() == 'help'

    def turn_on_the_light(self, update):
	text = update.message.text
	return text.lower() =='turn on the light'

    def on_enter_state1(self, update):
        update.message.reply_text("hi")
        self.go_back(update)
    def on_exit_state1(self, update):
        print('Leaving state1')

    def on_enter_state2(self, update):
        update.message.reply_text("nice to meet you too")
        self.go_back(update)

    def on_exit_state2(self, update):
        print('Leaving state2')

    def on_enter_state3(self, update):
        update.message.reply_text("bye bye")
        self.go_back(update)

    def on_exit_state3(self, update):
        print('Leaving state3')

    def on_exit_state4(self, update):
	print('Leaving state4')
	
    def on_enter_statehelp(self, update):
	update.message.reply_text("1.hello")
	update.message.reply_text("2.nice to meet you")
	update.message.reply_text("3.bye")
	update.message.reply_text("4.doge mode")
	self.go_back(update)
    def on_exit_statehelp(self, update):
	print('Leaving statehelp')

    def on_enter_statedoge1(self, update):
	update.message.reply_photo("https://imgur.com/gallery/ZKdLhzG")
	update.message.reply_text("anyone call me?")
	self.go_back(update)
    def on_exit_statedoge1(slef, update):
	print('Leaving statedoge1')
  
    def on_enter_statedoge2(self, update):
	update.message.reply_photo("https://imgur.com/gallery/WuNog")
	update.message.reply_text("don't touch me boo")
	self.go_back(update)
    def on_exit_statedoge2(self, update):
	print('Leaving statedoge2')

    def on_enter_statedoge3(self, update):
	update.message.reply_photo("https://imgur.com/gallery/FFm9wGR")
	update.message.reply_text("doge will miss you boo")
	self.go_back(update)
    def on_exit_statedoge3(self, update):
	print('Leaving statedoge3')

    def on_enter_statedoge4(self, update):
	update.message.reply_photo("https://imgur.com/gallery/3lwGX")
	update.message.reply_text("enough?")
	self.go_back(update)
    def on_exit_statedoge4(self, update):
	print('Leaving statedoge4')

    def on_enter_statedogehelp(self, update):
	update.message.reply_text("1.hello")
	update.message.reply_text("2.nice to meet you")
	update.message.reply_text("3.turn on the light")
	update.message.reply_text("4.bye")
	self.go_back(update)
    def on_exit_statedogehelp(self, update):
	print('Leaving statedogehelp')
