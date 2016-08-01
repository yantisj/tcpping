#!/usr/bin/env python3
"""
TCP Ping Test (defaults to port 80, 10000 packets)

Usage: ./tcpping.py host [port] [maxCount]
- Ctrl-C Exits with Results
"""

import sys
import socket
import time
import signal
from timeit import default_timer as timer

host = None
port = 80

# Default to 10000 connections max
maxCount = 10000
count = 0

## Inputs

# Required Host
try:
    host = sys.argv[1]
except IndexError:
    print("Usage: tcpping.py host [port] [maxCount]")
    sys.exit(1)

# Optional Port
try:
    port = int(sys.argv[2])
except ValueError:
    print("Error: Port Must be Integer:", sys.argv[3])
    sys.exit(1)
except IndexError:
    pass

# Optional maxCount
try:
    maxCount = int(sys.argv[3])
except ValueError:
    print("Error: Max Count Value Must be Integer", sys.argv[3])
    sys.exit(1)
except IndexError:
    pass

# Pass/Fail counters
passed = 0
failed = 0


def getResults():
    """ Summarize Results """

    lRate = 0
    if failed != 0:
        lRate = failed / (count) * 100
        lRate = "%.2f" % lRate

    print("\nTCP Ping Results: Connections (Total/Pass/Fail): [{:}/{:}/{:}] (Failed: {:}%)".format((count), passed, failed, str(lRate)))

def signal_handler(signal, frame):
    """ Catch Ctrl-C and Exit """
    getResults()
    sys.exit(0)

# Register SIGINT Handler
signal.signal(signal.SIGINT, signal_handler)

# Loop while less than max count or until Ctrl-C caught
while count < maxCount:

    # Increment Counter
    count += 1

    success = False

    # New Socket
    s = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)

    # 1sec Timeout
    s.settimeout(1)

    # Start a timer
    s_start = timer()

    # Try to Connect
    try:
        s.connect((host, int(port)))
        s.shutdown(socket.SHUT_RD)
        success = True
    
    # Connection Timed Out
    except socket.timeout:
        print("Connection timed out!")
        failed += 1
    except OSError as e:
        print("OS Error:", e)
        failed += 1

    # Stop Timer
    s_stop = timer()
    s_runtime = "%.2f" % (1000 * (s_stop - s_start))

    if success:
        print("Connected to %s[%s]: tcp_seq=%s time=%s ms" % (host, port, (count-1), s_runtime))
        passed += 1

    # Sleep for 1sec
    if count < maxCount:
        time.sleep(1)

# Output Results if maxCount reached
getResults()
