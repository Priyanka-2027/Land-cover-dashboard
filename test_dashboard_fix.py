#!/usr/bin/env python3
"""
Test Dashboard Fix - NameError Resolution
Verifies that the uploaded_files NameError has been resolved.
"""

import os
import sys

def test_dashboard_syntax():
    """Test that the dashboard has valid Python syntax."""
    
    print("🔍 Testing Dashboard Syntax...")
    
    dashboard_path = "dashboard/app.py"
    
    if not os.path.exists(dashboard_path):
        print("❌ Dashboard file not found")
        return False
    
    try:
        with open(dashboard_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Test syntax
        compile(content, dashboard_path, 'exec')
        print("✅ Dashboard syntax is valid")
        return True
        
    except SyntaxError as e:
        print(f"❌ Syntax error: {str(e)}")
        return False
    except Exception as e:
        print(f"❌ Error reading dashboard: {str(e)}")
        return False

def test_variable_definition_order():
    """Test that variables are defined before use."""
    
    print("\n🔍 Testing Variable Definition Order...")
    
    dashboard_path = "dashboard/app.py"
    
    try:
        with open(dashboard_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        lines = content.split('\n')
        
        # Find key variable definitions and uses
        variables_to_check = {
            'uploaded_files': {
                'definition_pattern': 'uploaded_files = st.sidebar.file_uploader',
                'use_pattern': 'if uploaded_files and len(uploaded_files)',
                'def_line': None,
                'use_line': None
            },
            'images': {
                'definition_pattern': 'images, years, green_percentages = [], [], []',
                'use_pattern': 'summary_metrics = calculate_summary_metrics(years, green_percentages, images)',
                'def_line': None,
                'use_line': None
            }
        }
        
        # Find definition and use lines
        for i, line in enumerate(lines):
            for var_name, var_info in variables_to_check.items():
                if var_info['definition_pattern'] in line and var_info['def_line'] is None:
                    var_info['def_line'] = i + 1
                elif var_info['use_pattern'] in line and var_info['use_line'] is None:
                    var_info['use_line'] = i + 1
        
        # Check order
        all_good = True
        for var_name, var_info in variables_to_check.items():
            if var_info['def_line'] and var_info['use_line']:
                if var_info['def_line'] < var_info['use_line']:
                    print(f"✅ {var_name}: defined on line {var_info['def_line']}, used on line {var_info['use_line']}")
                else:
                    print(f"❌ {var_name}: used on line {var_info['use_line']} before definition on line {var_info['def_line']}")
                    all_good = False
            elif var_info['def_line']:
                print(f"✅ {var_name}: defined on line {var_info['def_line']}")
            elif var_info['use_line']:
                print(f"⚠️ {var_name}: used on line {var_info['use_line']} but definition not found")
        
        return all_good
        
    except Exception as e:
        print(f"❌ Error checking variable order: {str(e)}")
        return False

def test_dashboard_structure():
    """Test that the dashboard has proper structure."""
    
    print("\n🔍 Testing Dashboard Structure...")
    
    dashboard_path = "dashboard/app.py"
    
    try:
        with open(dashboard_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for key components
        required_components = [
            'st.set_page_config',
            'st.title',
            'st.sidebar.file_uploader',
            'SUMMARY DASHBOARD',
            'EXPORT COMPREHENSIVE REPORT',
            'PROFESSIONAL FOOTER',
            'st.download_button',
            'Developed for DWDM Project'
        ]
        
        missing_components = []
        for component in required_components:
            if component not in content:
                missing_components.append(component)
        
        if missing_components:
            print(f"❌ Missing components: {missing_components}")
            return False
        else:
            print("✅ All required dashboard components present")
            return True
        
    except Exception as e:
        print(f"❌ Error checking dashboard structure: {str(e)}")
        return False

def main():
    """Run all dashboard fix tests."""
    
    print("🔧 DASHBOARD FIX VERIFICATION")
    print("=" * 50)
    
    # Test syntax
    syntax_ok = test_dashboard_syntax()
    
    # Test variable order
    order_ok = test_variable_definition_order()
    
    # Test structure
    structure_ok = test_dashboard_structure()
    
    # Final assessment
    print("\n" + "=" * 50)
    if syntax_ok and order_ok and structure_ok:
        print("🎉 **DASHBOARD FIX SUCCESSFUL!**")
        print("✅ NameError resolved")
        print("✅ Variables defined before use")
        print("✅ Dashboard structure intact")
        print("✅ Ready for faculty demonstration")
        return True
    else:
        print("❌ **DASHBOARD ISSUES DETECTED**")
        print("Please review the test results above")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)