# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 13:30:34 2018

@author: apersonett
"""
import pandas as pd
import requests

header={'Authorization':'TOKEN '+'AgAAAA**AQAAAA**aAAAAA**AaPPWg**nY+sHZ2PrBmdj6wVnY+sEZ2PrA2dj6wMlIWlAJmLoQmdj6x9nY+seQ**gcUDAA**AAMAAA**Accf+dhWw1dqz4x8dMMl5R6MVkC/tBS6EeRP2D2thv629VYWYTOcm9msF7Ps9Q/8SdtdleqxYdHKR+8rrvzGmh/Nl8a3YK0NqtvhFnAQDf2X9mraXVoaQZ6mkFC6nfXlTIYLM4u9JD9HgUwHAp5gVGdwFBzaj5J/eZP946+4CGmqwQ0vzBErZr6CI52hymOxNj1QRcrPRSHm1SiltYiZBwkpAbsqAV2XtlWBogJAXtZS+U+++ZTuNYtR/GCI8B3pZ/uwi+DILktYcW//HS4Go7UOUAzXkx99w5W6bfjrbfG8quMPjo446KgnDds/XkGZCrotWk+zkU5X4QDNDzq8K7B48r473ZKAQfUnKswe9ZZuQpQsnbdK1EL9zJRGKC6YLzZhW0bL1AgU9DXMCDBxPj6dkHpgwsKqUATqWc7GGKR3UsG3ZIN3vvcMxnLJaYjzdEWxQb5vHre8RlLGDnG2an638U9SMmrzuu+TXDt+kMN1qeGKoLh86Bni3Sqdq/4yxW4VQRIw8H9YdzQVf85z1t1mHV1iMftxwhddl1C+90N2akg1kpQJ8fIRa92M+6uV9yxkGujM71FiLU2EdIbQu0AGUrEAjpqR02dY1TCsIr/5qI59XWYB10rneXeJTpP9q2sr/JQEznGOpDWRGGqNYMmUEwMshLToj0CO4esRF0T3r7pn5/Kz5j1OCfsQfMfBEUoaGEzmTxnwLo0xKjseUMxhm1m/DD5ra1lLiQ4u8HjlI8/+Z7sY6uEJGEJBxnu2','Content-Type':'application/json','X-EBAY-C-MARKETPLACE-ID':'EBAY_US','Accept':'application/json'}
   

t=requests.get('https://api.ebay.com/post-order/v2/cancellation/search?creation_date_range_from=2018-04-01T00:00:01.000Z&creation_date_range_to=2018-04-30T23:59:59.000Z&sort=+CANCEL_REQUEST_DATE',headers=header)


totalpage  = t.json()['paginationOutput']['totalPages']



longlist = []

for j in range(0,totalpage+1 ):
    t=requests.get('https://api.ebay.com/post-order/v2/cancellation/search?creation_date_range_from=2018-04-01T00:00:01.000Z&creation_date_range_to=2018-04-30T23:59:59.000Z&offset=%s&sort=+CANCEL_REQUEST_DATE' %j,headers=header)
    try: 
        for i in range(0,len(t.json()['cancellations'])):
            smalllist = []
            smalllist.append(t.json()['cancellations'][i]['legacyOrderId'])
            smalllist.append(t.json()['cancellations'][i]['requestRefundAmount']['value'])
            smalllist.append(t.json()['cancellations'][i]['cancelRequestDate']['value'])
            smalllist.append(t.json()['cancellations'][i]['cancelCloseDate']['value'])
            smalllist.append(t.json()['cancellations'][i]['cancelStatus'])
            smalllist.append(t.json()['cancellations'][i]['paymentStatus'])
            longlist.append(smalllist)
            
    except:
        print("a")
        pass



df = pd.DataFrame(longlist)
df.columns =['legacyOrderId','requestRefundAmount','cancelRequestDate','cancelCloseDate','cancelStatus','paymentStatus']

df.to_csv(r'Y:\le\refund check\refund0401_0430.csv')


