#!/usr/bin/env python3
"""
Simple web server to run the Virtual Memory Simulator web application.

Copyright (c) 2026 Sai Spoorthy Eturu
Licensed under the MIT License - see LICENSE file for details.

Part of the Virtual Memory Simulator educational platform.
"""

import http.server
import socketserver
import webbrowser
import os
import sys

def run_server(port=8000):
    """Run a simple HTTP server to serve the web application."""
    
    # Change to the directory containing the HTML file
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Create server
    handler = http.server.SimpleHTTPRequestHandler
    
    try:
        with socketserver.TCPServer(("", port), handler) as httpd:
            print(f"╔{'═' * 60}╗")
            print(f"║{'Virtual Memory Simulator Web Server':^60}║")
            print(f"╚{'═' * 60}╝")
            print(f"\n🌐 Server running at: http://localhost:{port}")
            print(f"📁 Serving file: web_simulator.html")
            print(f"\n🚀 Opening browser automatically...")
            print(f"💡 If browser doesn't open, manually visit: http://localhost:{port}/web_simulator.html")
            print(f"\n⏹️  Press Ctrl+C to stop the server")
            print(f"{'─' * 60}")
            
            # Try to open browser automatically
            try:
                webbrowser.open(f'http://localhost:{port}/web_simulator.html')
            except:
                print("⚠️  Could not open browser automatically")
            
            # Start server
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print(f"\n\n👋 Server stopped by user")
        sys.exit(0)
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"❌ Port {port} is already in use. Trying port {port + 1}...")
            run_server(port + 1)
        else:
            print(f"❌ Error starting server: {e}")
            sys.exit(1)

if __name__ == "__main__":
    print("🧠 Virtual Memory Simulator - Web Version")
    print("=" * 60)
    
    # Check if HTML file exists
    if not os.path.exists('web_simulator.html'):
        print("❌ web_simulator.html not found!")
        print("💡 Make sure you're running this from the correct directory")
        sys.exit(1)
    
    # Get port from command line or use default
    port = 8000
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print("⚠️  Invalid port number, using default 8000")
    
    run_server(port)