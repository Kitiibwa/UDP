import socket

class UDP_Client:
    """
    This UDP client requests for data from a server at
    specified host and port.
    """
    def __init__(self,host=socket.gethostname(),port=0,BUFFERSIZE=0):   #host gets localhost
        self.host = host
        self.port = port
        self.BUFFERSIZE =BUFFERSIZE
        
        self.port = 7101    # an arbitrary non-privileged port
        self.BUFFERSIZE = 1024   # set buffer size for data to be received

    def requesting(self):
        # create a socket object and assign it variable c
        with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as c:
            
            # request message to be sent to server
            c_request = 'What is the weather in Kampala?'
            # send encoded message request to server
            c.sendto(c_request.encode('utf-8'),(self.host, self.port))
            # receive message from server
            data, addr = c.recvfrom(self.BUFFERSIZE)
            print('Server Response at {}:\n\t{}'.format(addr, data))     #display received data
        c.close()
if __name__ == '__main__':
    client1=UDP_Client()    # make an instance of the UDP_Client class 
    client1.requesting()    # call the requesting() method