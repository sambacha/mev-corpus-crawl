from lxml import etree
from crawler import crawl_url_by_get

def get_contract_addr(url):
	'''
		get contract address from an url
		Parameters : url
		return : [], list of contract address in this page
	'''
	text = crawl_url_by_get(url, proxy=None, enable_proxy=False)
	html = etree.HTML(text)
	contract_address = html.xpath('//table/tbody/tr/td[1]/a/text()')
	return contract_address

def main():
	base_url = 'https://etherscan.io/contractsVerified/'
	with open('./contract_addresses', 'w') as f:

		for page_num in range(1, 910):
			try:
				contract_addresses = get_contract_addr( str(base_url) + str(page_num) )
				for addr in contract_addresses:
					f.write(addr + '\n')

			except Exception, ex:
				print 'spider_url_by_get（） -------- ', str(ex) , page_num
				continue

if __name__ == '__main__':
    main()
