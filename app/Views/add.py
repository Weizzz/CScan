from app import app
from app.Forms.add import regoForm
from flask import request, redirect, url_for
from app.Views.views import render

@app.route('/add', methods=['GET', 'POST'])
def add():

    form = regoForm(request.form)
    if request.method == 'POST' and form.validate():
        return redirect(url_for('home'))

    return render('add.html', form=form)
