import requests
from bs4 import BeautifulSoup
from time import sleep
import re

page = 1
search_item = input("Please enter category to search\n")
base_url = "https://www.bestbuy.com/site/searchpage.jsp"+"?st="+search_item+"&_dyncharset=UTF-8&id=pcat17071&type=page&sc=Global"+"&cp="+str(page)+"&nrp=&sp=&qp=&list=n&af=true&iht=y&usc=All+Categories&ks=960&keys=keys"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36", "cookie": "UID=16b5f93b-2e61-4298-9f4c-1e8ac1539a31; vt=d8caad34-64da-11e9-a042-005056aedf5a; CTT=9742703e30eb2f108460c6dea95309a9; campaign=P10T12R103,BODY; AAMC_bestbuy_0=REGION%7C6; aam_uuid=77328575180584566152845750413035822462; oid=225939993; partner=P10T12R103&BODY&2019-04-22 03:44:34.483; optimizelyProtocol=https; optimizelyEndUserId=oeu1555922676566r0.48381810612963916; campaign_date=1555922678477; context_id=dd860314-64da-11e9-b85a-0e8f55625ce2; _gcl_au=1.1.1740165249.1555922680; 52245=; __gads=ID=c04c81307d4226a8:T=1555922691:S=ALNI_MYVi0roMV90hXwUls0ttblBD-qjAw; locDestZip=04785; locStoreId=463; pst2=463; customerZipCode=04401|Y; physical_dma=552; ui=1558358217952; G_ENABLED_IDPS=google; google_disable_auto_signon=%7B%22meta%22%3A%7B%22CreatedAt%22%3A%222019-05-20T13%3A18%3A31.287Z%22%2C%22ModifiedAt%22%3A%222019-05-20T13%3A18%3A31.287Z%22%2C%22ExpiresAt%22%3A%229999-01-01T00%3A00%3A00.000Z%22%7D%2C%22value%22%3A%221%22%7D; basketTimestamp=1558359127756; pt=3382742582; DYN_USER_CONFIRM=25e845c7f20801fb31537ea034b5b844; DYN_USER_ID=ATG49344901440; aamoptsegs=aam%3D9403891; lastBrowsedCategory=pcmcat214000050005; SID=f3c728e1-aa76-4e6e-abbe-b1f554f8d51c; bby_rdp=l; AMCVS_F6301253512D2BDB0A490D45%40AdobeOrg=1; AMCV_F6301253512D2BDB0A490D45%40AdobeOrg=-330454231%7CMCMID%7C70937882666923087413340739385820312668%7CMCAAMLH-1559805087%7C6%7CMCAAMB-1559805087%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1559207487s%7CNONE%7CMCAID%7CNONE%7CMCCIDH%7C-67067708%7CvVersion%7C3.1.2; s_cc=true; intl_splash=false; COM_TEST_FIX=2019-05-30T07:11:30.146Z; lastSearchTerm=tv; listFacets=undefined; c2=Search%20Results; context_session=2c78cc12-82aa-11e9-b3d2-0a7bdf5400b8; sc-location-v2=%7B%22meta%22%3A%7B%22CreatedAt%22%3A%222019-04-22T08%3A44%3A59.909Z%22%2C%22ModifiedAt%22%3A%222019-05-30T07%3A12%3A26.337Z%22%2C%22ExpiresAt%22%3A%222020-05-29T07%3A12%3A26.337Z%22%7D%2C%22value%22%3A%22%7B%5C%22physical%5C%22%3A%7B%5C%22zipCode%5C%22%3A%5C%2204785%5C%22%2C%5C%22source%5C%22%3A%5C%22A%5C%22%2C%5C%22captureTime%5C%22%3A%5C%222019-05-20T13%3A30%3A56.144Z%5C%22%7D%2C%5C%22store%5C%22%3A%7B%5C%22zipCode%5C%22%3A%5C%2204401%5C%22%2C%5C%22searchZipCode%5C%22%3A%5C%2204785%5C%22%2C%5C%22storeId%5C%22%3A%5C%22463%5C%22%2C%5C%22storeHydratedCaptureTime%5C%22%3A%5C%222019-04-22T08%3A45%3A01.796Z%5C%22%7D%2C%5C%22destination%5C%22%3A%7B%5C%22zipCode%5C%22%3A%5C%2204785%5C%22%7D%7D%22%7D; bby_cbc_lb=p-browse-e; ltc=%20"}

while True:
    base_url = "https://www.bestbuy.com/site/searchpage.jsp" + "?st=" + search_item + "&_dyncharset=UTF-8&id=pcat17071&type=page&sc=Global" + "&cp=" + str(page) + "&nrp=&sp=&qp=&list=n&af=true&iht=y&usc=All+Categories&ks=960&keys=keys"
    get_url = requests.get(base_url, headers =headers, timeout = 5)
    print(get_url.status_code)
    print(base_url)
    best_buy_soup = BeautifulSoup(get_url.text, 'html.parser')
    product_name = best_buy_soup.findAll('h4', {'class':'sku-header'})
    product_model_plus_sku = best_buy_soup.findAll('div', {'class':'sku-model'})
    product_model_detail = best_buy_soup.findAll('span',{'class':'sku-value'})
    products = best_buy_soup.findAll('li',{'class':'sku-item'})

    file_path = "bestbuy_{search_item}_new.txt".format(search_item=search_item)
    if len(products) < 1:
        break
    with open(file_path, "a", encoding='utf8') as textfile:
        products = best_buy_soup.findAll('li', {'class': 'sku-item'})
        for items in products:
            # print(product)
            product_name = items.findAll('h4', {'class': 'sku-header'})[0].text
            print(product_name + "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            if search_item == "laptop":
                parsed = product_name.split(' - ')
                brand = parsed[0]
                color = parsed[-1]
                hard_drive = ""
                screen_size = re.search('\d+\.?\d?\"', product_name)
                print(screen_size.group())
                string_to_search = parsed[1:-1]
                regexp = re.compile(r'(\d+GB)|(\d+TB)')
                for element in string_to_search:
                    if regexp.search(element):
                        if "GB Memory" not in element:
                            hard_drive= re.sub(r'\([\w\s]+\)', '', element)
                            print('"'+ hard_drive +'"')
                    # else:
                    #     print("SHIITTT++++++++++++++++++++++++++++++++++++++")

            product_model = items.findAll('div', {'class': 'sku-attribute-title'})[0].text
            #print(product_model)
            page_line = "{product_name}{product_model}\n".format(product_name=product_name, product_model=product_model)
            textfile.write(page_line)


    page = page +1
    sleep(2)
