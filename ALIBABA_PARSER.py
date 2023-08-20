#python
from os import mkdir
from time import sleep
from urllib.request import urlretrieve as src_to_jpg
from sys import path
path.append('/home/np_1961/parser/utils/')




import numpy as np    #pip 


#My
from browser import turn_on_the_browser as return_driver
from browser import By
from browser import scrollin
from browser import Keys
from browser import ActionChains
from browser import UserAgent
from File_workers import file_workers
from Norm_generate import get_random_url

from Terminal import terminal_write












class PARSER:
    def __init__(self, driver):
        self.driver=driver
        self.action=ActionChains(driver=driver)
        terminal_write('^'*40)
        terminal_write('---------WELCOME ALIBABA PARSER !!!')
        terminal_write('^'*40)
    def search(self,url='https://www.alibaba.com/'):
        search_text=input("Enter search_text-->")
        try:
            self.driver.get(url)
            value='[type="text"]'
            search_element=self.driver.find_element(By.CSS_SELECTOR, value)
            search_element.send_keys(search_text)
            search_element.send_keys(Keys.ENTER)
            return True
        except:
            print('---error in search text !!!')
            return False
    
    
    
    
    def page_to_page  (self, 
                       page_index=5,
                       scrolls=25,
                       file_path='true_urls/urls.txt'):
        #scroll down by page down
        [self.action.key_down(Keys.PAGE_DOWN).key_up(
                            Keys.PAGE_DOWN).perform() for scroll in range(scrolls)]
        
        
        
        #search and preprocessing to normal url
        value='[target="_blank"]'
        elements=self.driver.find_elements(By.CSS_SELECTOR, value=value)
        links=[element.get_attribute('href') for element in elements if element.get_attribute('href') ]

        #filter and set all normal url
        product_detail="//www.alibaba.com/product-detail/"
        links=list(set([link for link in links if product_detail in link ]))

        #save good url in txt file
        save_text=[file_workers.add_url(url=url , file_path=file_path) for url in links]
        
        #search next page value
        if page_index:
            page_index-=1
            value="seb-pagination__pages-link"
            try:
                next_page=self.driver.find_elements(By.CLASS_NAME, value)[-1]

            except:
                self.action.key_down(Keys.PAGE_UP).key_up(
                                         Keys.PAGE_UP).perform()
                sleep(4)
                next_page=self.driver.find_elements(By.CLASS_NAME, value)[-1]
            
            #go next page
            sleep(2)
            next_page.click()
            sleep(10)
            self.page_to_page(page_index=page_index)
        return True
    
    
    
    def photo_downloader(self,
                         link_quantity=50,
                         new_folder_name=0,
                         file_path='true_urls/urls.txt'):
        
        
        if link_quantity is None:
            link_quantity=int(input("How many links do you need to check ? --->"))
        
        
        
        #create index + 1 folder 
        try:
            mkdir(f"pictures/{new_folder_name}")
        except:
            new_folder_name+=1
            self.photo_downloader(link_quantity=link_quantity,
                                  new_folder_name=new_folder_name)
        
        
        #get random url in txt file
        url=get_random_url(urls=file_workers.txt_file_update(file_path=file_path))
        file_workers.del_url(url=url,
                            file_path=file_path)
        
        #go website
        self.driver.get(url)
        
        #open picture window
        try:
            value='[aria-posinset="2"]'
            self.driver.find_element(By.CSS_SELECTOR, value).click()
            
            value="main-index"
            photo_window=self.driver.find_element(By.CLASS_NAME, value).click()
            sleep(8)
            
        except:
            self.photo_downloader(link_quantity=link_quantity,
                                  new_folder_name=new_folder_name)

        #get photo quantity
        value="slider-list"
        window_element=self.driver.find_element(By.CLASS_NAME, value)
        photo_elements=window_element.find_elements(By.TAG_NAME, 'div')
        photo_quantity=len(photo_elements)
        
        
        
        #del bad grafics photo 
        elements=[element for element in self.driver.find_elements(By.TAG_NAME, 'img') if element.get_attribute('loading')=="lazy"]
        srcs=[element.get_attribute('src') for element in elements if element.get_attribute('src')]
        srcs=srcs[::-1]
        srcs=srcs[len(photo_elements):len(photo_elements)*2]
        
        
        #create folder and dowload good grafict photo
        print('---create new folder name --->',new_folder_name)
        [src_to_jpg(src, f"pictures/{new_folder_name}/{photo_index}.jpg") for photo_index,src in enumerate(srcs)]
        self.driver.implicitly_wait(10)
        print('------download photo --->',len(photo_elements))
        
        #recurse
        link_quantity-=1
        new_folder_name+=1
        if link_quantity:
            self.photo_downloader(link_quantity=link_quantity,
                                  new_folder_name=new_folder_name)
        else:
            print('---all photo downloading  !!!')
            raise SystemExit('FINISH !!!')
def Parser(search=False):
    if search:
        driver=return_driver()
        parser=PARSER(driver=driver)
        parser.search()
        parser.page_to_page(page_index=15)
    else:
        driver=return_driver()
        parser=PARSER(driver=driver)
        parser.photo_downloader()

    
    
