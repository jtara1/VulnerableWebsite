from app import app


""" Vulnerability 1
Run the app in debug mode so the stack trace is printed
to the web browser when there's an internal error.
"""
app.run(debug=True, host='0.0.0.0')
# app.run(debug=False)