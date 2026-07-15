#!/usr/bin/env python3
"""
Test script to verify the dashboard model loading fix works correctly.
This tests the improved path resolution logic.
"""

import os
import sys
import joblib

def test_improved_model_loading():
    """Test the improved model loading logic."""
    print("🔄 Testing Improved Model Loading Logic...")
    
    # Simulate the improved logic from dashboard
    script_dir = os.path.dirname(os.path.abspath(__file__))
    dashboard_dir = os.path.join(script_dir, 'dashboard')
    project_root = os.path.dirname(dashboard_dir)  # Go up from dashboard/ to landcover-project/
    
    print(f"📁 Script directory: {script_dir}")
    print(f"📁 Dashboard directory: {dashboard_dir}")
    print(f"📁 Project root: {project_root}")
    
    possible_paths = [
        os.path.join(project_root, 'models', 'model.pkl'),  # Absolute path to project/models/
        '../models/model.pkl',                              # Relative from dashboard/
        'models/model.pkl',                                 # If running from project root
        os.path.join('..', 'models', 'model.pkl'),        # Alternative relative path
    ]
    
    for i, model_path in enumerate(possible_paths, 1):
        abs_path = os.path.abspath(model_path)
        print(f"\n🔍 Path {i}: {model_path}")
        print(f"   Absolute: {abs_path}")
        print(f"   Exists: {os.path.exists(model_path)}")
        
        if os.path.exists(model_path):
            try:
                model = joblib.load(model_path)
                print(f"   ✅ SUCCESS! Model loaded")
                print(f"   📊 Type: {type(model).__name__}")
                if hasattr(model, 'classes_'):
                    print(f"   📋 Classes: {len(model.classes_)}")
                return True, abs_path
            except Exception as e:
                print(f"   ❌ Error: {str(e)}")
    
    print("\n❌ No model found!")
    return False, None

def test_data_path_resolution():
    """Test the improved data path resolution."""
    print("\n🔄 Testing Data Path Resolution...")
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    dashboard_dir = os.path.join(script_dir, 'dashboard')
    project_root = os.path.dirname(dashboard_dir)
    
    data_paths = [
        os.path.join(project_root, 'data', 'EuroSAT'),  # Absolute path to project/data/EuroSAT/
        "data/EuroSAT",                                  # Relative from project root
        "../data/EuroSAT"                               # Relative from dashboard/
    ]
    
    for i, path in enumerate(data_paths, 1):
        abs_path = os.path.abspath(path)
        print(f"\n🔍 Data path {i}: {path}")
        print(f"   Absolute: {abs_path}")
        print(f"   Exists: {os.path.exists(path)}")
        
        if os.path.exists(path):
            # Check for class folders
            try:
                folders = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
                print(f"   📁 Found {len(folders)} class folders")
                if len(folders) >= 5:  # Should have at least 5 classes
                    print(f"   ✅ Data path valid")
                    return True, abs_path
                else:
                    print(f"   ⚠️ Insufficient class folders")
            except Exception as e:
                print(f"   ❌ Error reading directory: {str(e)}")
    
    print("\n❌ No valid data path found!")
    return False, None

def test_models_directory_creation():
    """Test models directory creation logic."""
    print("\n🔄 Testing Models Directory Creation...")
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    dashboard_dir = os.path.join(script_dir, 'dashboard')
    project_root = os.path.dirname(dashboard_dir)
    models_dir = os.path.join(project_root, 'models')
    
    print(f"📁 Models directory: {models_dir}")
    print(f"   Exists: {os.path.exists(models_dir)}")
    
    if os.path.exists(models_dir):
        print("   ✅ Models directory exists")
        
        # Check if model file exists
        model_file = os.path.join(models_dir, 'model.pkl')
        print(f"📄 Model file: {model_file}")
        print(f"   Exists: {os.path.exists(model_file)}")
        
        if os.path.exists(model_file):
            print("   ✅ Model file exists")
            return True
        else:
            print("   ⚠️ Model file missing")
            return False
    else:
        print("   ❌ Models directory missing")
        return False

def simulate_dashboard_startup():
    """Simulate the dashboard startup process."""
    print("\n🔄 Simulating Dashboard Startup...")
    
    # Test the exact sequence that happens in dashboard
    try:
        # 1. Path resolution
        script_dir = os.path.dirname(os.path.abspath(__file__))
        dashboard_dir = os.path.join(script_dir, 'dashboard')
        project_root = os.path.dirname(dashboard_dir)
        
        print(f"📁 Project root resolved: {project_root}")
        
        # 2. Model loading
        model_path = os.path.join(project_root, 'models', 'model.pkl')
        print(f"📄 Model path: {model_path}")
        
        if os.path.exists(model_path):
            model = joblib.load(model_path)
            print(f"✅ Model loaded successfully!")
            print(f"📊 Model ready for classification")
            return True
        else:
            print(f"❌ Model not found at expected location")
            return False
            
    except Exception as e:
        print(f"❌ Startup simulation failed: {str(e)}")
        return False

def main():
    """Run all verification tests."""
    print("🧪 DASHBOARD FIX VERIFICATION")
    print("=" * 50)
    
    tests = [
        ("Improved Model Loading", test_improved_model_loading),
        ("Data Path Resolution", test_data_path_resolution),
        ("Models Directory", test_models_directory_creation),
        ("Dashboard Startup", simulate_dashboard_startup)
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n📋 Running: {test_name}")
        print("-" * 30)
        try:
            if test_name in ["Improved Model Loading", "Data Path Resolution"]:
                result, path = test_func()
                results.append((test_name, result))
                if result and path:
                    print(f"   🎯 Success path: {path}")
            else:
                result = test_func()
                results.append((test_name, result))
        except Exception as e:
            print(f"❌ Test failed: {str(e)}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 VERIFICATION RESULTS")
    print("=" * 50)
    
    passed = 0
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {test_name}")
        if result:
            passed += 1
    
    print(f"\n📈 Overall: {passed}/{len(results)} tests passed")
    
    if passed == len(results):
        print("🎉 ALL FIXES VERIFIED! Dashboard should work correctly now.")
        print("🚀 Ready to run dashboard:")
        print("   cd landcover-project")
        print("   streamlit run dashboard/app.py")
    else:
        print("🚨 SOME FIXES NEED ATTENTION!")
        print("💡 Check failed tests above for issues")

if __name__ == "__main__":
    main()