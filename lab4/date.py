from datetime import datetime, timedelta

print("-----------1-----------")
today = datetime.now()
new_date = today - timedelta(days = 5 )
print(new_date)


print("\n-----------2-----------")
yesterday = datetime.strftime(today - timedelta(days = 1), "%x")
today2 = datetime.strftime(today, "%x")
tomorrow = datetime.strftime(today + timedelta(days = 1), "%x")
print("Yesterday:", yesterday)
print("Today:", today2)
print("Tomorrow:", tomorrow)


print("\n-----------3-----------")
todaywithoutmicsec = today.replace(microsecond=0)
print(todaywithoutmicsec)

print("\n-----------4-----------")
date1 = datetime(2022, 5, 17, 14, 30, 0)
date2 = datetime(2024, 5, 17, 14, 45, 30)

difference = (date2 - date1).total_seconds()

print(difference)