
from models import User, Record

users = []
records = []

uid = 1
rid = 1

def create_user(user: User):
    global uid
    user.id = uid
    uid += 1
    users.append(user)
    return user

def get_user(id):
    for u in users:
        if u.id == id:
            return u

def add_record(record: Record):
    global rid
    record.id = rid
    rid += 1
    records.append(record)
    return record

def get_records():
    return records

def get_summary():
    income = sum(r.amount for r in records if r.type.strip().lower()=="income")
    expense = sum(r.amount for r in records if r.type.strip().lower()=="expense")

    return {
        "total_income": income,
        "total_expense": expense,
        "balance": income-expense
    }

def get_category_summary():
    data={}
    for r in records:
        data[r.category]=data.get(r.category,0)+r.amount
    return data

def get_trends():
    trends={}
    for r in records:
        month=r.date[:7]
        trends[month]=trends.get(month,0)+r.amount
    return trends


