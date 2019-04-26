from flask import Flask, render_template, flash, request
import pandas as pd

# Having problems getting this to run?
# Make sure you're in the correct virtual environment
# Make sure you're in the correct path
# Use flask run
# If that doesn't fix it, you're on your own

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


# The details for the below will vary by project. For help, see:
# http://flask.pocoo.org/docs/1.0/quickstart/

@app.route("/metrics")
def show_metrics():
    df = pd.read_csv('app/tables/perf_metrics.csv')

    return render_template('view.html',
                           tables=[df.to_html(classes='metrics',
                                              table_id='overall_table')],
                           titles=['na', 'Overall'])