#!/usr/bin/python3
import sys
import signal

def print_stats(total_size, status_codes):
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

def signal_handler(sig, frame):
    print_stats(total_size, status_codes)
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

total_size = 0
status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
line_count = 0

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) >= 9:
            ip, date, path, status, size = parts[:5]
            if path == '"GET /projects/260 HTTP/1.1"':
                total_size += int(size)
                if status in status_codes:
                    status_codes[status] += 1
                line_count += 1

                if line_count % 10 == 0:
                    print_stats(total_size, status_codes)

except KeyboardInterrupt:
    print_stats(total_size, status_codes)
    sys.exit(0)
  
