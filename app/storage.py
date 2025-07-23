url_mapping = {}

def save_url_mapping(code, original_url):
    url_mapping[code] = original_url
def get_url_mapping(code):
    return url_mapping.get(code)
