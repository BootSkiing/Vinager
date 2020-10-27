# Vinager
Proof of concept botnet controller covert channel via DNS packets


## DNS Packets as a Covert Channel
DNS is an integral part of any network infustructure. This means that most firewalls will allow packet travel through that port (53). By hand crafting a DNS query/response, it is possible to encode data in mny of the fields that the DNS protocol requires.

### Detection
This idea is not fool-proof. The form of encoding and the fields used will make or break this channel. Firewalls performing deep packet inspection can detect if something doesn't add up, or can be tuned to check for your the CCs fingerprint. For example, my current implimentation uses the query field to hide a base64 encoded message. You could block this kind of packet by checking for a valid domain name structure, and blocking any npn-valid queries

## Reflected Commands
To aid in the concealment of the the controller, packet reflection is used. The idea is that the sender will "bounce" the DNS query off of a legitamte DNS server to the receiver. This is done by spoofing the source address of the query to be the target IP. The DNS server will recieve the packet from the sender, and then send a response to the receiver. It helps that queries/replies are made with UDP anyway.

## Usage
At the momoement everything is hard-coded. Come back soon!
