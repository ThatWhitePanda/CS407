from app.helpers import pretty_date
from datetime import datetime, timedelta

def test_now():
	assert pretty_date(datetime.utcnow()) == "just now"

def test_second():
	assert pretty_date(datetime.utcnow() - timedelta(seconds=59)) == "59 seconds ago"

def test_minute():
	assert pretty_date(datetime.utcnow() - timedelta(seconds=119)) == "a minute ago"

def test_minutes():
	assert pretty_date(datetime.utcnow() - timedelta(seconds=120)) == "2 minutes ago"

def test_hour():
	assert pretty_date(datetime.utcnow() - timedelta(seconds=7199)) == "an hour ago"

def test_hours():
	assert pretty_date(datetime.utcnow() - timedelta(seconds=10800)) == "3 hours ago"

def test_aboutNow():
	assert pretty_date(datetime.utcnow() - timedelta(days=-1)) == "just about now"	

def test_yesterday():
	assert pretty_date(datetime.utcnow() - timedelta(days=1)) == "Yesterday"

def test_days():
	assert pretty_date(datetime.utcnow() - timedelta(days=3)) == "3 days ago"

def test_weeks():
	assert pretty_date(datetime.utcnow() - timedelta(weeks=2)) == "2 weeks ago"

def test_month():
	assert pretty_date(datetime.utcnow() - timedelta(days=90)) == "3 months ago"

def test_years():
	assert pretty_date(datetime.utcnow() - timedelta(days=365*2)) == "2 years ago"


