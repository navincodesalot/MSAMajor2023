import csv, datetime, requests, pygal
from flask import Flask, render_template, request, url_for, flash, redirect, abort

app = Flask(__name__)
app.config["DEBUG"] = True
app.config['SECRET_KEY'] = 'your secret key'

av_key = "HBO16J3B7IVBFJKQ"

def read_file():
    with open('stocks.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        return [row[0] for row in csv_reader]

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        symbol = request.form.get("symbol")
        chartType = request.form.get("chart")
        timeSeries = request.form.get("time")
        startDate = (request.form.get("start_date"))
        endDate = (request.form.get("end_date"))
        sd = startDate.split("-")
        ed = endDate.split("-")
        sd = datetime.date(int(sd[0]), int(sd[1]), int(sd[2]))
        ed = datetime.date(int(ed[0]), int(ed[1]), int(ed[2]))
        data = None

        if sd > ed:
            flash('End Date cannot begin before start date')
            return redirect(url_for('index'))

        if timeSeries.lower() == "intraday":
            data = requests.get(f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=15min&apikey=' + av_key)
            for d in data:
                print(d)
        elif timeSeries.lower() == "daily":
            data = requests.get(f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey=' + av_key)
        elif timeSeries.lower() == "weekly":  
            data = requests.get(f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol={symbol}&apikey=' + av_key)
        elif timeSeries.lower() == "monthly":
            data = requests.get(f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol={symbol}&apikey=' + av_key)

        print(data.json())
        return render_template('index.html', sdata=read_file(), chart=data, symbol=symbol, chartType=chartType, timeSeries=timeSeries, startDate=startDate, endDate=endDate)
    return render_template('index.html', sdata=read_file())

app.run(host="0.0.0.0")