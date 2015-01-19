[![Build Status](https://travis-ci.org/iter8ve/pyvo.svg?branch=master)](https://travis-ci.org/iter8ve/pyvo)

# Introduction

Pyvo is a Python client for the Pivotal Tracker v5 API that uses the Requests HTTP library under the hood. It has three design goals:

* Recency. Pyvo addresses the v5 Pivotal API.
* Flexibility. Pyvo maps attribute access to Pivotal’s API resources; making support for changes to the API easy to accommodate.
* Minimalism. At this point there aren’t a lot of bells and whistles, and the feature set is likely to remain small. It should be easy to read and extend as you see fit.

The current feature set can best be described as alpha (at best). It works, though.

# Installation
Clone this repository and do `pip install -e .` from the clone’s root directory.

# Usage
You’ll need a Pivotal API access token. Then:

```
from pyvo import Client

client = Client(YOUR_API_TOKEN)

r = client.me.get()
```

# Tests
Tested for Python 2.7 using py.test and tox.

# To dos
* Python 3 compatibility.
* Lightweight model objects using JSON Schema for validation.
* Support for OAuth helpers.

