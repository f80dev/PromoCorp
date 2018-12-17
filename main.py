import Corporate as Corp

c=Corp.Corporate("F80")

print(c.toYAML())
c.update(open("index.html","r"))
