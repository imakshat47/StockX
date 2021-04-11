# StockX
Limit Order Book(Trading) in python. Maintains both buy side and sell side of Order.  Implemented Market Order, Limit Order and Stop Order.

## SetUp
1. Requirements:
```python
pip install -r requirements.txt
```
2. Open CMD in root folder and Run:
```python
py main.py
```

## Features
* Supports Market Order, Limit Order and Stop Order
* Easy setup by setup walk through:
    - Un-comment line after #Run next ?
    ```
    _next = input("Do you want to continue? (Y/N): ")
        if(_next == 'N' or _next == 'n'):
            break
    ```
* To pass data CSV
    - Un comment and pass user defined file path.
    ```
    csv_data = app.extract_csv()
    -or-
    csv_data = app.extract_csv(file_path)
    ```

## Symbols Usage

* bids:

	`B,<symbol>,<exchange>,<id>,<quantity>,<price>,<timestamp>`

* asks:

	`A,<symbol>,<exchange>,<id>,<quantity>,<price>,<timestamp>`
