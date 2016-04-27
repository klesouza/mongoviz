import os
from mongoviz import app


def runserver():
    port = int(os.environ.get('PORT', 5000))
    app.run(host=os.environ.get('WEB_HOST', '127.0.0.1'), port=port, debug=True)

if __name__ == '__main__':
    runserver()