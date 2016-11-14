# Event Sourcing Example

This is a simple API service that shows some common usages of the event sourcing concept covered in [Alex Tucker's](https://github.com/alextucker) talk from PyCon Canada 2015. ([video](https://2015.pycon.ca/en/schedule/39/))

The API offers the ability to create, update and delete expenses as well as querying individual expenses and generating a monthly expense report.

## API endpoints

TODO: What is the payload for post?

    POST /expense
    PUT /expense
    DELETE /expense

    GET /monthly-report
    GET /expense/{id}
