# payment_sdk_python
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

### Init Payment Object
```python
from ksherpay import Payment
BASE_URL = 'https://dev.vip.ksher.net'
token = testtoken1234
payment_handle = Payment(base_url=self.BASE_URL, token=self.token)
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
resp = payment_handle.order.query(data)
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