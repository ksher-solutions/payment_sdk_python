# Payment_sdk_python

> Ksher will shut down the API connection via .vip.ksher.net. That make new register merchant will unable to use system over .vip.ksher.net.
>
> Merchants are currently connected, Please change the API to connection http://api.ksher.net.

This is python sdk for integrating your python application with Ksher Payment Gateway. Please refers to our official api document [here](https://doc.vip.ksher.net)

## Requirement
- Python 3.7
    - other python3 version should also work, but python package version might cause some conflict and minor change might need to be done.

- Ksher Payment API Account
    - Requesting sandbox account please contact support@ksher.com
    
- API_URL
    - Along with a sandbox account, you will be receiving a API_URL in this format: s[UNIQUE_NAME].vip.ksher.net

- API_TOKEN
    - Log in into API_URL using given sandbox account and get the token. see [How to get API Token](https://doc.vip.ksher.net/docs/howto/api_token)


The Payment SDK for accessing *.vip.ksher.net

## How to Install

there are two option two install this package;

1. Pip Install This package
2. Clone this repository

### Option 1: Pip Install This package
```
pip install ksherpay
```

### Option 2: Clone this repository

#### Step1: clone this repository
```shell
git clone https://github.com/ksher-solutions/payment_sdk_python
```

#### Step2: cd into cloned source code and pip install all the requriements and the package itself
```shell
cd payment_sdk_python
pip install -r requirements.txt
pip install .

```

or if you want to pip install from local please use
```
pip install ./payment_sdk_python --user 
```


## How to Use
you need to first init the payment object and that you can use it to;
- Init Payment Object
- Create New Order
- Query Order Status
- Refund the Order


### Init Payment Object
ksherpay have multiple api (apiType) such as;
- redirect API is for Website and Mobile App integration.
- settlement API is for checking the settlement information.
- miniapp API is for WeChat and Alipay Mini-Program integration.
- event API is for checking the events deliveried.
- C scan B API is for C scan B(merchant present QR code) or Kiosk integration.
- B scan C API is for B scan C(customer present QR code) or POS integration.

you can read about it [here](https://doc.vip.ksher.net/docs/user_guide/swagger)

currently this python sdk support only two api; 'redirect api' and 'c scan b api'

#### Redirect API

the default api is redirect api you can just init it like this

```python
from ksherpay import Payment
API_URL = 'https://sandboxbkk.vip.ksher.net'
API_TOKEN = testtoken1234
payment_handle = Payment(base_url=API_URL, token=API_TOKEN)
```

#### C_Scan_B API
to use 'C_Scan_B API', you need to specified it when init the object

**as shown in the code, please use ksherpay package's provided value to specified the apiType value**

```python
from ksherpay import Payment, API_TYPE
API_URL = 'https://sandboxbkk.vip.ksher.net'
API_TOKEN = testtoken1234
payment_handle = Payment(base_url=API_URL, apiType=API_TYPE.CSCANB, token=API_TOKEN)
```

#### B_Scan_C API
to use 'B_Scan_C API', you need to specified it when init the object

**as shown in the code, please use ksherpay package's provided value to specified the apiType value**

```python
from ksherpay import Payment, API_TYPE
API_URL = 'https://sandboxbkk.vip.ksher.net'
API_TOKEN = testtoken1234
payment_handle = Payment(base_url=API_URL, apiType=API_TYPE.BSCANC, token=API_TOKEN)
```

#### Finance API
to use 'Finance API', you need to specified it when init the object

**as shown in the code, please use ksherpay package's provided value to specified the apiType value**

```python
from ksherpay import Payment, API_TYPE
API_URL = 'https://sandboxbkk.vip.ksher.net'
API_TOKEN = testtoken1234
payment_handle = Payment(base_url=API_URL, apiType=API_TYPE.FINANCE, token=API_TOKEN)
data = {
            "mid": "35618",
            "signature": "string",
            "timestamp": "string"
        }
resp = payment_handle.settlements.channels(params=data)
```

#### Disable Sign Verification
In early phase of implementation. You might want to disable Sign Verification to debug on other thing without the need to worry if the bug is coming for signature.

*** for Security purpose, don't forget to enable this sign verification back first before going on Production environment.

to disable sign you simply do this;
```python
from ksherpay import Payment
API_URL = 'https://sandboxbkk.vip.ksher.net'
API_TOKEN = testtoken1234
payment_handle = Payment(base_url=API_URL, token=API_TOKEN, verify=False)
```


### Create New Order
***merchant_order_id need to be unique or else the request will end with error***

to create new order, each apiType has slightly different required parameters

#### Redirect API
```python
data = {
            "amount": 100,
            "merchant_order_id": "OrderId000001",
            "channel": "linepay,airpay,wechat,bbl_promptpay,truemoney,ktbcard",
            "note": "string",
            "redirect_url": "http://www.baidu.com",
            "redirect_url_fail": "http://www.baidu.com"
        }
resp = payment_handle.order.create(data)
print(resp.status_code) # this should return 200
```
#### C_Scan_B API
for 'C_Scan_B API', redirect_url is not needed and you can specified one channel at a time.
```python
data = {
            "amount": 100,
            "merchant_order_id": "OrderId000001",
            "channel": "truemoney",
            "note": "string",
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
