
import requests
import json
from flask import Flask
from flask_table import Table, Col

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        items = []
        class ItemTable(Table):
            name = Col("Pair")
            rate = Col("Rate")
            inverse = Col("Inverse")

        class Item(object):
            def __init__(self, name, rate, inverse):
                self.name = name
                self.rate = rate
                self.inverse = inverse


        response = requests.get('http://api.vexchange.io/v1/pairs').json()
        printString = ""

        for x in response:
            token0 = response[x]['token0']['symbol']
            token1 = response[x]['token1']['symbol']
            price = response[x]['price']
            printString = printString + token0 + "/" + token1 + " - " + str(price) + "<br>"
            items.append(Item(token0 + "/" + token1,str(price),str(1/float(price))))
        table = ItemTable(items)
        disclaimer = "Simple data pull using the Vexchange API found <a href='http://api.vexchange.io/static/index.html#/'>here</a> <br> <a href='https://github.com/FarzanAkhtar1/VexchangeData'>GitHub repo</a>  <br> My <a href='https://twitter.com/FarzanAkhtar1'>Twitter</a>  <br><br><h1>Vexchange Pair Information</h1>"


        tablehtml = (table.__html__()).replace("<table>",'<table class="center">')
        tablehtml = disclaimer + tablehtml
        return tablehtml
        return printString
    except Exception as e:
        return e