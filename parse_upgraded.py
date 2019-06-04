import requests
from bs4 import BeautifulSoup
from time import sleep
import re

page = 1
search_item = input("Please enter category to search\n")
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36", "cookie": "UID=16b5f93b-2e61-4298-9f4c-1e8ac1539a31; vt=d8caad34-64da-11e9-a042-005056aedf5a; CTT=9742703e30eb2f108460c6dea95309a9; campaign=P10T12R103,BODY; AAMC_bestbuy_0=REGION%7C6; aam_uuid=77328575180584566152845750413035822462; oid=225939993; partner=P10T12R103&BODY&2019-04-22 03:44:34.483; optimizelyProtocol=https; optimizelyEndUserId=oeu1555922676566r0.48381810612963916; campaign_date=1555922678477; context_id=dd860314-64da-11e9-b85a-0e8f55625ce2; _gcl_au=1.1.1740165249.1555922680; 52245=; __gads=ID=c04c81307d4226a8:T=1555922691:S=ALNI_MYVi0roMV90hXwUls0ttblBD-qjAw; locDestZip=04785; locStoreId=463; pst2=463; customerZipCode=04401|Y; physical_dma=552; ui=1558358217952; G_ENABLED_IDPS=google; google_disable_auto_signon=%7B%22meta%22%3A%7B%22CreatedAt%22%3A%222019-05-20T13%3A18%3A31.287Z%22%2C%22ModifiedAt%22%3A%222019-05-20T13%3A18%3A31.287Z%22%2C%22ExpiresAt%22%3A%229999-01-01T00%3A00%3A00.000Z%22%7D%2C%22value%22%3A%221%22%7D; basketTimestamp=1558359127756; pt=3382742582; DYN_USER_CONFIRM=25e845c7f20801fb31537ea034b5b844; DYN_USER_ID=ATG49344901440; aamoptsegs=aam%3D9403891; lastBrowsedCategory=pcmcat214000050005; SID=f3c728e1-aa76-4e6e-abbe-b1f554f8d51c; bby_rdp=l; AMCVS_F6301253512D2BDB0A490D45%40AdobeOrg=1; AMCV_F6301253512D2BDB0A490D45%40AdobeOrg=-330454231%7CMCMID%7C70937882666923087413340739385820312668%7CMCAAMLH-1559805087%7C6%7CMCAAMB-1559805087%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1559207487s%7CNONE%7CMCAID%7CNONE%7CMCCIDH%7C-67067708%7CvVersion%7C3.1.2; s_cc=true; intl_splash=false; COM_TEST_FIX=2019-05-30T07:11:30.146Z; lastSearchTerm=tv; listFacets=undefined; c2=Search%20Results; context_session=2c78cc12-82aa-11e9-b3d2-0a7bdf5400b8; sc-location-v2=%7B%22meta%22%3A%7B%22CreatedAt%22%3A%222019-04-22T08%3A44%3A59.909Z%22%2C%22ModifiedAt%22%3A%222019-05-30T07%3A12%3A26.337Z%22%2C%22ExpiresAt%22%3A%222020-05-29T07%3A12%3A26.337Z%22%7D%2C%22value%22%3A%22%7B%5C%22physical%5C%22%3A%7B%5C%22zipCode%5C%22%3A%5C%2204785%5C%22%2C%5C%22source%5C%22%3A%5C%22A%5C%22%2C%5C%22captureTime%5C%22%3A%5C%222019-05-20T13%3A30%3A56.144Z%5C%22%7D%2C%5C%22store%5C%22%3A%7B%5C%22zipCode%5C%22%3A%5C%2204401%5C%22%2C%5C%22searchZipCode%5C%22%3A%5C%2204785%5C%22%2C%5C%22storeId%5C%22%3A%5C%22463%5C%22%2C%5C%22storeHydratedCaptureTime%5C%22%3A%5C%222019-04-22T08%3A45%3A01.796Z%5C%22%7D%2C%5C%22destination%5C%22%3A%7B%5C%22zipCode%5C%22%3A%5C%2204785%5C%22%7D%7D%22%7D; bby_cbc_lb=p-browse-e; ltc=%20"}

def quick_search(pattern, search_in_string):
    pattern_search = re.search(pattern, search_in_string)
    if bool(pattern_search) == True:
        return pattern_search.group()
    else:
        return None

