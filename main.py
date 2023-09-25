
from config.tools import get_config
from utils.extract import extract_full_body_html
from utils.parse import parse_raw_attributes
from utils.processing import format_and_transforms, save_to_file


if __name__ == "__main__":
        config = get_config()
        URL = config.get('url')

        html = extract_full_body_html(from_url = URL, 
                                      wait_for=config.get("container").get("selector"))
        nodes = parse_raw_attributes(html, [config.get('container')])

        game_data = []
        for node in nodes.get('store_sale_divs'):
            #parse the values
            attrs = parse_raw_attributes(node, config.get('item'))
            #formatting
            attrs = format_and_transforms(attrs)
            game_data.append(attrs)
            # print(attrs)

            #save to some csv file
            save_to_file("extract", game_data)



