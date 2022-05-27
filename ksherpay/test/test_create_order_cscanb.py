import unittest
from ksherpay import Payment
from ksherpay import API_TYPE
import os
import json
import logging
from dotenv import load_dotenv
import webbrowser
logging.root.setLevel('INFO')
import time
import base64
import os


class CscanBOrderCreateTestCase(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        load_dotenv()
        self.BASE_URL = 'https://sandboxdoc.vip.ksher.net'
        self.token = os.environ.get("API_TOKEN") 
        logging.info("token:{}".format(self.token))
        # self.database_name = "trivia_test"
        # self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        # setup_db(self.app, self.database_path)

    def tearDown(self):
        """Executed after reach test"""
        print('-=- teart donw-=-')
        pass

    def test_success_create(self):
        logging.info("============ START test case: test_success_create ============")
        payment_handle = Payment(base_url=self.BASE_URL, apiType=API_TYPE.CSCANB ,token=self.token)
        data = {
            "amount": 100,
            "channel": "truemoney",
            "note": "string",
            "signature": "string",
            "timestamp": "string"
        }
        # make sure time will be different for altest 1 second
        time.sleep(1)
        data['merchant_order_id'] = payment_handle.order.generate_order_id()
        resp = payment_handle.order.create(data)
        data = resp.json()
        if resp.status_code == 200:
            logging.info("successfully create order with following response data:")
            data = resp.json()
            logging.info(f"data:{data}")
            self.assertEqual(data['error_code'], 'SUCCESS')
            self.assertIn('data:image/png;base64,',data['reserved1'])

        logging.info("============ END test case: test_success_create ============")
    
    def test_fail_create(self):
        logging.info("============ START test case: test_fail_create ============")
        payment_handle = Payment(base_url=self.BASE_URL, apiType=API_TYPE.CSCANB, token=self.token)
        # missing need param
        data = {
            "channel": "truemoney",
            "note": "string",
            "signature": "string",
            "timestamp": "string"
        }
        time.sleep(1)
        data['merchant_order_id'] = payment_handle.order.generate_order_id()
        resp = payment_handle.order.create(data)
        self.assertEqual(resp.status_code, 400)
        logging.info("============ END test case: test_fail_create ============")

    def test_create_query_pending(self):
        logging.info("============ START test case: test_create_query_pending ============")
        # ceate an order and not pay result in pending order
        payment_handle = Payment(base_url=self.BASE_URL, apiType=API_TYPE.CSCANB ,token=self.token)
        data = {
            "amount": 100,
            "channel": "truemoney",
            "note": "string",
            "signature": "string",
            "timestamp": "string"
        }
        # make sure time will be different for altest 1 second
        time.sleep(1)
        data['merchant_order_id'] = payment_handle.order.generate_order_id()
        resp = payment_handle.order.create(data)
        self.assertEqual(resp.status_code, 200)
        if resp.status_code == 200:
            logging.info("successfully create order with following response data:")
            data = resp.json()
            logging.info(f"data:{data}")
            self.assertEqual(data['error_code'], 'SUCCESS')
            self.assertIn('data:image/png;base64,',data['reserved1'])

            resp = payment_handle.order.query(data['merchant_order_id'])
            self.assertEqual(resp.status_code, 200)
            logging.info("successfully query order with following response data:")
            data = resp.json()
            logging.info(f"data:{data}")
            self.assertEqual(data['error_message'], 'PENDING')
        logging.info("============ END test case: test_create_query_pending ============")

    def test_pay_success(self):
        logging.info("============ START test case: test_pay_success ============")
        payment_handle = Payment(base_url=self.BASE_URL, apiType=API_TYPE.CSCANB, token=self.token)
        payment_amount = 100
        data = {
            "amount": payment_amount,
            "channel": "truemoney",
            "note": "string",
            "signature": "string",
            "timestamp": "string"
        }
        # make sure time will be different for altest 1 second
        time.sleep(1)
        merchant_order_id = payment_handle.order.generate_order_id()
        data['merchant_order_id'] = merchant_order_id
        resp = payment_handle.order.create(data)
        
        self.assertEqual(resp.status_code, 200)
        if resp.status_code == 200:
            logging.info("successfully create order with following response data:")
            data = resp.json()
            logging.info(f"data:{data}")
            self.assertEqual(data['error_code'], 'SUCCESS')
            self.assertIn('data:image/png;base64,',data['reserved1'])
            imgDataStr = data['reserved1']
            imgData = base64.b64decode(imgDataStr.replace('data:image/png;base64,','')) 
            fileName = 'testQR.png'
            with open(fileName, 'wb') as f:
                f.write(imgData)
            filePath = os.getcwd() + f'/{fileName}'
            input(f"Pleae make truemoney payment on QR code locate here:{filePath}, AFTER the payment is made, click any key to continue...")

            resp = payment_handle.order.query(data['merchant_order_id'])
            self.assertEqual(resp.status_code, 200)
            logging.info("successfully query order with following response data:")
            data = resp.json()
            logging.info(f"data:{data}")
            self.assertEqual(data['error_code'], 'SUCCESS')
            # and refund
            if (resp.status_code == 200) and (data['error_code'] == 'SUCCESS'):
                logging.info('the order is successfully pay. now testing refund ......')
                params = {
                    'refund_amount':payment_amount,
                    'refund_order_id':"Refund_" + merchant_order_id
                }
                resp = payment_handle.order.refund(data['merchant_order_id'],params=params)
                self.assertEqual(resp.status_code, 200)
                logging.info("successfully refund order with following response data:")
                data = resp.json()
                logging.info(f"data:{data}")
                self.assertEqual(data['error_code'], 'REFUNDED')
        logging.info("============ END test case: test_pay_success ============")





        

        

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()