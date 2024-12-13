![banner](https://github.com/PJURC-data-analysis/south-korea-covid/blob/main/media/banner.png)

# South Korea COVID Analysis: Pandemic Prevention Strategy
[View Notebook](https://github.com/PJURC-data-analysis/south-korea-covid/blob/main/South%20Korea%20COVID.ipynb)

An analysis of South Korean COVID-19 patient data to develop evidence-based pandemic prevention strategies. This study examines location-based transmission patterns and risk factors to create actionable recommendations for future pandemic response.

## Overview

### Business Question 
How can patient-level COVID-19 data from South Korea inform strategic pandemic prevention planning for future outbreaks?

### Key Findings
- Churches were primary infection sources
- Nightlife clusters in Yonhsan-gu showed significant spread
- Workplace transmissions formed notable clusters
- International travel contributed to case numbers
- Medical facilities in Southeast showed high infection rates
- Nursing homes experienced significant outbreaks

### Impact/Results
- Developed comprehensive Pandemic Prevention Plan
- Identified high-risk locations and activities
- Created framework for infection monitoring
- Established pre-pandemic preparation guidelines

## Data

### Source Information
- Dataset: South Korea COVID-19 patient data
- Source: Kaggle Dataset
- Time Period: Through 2020-06-30

### Variables Analyzed
- Location data
- Patient demographics
- Infection sources
- Regional distribution
- Healthcare facility data

## Methods

### Analysis Approach
1. Location-based Analysis
   - Regional infection patterns
   - Institution-specific outbreaks
   - Travel-related cases
2. Risk Factor Analysis
   - Demographic vulnerabilities
   - Transmission patterns
   - Facility-specific risks

### Tools Used
- Python (Data Analysis)
  - Pandas: Data manipulation
  - Numpy: Numerical computations
  - Matplotlib: Visualization
  - Seaborn: Visualization

## Getting Started

### Prerequisites
```python
matplotlib==3.9.4
numpy==2.2.0
pandas==2.2.3
seaborn==0.13.2
```

### Installation & Usage
```bash
git clone git@github.com:PJURC-data-analysis/south-korea-covid.git
cd south-korea-covid
pip install -r requirements.txt
jupyter notebook "South Korea COVID.ipynb"
```

## Project Structure
```
coursera-analysis/
│   README.md
│   requirements.txt
│   South Korea COVID.ipynb
|   utils.py
└── data/
    └── Case.csv
    └── PatientInfo.csv
    └── Policy.csv
    └── Region.csv
    └── SearchTrend.csv
    └── SeoulFloating.csv
    └── Time.csv
    └── TimeAge.csv
    └── TimeGender.csv
    └── TimeProvince.csv
    └── Weather.csv
```

## Strategic Recommendations
1. **Religious Gathering Management**
   - Negotiate church service closures
   - Monitor large gatherings

2. **Nightlife Monitoring**
   - Focus on tourist areas
   - Track inter-city spread

3. **Workplace Safety**
   - Develop health guidelines
   - Conduct regular audits

4. **Travel Controls**
   - Airport screening protocols
   - Coastal city monitoring

5. **Healthcare Facility Protocol**
   - Patient isolation procedures
   - Staff safety measures

6. **Nursing Home Protection**
   - Stringent safety measures
   - Demographic risk management

## Future Improvements
- Extended time period coverage
- Policy impact analysis
- Cross-country comparisons
- Complete pandemic timeline
- Policy-location correlation studies