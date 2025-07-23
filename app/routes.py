from flask import Blueprint, request, render_template, redirect, abort
from .service import shorten_url, get_original_url

main = Blueprint('main', __name__)
@main.route("/", methods=["GET", "POST"])
def index():
    short_url = None
    error = None
    if request.method == "POST":
        original_url = request.form.get("url")
        if not original_url:
            error = "Please enter a URL."
        else:
            short_url = shorten_url(original_url)
    return render_template("index.html", short_url=short_url, error=error)

@main.route("/<code>")
def redirect_to_original(code):
    url = get_original_url(code)
    if url:
        return redirect(url)
    else:
        abort(404)
