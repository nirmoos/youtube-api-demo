# YouTube Search API

## Installation

Use the requirements.txt file to install all the necessary packages (better to use a separate virtual environment)

```commandline
pip install -r requirements.txt
```

## Requirements

  1. Python 3.8+

## Prerequisites

Please follow the following steps prior to execution of the program

1. Create/Select a project in the [Google Developers Console](https://console.developers.google.com/) and obtain an [API key](https://developers.google.com/youtube/registering_an_application)
2. Make sure the 'YouTube Data API v3' is enabled, otherwise enable it. (You can see all the enabled APIs in the [Enabled APIs page](https://console.developers.google.com/apis/enabled))
3. Create a .env file under root folder and provide the API key obtained from the step 1 (Please use the .env.sample file for the keys)

## Usage

Navigate to the root folder prior to execution

```commandline
python main.py --q surfing --max-results 10
```

q argument is mandatory, it is the search term we are about to search in YouTube data API.<br />
max-results is optional, and defaults to 10. It describes how many results we need.

## Reference links
  * [YouTube Data API Overview](https://developers.google.com/youtube/v3/getting-started)
  * [YouTube Data Search List API](https://developers.google.com/youtube/v3/docs/search/list)
  * [Google API Client Library for Python](https://developers.google.com/api-client-library/python)
  * [Google API Client Library for Python - Samples](https://github.com/google/google-api-python-client/tree/master/samples)
  * [YouTube Search Data API - Python sample](https://github.com/youtube/api-samples/blob/master/python/search.py)