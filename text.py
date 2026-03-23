#!/usr/bin/env python3
import socket
import struct
import time

# 和 C++ 枚举一致
CMD_CREATE = 1

def main():
    fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    fd.connect(("127.0.0.1", 5050))
    print("connected")

    # ===== body =====
    username = b"use12".ljust(32, b'\0')
    password = b"123456".ljust(32, b'\0')
    body = username + password            # 64 bytes

    # ===== head =====
    cmd = struct.pack("!I", CMD_CREATE)   # cmd
    length = struct.pack("!I", 8 + len(body))  # total length
    packet = cmd + length + body

    # ===== send =====
    fd.sendall(packet)
    print("CREATE sent")

    time.sleep(1)
    fd.close()

if __name__ == "__main__":
    main()
