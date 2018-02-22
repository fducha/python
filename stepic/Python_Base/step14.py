from datetime import date
from datetime import timedelta


y, m, d = map(int, input().split())

nd = date(y, m, d) + timedelta(days=int(input()))

print(nd.year, nd.month, nd.day)
