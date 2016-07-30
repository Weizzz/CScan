from app import app
from app.Views.views import render

@app.route('/')
def home():
    return render('index.html', extra='')
