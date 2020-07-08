from flask import Flask, url_for, render_template, session, request, redirect
import time
app = Flask(__name__)
import user_module
import globals
import gpio_led
import camera_controller
MOST_RECENT_CAPTURE = ""
CAPTURE_INTERVAL = 10 #30 SECONDS
#class contect setup / init?

app.config['SECRET_KEY'] = globals.SECRET_KEY_DEV

@app.route('/')
def index():
    if 'username' in session:
        gpio_led.blue()
        return render_template('index.html', greeting='RasPI Dashboard', username=session['username'])
    else:
        gpio_led.red()
        return render_template('login.html', error_info="You must be logged-in to view this page! Please log in then try again", err_info='info')


#login route
@app.route("/login", methods=["GET", "POST"])
def login():
    if 'username' in session:
        gpio_led.blue()
        return redirect("/", code=302)
    else:
        gpio_led.green()
        if request.method == "GET":
            return render_template('login.html')
        else: 
            form_password = request.form['password']
            form_username = request.form['username']
            valid_user = user_module.check_credientials(form_password, form_username) # check data against server secret

            if valid_user == True:
                session['username'] = form_username
                session['admin'] = True
                return redirect("/", code=302)
            else:
                gpio_led.red()
                return render_template('login.html', error="Incorrect user information was entered! Please enter the information correctly.")


@app.route("/logout", methods=['GET', 'POST'])
def logout():
    session.pop('username', None)
    gpio_led.red()
    return redirect("/login", code=302)



@app.route("/camera", methods=['GET', 'POST'])
def camera ():
    if 'username' in session:
        gpio_led.blue()
        if request.method == "GET":
            file_name = camera_controller.take_still(globals.PHOTOS_FOLDER)
            return render_template('camera.html', file_name = file_name)
            
        else:
            file_name = camera_controller.take_still(globals.PHOTOS_FOLDER)
            return render_template('camera.html', error_info="Your photo was taken", err_info='info', file_name = file_name)
    
    else:
        gpio_led.red()
        return render_template('login.html', error_info="You must be logged-in to view this page! Please log in then try again", err_info='info')
        



