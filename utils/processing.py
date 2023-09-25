import re
import pandas as pd
from datetime import datetime
from selectolax.parser import Node


def get_attrs_from_node(node: Node, attr: str):
    if node is None or not issubclass(Node, type(node)):
        raise ValueError("The function expects a selectolax node to be provided")
    
    return node.attributes.get(attr)

def get_first_n(input_list: list, n:int = 5):
    return input_list[:5]

def reformat_date(date_raw:str , from_format: str = '%b %d, %Y', to_format: str = '%Y-%m-%d'): #datetime library
    dt_obj = datetime.strptime(date_raw, from_format)
    return datetime.strftime(dt_obj, to_format)

def regex(input_str: str, pattern: str, do_what: str= "findall"):
    if do_what == "findall":
        return re.findall(pattern, input_str)
    elif do_what == "split":
        return re.split(pattern, input_str)
    else:
        raise ValueError("The function expects 'findall' or 'split' to be provided")

def format_and_transforms(attrs: dict):
    transforms = {
        "thumbnail": lambda n: get_attrs_from_node(n, "src"),
        "tags": lambda input_list: get_first_n(input_list, 5),
        "release_date": lambda date: reformat_date(date, '%b %d, %Y', '%Y-%M-%d'),
        "reviewed_by": lambda raw: int(''.join(regex(raw, r'\d+', "findall"))),
        "price_currency": lambda raw: regex(raw, r'(\D+)(\d+\.\d+)', "split")[1],
        "original_price": lambda raw: float(regex(raw, r'(\D+)(\d+\.\d+)', "split")[2]),
        "selling_price": lambda raw: float(regex(raw,r'(\D+)(\d+\.\d+)', "split")[2]),

    }

    for k, v in transforms.items():
        if k in attrs:
            attrs[k] = v(attrs[k])

    return attrs

def save_to_file(filename = "extract", data: list[dict] = None):
    if data is None:
        raise ValueError("The function expects data to be provided as a list of dictionaries")
    
    df = pd.DataFrame(data)
    filename = f"{datetime.now().strftime('%Y_%m_%d')}_{filename}.csv"
    df.to_csv(filename, index = False)