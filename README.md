PiGuard Lite

PiGuard Liteis a lightweight, no-root network monitor designed for Termux on Android devices. It offers a simple web interface to view active network connections.

Features

- No root access required
- Real-time display of active network connections
- Web interface accessible via `http://127.0.0.1:8080`

Installation

1. Install Dependencies:

   bash
   pkg update && pkg upgrade
   pkg install python iproute2
   pip install flask
