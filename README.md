# Advent of Code 2019

## Setup
Requires Python3 and virtualenv.

Create a virtual environment:
    virtualenv venv

Activate virtual environment:

* Mac:

    `source venv/bin/activate`

* Windows:

    `source venv/Scripts/activate`

Install dependencies:

    pip install pytest

Run unit tests:

    python -m pytest

Run main method:

    python day1/day.py

## Gotchas

* Don't reuse variables as values might have changed (point by reference).
* Write unit tests for simple cases that are easy to debug and make sure they pass.
* Go for the simplest solution, not the most efficient or elegant.
