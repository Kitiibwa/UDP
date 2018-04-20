import socket # import socket module

class UDP_Server:
    """
    TUDP server responds to requests from a client at
    specified host and port.
    """
    def __init__(self,host=socket.gethostname(),port=0,BUFFERSIZE=0):   #host gets localhost
        self.host = host
        self.port = port
        self.BUFFERSIZE =BUFFERSIZE
        
        self.port = 7101    # an arbitrary non-privileged port
        self.BUFFERSIZE = 1024   # set buffer size for data to be received
    
    def sending(self):
        # create a socket object and assign it to variable s
        with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as s:
            s.bind((self.host,self.port))   # bind the socket to the (host,port) tuple
        
            while True:
                # receive request message and client's address 
                data, addr = s.recvfrom(self.BUFFERSIZE)
                print('Received from client {}:\n\t {}'.format(addr, data)) #display received data
                
                # message to be sent to client
                s_response = "High temperatures of 71C with lows of 69C!" 
                # encoding the message to be sent
                s.sendto(s_response.encode('utf-8'),addr)
        
if __name__ == '__main__':
    server1=UDP_Server() # make instance of UDP_Server class
    server1.sending()   # call the sending() method