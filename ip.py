#!/usr/bin/env python3
import socket

def is_ip4(address):
    try:
        socket.inet_aton(address)
    except socket.error:
        return False
    return True

def is_ip6(address):
    try:
        socket.inet_pton(socket.AF_INET6, address)
    except socket.error:
        return False
    return True

def is_ip(address):
    return is_ip4(address) or is_ip6(address)


### Main Program If Called Directly
def main():
    import argparse
    # Parse The Command Line Arguements
    parser = argparse.ArgumentParser(description = "Test If IP Address Is Valid Or Not")
    parser.add_argument('address', metavar = 'IP', type=str, help = "IP Address To Test")
    args = parser.parse_args()

    # Execute Check
    if is_ip(args.address):
        print("The IP Address %s Is Valid." % (args.address))
    else:
        print ("The IP Address %s Is Invalid." % (args.address))

if __name__ == "__main__":
    main()

