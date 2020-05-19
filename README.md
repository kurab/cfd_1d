# 1 Dimensional Flow Calculation by Python

Sample codes for simple 1D flow caluclation with CIP scheme and Upwind difference scheme.

## environment

MacOS 10.15.4
Python: 3.7.4 (anaconda3-2019.10)
ImageMagick

## structure

```
├── config
│   └── config.yml
├── controllers
│   └── flow1d.py
├── models
│   ├── calculator.py
│   └── condition.py
├── views
│   └── output.py
└── main.py
```

## result images

![1d_flow_cip](https://user-images.githubusercontent.com/9692738/82308773-37ca4580-99fd-11ea-9dc6-7ba25618eb2a.gif)
![1d_flow_upwind](https://user-images.githubusercontent.com/9692738/82308845-503a6000-99fd-11ea-8bb6-e8fc98838fdb.gif)
