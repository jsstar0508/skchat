# -*- coding: utf-8 -*-
"""
   Put your passwords in ENV variables
      ('skype_user', 'user')
      ('skype_pass', 'pass')

   pip install py38.txt
   pip install fire

   ######## Start
   python server.py run_server  --port 12345

   python server.py test



"""
from flask import Flask, request
import fire, os
from getpass import getpass
from skpy import SkypeEventLoop


########################################################################3########
global user1, pass1, bingchat, sk, app
user1= os.environ.get('skype_user', 'user')
pass1= os.environ.get('skype_pass', 'pass')
basid= os.environ.get('skype_chatid', 'someid')


################################################################################
def test():
    chatid="" 
	sk = Skype(user1, pass1) # connect to Skype
	ch = sk.chats[chatid]
	txt= "ok"
	ch.sendMsg(txt) # plain-text message
	time.sleep(8)
	mlist= ch.getMsgs() # retrieve recent message
	m0 = mlist[0].markup
	print(m0)





##############################################################################
app = Flask(__name__)


@app.route('/sendmsg', methods=['POST'])
def send_message_chatid(chatid=None):
    """
    method query = POST

    Receives a json via http/https with the message text 
    (the `text` field) and who to send it to with the 
    `recipient` field
    """
    try:
        data = request.json
        text = data.get('text')
        recipient = data.get('recipient')
        # Send message
        ch = sk.contacts[recipient].chat
        ch.sendMsg(text)
        return 1
    except  Exception as e:
        print(e)
        return -1 


@app.route('/getmsg', methods=['GET'])
def get_messages_chatid(chatid=None):
    """
    """
    try:
        chatid = baseid if chatid is None else chatid  
        chat0= sk.chats[chatid]
        messages = []
        # Get recent chats and their messages
        for chat in chat0:
            msglist= chat.getMsgs()
        return msglist

    except  Exception as e:
        print(e)
        return -1 


def run_server(port=12354):
    skype_init() 
    app.run(port=port)


#######################################################################################

def run_loop_event()
    sk = MySkype(user, pass1, autoAck=True)
    sk.subscribePresence() # Only if you need contact presence events.
    print('start')
    sk.loop()

#######################################################################################
########## utils ######################################################################
class MySkype(SkypeEventLoop):
    def onEvent(self, event):
        print(repr(event))


def skype_init():
   # Initialize Skype object with your credentials
   global sk 
   sk = Skype(user1, pass1)





#######################################################################################
if __name__ == '__main__':
    fire.Fire()



