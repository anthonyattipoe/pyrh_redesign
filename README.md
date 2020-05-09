![robinhood-logo](https://imgur.com/U4A1ciD.png)

# API Design & Implementation  Final Project

## Introduction
There are many public APIs with flawed functionality. This could range from broken methods
to simply poor documentation. Our task for this assignment was to find a broken public API and redesign it. The public
 API chosen for this assignment was 'pyrh' (https://pyrh.readthedocs.io/en/latest/), with the following description
 "Python Framework to make trades with Unofficial Robinhood API. Supports Python 3.6+."  

## Pyrh Redesign
Although Pyrh does allow Robinhood users to trade using the API, there were many flaws found including:
* API Organization
* Broken Methods
* Poor Documentation
* Incorrect Return Types

Our redesign of the API resolves the issues listed above while providing users with a more intuitive design for trading. The full documentation for our redesign can be found here: https://pyrh-redesign.readthedocs.io/en/latest/

## Directory Overview
* [client/] (https://github.com/anthonyattipoe/pyrh_redesign/tree/master/client)  - contains client code samples performing various tasks a user may be interested in.
* results/ - contains results outputted from executing the client code samples in the client directory.
* docs/    - contains relevant files used to manage the project documentation found at https://pyrh-redesign.readthedocs.io/en/latest/
* pyrh/    - contains modified source code from the original pyrh project

## Relevant Files
* instrument.py   - the newly designed Instrument class
* order.py        - the newly designed Order class
* portfolio.py    - the newly designed Portfolio class
* session.py      - the newly designed Robinhood session class
* user.py         - the newly designed User class
* exceptions.py   - a collection of new exceptions designed for use with our updated API
* test.py         - a collection of unit tests which test functionality of the newly implemented classes
* requirements.md - a collection of use cases and top level requirements meant to be addressed by the redesign of this API
* responses.md    - responses returned from various endpoints using the original pyrh API


## Team Members:
* Sara Harvey Browne
* Chinedu Ojukwu
* John Paul Harriman
* Evangeline Liu
* Anthony Attipoe
