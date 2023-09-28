import datetime


date = datetime.date.today()


def greeting(name, date):
    return f"Hello {name}, today is {date}"


def mami():
    text = "ma kore motek"
    return text


#print(greeting("Elazar", date))

if __name__ == '__main__':

    print(greeting("Erez", date))

