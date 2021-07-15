# System modules
from datetime import datetime

# 3rd party modules
from flask import make_response, abort


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


# Data to serve with our API
PEOPLE = {
    "Norris": {
        "fname": "Chuck",
        "lname": "Norris",
        "timestamp": get_timestamp(),
    },
    "Lee": {
        "fname": "Bruce",
        "lname": "Lee",
        "timestamp": get_timestamp(),
    
    },
    "Stallone": {
        "fname": "Sylvester",
        "lname": "Stallone",
        "timestamp": get_timestamp(),
    },
    "Seagal": {
        "fname": "Steven",
        "lname": "Seagal",
        "timestamp": get_timestamp(),
    },
    "Schwarzenegger": {
        "fname": "Arnold",
        "lname": "Schwarzenegger",
        "timestamp": get_timestamp(),
    },
    "Van Damme": {
        "fname": "Jean-Claude",
        "lname": "Van Damme",
        "timestamp": get_timestamp(),
    },
    "Reeves": {
        "fname": "Keanu",
        "lname": "Reeves",
        "timestamp": get_timestamp(),
    },
    "Diesel": {
        "fname": "Vin",
        "lname": "Diesel",
        "timestamp": get_timestamp(),
    },
    "Statham": {
        "fname": "Jason",
        "lname": "Statham",
        "timestamp": get_timestamp(),
    },
    "The-Rock": {
        "fname": "Dwayne Johnson",
        "lname": "The-Rock",
        "timestamp": get_timestamp(),
    },
    "Crews": {
        "fname": "Terry",
        "lname": "Crews",
        "timestamp": get_timestamp(),
    },
}

def read_all():

    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]


def read_one(lname):
    
    if lname in PEOPLE:
        person = PEOPLE.get(lname)
    else:
        abort(
            404, "Person with last name {lname} not found".format(lname=lname)
        )

    return person


def create(person):
    
    lname = person.get("lname", None)
    fname = person.get("fname", None)
    
    if lname not in PEOPLE and lname is not None:
        PEOPLE[lname] = {
            "lname": lname,
            "fname": fname,
            "timestamp": get_timestamp(),
        }
        return PEOPLE[lname], 201
    else:
        abort(
            406,
            "Person with last name {lname} already exists".format(lname=lname),
        )


def update(lname, person):    
    if lname in PEOPLE:
        PEOPLE[lname]["fname"] = person.get("fname")
        PEOPLE[lname]["timestamp"] = get_timestamp()

        return PEOPLE[lname]    
    else:
        abort(
            404, "Person with last name {lname} not found".format(lname=lname)
        )


def delete(lname):    
    if lname in PEOPLE:
        del PEOPLE[lname]
        return make_response(
            "{lname} successfully deleted".format(lname=lname), 200
        )    
    else:
        abort(
            404, "Person with last name {lname} not found".format(lname=lname)
        )