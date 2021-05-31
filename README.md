# payment_sdk_python
The Payment SDK for accessing *.vip.ksher.net

# How to Use

## Init the object
```python
from payment import Payment
BASE_URL = 'https://dev.vip.ksher.net'
token = testtoken1234
payment_handle = Payment(base_url=self.BASE_URL, token=self.token)
```

## Create New Order
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
```
