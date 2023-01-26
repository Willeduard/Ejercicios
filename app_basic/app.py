from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
   if request.method=='POST':
      # Handle POST Request here
      return render_template('index.html')
   return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Recolectar datos del formulario
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        # Validar datos y guardarlos en la base de datos
        # ...

        return redirect(url_for('home'))

    return render_template('register.html')

if __name__ == '__main__':
   #DEBUG is SET to TRUE. CHANGE FOR PROD
   app.run(port=5000,debug=True)