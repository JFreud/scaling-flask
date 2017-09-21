from flask import Flask

my_app = Flask(__name__)

@my_app.route('/')
def root():
    print "link start"
    return "<h1> Welcome </h1>"


@my_app.route('/foo')
def branch():
    return '''<!DOCTYPE html>
<html>
<head>
  <title>Softdev HW</title>
  <style>
			body {
				background-image: url("http://searchengineland.com/figz/wp-content/seloads/2014/08/maps-local-search1-ss-1920-800x450.jpg");
				background-attachment: fixed;
				background-repeat: no-repeat;
				background-size:cover;
			}
             </style>
</head>
</html>
			'''


@my_app.route('/profile')
def leaf():
    return "its me"


if __name__ == "__main__":
    my_app.debug = True
    my_app.run()
