# Client-Server
A small project to get familiar with sockets and basic detection. You can craft both TCP and UDP packets. I developed a server and client model to develop over time, and to later aid testing of intrusion detection and firewalling. I can play both attack and defence by altering code for a given attack, with this being a solid base.

## Usage
python3 PacketServer.py -tcp/udp <port>
python3 PacketClient.py -tcp/udp <host> <port>
  

 ## Built With:

 * [Python3](https://docs.python.org/3.6/) - The language used
 * [Sockets](https://docs.python.org/3/library/socket.html) - Used for pseudo low level packet crafting

 ## TODO:
 * Raw sockets: spoofed sender support
 * Payload support
 * UDP scanning detection
 * Fragmented scan detection
 * DoS detection with ICMP listener
 * Nicer message output
 * Proper comments & docs

## Authors:

* **Carl Slatter** - *Creation* - [Carlslatter16](https://github.com/carlslatter16)
