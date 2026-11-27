def emp (**data):
    for key, val in data.items():
        print(key, ':' , val)

emp(id=101, name='NEETA', sal= 35000, dept='IT')