🌍 Climate Change Modeling
📌 Project Overview

This project focuses on leveraging Machine Learning (ML) techniques to model, analyze, and forecast aspects of climate change using public sentiment data and satellite-based environmental metrics. The goal is to build data-driven models that help predict climate indicators like CO₂ emissions, temperature anomalies, and other atmospheric patterns.
📂 Dataset Description
1. NASA Climate Change Comments Dataset

    Source: NASA Climate Facebook Page

    Type: Textual user comments (2020–2023)

    Columns:

        Date: Timestamp of the comment

        LikesCount: Number of likes the comment received

        ProfileName: Anonymized name (SHA-256 hashed)

        CommentsCount: Number of replies

        Text: Actual comment content

    Applications:

        Sentiment Analysis

        Topic Modeling

        Engagement Trend Detection

2. Climate Emissions Dataset (climate_nasa.csv)

    Rows: 79,023 (train), 24,353 (test)

    Features: 75+ climate-related variables, including:

        CO₂ Emissions

        Sulphur Dioxide Density

        Cloud Base Height/Pressure

        Surface Albedo

        Aerosol Optical Depth

        Geographic Coordinates (Latitude, Longitude)

        Temporal Data (Year, Week)

🛠️ Tools & Technologies

    Languages: Python

    IDE: Jupyter Notebook, VS Code

    Libraries:

        pandas, numpy

        scikit-learn, xgboost

        matplotlib, seaborn, folium, geopandas

        tqdm, shapely
