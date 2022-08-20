key_id = 'rzp_test_0iZfv7HdoeqVy6'
key_secret = 'G36fFHlUIMFi8zaPSJ3h14o4'

from http import client
import razorpay

client = razorpay.Client(auth=(key_id,key_secret))

# --- To create an order --- #
data = { 
    "amount": 500*100, 
    "currency": "INR",
    "receipt": "order_rcptid_11" 
    }
order = client.order.create(data=data)
print("Order : ",order)

# ---Verify---#
# --- Pass these ids & signature from button.html (JS-console) ,you will get these when user do payment...  ---#
# param_dict = {
#         'razorpay_order_id' : 'order_K7z4rqXJaH0AO0',
#         'razorpay_payment_id' : 'pay_K7zcJIeFRS2IGM',
#         'razorpay_signature' : '679648d4627e78734542ba53b0388d04101682965c8373dfde1d729a0135f231'
#       }
# verify = client.utility.verify_payment_signature(param_dict)
# print("verify_payment_signature : ",verify)