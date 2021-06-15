# Payment_sdk_python

This is python sdk for intergrating your python application with Ksher Payment Gateway. Please refers to our official api document [here](https://doc.vip.ksher.net)

## Requirement
- Python 3.7
    - other python3 version should also work, but python package version might cause some conflice and minor change might need to be done.

- Ksher Payment API Account
    - Requesting sandbox account please contact support@ksher.com
    
- API_URL
    - Along with a sandbox accout, you will be receiving a API_URL in this format: s[UNIQUE_NAME].vip.ksher.net

- API_TOKEN
    - Log in into API_URL using given sandbox account and get the token. see (How to get API Token)[https://doc.vip.ksher.net/docs/howto/api_token]


The Payment SDK for accessing *.vip.ksher.net

## How to Install

you can git clone this repository and install this package

### step1: clone this repository
```shell
git clone https://github.com/ksher-solutions/payment_sdk_python
```

### step2: cd into cloned source code and pip install all the requriements and the package itself
```shell
cd payment_sdk_python
pip install -r requirements.txt
pip install .

```

## How to Use
you need to first init the payment object and that you can use it to;
- Create New Order
- Query Order Status
- Refund the Order


### Init Payment Object
```python
from ksherpay import Payment
API_URL = 'https://sandboxbkk.vip.ksher.net'
API_TOKEN = testtoken1234
payment_handle = Payment(base_url=API_URL, token=API_TOKEN)
```

### Create New Order
***merchant_order_id need to be unique or else the request will end with error***

```python
data = {
            "amount": 100,
            "merchant_order_id": "OrderId000001",
            "channel_list": "linepay,airpay,wechat,bbl_promptpay,truemoney,ktbcard",
            "note": "string",
            "redirect_url": "http://www.baidu.com",
            "redirect_url_fail": "http://www.baidu.com",
            "signature": "string",
            "timestamp": "string"
        }
resp = payment_handle.order.create(data)
print(resp.status_code) # this should return 200
```

### Query order status
```python
merchant_order_id = 'OrderId000001'
resp = payment_handle.order.query(merchant_order_id)
print(resp.status_code) # this should return 200
```

### Refund
***Refund_id need to be unique or else the request will end with error***
```python
merchant_order_id = 'OrderId000001'
refund_id = "Refund_" + merchant_order_id
data = {
    'refund_amount':100,
    'refund_order_id':refund_id
}
resp = payment_handle.order.refund(merchant_order_id,params=data)
print(resp.status_code) # this should return 200
```