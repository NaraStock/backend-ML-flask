NaraStock ML API Model Capstone Project DBSFoundation

## Prequisite
- Python3.10-3.12
### Notes : Use conda or anaconda and other virtual environment to install required Python version

## Getting Started
### Step 1 : Clone Repo
```
https://github.com/NaraStock/backend-ML-flask.git
```
### Step 2 : Download all dependencies
```
pip install -r requirements.txt
```
### Step 3 : Run the server
```
python app.py
```

# Request Backend

our public server API
url = https://flasknarastock.onrender.com

### If you run local it will be
http://127.0.0.1:5000
or
localhost:5000

symbol = ['EURUSD=X', 'NZDUSD=X', 'GBPUSD=X', 'USDJPY=X', 'AUDUSD=X']

Prediksi close, high, low harian
```
http://url/predict?symbol={symbol}
```
```
output json
{
  "predicted_close": 1.13992472472937,
  "predicted_high": 1.14410242484721,
  "predicted_low": 1.13708274047372
}
```

Prediksi mingguan

```
http://url/weekly?symbol={symbol}
```
output json
```
[
  {
    "t+1": {
      "classification": "Naik",
      "classification_probability": 0.664744973182678,
      "predicted_close_price": 1.14174861263827
    }
  },
  {
    "t+2": {
      "classification": "Turun",
      "classification_probability": 0.885912358760834,
      "predicted_close_price": 1.14174739689901
    }
  },
  {
    "t+3": {
      "classification": "Turun",
      "classification_probability": 0.948593735694885,
      "predicted_close_price": 1.14166667181212
    }
  },
  {
    "t+4": {
      "classification": "Turun",
      "classification_probability": 0.97331315279007,
      "predicted_close_price": 1.14148879179063
    }
  },
  {
    "t+5": {
      "classification": "Naik",
      "classification_probability": 0.979985177516937,
      "predicted_close_price": 1.14192388750421
    }
  }
]
```

t+1 = senin
t+2 = selasa
t+3 = rabu
t+4 = kamis
t+5 = jumat
