import certifi
import os
import ssl
import socket

try:
    from httplib import HTTPSConnection
except ImportError:
    from http.client import HTTPSConnection


class ValidatedHTTPSConnection(HTTPSConnection):

    def connect(self):
        # Function used to wrap sockets with SSL
        contextInstance = ssl.SSLContext();
        contextInstance.verify_mode = ssl.CERT_REQUIRED;
        contextInstance.load_verify_locations(cafile=os.path.relpath(certifi.where()),
                                              capath=None, cadata=None);
        socketInstance = socket.create_connection((self.host, self.port),
                                        self.timeout,
                                        self.source_address)
        _SocketWrapper = contextInstance.wrap_socket(socketInstance);
        # _SocketWrapper = ssl.wrap_socket
        self.sock = _SocketWrapper
