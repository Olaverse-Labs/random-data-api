#!/usr/bin/env python3
"""
Test script for Random Data Generator API
"""

import requests
import json
import time
from typing import Dict, Any

BASE_URL = "http://localhost:8000"

def test_endpoint(endpoint: str, description: str, params: Dict[str, Any] = None) -> bool:
    """Test a single endpoint"""
    try:
        url = f"{BASE_URL}{endpoint}"
        response = requests.get(url, params=params, timeout=10)
        
        if response.status_code == 200:
            print(f"✅ {description}")
            return True
        else:
            print(f"❌ {description} - Status: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ {description} - Error: {e}")
        return False

def main():
    print("🧪 Testing Random Data Generator API")
    print("=" * 50)
    
    # Test basic endpoints
    tests = [
        ("/", "Root endpoint"),
        ("/api/health", "Health check"),
        ("/api/person", "Single person data"),
        ("/api/person/bulk", "Bulk person data", {"count": 3}),
        ("/api/company", "Single company data"),
        ("/api/company/bulk", "Bulk company data", {"count": 3}),
        ("/api/credit-card", "Credit card data"),
        ("/api/product", "Product data"),
        ("/api/technical", "Technical data"),
        ("/api/custom", "Custom data - emails", {"data_type": "email", "count": 3}),
        ("/api/custom", "Custom data - names", {"data_type": "name", "count": 3}),
        ("/api/custom", "Custom data - addresses", {"data_type": "address", "count": 3}),
    ]
    
    passed = 0
    total = len(tests)
    
    for endpoint, description, *params in tests:
        params = params[0] if params else None
        if test_endpoint(endpoint, description, params):
            passed += 1
        time.sleep(0.1)  # Small delay between requests
    
    print("=" * 50)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! API is working correctly.")
    else:
        print("⚠️  Some tests failed. Please check the API.")
    
    # Test with different locales
    print("\n🌍 Testing different locales:")
    locale_tests = [
        ("en_US", "English (US)"),
        ("en_GB", "English (UK)"),
        ("de_DE", "German"),
        ("fr_FR", "French"),
    ]
    
    for locale, name in locale_tests:
        if test_endpoint("/api/person", f"Person data ({name})", {"locale": locale}):
            print(f"   ✅ {name} locale works")
        else:
            print(f"   ❌ {name} locale failed")

if __name__ == "__main__":
    main() 