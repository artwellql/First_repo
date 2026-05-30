from datetime import datetime 

def get_days_from_today(date):

    user_date = datetime.strptime(date, "%Y-%m-%d")
    today = datetime.today()
    delta = today.date() - user_date.date()

    return delta.days
