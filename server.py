import socket

class Proxy: 
    def __init__(self):
        self.username = "username"
        self.password = "password"
        
    def run(self):
        pass

if __name__ == "__main__":
    proxy = Proxy()
    proxy.run("127.0.0.1", 3000)