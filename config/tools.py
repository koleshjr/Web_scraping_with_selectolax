import json
_config = {
    "url" : "https://store.steampowered.com/specials",
    "container": {
        "name": 'store_sale_divs',
        "selector": 'div[class*="salepreviewwidgets_StoreSaleWidgetOuterContainer"]',
        "match": 'all',
        "type": 'node'

    },

    "item":[
    {
        "name": 'title',
        "selector": 'div[class*="StoreSaleWidgetTitle"]',
        "match": 'first',
        "type": 'text',
    },

    {
        "name": 'thumbnail',
        "selector": 'img[class*="CapsuleImage"]',
        "match": 'first',
        "type": 'node',
    },
    {
        "name": 'tags',
        "selector": 'div[class*="StoreSaleWidgetTags"] > a',
        "match": 'all',
        "type": 'text',
    },
    {
        "name": 'release_date',
        "selector": 'div[class*="WidgetReleaseDateAndPlatformCtn"] > div[class*="StoreSaleWidgetRelease"]',
        "match": 'first',
        "type": 'text',
    },    
    {
        "name": 'review_score',
        "selector": 'div[class*="ReviewScoreValue"] > div',
        "match": 'first',
        "type": 'text',
    },       

    {
        "name": 'reviewed_by',
        "selector": 'div[class*="ReviewScoreCount"]',
        "match": 'first',
        "type": 'text',
    },   

    {
        "name": 'price_currency',
        "selector": 'div[class*="StoreOriginalPrice"]',
        "match": 'first',
        "type": 'text',
    },        

    {
        "name": 'original_price',
        "selector": 'div[class*="StoreOriginalPrice"]',
        "match": 'first',
        "type": 'text',
    },    
    {
        "name": 'selling_price',
        "selector": 'div[class*="StoreSalePriceBox"]',
        "match": 'first',
        "type": 'text',
    },       
               
        



 


    ]
}

def generate_config():
    with open("config.json", "w") as f:
        json.dump(_config, f, indent=4)

def get_config(load_from_file = False):
    if load_from_file:
        with open("config.json", "r") as f:
            return json.load(f)
        
    return _config

if __name__ == "__main__":
    generate_config()