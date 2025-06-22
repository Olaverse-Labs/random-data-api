#!/usr/bin/env python3
"""
Startup script for Random Data Generator API
"""

import uvicorn
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Random Data Generator API")
    parser.add_argument("--host", default="0.0.0.0", help="Host to bind to (default: 0.0.0.0)")
    parser.add_argument("--port", type=int, default=8000, help="Port to bind to (default: 8000)")
    parser.add_argument("--reload", action="store_true", help="Enable auto-reload for development")
    parser.add_argument("--workers", type=int, default=1, help="Number of worker processes (default: 1)")
    
    args = parser.parse_args()
    
    print("🚀 Starting Random Data Generator API...")
    print(f"📍 Host: {args.host}")
    print(f"🔌 Port: {args.port}")
    print(f"🔄 Reload: {args.reload}")
    print(f"👥 Workers: {args.workers}")
    print()
    print("📚 API Documentation:")
    print(f"   Swagger UI: http://{args.host}:{args.port}/docs")
    print(f"   ReDoc: http://{args.host}:{args.port}/redoc")
    print()
    print("🎯 Example endpoints:")
    print(f"   GET http://{args.host}:{args.port}/api/person")
    print(f"   GET http://{args.host}:{args.port}/api/company")
    print(f"   GET http://{args.host}:{args.port}/api/credit-card")
    print()
    
    try:
        uvicorn.run(
            "main:app",
            host=args.host,
            port=args.port,
            reload=args.reload,
            workers=args.workers
        )
    except KeyboardInterrupt:
        print("\n👋 API stopped by user")
    except Exception as e:
        print(f"❌ Error starting API: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 