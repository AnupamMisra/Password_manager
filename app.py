from flask import Flask, render_template, url_for, flash,redirect
from forms import RegistrationForm, LoginForm, Newcredentialssetup, Get_passwordform,reset_credsform,securityques
import backend


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'


@app.route("/register", methods=['GET', 'POST'])
def register():
    formx = RegistrationForm()
    if formx.validate_on_submit():
        flash(f'Account created for {formx.username.data}!', 'success')
    return render_template('register.html', title='Register', form=formx)

#DONE!!!
@app.route("/",methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if backend.check_pwd(form.password.data):
            flash('You have been logged in!', 'success')
            return redirect(url_for('console'))
        else:
            flash('Login Unsuccessful.', 'danger')
    return render_template('login.html', title='Login', form=form)

#DONE!!!
@app.route("/console")
def console():
    return render_template('console.html')


@app.route("/console/Newcredentials", methods=['GET', 'POST'])
def Newcredentials():
    form1 = Newcredentialssetup()
    if form1.validate_on_submit():
        backend.insert_pass(form1.website.data, form1.URL.data, form1.username.data, form1.pwd_choice.data, form1.p.data)
        #flash("Data entered","success")                #Doesn't work on time
        return redirect(url_for('console'))
    return render_template('Newcredentials.html', title='Newcredentials', form=form1)

@app.route("/console/Get_password", methods=['GET', 'POST'])
def Get_password():
    form2 = Get_passwordform()
    if form2.validate_on_submit():
        if backend.fetch_pass(form2.web.data)==1:
            #flash("tEXT COPIED?","success")                #Doesn't work on time
            return redirect(url_for('console'))
        elif backend.fetch_pass(form2.web.data)==2:    
            #flash("doesn't exist","danger")                #Doesn't work on time
            return redirect(url_for('console'))
    return render_template('Get_password.html', title='Get_password', form=form2)

@app.route("/console/Reset_credentials", methods=['GET', 'POST'])
def Reset_credentials():        
    form3 = reset_credsform()
    if form3.validate_on_submit():
        backend.update_pass(form3.answer.data,form3.website.data, form3.URL.data, form3.username.data, form3.pwd_choice.data, form3.p.data)
        #flash("Resetted","success")
        return redirect(url_for('console'))
    return render_template('Reset_credentials.html', title='Reset_credentials', form=form3)

@app.route("/forgot", methods=['GET', 'POST'])
def forgot():
    form5=securityques()
    if form5.validate_on_submit():
        backend.forgot_passwd(form5.answer.data, form5.p.data)
        return redirect(url_for('login'))
    return render_template('forgotpass.html', title='Forgot password', form=form5)


if __name__ == '__main__':
    app.run(host='127.0.0.1',debug=True)

