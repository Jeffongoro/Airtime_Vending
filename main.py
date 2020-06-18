from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/home")
def home():
    return render_template("index.html")

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      phone_number = result['phone_number']
      amount =  result['amount']
      top_up(phone_number, amount)
      return render_template("result.html",result = result)

def top_up(phone_number,amount):
    import africastalking
    #Define credentials here
    username = ""
    api_key = ""


    #Authenticate with the service
    africastalking.initialize(username, api_key)

    #Define the airtime service
    airtime = africastalking.Airtime 

    #Define user variables
    phone_number = "phone_number"
    amount = "amount"
    currency_code = "KES"

    #Send the airtime!
    response = airtime.send(phone_number = phone_number, amount = amount, currency_code = currency_code)
    print(response)


if __name__ == "__main__":
    app.run(debug=True)