from socket import gethostname, gethostbyname
from REST.REST import create

if __name__ == '__main__':

    app = create()
    host_address = gethostbyname(gethostname())
    app.run(host=host_address, port=5000, debug=True)