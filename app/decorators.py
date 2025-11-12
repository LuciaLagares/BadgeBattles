from functools import wraps
from flask import session, redirect, url_for

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "trainer" not in session:
            return redirect(url_for("home.welcome"))
        return func(*args, **kwargs)
    return wrapper