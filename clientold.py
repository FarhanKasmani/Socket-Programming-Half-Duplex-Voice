
# Python program to implement client side of chat room. 
import socket 
import select 
import sys 
import pyaudio
  
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

IP_address = '10.120.106.85'
Port = 50007
server.connect((IP_address, Port)) 

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 40
WIDTH = 2

p = pyaudio.PyAudio()

stream_input = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

stream_output = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                output=True,
                frames_per_buffer=CHUNK)

  
while True: 
  
    # maintains a list of possible input streams 
    sockets_list = [sys.stdin, server] 
  
    """ There are two possible input situations. Either the 
    user wants to give  manual input to send to other people, 
    or the server is sending a message  to be printed on the 
    screen. Select returns from sockets_list, the stream that 
    is reader for input. So for example, if the server wants 
    to send a message, then the if condition will hold true 
    below.If the user wants to send a message, the else 
    condition will evaluate as true"""
    read_sockets,write_socket, error_socket = select.select(sockets_list,[],[]) 
  
    frames_input = []
    frames_output = []

    for i in range(0, int(RATE/CHUNK*RECORD_SECONDS)):
        data  = stream_input.read(CHUNK)
        frames_input.append(data)
        server.sendall(data)
        # t = input("Enter number:")

    # for socks in read_sockets: 
    #     if socks == server: 
    #         data = socks.recv(1024) 
    #         stream_output.write(data)
    #         frames_output.append(data)
    #         print("Recieved message: ")
    #         print(data)
    #     else: 
    #         for i in range(0, int(RATE/CHUNK*RECORD_SECONDS)):
    #             print(i)
    #             data  = stream_input.read(CHUNK)
    #             frames_input.append(data)
    #             server.sendall(data)

            # message = input() 
            # server.send(message.encode()) 
            # sys.stdout.write("<You>") 
            # sys.stdout.write(message) 
            # sys.stdout.flush() 
server.close() 