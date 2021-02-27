import os

from src.application import create_app

app = create_app()

if __name__ == '__main__':
    os.environ['CACHE_HOST'] = 'localhost'
    os.environ['CACHE_PORT'] = '11211'

    app.run(debug=True,
            threaded=True,
            host='0.0.0.0',
            port=5555)
