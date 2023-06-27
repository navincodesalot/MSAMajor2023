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
        data, line_chart = None, None
        open_info = []
        high_info = []
        low_info = []
        close_info = []
        time_info = []

        if startDate > endDate:
            flash('End Date cannot begin before start date')
            return redirect(url_for('index'))

        if timeSeries.lower() == "intraday":
            data = requests.get(f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=15min&apikey=' + av_key).json()
            for d in data["Time Series (15min)"]:
                
                if d.split(" ")[0] >= startDate and d.split(" ")[0] <= endDate:
                    time_info.insert(0, d)
                    open_info.insert(0, float(data["Time Series (15min)"][d]["1. open"]))
                    high_info.insert(0, float(data["Time Series (15min)"][d]["2. high"]))
                    low_info.insert(0, float(data["Time Series (15min)"][d]["3. low"]))
                    close_info.insert(0, float(data["Time Series (15min)"][d]["4. close"]))
            if chartType == "bar":
                line_chart = pygal.Bar()
                line_chart.title = f'Stock Data for {symbol}: {startDate} to {endDate}'
                line_chart.x_labels = time_info
                line_chart.add('Open', open_info)
                line_chart.add('High', high_info)
                line_chart.add('Low', low_info)
                line_chart.add('Close', close_info)
                line_chart = line_chart.render_data_uri()
            elif chartType == "line":
                line_chart = pygal.Line()
                line_chart.title = f'Stock Data for {symbol}: {startDate} to {endDate}'
                line_chart.x_labels = time_info
                line_chart.add('Open', open_info)
                line_chart.add('High', high_info)
                line_chart.add('Low', low_info)
                line_chart.add('Close', close_info)
                line_chart = line_chart.render_data_uri()
        elif timeSeries.lower() == "daily":
            data = requests.get(f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey=' + av_key).json()
            for d in data["Time Series (Daily)"]:
                if d >= startDate and d <= endDate:
                    time_info.insert(0, d)
                    open_info.insert(0, float(data["Time Series (Daily)"][d]["1. open"]))
                    high_info.insert(0, float(data["Time Series (Daily)"][d]["2. high"]))
                    low_info.insert(0, float(data["Time Series (Daily)"][d]["3. low"]))
                    close_info.insert(0, float(data["Time Series (Daily)"][d]["4. close"]))
            if chartType == "bar":
                line_chart = pygal.Bar()
                line_chart.title = f'Stock Data for {symbol}: {startDate} to {endDate}'
                line_chart.x_labels = time_info
                line_chart.add('Open', open_info)
                line_chart.add('High', high_info)
                line_chart.add('Low', low_info)
                line_chart.add('Close', close_info)
                line_chart = line_chart.render_data_uri()
            elif chartType == "line":
                line_chart = pygal.Line()
                line_chart.title = f'Stock Data for {symbol}: {startDate} to {endDate}'
                line_chart.x_labels = time_info
                line_chart.add('Open', open_info)
                line_chart.add('High', high_info)
                line_chart.add('Low', low_info)
                line_chart.add('Close', close_info)
                line_chart = line_chart.render_data_uri()
                
        elif timeSeries.lower() == "weekly":  
            data = requests.get(f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol={symbol}&apikey=' + av_key).json()
            for d in data["Weekly Adjusted Time Series"]:
                if d >= startDate and d <= endDate:
                    time_info.insert(0, d)
                    open_info.insert(0, float(data["Weekly Adjusted Time Series"][d]["1. open"]))
                    high_info.insert(0, float(data["Weekly Adjusted Time Series"][d]["2. high"]))
                    low_info.insert(0, float(data["Weekly Adjusted Time Series"][d]["3. low"]))
                    close_info.insert(0, float(data["Weekly Adjusted Time Series"][d]["4. close"]))
            if chartType == "bar":
                line_chart = pygal.Bar()
                line_chart.title = f'Stock Data for {symbol}: {startDate} to {endDate}'
                line_chart.x_labels = time_info
                line_chart.add('Open', open_info)
                line_chart.add('High', high_info)
                line_chart.add('Low', low_info)
                line_chart.add('Close', close_info)
                line_chart = line_chart.render_data_uri()
            elif chartType == "line":
                line_chart = pygal.Line()
                line_chart.title = f'Stock Data for {symbol}: {startDate} to {endDate}'
                line_chart.x_labels = time_info
                line_chart.add('Open', open_info)
                line_chart.add('High', high_info)
                line_chart.add('Low', low_info)
                line_chart.add('Close', close_info)
                line_chart = line_chart.render_data_uri()
        elif timeSeries.lower() == "monthly":
            data = requests.get(f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol={symbol}&apikey=' + av_key).json()
            for d in data["Monthly Adjusted Time Series"]:
                if d >= startDate and d <= endDate:
                    time_info.insert(0, d)
                    open_info.insert(0, float(data["Monthly Adjusted Time Series"][d]["1. open"]))
                    high_info.insert(0, float(data["Monthly Adjusted Time Series"][d]["2. high"]))
                    low_info.insert(0, float(data["Monthly Adjusted Time Series"][d]["3. low"]))
                    close_info.insert(0, float(data["Monthly Adjusted Time Series"][d]["4. close"]))
            if chartType == "bar":
                line_chart = pygal.Bar()
                line_chart.title = f'Stock Data for {symbol}: {startDate} to {endDate}'
                line_chart.x_labels = time_info
                line_chart.add('Open', open_info)
                line_chart.add('High', high_info)
                line_chart.add('Low', low_info)
                line_chart.add('Close', close_info)
                line_chart = line_chart.render_data_uri()
            elif chartType == "line":
                line_chart = pygal.Line()
                line_chart.title = f'Stock Data for {symbol}: {startDate} to {endDate}'
                line_chart.x_labels = time_info
                line_chart.add('Open', open_info)
                line_chart.add('High', high_info)
                line_chart.add('Low', low_info)
                line_chart.add('Close', close_info)
                line_chart = line_chart.render_data_uri()
        return render_template('index.html', sdata=read_file(), chart=line_chart, symbol=symbol, chartType=chartType, timeSeries=timeSeries, startDate=startDate, endDate=endDate)
    return render_template('index.html', sdata=read_file())

app.run(host="0.0.0.0")