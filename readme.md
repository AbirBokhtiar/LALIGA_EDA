Demo Link - https://drive.google.com/file/d/19YPZ1tPGD2krjiax8eYhy8l_Pq3yNGxc/view?usp=sharing

Generated markdown
# La Liga Match Analysis: 2019-2025

## Overview

This repository contains Python code for analyzing La Liga match data from the 2019 to 2025 seasons. The analysis focuses on team performance metrics, patterns, and visualizations, providing insights into team strengths, weaknesses, and areas for potential improvement.  The code leverages libraries such as Pandas, Matplotlib, and Seaborn for data manipulation, statistical calculations, and visualization.

## Project Structure


├── README.md # This documentation file
├── analysis.ipynb # Jupyter Notebook with the full analysis (alternative)
├── la_liga_analysis.py # Main Python script containing the functions
├── data/ # Directory for storing the data
│ └── matches_full.csv # Sample La Liga match data (CSV format)
| └── cleaned_la_liga_matches.csv # Cleaned La Liga match data (CSV format)
| └── la_liga_team_summary.csv # Summary of Laliga Teams Performance (CSV format)
| └── laliga_analysis_report.html # La Liga match data Analysis (HTML Report)
├── eda/ # Directory for exploratory data analysis notebook
│ └── eda.ipynb # Exploratory Data Analysis pipeline
├── images/ # Directory for saving c
│ └── (example images of charts generated)
├── scripts/ # Directory for python scripts
│ └── report.py # Html report generation
│ └── visuals.py # generating visualizations
└── requirements.txt # List of Python dependencies

Generated code
## Data Source

The analysis utilizes La Liga match data uploaded on Kaggle, typically scraped from websites like FBref or other sports data providers. The dataset (`matches_full.csv`) is included in the `data/` directory for demonstration purposes.  You may need to adjust the data loading path in the code to reflect your actual data location.

Kaggle Dataset link - https://www.kaggle.com/datasets/marcelbiezunski/laliga-matches-dataset-2019-2025-fbref

**Note:**  Ensure the CSV file contains the following columns:

*   `date`: Match date (YYYY-MM-DD format)
*   `team`: Team name
*   `venue`: "Home" or "Away"
*   `gf`: Goals For
*   `ga`: Goals Against
*   `xg`: Expected Goals For
*   `xga`: Expected Goals Against
*   `poss`: Possession (%)
*   `sh`: Shots
*   `sot`: Shots on Target
*   `dist`: Average shot distance
*   `fk`: Free Kicks
*   `pk`: Penalties Scored
*   `pkatt`: Penalties Attempted
*   `result`: "W" (Win), "D" (Draw), or "L" (Loss)

## Dependencies

To run the analysis, you'll need to install the following Python packages. It is recommended to use a virtual environment to manage dependencies.

1.  **Create a virtual environment (optional but recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

2.  **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

The `requirements.txt` file lists the required packages:

pandas==2.1.0
matplotlib==3.7.1
seaborn==0.12.2
numpy==1.24.3

## Usage

1.  **Download the repository:**

    ```bash
    git clone <repository_url>
    cd la-liga-analysis
    ```

2.  **Place your La Liga match data CSV file in the `data/` directory (or update the file path in the script).**

3.  **Run the analysis script:**

    ```bash
    python la_liga_analysis.py
    ```

    Alternatively, you can open and run the `analysis.ipynb` Jupyter Notebook.

4.  **The script will:**

    *   Load and clean the data.
    *   Calculate team performance metrics.
    *   Print an "interesting fact" – the team with the largest positive difference between goals scored and expected goals.
    *   Generate several visualizations:
        *   Bar chart of average goals scored vs. goals conceded per team.
        *   Pie charts breaking down wins, draws, and losses for the top 5 teams (based on goals scored).
        *   Scatter plot of xG vs. goals scored for each match.
        *   Box plot showing the distribution of goals scored per team.
        *   Correlation Heatmap.
        *   Radar chart comparing selected teams across key performance indicators.
    *   Save the visualizations to the `images/` directory.

## Key Functions

*   **`load_and_clean_data(path)`:**  Loads the data from a CSV file, cleans column names, converts data types, and handles missing values.  Returns a cleaned Pandas DataFrame.

*   **`calculate_metrics(df)`:**  Calculates team-level performance metrics from the cleaned DataFrame, including average goals, expected goals, possession, win/draw/loss counts and percentages, and home/away win percentages.  Returns a Pandas DataFrame with the calculated metrics.

*   **`plot_team_radar(metrics, teams)`:** Generates a radar chart comparing the specified teams across key performance indicators (GF, GA, xG, xGA, Poss).  Requires a DataFrame of team metrics and a list of team names.

*   **`find_interesting_fact(metrics)`:**  Identifies and returns a dictionary containing information about the team with the largest positive difference between goals scored and expected goals.

*   **`generate_visuals(df, metrics)`:** Generates various visualizations including bar charts, pie charts, scatter plots, box plots and a correlation heatmap. Requires the raw DataFrame `df` and the aggregated metrics DataFrame `metrics`.

## Interpreting the Results

*   **Goals For vs. Against Bar Chart:** Provides a visual comparison of each team's offensive and defensive capabilities.  Higher "Goals For" indicates a stronger attack, while lower "Goals Against" suggests a more solid defense.

*   **Top 5 Teams Result Breakdown Pie Charts:**  Illustrates the relative success rates of the top teams based on goals scored, showing the proportion of wins, draws, and losses.

*   **xG vs. Goals For Scatter Plot:**  Helps identify teams that are over or underperforming their expected goals (xG).  Points above the diagonal line indicate teams scoring more goals than expected, while points below the line show teams underperforming their xG.

*   **Goal Distribution per Team Box Plot:**  Provides insights into the consistency of each team's scoring performance.  The median shows the typical number of goals scored, while the spread of the box indicates the variability.

*   **Feature Correlation Heatmap:** Reveals relationships between different performance metrics. Strong positive correlations (close to 1) indicate features that tend to increase together, while strong negative correlations (close to -1) indicate features that move in opposite directions.  Helps identify key drivers of success.

*   **Team Performance Radar Chart:**  Offers a multi-dimensional comparison of team performance. The shape and area enclosed by the radar chart provide a visual representation of each team's strengths and weaknesses across the chosen metrics.

*   **"Interesting Fact":**  Highlights a team that is either exceptionally efficient at converting chances (scoring more goals than expected) or struggling to convert good chances (scoring fewer goals than expected).

## Customization

*   **Data Path:** Modify the `path` variable in `la_liga_analysis.py` to point to your La Liga match data CSV file.
*   **Team Selection:** Adjust the `teams` list in `plot_team_radar` to compare different sets of teams in the radar chart.
*   **Visualization Parameters:** Customize the colors, labels, and other aesthetic properties of the visualizations within the `generate_visuals` function.
*   **Metrics:** Add or modify the calculated metrics in the `calculate_metrics` function to focus on specific aspects of team performance.
*   **Additional Visualizations:** Implement new visualizations to explore different aspects of the data.

## Potential Enhancements

*   Implement time series analysis to track changes in team performance over time.
*   Develop predictive models to forecast match outcomes based on historical data.
*   Incorporate data from other sources, such as player statistics or tactical formations, to provide a more comprehensive analysis.
*   Create an interactive dashboard for exploring the data and visualizations.
*   Add functionality to automatically update the analysis with new match data.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

Abir Bokhtiar - abirbokhtiar107@gmail.com
