import socket
import time

# TCP Socket Connection Details
HOST = "127.0.0.1"  			# Standard loopback interface address (localhost)
PORT = 9999  					# Port to listen on 
HEADER = 64						
FORMAT = 'utf-8'				
ADDR = (HOST, PORT)


def produce_data():
	# Establishing a socket on given port and host and start listening to connection attempts
	print(f"[CONNECTING] Trying to establish socket on {HOST} and port number {str(PORT)}...")
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.bind(ADDR)
	client.listen(1)
	print(f"[LISTENING] Listening on {HOST} and port number {str(PORT)}. Accepting connections...")
	conn, address = client.accept()
	print(f"[CONNECTED] Connection successfully received from {address}!")

	# Put a small delay before starting the stream
	print("[SLEEP] Sleeping 5 seconds.")
	time.sleep(5)

	# Iterate through each line in the CSV
	for line in open("/path_to_your_csv/filename.csv","r"):
		try:
			# Put a small delay of 200 ms between each message 
			time.sleep(0.2)

			# Encode the string to UTF-8
			message = line.encode(FORMAT)

			# Send the string to the socket
			conn.send(message)
		except Exception as e: 
			print(e)
	
def current_milli_time():
	return round(time.time() * 1000) # Return the current time in milliseconds rounded 

def main():
	print("[STARTING] stream is starting...")
	# Establishes a socket listening to connections
	# Once a connection is established, start iterating through the CSV and send each line to the socket
	produce_data()

if __name__ == "__main__":
	main()


