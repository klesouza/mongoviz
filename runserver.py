import os
from mongoviz import app


def runserver():
    port = int(os.environ.get('PORT', 5000))
    app.run(port=port, debug=True)

if __name__ == '__main__':
    runserver()