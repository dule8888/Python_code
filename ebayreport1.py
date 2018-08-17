import requests

class ebayreport():
	"""one example for the trafficreport"""
	def gettrafficreport(timespan, listoflistings=[]):
		"""get request for trafficreport, if listoflisting is not specified it will set the dimension to Day
		-> aggregated numbers on account level
		it takes a timespan as input in the following format: [20170501..20170601]"""
		metrics_trafficreport = ('CLICK_THROUGH_RATE,LISTING_IMPRESSION_SEARCH_RESULTS_PAGE,'
								'LISTING_IMPRESSION_STORE,LISTING_IMPRESSION_TOTAL,'
								'LISTING_VIEWS_SOURCE_DIRECT,LISTING_VIEWS_SOURCE_OFF_EBAY,'
								'LISTING_VIEWS_SOURCE_OTHER_EBAY,LISTING_VIEWS_SOURCE_SEARCH_RESULTS_PAGE,'
								'LISTING_VIEWS_SOURCE_STORE,LISTING_VIEWS_TOTAL,'
								'SALES_CONVERSION_RATE,TRANSACTION')
		if listoflistings == []:
			dimension_trafficreport = 'DAY'
		else:
			dimension_trafficreport = 'Listing'

		url_trafficreport = 'https://api.ebay.com/sell/analytics/v1/traffic_report'

		querystring = {"filter":str("marketplace_ids:{EBAY_US},date_range:"+str(timespan)),
						"dimension":dimension_trafficreport,
						'metric':metrics_trafficreport}

		headers = {
					'authorization': str('Bearer ' + 'https://signin.ebay.com/authorize?client_id=autoligh-e-PRD-a91ebc5cc-9dd14f69&response_type=code&redirect_uri=autolighthouse-autoligh-e-PRD--ycsmpobk&scope=https://api.ebay.com/oauth/api_scope https://api.ebay.com/oauth/api_scope/sell.marketing.readonly https://api.ebay.com/oauth/api_scope/sell.marketing https://api.ebay.com/oauth/api_scope/sell.inventory.readonly https://api.ebay.com/oauth/api_scope/sell.inventory https://api.ebay.com/oauth/api_scope/sell.account.readonly https://api.ebay.com/oauth/api_scope/sell.account https://api.ebay.com/oauth/api_scope/sell.fulfillment.readonly https://api.ebay.com/oauth/api_scope/sell.fulfillment https://api.ebay.com/oauth/api_scope/sell.analytics.readonly')
		}
		requesttype = 'GET'

		response = requests.request("GET", url_trafficreport, headers=headers, params=querystring)
		print(response.status_code)
