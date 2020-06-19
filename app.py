from flask import Flask,render_template,request
import requests


api_key = "b9aabc2ced9bb9226f4b7ea5493d0f8f"
url="http://data.fixer.io/api/latest?access_key=" + api_key


app=Flask(__name__)
@app.route("/",methods=["GET","POST"])
def index():
    if request.method =="POST":
        firstCurrency = request.form.get("firstCurrency") #usd
        secondCurrency=request.form.get("secondCurrency") #euro

        amount = request.form.get("amount") #15
        response = requests.get(url)

        infos = response.json()

        firstValue = infos["rates"][firstCurrency] #1.090277
        secondValue = infos["rates"][secondCurrency] #7.681871


        result = (secondValue /firstValue)*float(amount) # 1 dolar kac try

        currencyInfo=dict()

        currencyInfo["firstCurrency"]=firstCurrency
        currencyInfo["secondCurrency"]=secondCurrency
        currencyInfo["amount"]=amount
        currencyInfo["result"]=result
        return render_template("index.html",info=currencyInfo)


    else:
        return render_template("index.html")

 
if __name__ =="__main__":
    app.run(debug=True)