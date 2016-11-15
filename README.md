# Event Sourcing Example

[![Build Status](https://travis-ci.org/waveaccounting/event-sourcing-example.svg?branch=master)](https://travis-ci.org/waveaccounting/event-sourcing-example)

This is a simple API service that shows some common usages of the event sourcing concept covered in [Alex Tucker's](https://github.com/alextucker) talk from PyCon Canada 2015. ([video](https://2015.pycon.ca/en/schedule/39/))

The API offers the ability to create, update and delete expenses as well as querying individual expenses and generating a monthly expense report.


## Running project

Follow these steps to setup the project to the point where the tests will pass. First clone the repo:

    git clone git@github.com:waveaccounting/event-sourcing-example.git
    cd event_sourcing-example

Then create a virtualenv and install requirements:

    python3 -m venv .venv
    source .venv/bin/activate

And now run the tests:

    ./scripts/test

Assuming the tests pass, try running the server:

    ./scripts/server
    # Or on a specific port
    ./scripts/server --port=8001


## API endpoints

We use an expenses model as a example of using the event sourcing. We expose these as endpoints.

### Modifying state

For mutation we present the following endpoints

    POST /expense    # Creates the expense record
    PUT /expense     # Updates an expense record
    DELETE /expense  # Marks an expense record as deleted

These endpoints expect a payload similar to:

    create_expense_fixture = {
        "amount": "150.0000",
        "date": "2016-11-14T12:34:56",
        "name": "pycon ticket",
        "sequence": 1,
    }

### Retrieving state

You can get the current state of a expense with:

    GET /expense/{id}

You can also get the state of the expense at a specific time by passing a ISO8601 datetime string as a querystring:

    GET /expense/{id}?datetime=2016-11-14T20:42:29+00:00

We also present the expenses per month with:

    GET /monthly-report
