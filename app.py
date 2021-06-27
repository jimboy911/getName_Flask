from flask import Flask,render_template,request
app = Flask(__name__)
@app.route('/form-example', methods=['GET', 'POST'])
def form_example():
   # handle the POST request
   if request.method == 'POST':
       yourName = request.form.get('yourName')
       return render_template("name.html", yourName = yourName)
 
   # otherwise handle the GET request
   else:
       return render_template("nameGet.html")
