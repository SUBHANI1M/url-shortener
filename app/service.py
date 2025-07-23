import hashlib
from .storage import save_url_mapping, get_url_mapping
from .utils import sanitize_url

def shorten_url(original_url):
    original_url = sanitize_url(original_url)
    code = hashlib.md5(original_url.encode()).hexdigest()[:6]
    save_url_mapping(code, original_url)
    return f"/{code}"
def get_original_url(code):
    return get_url_mapping(code)
