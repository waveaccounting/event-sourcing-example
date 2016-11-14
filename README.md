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

TODO: What is the payload for post?

    POST /expense
    PUT /expense
    DELETE /expense

    GET /monthly-report
    GET /expense/{id}
