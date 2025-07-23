def sanitize_url(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        return "http://" + url
    return url
