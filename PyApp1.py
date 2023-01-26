PyApp1.py
---------

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Web App with Python Flask!'

app.run(host='0.0.0.0', port=5000)

-----End Code----

Once, the app is run
by

(PythonDevEnv) devops@devops:~/Python_Projects/PyApp1$ NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program python3 app1.py  
 The NewRelic App is activated..

For every page request a bar diagram is shown in Nrelic

We can customize the view on Dashboard or Specific Query (NRQL) could be written 
to generate alert on email....

---------Happy-------
