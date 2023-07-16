import requests
from bs4 import BeautifulSoup


url = "https://www.giztop.com/phones.html"
base_url = "https://www.giztop.com/"

class Giztop_Pruduct: 
    def __init__(self, title : str, price : str, description : str) :
        self.title = title
        self.price = price
        self.description = description

def Get_all_current_products ():
    ''' Get all current product from giztop.com

    return :
        product_link (list): list of product links '''
    
    # land on page
    url_data = requests.get(url)
    soup = BeautifulSoup(url_data.text, 'html.parser')

    # Get products
    product_links = set()
    product_divs = soup.find_all("li", class_="item product product-item")
    for product_div in product_divs:
        link_tag = product_div.find("a")
        product_links.add(link_tag.get("href"))

    #  # get next pages
    # page_set = set()
    # data = soup.find("div", class_="pagination")
    # pages = data.find_all("a")
    # for page in pages:
    #     new_url = base_url + page.get("href")
    #     page_set.add(new_url)


    return product_links


# get information from specific products

def get_product_info (product_url):

     """
    Get product name, price and description for Giztop.com

    Arguments:
        product_url: a string 

    Returns:
        product_title (string): Title of product 
        product_price (string): price of product
        product_description (string): description of product
    """
     page_data = requests.get(product_url)
     product_soup = BeautifulSoup(page_data.text, 'html.parser')   


     #   # get product details 
    # product_details_div = product_soup.find("div", {"id": "product-details"})
    # details_section = product_details_div.find("p")
    # product_details = details_section.text 
 

    #  get product title 
     prod_title_div = product_soup.find("h1", {"class": "page-title"})
     product_title = prod_title_div.text
     
     # get product price
     product_price_div = product_soup.find("span", {"class": "price"})
     product_price = product_price_div.text

    # get product description 
     product_description_div = product_soup.find("div", {"class": "product attribute overview"})
     product_des_section = product_description_div.find("li")
     product_description = product_description_div.text

     return Giztop_Pruduct (product_title, product_price, product_description) 


if __name__ == "__main__":
    product_links = Get_all_current_products()

     # Print product links to a file
    with open("Giztop_product_links.txt", "w") as file:
        for link in product_links:
            file.write(link + "\n")

