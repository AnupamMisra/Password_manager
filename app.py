from flask import Flask, render_template, url_for, flash,redirect
from forms import RegistrationForm, LoginForm, Newcredentialssetup, Get_passwordform,reset_credsform,securityques
from secure import SecureHeaders
import backend
#import pyperclip as pc
import hashlib
from flask_httpauth import HTTPBasicAuth
from flask_sslify import SSLify
sc=SecureHeaders(csp=True, hsts=True,xfo='Deny')
auth = HTTPBasicAuth()

app = Flask(__name__)
app.secret_key="1234"
sslify = SSLify(app)

@app.after_request
def set_secure_headers(response):
    sc.flask(response)
    return response

@auth.verify_password
def f(a,b):
    us=hashlib.sha224(a.encode()).hexdigest()
    p=hashlib.sha224(b.encode()).hexdigest()

    if backend.check_user(us,p): 
        return True
    else: return False    


@app.route("/register", methods=['GET', 'POST'])
def register():
    formx = RegistrationForm()
    if formx.validate_on_submit():
        flash(f'Account created for {formx.username.data}!', 'success')
    return render_template('register.html', title='Register', form=formx)

#DONE!!!
@app.route("/",methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
@auth.login_required
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if backend.check_pwd(form.password.data):
            return redirect(url_for('console'))    
    return render_template('login.html', title='Login', form=form)

#DONE!!!
@app.route("/console")
@auth.login_required
def console():
    return render_template('console.html')


@app.route("/console/Newcredentials", methods=['GET', 'POST'])
@auth.login_required
def Newcredentials():
    form1 = Newcredentialssetup()
    if form1.validate_on_submit():
        p = backend.insert_pass(form1.website.data, form1.URL.data, form1.username.data, form1.pwd_choice.data, form1.p.data)
        flash(p,"success")                #Doesn't work on time
        return redirect(url_for('Newcredentials'))
    return render_template('Newcredentials.html', title='Newcredentials', form=form1)

@app.route("/console/Get_password", methods=['GET', 'POST'])
@auth.login_required
def Get_password():
    form2 = Get_passwordform()
    if form2.validate_on_submit():
        aa,passs=backend.fetch_pass(form2.web.data)
        if aa==1:
            print(passs)
            #pc.copy(passs)
            flash(passs,"success")                #Doesn't work on time
            return redirect(url_for('Get_password'))
        elif aa==2:    
            flash("Doesn't exist","danger")                #Doesn't work on time
            return redirect(url_for('Get_password'))
    return render_template('Get_password.html', title='Get_password', form=form2)

@app.route("/console/Reset_credentials", methods=['GET', 'POST'])
@auth.login_required
def Reset_credentials():        
    form3 = reset_credsform()

    #Call OTP generation function

    if form3.validate_on_submit():        
        jh=backend.update_pass(form3.answer.data,form3.otp.data,form3.website.data, form3.URL.data, form3.username.data, form3.pwd_choice.data, form3.p.data)
        if jh==1:
            flash("Resetted","success")
        elif jh==0:
            flash("Doesn't exist","danger")
        return redirect(url_for('Reset_credentials'))
    return render_template('Reset_credentials.html', title='Reset_credentials', form=form3)

@app.route("/forgot", methods=['GET', 'POST'])
@auth.login_required
def forgot():
    form5=securityques()
    
    #Call OTP generation function

    if form5.validate_on_submit():
        backend.forgot_passwd(form5.answer.data, form5.otp.data, form5.p.data)
        return redirect(url_for('login'))
    return render_template('forgotpass.html', title='Forgot password', form=form5)

if __name__ == '__main__':
    app.run(host='127.0.0.1',debug=False)
    us=""
    p=""

