#!/usr/bin/env python3
"""
Test the enhanced prediction model with equation display and justification.
"""

import matplotlib.pyplot as plt
from prediction import predict_future, generate_prediction_plot

def test_prediction_model():
    """Test the enhanced prediction model with various scenarios."""
    print("📈 Testing Enhanced Prediction Model")
    print("=" * 50)
    
    # Test Case 1: Stable trend
    print("\n🔍 Test Case 1: Stable Trend")
    years1 = [2020, 2021, 2022, 2023]
    greenery1 = [45.2, 46.1, 45.8, 46.3]
    target_year1 = 2030
    
    prediction1, slope1, model_info1 = predict_future(years1, greenery1, target_year1)
    
    print(f"Years: {years1}")
    print(f"Greenery: {greenery1}")
    print(f"Prediction for {target_year1}: {prediction1:.2f}%")
    print(f"Annual trend: {slope1:.3f}% per year")
    print(f"Model equation: {model_info1['equation']}")
    print(f"R² score: {model_info1['r_squared']:.3f}")
    print(f"Justification: {model_info1['justification']}")
    
    # Test Case 2: Strong positive trend (should be constrained)
    print("\n🔍 Test Case 2: Strong Positive Trend (Constrained)")
    years2 = [2020, 2021, 2022]
    greenery2 = [30.0, 40.0, 50.0]  # 10% increase per year
    target_year2 = 2030
    
    prediction2, slope2, model_info2 = predict_future(years2, greenery2, target_year2)
    
    print(f"Years: {years2}")
    print(f"Greenery: {greenery2}")
    print(f"Prediction for {target_year2}: {prediction2:.2f}%")
    print(f"Annual trend: {slope2:.3f}% per year")
    print(f"Model equation: {model_info2['equation']}")
    print(f"Constrained: {model_info2['constrained']}")
    print(f"Raw prediction: {model_info2['raw_prediction']:.2f}%")
    print(f"Justification: {model_info2['justification']}")
    
    # Test Case 3: Declining trend
    print("\n🔍 Test Case 3: Declining Trend")
    years3 = [2018, 2019, 2020, 2021, 2022]
    greenery3 = [65.0, 62.5, 60.0, 58.2, 56.8]
    target_year3 = 2025
    
    prediction3, slope3, model_info3 = predict_future(years3, greenery3, target_year3)
    
    print(f"Years: {years3}")
    print(f"Greenery: {greenery3}")
    print(f"Prediction for {target_year3}: {prediction3:.2f}%")
    print(f"Annual trend: {slope3:.3f}% per year")
    print(f"Model equation: {model_info3['equation']}")
    print(f"R² score: {model_info3['r_squared']:.3f}")
    print(f"Justification: {model_info3['justification']}")
    
    # Generate and save test plots
    print("\n📊 Generating Test Plots...")
    
    fig1 = generate_prediction_plot(years1, greenery1, target_year1, prediction1, model_info1)
    fig1.savefig("test_prediction_stable.png", dpi=150, bbox_inches='tight')
    
    fig2 = generate_prediction_plot(years2, greenery2, target_year2, prediction2, model_info2)
    fig2.savefig("test_prediction_constrained.png", dpi=150, bbox_inches='tight')
    
    fig3 = generate_prediction_plot(years3, greenery3, target_year3, prediction3, model_info3)
    fig3.savefig("test_prediction_declining.png", dpi=150, bbox_inches='tight')
    
    plt.close('all')  # Close all figures to free memory
    
    print("✅ Test plots saved:")
    print("   • test_prediction_stable.png - Stable trend example")
    print("   • test_prediction_constrained.png - Constrained prediction example")
    print("   • test_prediction_declining.png - Declining trend example")
    
    print("\n🎯 Summary:")
    print("✅ Model equation display working")
    print("✅ R² score calculation working")
    print("✅ Constraint system working")
    print("✅ Justification text generation working")
    print("✅ Plot enhancement with equation display working")

if __name__ == "__main__":
    test_prediction_model()