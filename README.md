
# 🌍 Land Cover Classification & Greenery Prediction Dashboard

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-orange.svg)](https://streamlit.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A professional, interactive web application built with Streamlit for comprehensive satellite image analysis, land cover classification, change detection, and predictive modeling of greenery trends.

---

## 📋 Table of Contents
- [Project Overview](#project-overview)
- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation Guide](#installation-guide)
- [Usage Instructions](#usage-instructions)
- [Model Details](#model-details)
- [Deployment Options](#deployment-options)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## 🎯 Project Overview

This dashboard provides a complete solution for environmental monitoring using satellite imagery. It allows users to:
- Analyze multi-temporal satellite images
- Classify land cover types (forest, agriculture, urban, water, etc.)
- Detect spatial and temporal changes
- Predict future greenery trends using statistical modeling
- Generate professional, comprehensive reports for documentation

**Goal**: To make environmental data analysis accessible, intuitive, and actionable for researchers, urban planners, and environmentalists.

---

## ✨ Key Features

### 📊 Executive Summary Dashboard
- Real-time metrics (average greenery, total change, prediction, analysis period)
- Color-coded status indicators
- Quick insights into environmental health

### 🌿 Greenery & Vegetation Analysis
- Green percentage calculation using HSV color space
- Approximated NDVI (Normalized Difference Vegetation Index)
- Smoothed trends for realistic environmental interpretation

### 🗺️ Land Cover Classification
- Pre-trained Random Forest classifier on EuroSAT dataset
- Sliding window technique for large image analysis
- 10 land cover classes: Annual Crop, Forest, Herbaceous Vegetation, Highway, Industrial, Pasture, Permanent Crop, Residential, River, Sea/Lake
- Confidence scoring per patch and overall

### 🔄 Change Detection
- Multiple visualization options:
  - Before/After comparison
  - Heatmap overlay
  - Contour analysis with intelligent labeling
- Adjustable sensitivity threshold
- Impact scale classification (Minor/Moderate/Significant)

### 🔮 Predictive Modeling
- Linear regression with moving average smoothing
- Realistic environmental constraints (max ±2% change per year)
- Target year selection (2030–2050)
- 95% confidence interval calculation
- Trend visualization with uncertainty bands

### 📄 Report Generation
- Comprehensive Markdown reports with all analysis results
- Executive summary
- Temporal analysis
- Prediction details
- Change detection findings
- Land cover distribution
- Methodology and limitations

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| **Frontend** | Streamlit |
| **Image Processing** | OpenCV (cv2) |
| **Machine Learning** | Scikit-learn (Random Forest) |
| **Data Handling** | NumPy, Pandas |
| **Visualization** | Matplotlib |
| **Model Serialization** | Joblib |
| **Deployment** | Docker, Streamlit Cloud, Render, Heroku |

---

## 📁 Project Structure

```
landcover-project/
├── dashboard/
│   └── app.py                      # Main Streamlit application entry point
├── models/
│   └── model.pkl                   # Pre-trained Random Forest model
├── data/
│   ├── EuroSAT/                    # Training dataset (10 classes of satellite images)
│   │   ├── AnnualCrop/
│   │   ├── Forest/
│   │   ├── HerbaceousVegetation/
│   │   ├── Highway/
│   │   ├── Industrial/
│   │   ├── Pasture/
│   │   ├── PermanentCrop/
│   │   ├── Residential/
│   │   ├── River/
│   │   └── SeaLake/
│   └── EuroSATallBands/            # (Optional) Full EuroSAT dataset with all spectral bands
├── testing/                        # Sample test images
│   ├── amaravathi/
│   ├── srmap/
│   └── vizag/
├── __pycache__/                    # Python bytecode cache (auto-generated)
├── classification.py               # Model training, feature extraction, prediction
├── change_detection.py             # Change detection algorithms & visualizations
├── greenery.py                     # Green percentage, NDVI calculation, trend smoothing
├── sliding_window.py               # Sliding window classification & confidence scoring
├── prediction.py                   # Future prediction with linear regression
├── summary_dashboard.py            # Executive summary metrics & insights
├── temporal_analysis.py            # Year-to-year change & trend analysis
├── key_insights.py                 # Research-level insight generation
├── validation_system.py            # Prediction confidence & validation
├── report_generator.py             # Comprehensive Markdown report creation
├── land_cover_analysis.py          # Land cover distribution & visualization
├── simulation.py                   # (Optional) Simulation module
├── suggestion.py                   # Automated suggestions based on greenery
├── features.py                     # Feature extraction for classification
├── preprocessing.py                # Image preprocessing utilities
├── analyze_all_categories.py       # Helper script for dataset analysis
├── comprehensive_test.py           # Testing script
├── requirements.txt                # Python dependencies
├── .gitignore                      # Git ignore rules
├── Dockerfile                      # Docker container configuration
├── Procfile                        # Heroku deployment configuration
└── README.md                       # This file
```

---

## 🚀 Installation Guide

### Prerequisites
- **Python 3.8 or higher**
- **pip package manager**
- (Optional) Git for version control

### Step 1: Get the Code
Clone or navigate to the project directory:
```bash
# If cloning from a repo:
git clone &lt;your-repo-url&gt;
cd landcover-project

# Or if you already have the files locally:
cd "c:\Users\venky\OneDrive\Desktop\land cover (4)\land cover\landcover-project"
```

### Step 2: Create Virtual Environment (Highly Recommended)
Isolate project dependencies:
```bash
# Create virtual environment
python -m venv .venv

# Activate on Windows (PowerShell):
.venv\Scripts\Activate.ps1

# Activate on Windows (Command Prompt):
.venv\Scripts\activate.bat

# Activate on macOS/Linux:
source .venv/bin/activate
```

### Step 3: Install Dependencies
Install all required packages:
```bash
pip install -r requirements.txt
```

---

## 🖥️ Usage Instructions

### Run the App Locally
Launch the Streamlit app:
```bash
streamlit run dashboard/app.py
```
The app will automatically open in your default browser at:
`http://localhost:8501`

### How to Use the Dashboard

#### 1. Upload Images
- Use the sidebar to upload satellite images (JPG, PNG formats)
- **Tip**: Name files with years (e.g., `2020_visakhapatnam.jpg`) for automatic year detection
- You can upload multiple images from different years

#### 2. Explore Tabs
The dashboard has 7 main tabs:
1. **📊 Analysis**: View per-image greenery, NDVI, and land cover classification
2. **🔄 Change Detection**: Compare first & last image, view changes
3. **🔮 Prediction & Simulation**: Predict future greenery trends
4. **📈 Land Cover Distribution**: See pie charts and bar graphs of land cover types
5. **📖 Methodology**: Learn about the algorithms used
6. **🤖 AI Assistant**: (Optional) Ask questions about the analysis
7. **🖼️ Classify Image**: Quick classification of a single image

#### 3. Generate Report
- Click "📄 Generate Report" on the main page
- Download the comprehensive Markdown report
- Preview the report before downloading

---

## 🤖 Model Details

### Classifier
- **Algorithm**: Random Forest Classifier
- **Training Data**: EuroSAT dataset (27,000 labeled satellite images)
- **Features**: Color histograms, texture features, spatial statistics
- **Data Augmentation**: Flips (horizontal/vertical), rotations (90/180/270 degrees)
- **Accuracy**: ~85-90% on test set

### Prediction Model
- **Algorithm**: Linear Regression with Moving Average Smoothing
- **Constraints**:
  - Maximum ±2% change per year (realistic for environmental systems)
  - Predictions clamped between 0% and 100%
- **Confidence**: Based on residual standard deviation

### Re-Training the Model
To re-train the model:
1. Ensure the EuroSAT dataset is present in `data/EuroSAT/`
2. Use the `classification.train_model()` function:
   ```python
   from classification import train_model
   model = train_model(data_dir="data/EuroSAT", save_path="models/model.pkl")
   ```

---

## ☁️ Deployment Options

### 1. Streamlit Community Cloud (Easiest & Free)
Deploy in minutes:
1. Push your code to GitHub/GitLab/Bitbucket
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with your GitHub account
4. Click "New app"
5. Select your repository, branch, and file path (`dashboard/app.py`)
6. Click "Deploy!"

### 2. Render
1. Push your code to GitHub
2. Sign up at [render.com](https://render.com)
3. Create a new **Web Service**
4. Connect your repository
5. Configure:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run dashboard/app.py --server.port $PORT --server.address 0.0.0.0`
6. Click "Create Web Service"

### 3. Heroku
1. Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
2. The project already includes a `Procfile`!
3. (Optional) Create a `setup.sh` for Streamlit config:
   ```bash
   # setup.sh
   mkdir -p ~/.streamlit/
   echo "\
   [server]\n\
   headless = true\n\
   port = $PORT\n\
   enableCORS = false\n\
   \n\
   " > ~/.streamlit/config.toml
   ```
4. Deploy via Git:
   ```bash
   git init
   git add .
   git commit -m "Initial deployment commit"
   heroku create your-app-name
   git push heroku master
   ```

### 4. Docker (Any Cloud Provider)
The project includes a `Dockerfile`! Build and run locally:
```bash
# Build the image
docker build -t landcover-dashboard .

# Run the container
docker run -p 8501:8501 landcover-dashboard
```
Then deploy the Docker image to AWS ECS, Azure Container Instances, GCP Cloud Run, or any other container service!

---

## 🔧 Troubleshooting

### Common Issues

1. **Model not loading**:
   - Ensure `models/model.pkl` exists
   - Check that you're in the correct directory
   - Verify all dependencies are installed

2. **OpenCV errors**:
   - Make sure `opencv-python` is installed: `pip install opencv-python`
   - On Linux/Docker: Install system dependencies:
     ```bash
     apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-0
     ```

3. **Port already in use**:
   - Kill the process on port 8501 or use a different port:
     ```bash
     streamlit run dashboard/app.py --server.port 8502
     ```

4. **Large images are slow**:
   - The sliding window technique can be slow on very large images; resize images before uploading if needed

---

## 🤝 Contributing

Contributions are welcome! Here's how:
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-awesome-feature`
3. Commit your changes: `git commit -m "Add some awesome feature"`
4. Push to the branch: `git push origin feature/my-awesome-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details (or create a LICENSE file if you don't have one!).

---

## 🙏 Acknowledgements

- **EuroSAT Dataset**: Thanks to the developers of the [EuroSAT](https://github.com/phelber/EuroSAT) dataset for providing labeled satellite imagery
- **Streamlit**: For the amazing web application framework
- **OpenCV**: For powerful image processing capabilities
- **Scikit-learn**: For machine learning tools

---

## 📞 Contact

For questions or feedback, reach out!

---

Made with ❤️ for environmental analysis!
