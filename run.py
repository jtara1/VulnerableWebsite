from app import app


""" Vulnerability 1
Run the app in debug mode so anyone on the network can access the running
instance of the web app. Since debug mode is enable too, anyone can run arbitrary 
Python code on the computer running this app
"""
app.run(debug=True, host='0.0.0.0')
# safely run the app such that only the PC running it has access to webpage of the app
# app.run(debug=False)