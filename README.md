# duckdb-with-delta
Testing a new duckdb release that allow reading directly from delta tables using Linkedin data.

## Installation

Create a venv with python.
```bash
python3 -m venv venv
```

Install requirements.txt file, available in root path.

```bash
pip install requirements.txt
```

Download file from https://www.kaggle.com/datasets/arshkon/linkedin-job-postings?resource=download , extract and copy "postings.csv" into to file/ on root path.

Run __main__.py

```bash
python3 __main__.py
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.
