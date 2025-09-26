#!/usr/bin/env python3
"""
Startup verification script for AgroSmart Backend
Tests all critical components before main launch
"""

import sys
import importlib.util

def test_imports():
    """Test required imports"""
    try:
        import flask
        import flask_cors
        import datetime
        import json
        print("✅ All required imports available")
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("Run: pip install Flask Flask-CORS")
        return False

def test_backend_syntax():
    """Test backend file syntax"""
    try:
        with open('agrosmart_api_bulletproof.py', 'r') as f:
            code = f.read()
        compile(code, 'agrosmart_api_bulletproof.py', 'exec')
        print("✅ Backend syntax verification passed")
        return True
    except Exception as e:
        print(f"❌ Backend syntax error: {e}")
        return False

def main():
    print("🚀 AgroSmart Backend Startup Verification")
    print("=" * 50)

    tests = [
        ("Import Dependencies", test_imports),
        ("Backend Syntax", test_backend_syntax)
    ]

    all_passed = True
    for test_name, test_func in tests:
        print(f"\n🧪 Testing {test_name}...")
        if not test_func():
            all_passed = False

    if all_passed:
        print("\n✅ ALL TESTS PASSED - Backend ready to start!")
        print("Run: python agrosmart_api_bulletproof.py")
    else:
        print("\n❌ Some tests failed - check errors above")

    return all_passed

if __name__ == "__main__":
    main()
