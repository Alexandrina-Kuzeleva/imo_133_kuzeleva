from datetime import datetime, timedelta
now = datetime.now()
averageman = 60.7
averagewoman = 67.5
bday = datetime(2005,6,24)
notice_interval = timedelta(days = averagewoman*365)
avdeath = bday + notice_interval
print(avdeath)
print(avdeath.strftime("%Y-%m-%d"))