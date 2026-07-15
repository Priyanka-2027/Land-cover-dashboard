#!/usr/bin/env python3
"""
Test script to verify dashboard model loading works correctly.
This simulates the exact model loading logic from the dashboard.
"""

import os
import sys
import joblib

# Add project paths
sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.join(os.path.dirname(__file__), 'dashboard'))

def simulate_dashboard_load_model():
    """Simulate the exact load_model function from dashboard."""
    print("🔄 Simulating Dashboard Model Loading...")
    
    # Exact same logic as in dashboard/app.py
    possible_paths = [
        'models/model.pkl',           # When running from landcover-project/
        '../models/model.pkl',        # When running from landcover-project/dashboard/
        os.path.join('..', 'models', 'model.pkl'),
        os.path.join(os.path.dirname(__file__), '..', 'models', 'model.pkl')
    ]
    
    print(f"📁 Current directory: {os.getcwd()}")
    print(f"📁 Script file: {__file__}")
    print(f"📁 Script directory: {os.path.dirname(__file__)}")
    
    for i, model_path in enumerate(possible_paths, 1):
        print(f"\n🔍 Testing path {i}: {model_path}")
        abs_path = os.path.abspath(model_path)
        print(f"   Absolute: {abs_path}")
        print(f"   Exists: {os.path.exists(model_path)}")
        
        if os.path.exists(model_path):
            try:
                model = joblib.load(model_path)
                print(f"   ✅ SUCCESS! Model loaded from: {model_path}")
                print(f"   📊 Model type: {type(model).__name__}")
                return model
            except Exception as e:
                print(f"   ❌ Error loading: {str(e)}")
                continue
    
    print("\n❌ No model found in any path!")
    return None

def simulate_dashboard_from_dashboard_dir():
    """Simulate running from dashboard directory."""
    print("\n🔄 Simulating from Dashboard Directory...")
    
    # Change to dashboard directory perspective
    dashboard_dir = os.path.join(os.path.dirname(__file__), 'dashboard')
    print(f"📁 Dashboard directory: {dashboard_dir}")
    
    # Paths as they would be seen from dashboard/
    possible_paths = [
        '../models/model.pkl',        # When running from landcover-project/dashboard/
        os.path.join('..', 'models', 'model.pkl'),
        os.path.join(os.path.dirname(dashboard_dir), 'models', 'model.pkl')
    ]
    
    for i, model_path in enumerate(possible_paths, 1):
        print(f"\n🔍 Dashboard path {i}: {model_path}")
        
        # Resolve relative to dashboard directory
        if not os.path.isabs(model_path):
            full_path = os.path.join(dashboard_dir, model_path)
        else:
            full_path = model_path
            
        abs_path = os.path.abspath(full_path)
        print(f"   Full path: {full_path}")
        print(f"   Absolute: {abs_path}")
        print(f"   Exists: {os.path.exists(full_path)}")
        
        if os.path.exists(full_path):
            try:
                model = joblib.load(full_path)
                print(f"   ✅ SUCCESS from dashboard dir!")
                return model
            except Exception as e:
                print(f"   ❌ Error: {str(e)}")
    
    return None

def test_streamlit_cache_behavior():
    """Test if there might be caching issues."""
    print("\n🔄 Testing Streamlit Cache Behavior...")
    
    # Test multiple loads to see if there are any issues
    model_path = os.path.join(os.path.dirname(__file__), 'models', 'model.pkl')
    
    if os.path.exists(model_path):
        print(f"📁 Model path: {model_path}")
        
        for i in range(3):
            try:
                model = joblib.load(model_path)
                print(f"   Load {i+1}: ✅ Success")
            except Exception as e:
                print(f"   Load {i+1}: ❌ Error - {str(e)}")
                return False
        
        print("✅ Multiple loads successful - no caching issues detected")
        return True
    else:
        print("❌ Model file not found for cache testing")
        return False

def main():
    """Run dashboard model loading simulation."""
    print("🧪 DASHBOARD MODEL LOADING SIMULATION")
    print("=" * 50)
    
    # Test 1: Simulate exact dashboard logic
    print("\n📋 Test 1: Exact Dashboard Logic")
    print("-" * 30)
    model1 = simulate_dashboard_load_model()
    
    # Test 2: Simulate from dashboard directory
    print("\n📋 Test 2: From Dashboard Directory")
    print("-" * 30)
    model2 = simulate_dashboard_from_dashboard_dir()
    
    # Test 3: Cache behavior
    print("\n📋 Test 3: Cache Behavior")
    print("-" * 30)
    cache_ok = test_streamlit_cache_behavior()
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 SIMULATION RESULTS")
    print("=" * 50)
    
    results = [
        ("Dashboard Logic", model1 is not None),
        ("Dashboard Directory", model2 is not None),
        ("Cache Behavior", cache_ok)
    ]
    
    for test_name, success in results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status} - {test_name}")
    
    all_passed = all(result[1] for result in results)
    
    if all_passed:
        print(f"\n🎉 ALL TESTS PASSED!")
        print("💡 Model loading should work in dashboard. If still seeing issues:")
        print("   • Clear Streamlit cache: Ctrl+F5 or Settings > Clear Cache")
        print("   • Restart Streamlit server")
        print("   • Check browser console for errors")
    else:
        print(f"\n🚨 SOME TESTS FAILED!")
        print("💡 Potential fixes:")
        print("   • Verify model file integrity")
        print("   • Check file permissions")
        print("   • Ensure all dependencies are installed")
    
    # Show how to run dashboard
    print(f"\n🚀 TO RUN DASHBOARD:")
    print(f"   cd landcover-project")
    print(f"   streamlit run dashboard/app.py")

if __name__ == "__main__":
    main()