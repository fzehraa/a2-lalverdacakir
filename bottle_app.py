
#####################################################################
### Assignment skeleton
### You can alter the below code to make your own dynamic website.
### The landing page for assignment 3 should be at /
#####################################################################

from bottle import Bottle, debug,route,default_app,run,request,template,static_file,TEMPLATE_PATH
from hashlib import sha256

TEMPLATE_PATH.insert(0,'./page')

@route('/static/<filename:path>')
def css(filename):
    return static_file(filename, root='static/')

app= Bottle()


#for pages

def index():
    return template('index')

route('/','GET',hello)
#####################################################################
### Don't alter the below code.
### It allows this website to be hosted on Heroku
### OR run on your computer.
#####################################################################

# This line makes bottle give nicer error messages
debug(True)
# This line is necessary for running on Heroku
app = default_app()
# The below code is necessary for running this bottle app standalone on your computer.
if __name__ == "__main__":
  run()