while True:
    base_url = "https://www.bestbuy.com/site/searchpage.jsp" + "?st=" + search_item +"&_dyncharset=UTF-8&id=pcat17071&type=page&sc=Global" + "&cp=" + str(page) + "&nrp=&sp=&qp=&list=n&af=true&iht=y&usc=All+Categories&ks=960&keys=keys"
    get_url = requests.get(base_url, headers =headers, timeout = 5)
    print(get_url.status_code)
    print(base_url)
    best_buy_soup = BeautifulSoup(get_url.text, 'html.parser')
    products = best_buy_soup.findAll('li', {'class': 'sku-item'})

    file_path = "bestbuy_{search_item}_4.txt".format(search_item=search_item)
    if len(products) < 1:
        break
    with open(file_path, "a", encoding='utf8') as textfile:
        products = best_buy_soup.findAll('li', {'class': 'sku-item'})
        for items in products:
            product_name = items.findAll('h4', {'class': 'sku-header'})[0].text.replace('”', '"').replace('–', '-')
            product_model = items.findAll('span', {'class': 'sku-value'})[0].text.replace(" ", "")
            if search_item == "laptop" or search_item == "desktop pc":
                parsed_product_name = product_name.split(' - ')
                brand = parsed_product_name[0].strip()
                model = parsed_product_name[1]
                new_model = re.sub(r'\d+\.?\d?\"\s', '', model)
                new_model2 = re.sub('\s*Laptop\s*','',new_model).strip()
                string_to_search = parsed_product_name[1:-1]
                # proc_pattern = "AMD\sRyzen\s\w+|AMD\s\w+-\w+|Intel\s\w+\s?\w*"
                # video_pattern = "AMD Radeon[\s\w]+[^\s-]|NVIDIA[\s\w]+-?[^\s]"
                # screen_pattern = '\d+\.?\d?\"'
                # ram = ""
                # hard_drive = ""
                # lala = re.compile(screen_pattern)

                hd_pattern = re.compile(r'(\d+GB)|(\d+TB)')
                color = parsed_product_name[-1].strip()

                # screen_size = re.search(screen_pattern, product_name)
                # if bool(screen_size) == True:
                #     screen = screen_size.group().strip()
                # else:
                #
                #     screen = None

                screen = quick_search('\d+\.?\d?\"', product_name)
                print(product_name)

                # processor_search = re.search(proc_pattern, product_name)
                # if bool(processor_search) == True:
                #     processor_name = processor_search.group().strip()
                # else:
                #     processor_name = None

                processor_name = quick_search('AMD\sRyzen\s\w+|AMD\s\w+-\w+|Intel\s\w+\s?\w*', product_name)

                video_card_name = quick_search('AMD Radeon[\s\w]+[^\s-]|NVIDIA[\s\w]+-?[^\s]', product_name)

                # video_search = re.search(video_pattern, product_name)
                # if bool(video_search) == True:
                #     video_name = video_search.group().replace(' -', '').strip()
                # else:
                #     video_name = None

                for element in string_to_search:
                    if hd_pattern.search(element):
                        if "GB Memory" not in element:
                            hard_drive = re.sub(r'\([\w\s]+\)', '', element).strip()
                            print(hard_drive)
                            print(element)
                        else:
                            ram = element.strip()
                            print(element)
                print(new_model2)
                page_line = '"{brand}"\t"{screen}"\t"{model}"\t"{processor_name}"\t"{ram}"\t"{video}"\t"{hard_drive}"\t"{color}"\t"{product_model}"' \
                            '\n'.format(brand=brand, model=new_model2, video=video_card_name, color=color, processor_name=processor_name.strip(), ram=ram,
                                      hard_drive=hard_drive, screen=screen.strip(), product_model=product_model, product_name=product_name)
                textfile.write(page_line)

            elif search_item == "tv":
                parsed_product_name = product_name.split(' - ')
                print(parsed_product_name)
                brand = parsed_product_name[0].replace("™", '')

                screen = quick_search('\d+\.?\d?\"', product_name)
                tv_class = quick_search('(LED)|(OLED)', product_name)
                tv_series = quick_search('\w+\sSeries', product_name)
                resolution = quick_search('\d+p',product_name)

                description = parsed_product_name[-1]
                page_line = '"{brand}"\t"{screen_size}"\t"{tv_class}"\t"{resolution}"' \
                            '\t"{tv_series}"\t"{description}"\t"{product_model}"' \
                            '\n'.format(product_model=product_model, resolution=resolution, brand=brand, screen_size=screen.replace('"', ''), tv_class=tv_class, tv_series=tv_series, description=description)
                textfile.write(page_line)
            else:
                page_line = '"{product_name}"\t"{product_model}"\n'.format(product_name=product_name, product_model=product_model)
                textfile.write(page_line)

    page = page +1
    sleep(2)
