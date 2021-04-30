from datetime import datetime

end = datetime(2021, 5, 12, 6, 0, 0)
now = datetime.now()

duration = end - now
print(duration)