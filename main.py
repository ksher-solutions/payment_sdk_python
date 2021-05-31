from payment import Payment
import time


my_token = '186d6c953c90f39c2973e6dd2e110d4057194996ef08fb4b3338180517b509c7'
my_payment = Payment('https://dev.vip.ksher.net',token=my_token)


data = {
    # "amount": 100,
    "channel_list": "linepay,airpay,wechat,bbl_promptpay,truemoney,ktbcard",
    "merchant_order_id": "dev61",
    "note": "string",
    "redirect_url": "http://www.baidu.com",
    "redirect_url_fail": "http://www.baidu.com",
    "signature": "string",
    "timestamp": "string"
}
data['merchant_order_id'] = my_payment.order.generate_order_id()

# my_order._make_sign('https://dev.vip.ksher.net/api/v1/redirect/orders',data)

# resp = my_order.create(data)
# print('status_code:{}'.format(resp.status_code))
# if resp.status_code == 200:
#     print(resp.json())
# else:
#     print(resp.text)

# for i in range(3):
#     time.sleep(0.5)
#     print('================= sleep ===============')

# resp = my_order.query('OrderAt20210531T144915')
# params = {
#     'refund_amount':100,
#     'refund_order_id': 'refund_OrderAt20210531T144915'
# }
# resp = my_order.refund('OrderAt20210531T144915',params=params)
resp = my_payment.order.cancle('OrderAt20210531T171241')

print('status_code:{}'.format(resp.status_code))
if resp.status_code == 200:
    print(resp.json())
else:
    print(resp.text)


