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
        data, line_chart = None, None
        open_info = []
        high_info = []
        low_info = []
        close_info = []

        daysInDaily = []
        if sd > ed:
            flash('End Date cannot begin before start date')
            return redirect(url_for('index'))

        if timeSeries.lower() == "intraday":
            data = requests.get(f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=15min&apikey=' + av_key).json()
            # open_info.insert(0, float(data["Time Series (15min)"]["1. open"]))
            # high_info.insert(0, float(data["Time Series (15min)"]["2. high"]))
            # low_info.insert(0, float(data["Time Series (15min)"]["3. low"]))
            # close_info.insert(0, float(data["Time Series (15min)"]["4. close"]))
            # for d in data["Time Series (15min)"]:
            #     if startDate in d:
            #         chartDates = d
            #         # print(data["Time Series (15min)"])
            # if chartType == "bar":
            #     pass
            # elif chartType == "line":
            #     line_chart = pygal.line()
            #     line_chart.Line(legend_box_size=18, title=f'Stock Data for {symbol}: {startDate} to {endDate}')
            #     line_chart.x_labels = chartDates
            #     line_chart.add('Open', open_info)
            #     line_chart.add('High', high_info)
            #     line_chart.add('Low', low_info)
            #     line_chart.add('Close', close_info)
            #     line_chart.render_data_uri()

        elif timeSeries.lower() == "daily":
            data = requests.get(f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey=' + av_key).json()
            newStartDate = sd
            daysInDaily.append(newStartDate)
            for _ in range((ed - sd).days):
                newStartDate += datetime.timedelta(days=1)
                newStartDate.strftime('%Y/%m/%d')
                daysInDaily.append(newStartDate)
            c = 0
            for d in data["Time Series (Daily)"]:
                open_info.insert(d, float(data["Time Series (Daily)"][daysInDaily[c]]["1. open"]))
                high_info.insert(d, float(data["Time Series (Daily)"][daysInDaily[c]]["2. high"]))
                low_info.insert(d, float(data["Time Series (Daily)"][daysInDaily[c]]["3. low"]))
                close_info.insert(d, float(data["Time Series (Daily)"][daysInDaily[c]]["4. close"]))
                c += 1
            if chartType == "bar":
                pass
            elif chartType == "line":
                line_chart = pygal.line()
                line_chart.Line(legend_box_size=18, title=f'Stock Data for {symbol}: {startDate} to {endDate}')
                line_chart.x_labels = daysInDaily
                line_chart.add('Open', open_info)
                line_chart.add('High', high_info)
                line_chart.add('Low', low_info)
                line_chart.add('Close', close_info)
                line_chart.render_data_uri()
                pass
        elif timeSeries.lower() == "weekly":  
            data = requests.get(f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol={symbol}&apikey=' + av_key).json()
            open_info.insert(0, float(data["Time Series (Weekly)"][startDate]["1. open"]))
            high_info.insert(0, float(data["Time Series (Weekly)"][startDate]["2. high"]))
            low_info.insert(0, float(data["Time Series (Weekly)"][startDate]["3. low"]))
            close_info.insert(0, float(data["Time Series (Weekly)"][startDate]["4. close"]))
        elif timeSeries.lower() == "monthly":
            data = requests.get(f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol={symbol}&apikey=' + av_key).json()
            open_info.insert(0, float(data["Time Series (Monthly)"][startDate]["1. open"]))
            high_info.insert(0, float(data["Time Series (Monthly)"][startDate]["2. high"]))
            low_info.insert(0, float(data["Time Series (Monthly)"][startDate]["3. low"]))
            close_info.insert(0, float(data["Time Series (Monthly)"][startDate]["4. close"]))
        return render_template('index.html', sdata=read_file(), chart=line_chart, symbol=symbol, chartType=chartType, timeSeries=timeSeries, startDate=startDate, endDate=endDate)
    return render_template('index.html', sdata=read_file())

app.run(host="0.0.0.0")