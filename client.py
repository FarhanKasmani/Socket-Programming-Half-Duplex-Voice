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

frames_input = []
frames_output = []

def send():
	data  = stream_input.read(CHUNK)
	frames_input.append(data)
	server.sendall(data)	

def receive(read_sockets):

	for socks in read_sockets: 
		if socks == server: 
			data = socks.recv(1024) 
			stream_output.write(data)
			frames_output.append(data)
			print("Recieved message: ")
			print(data)
 
while True: 
   
    sockets_list = [sys.stdin, server]

    read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])
    receive(read_sockets)
    
    # for i in range(0, int(RATE/CHUNK*RECORD_SECONDS)):
    # 	send()

server.close() 