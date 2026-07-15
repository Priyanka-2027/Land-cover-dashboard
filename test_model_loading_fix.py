#!/usr/bin/env python3
"""
Test script to verify model loading functionality works correctly.
This addresses the critical bug where dashboard shows "Model not available" error.
"""

import os
import sys
import joblib

# Add project root to path
sys.path.append(os.path.dirname(__file__))

def test_model_loading():
    """Test the model loading logic from dashboard."""
    print("🔄 Testing Model Loading Logic...")
    
    # Test the same paths as in dashboard
    possible_paths = [
        'models/model.pkl',           # When running from landcover-project/
        '../models/model.pkl',        # When running from landcover-project/dashboard/
        os.path.join('..', 'models', 'model.pkl'),
        os.path.join(os.path.dirname(__file__), 'models', 'model.pkl')
    ]
    
    print(f"📁 Current working directory: {os.getcwd()}")
    print(f"📁 Script directory: {os.path.dirname(__file__)}")
    
    model_found = False
    for i, model_path in enumerate(possible_paths, 1):
        print(f"\n🔍 Path {i}: {model_path}")
        print(f"   Absolute path: {os.path.abspath(model_path)}")
        print(f"   Exists: {os.path.exists(model_path)}")
        
        if os.path.exists(model_path):
            try:
                model = joblib.load(model_path)
                print(f"   ✅ Model loaded successfully!")
                print(f"   📊 Model type: {type(model)}")
                if hasattr(model, 'n_estimators'):
                    print(f"   🌳 Estimators: {model.n_estimators}")
                if hasattr(model, 'classes_'):
                    print(f"   📋 Classes: {len(model.classes_)} classes")
                model_found = True
                break
            except Exception as e:
                print(f"   ❌ Error loading model: {str(e)}")
                continue
    
    if not model_found:
        print("\n🚨 NO MODEL FOUND!")
        print("💡 Troubleshooting:")
        print("   • Check if models/model.pkl exists")
        print("   • Verify model file is not corrupted")
        print("   • Run training script to create model")
        return False
    
    print(f"\n✅ Model loading test PASSED!")
    return True

def test_dashboard_model_loading():
    """Test model loading from dashboard directory perspective."""
    print("\n🔄 Testing Dashboard Model Loading...")
    
    # Simulate running from dashboard directory
    dashboard_dir = os.path.join(os.path.dirname(__file__), 'dashboard')
    
    # Test paths from dashboard perspective
    dashboard_paths = [
        os.path.join('..', 'models', 'model.pkl'),  # ../models/model.pkl
        os.path.join(os.path.dirname(dashboard_dir), 'models', 'model.pkl')
    ]
    
    for i, model_path in enumerate(dashboard_paths, 1):
        print(f"\n🔍 Dashboard Path {i}: {model_path}")
        print(f"   Absolute path: {os.path.abspath(model_path)}")
        print(f"   Exists: {os.path.exists(model_path)}")
        
        if os.path.exists(model_path):
            try:
                model = joblib.load(model_path)
                print(f"   ✅ Model loaded from dashboard perspective!")
                return True
            except Exception as e:
                print(f"   ❌ Error: {str(e)}")
    
    print("❌ Dashboard model loading failed")
    return False

def test_classification_import():
    """Test if classification module can be imported."""
    print("\n🔄 Testing Classification Module Import...")
    
    try:
        from classification import CLASSES, train_model
        print(f"✅ Classification module imported successfully")
        print(f"📋 Available classes: {len(CLASSES)}")
        print(f"🏷️  Classes: {', '.join(CLASSES[:5])}{'...' if len(CLASSES) > 5 else ''}")
        return True
    except ImportError as e:
        print(f"❌ Import error: {str(e)}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")
        return False

def main():
    """Run all model loading tests."""
    print("🧪 CRITICAL BUG FIX: Model Loading Test Suite")
    print("=" * 50)
    
    tests = [
        ("Model Loading Logic", test_model_loading),
        ("Dashboard Model Loading", test_dashboard_model_loading),
        ("Classification Import", test_classification_import)
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n📋 Running: {test_name}")
        print("-" * 30)
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ Test failed with exception: {str(e)}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 TEST RESULTS SUMMARY")
    print("=" * 50)
    
    passed = 0
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {test_name}")
        if result:
            passed += 1
    
    print(f"\n📈 Overall: {passed}/{len(results)} tests passed")
    
    if passed == len(results):
        print("🎉 ALL TESTS PASSED! Model loading should work correctly.")
        print("💡 If dashboard still shows 'Model not available', try:")
        print("   • Refresh the browser page")
        print("   • Restart the Streamlit server")
        print("   • Clear Streamlit cache")
    else:
        print("🚨 SOME TESTS FAILED! Model loading needs attention.")
        print("💡 Next steps:")
        print("   • Check failed tests above")
        print("   • Verify model file integrity")
        print("   • Run model training if needed")

if __name__ == "__main__":
    main()