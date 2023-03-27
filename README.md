# analyze-text

`analyze-text` is a Python microservice using FastAPI web framework.

## How to Run
To use this, you need Python 3.7. To set up, run
```commandline
pip3 install -r requirements.txt
```
Alternatively, you can use the commands below in the Makefile for installation and other usages.
- `make install`: install the library's dependencies using `pip`
- `make lint`: perform static analysis of this library with `black` and `flake8`
- `make format`: autoformat this library with `black`
- `make test`: run automated tests with `pytest`
- `make coverage`: run automated tests with `pytest` and collect coverage information (passes with coverage > 90%)

Start the service by running
```commandline
python3 run.py
```
The default host is 0.0.0.0 and the default port number is 8000. These are configured in `src/config.py`. The Swagger UI can be found at `http://0.0.0.0:8000/docs`

## Example Usage:

### Bigram Analysis Service
Returns the most frequently occurring bigrams in text ignoring non-alphanumeric characters.

Request:

```
POST /analyze-text
{
  "service": "bigram",
  "text": "The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog again and again."
}
```

Response:

```
HTTP 200 OK
{
  "result": [    ["the", "quick"],
    ["quick", "brown"],
    ["brown", "fox"],
    ["fox", "jumps"],
    ["jumps", "over"],
    ["over", "the"],
    ["the", "lazy"],
    ["lazy", "dog"],
  ]
}
```

### Word Count Service
Counts the occurrences of each word in the text ignoring non-alphanumeric characters.

Request:
```
POST /analyze-text
{
  "service": "word-count",
  "text": "The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog again and again."
}
```
Response:
```
HTTP 200 OK
{
  "result": {
    "the": 4,
    "quick": 2,
    "brown": 2,
    "fox": 2,
    "jumps": 2,
    "over": 2,
    "lazy": 2,
    "dog": 2,
    "again": 2,
    "and": 1
  }
}
```

Only `bigram` and `word-count` are allowed values for `service` field. `text` field cannot be empty.
