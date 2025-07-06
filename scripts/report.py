# Generate HTML report (to be embedded in the artifact)
# Generating HTML report
def generate_html_report(metrics, plots, interesting_fact):
    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>La Liga Full Analysis Report</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 font-sans">
    <div class="container mx-auto p-4">
        <h1 class="text-3xl font-bold text-center mb-4">La Liga Match Analysis (2020 & 2025 Seasons)</h1>
        
        <div class="bg-white p-6 rounded-lg shadow-md mb-6">
            <h2 class="text-2xl font-semibold mb-4">Summary</h2>
            <p class="text-gray-700">
                This report analyzes La Liga match data for all teams in the 2020 and 2025 seasons. It includes metrics 
                like goals scored (GF), goals conceded (GA), expected goals (xG), expected goals against (xGA), 
                possession, and match outcomes. The analysis reveals team performance trends, home vs. away differences, 
                and xG correlations.
            </p>
            <h3 class="text-xl font-semibold mt-4">Key Findings</h3>
            <ul class="list-disc pl-6">
                <li>Highest scoring team: {metrics.loc[metrics['gf'].idxmax(), 'team']} 
                    ({metrics['gf'].max():.2f} goals per match).</li>
                <li>Most defensive team: {metrics.loc[metrics['ga'].idxmin(), 'team']} 
                    ({metrics['ga'].min():.2f} goals conceded per match).</li>
                <li>Interesting Fact: {interesting_fact['team']} overperforms its xG by {interesting_fact['xG_Diff']} 
                    goals per match (Actual: {interesting_fact['gf']}, xG: {interesting_fact['xg']}), 
                    indicating clinical finishing.</li>
            </ul>
        </div>
        
        <div class="bg-white p-6 rounded-lg shadow-md mb-6">
            <h2 class="text-2xl font-semibold mb-4">Performance Metrics</h2>
            <div class="overflow-x-auto">
                <table class="min-w-full bg-white">
                    <thead>
                        <tr>
                            <th class="py-2 px-4 border-b">Team</th>
                            <th class="py-2 px-4 border-b">Avg GF</th>
                            <th class="py-2 px-4 border-b">Avg GA</th>
                            <th class="py-2 px-4 border-b">Avg xG</th>
                            <th class="py-2 px-4 border-b">Avg xGA</th>
                            <th class="py-2 px-4 border-b">Avg Poss</th>
                            <th class="py-2 px-4 border-b">Win%</th>
                            <th class="py-2 px-4 border-b">Draw%</th>
                            <th class="py-2 px-4 border-b">Loss%</th>
                            <th class="py-2 px-4 border-b">Home GF</th>
                            <th class="py-2 px-4 border-b">Home GA</th>
                            <th class="py-2 px-4 border-b">Home Win%</th>
                            <th class="py-2 px-4 border-b">Away GF</th>
                            <th class="py-2 px-4 border-b">Away GA</th>
                            <th class="py-2 px-4 border-b">Away Win%</th>
                        </tr>
                    </thead>
                    <tbody>
    """
    
    for _, row in metrics.iterrows():
        html_content += f"""
                        <tr>
                            <td class="py-2 px-4 border-b">{row['team']}</td>
                            <td class="py-2 px-4 border-b">{row['gf']:.2f}</td>
                            <td class="py-2 px-4 border-b">{row['ga']:.2f}</td>
                            <td class="py-2 px-4 border-b">{row['xg']:.2f}</td>
                            <td class="py-2 px-4 border-b">{row['xga']:.2f}</td>
                            <td class="py-2 px-4 border-b">{row['poss']:.2f}%</td>
                            <td class="py-2 px-4 border-b">{row['Win%']:.2f}%</td>
                            <td class="py-2 px-4 border-b">{row['Draw%']:.2f}%</td>
                            <td class="py-2 px-4 border-b">{row['Loss%']:.2f}%</td>
                            <td class="py-2 px-4 border-b">{row['Home_GF']:.2f}</td>
                            <td class="py-2 px-4 border-b">{row['Home_GA']:.2f}</td>
                            <td class="py-2 px-4 border-b">{row['Home_Win%']:.2f}%</td>
                            <td class="py-2 px-4 border-b">{row['Away_GF']:.2f}</td>
                            <td class="py-2 px-4 border-b">{row['Away_GA']:.2f}</td>
                            <td class="py-2 px-4 border-b">{row['Away_Win%']:.2f}%</td>
                        </tr>
        """
    
    html_content += """
                    </tbody>
                </table>
            </div>
        </div>
        
        <div class="bg-white p-6 rounded-lg shadow-md mb-6">
            <h2 class="text-2xl font-semibold mb-4">Visualizations</h2>
            <h3 class="text-xl font-semibold mb-2">Average Goals Scored and Conceded</h3>
            <img src="data:image/png;base64,{}" alt="Goals Bar Chart" class="w-full mb-4">
            
            <h3 class="text-xl font-semibold mb-2">Win/Loss/Draw Distribution (Top 5 Scoring Teams)</h3>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
    """.format(plots[0])
    
    # Adding pie charts for top 5 teams
    top_teams = metrics.sort_values('gf', ascending=False).head(5)['team'].tolist()
    for i, team in enumerate(top_teams, 1):
        html_content += f"""
                <div>
                    <h4 class="text-lg font-semibold text-center">{team}</h4>
                    <img src="data:image/png;base64,{plots[i]}" alt="{team} Pie Chart" class="w-full">
                </div>
        """
    
    html_content += f"""
            </div>
            
            <h3 class="text-xl font-semibold mb-2 mt-4">Expected Goals vs Actual Goals</h3>
            <img src="data:image/png;base64,{plots[-4]}" alt="xG Scatter Plot" class="w-full mb-4">
            <p class="text-gray-700 mb-4">
                This box plot shows the distribution of goals scored per match for each team. The box represents the interquartile range (IQR), with the median as the central line, and whiskers show the range of typical scores. Outliers (dots) indicate unusually high-scoring matches. Teams like {metrics.loc[metrics['gf'].idxmax(), 'team']} have a higher median and wider IQR, reflecting consistent and high-scoring performances, while teams with lower medians, like {metrics.loc[metrics['gf'].idxmin(), 'team']}, struggle offensively.
            </p>
            <h3 class="text-xl font-semibold mb-2">Goal Distribution by Team</h3>
            <
            <img src="data:image/png;base64,{plots[-3]}" alt="Goal Box Plot" class="w-full mb-4">

            <h3 class="text-xl font-semibold mb-2 mt-6">Feature Correlation Heatmap</h3>
            <p class="text-gray-700 mb-4">
                This heatmap displays correlations between key features such as GF, GA, xG, xGA, shots, and possession. Strong positive correlations (e.g., between xG and GF) indicate good prediction alignment, while negative correlations (e.g., GA and result_num) show how conceding goals affects outcomes.
            </p>
            <img src="data:image/png;base64,{plots[-2]}" alt="Feature Correlation Heatmap" class="w-full mb-4">
            
            <h3 class="text-xl font-semibold mb-2 mt-6">Team Performance Radar Chart</h3>
            <p class="text-gray-700 mb-4">
                TThis radar chart compares the performance of several football teams—Barcelona, Girona, Real Madrid, Atletico Madrid, Villarreal, Sevilla, and Athletic Club—across normalized metrics: goals for (gf), goals against (ga), expected goals (xg), expected goals against (xga), possession (poss), shots (sh), and shots on target (sot). A larger area enclosed by a team's line indicates stronger overall performance, suggesting higher values in key offensive metrics like gf and xg, and strong defensive metrics. For example, Barcelona's large area highlights its strengths in generating scoring opportunities and converting them into goals, while teams with smaller areas, such as Sevilla, underperform across multiple metrics. The visualization effectively highlights the relative strengths and weaknesses of each team in a comparative format.
            </p>
            <img src="data:image/png;base64,{plots[-1]}" alt="Radar Chart" class="w-full mb-4">
            </div>
                    
            <div class="bg-white p-6 rounded-lg shadow-md">

            <h2 class="text-2xl font-semibold mb-4">Conclusion</h2>
            <p class="text-gray-700">
                The analysis reveals significant performance differences across La Liga teams. Top teams like 
                {metrics.loc[metrics['gf'].idxmax(), 'team']} dominate offensively, while teams like 
                {metrics.loc[metrics['ga'].idxmin(), 'team']} excel defensively. Home advantage is evident, 
                with most teams scoring more and conceding less at home. The xG analysis shows that teams like 
                {interesting_fact['team']} are highly efficient in converting chances. Lower-performing teams 
                in 2020, such as Espanyol and Mallorca, struggled with both offense and defense, likely contributing 
                to relegation risks.
            </p>
        </div>
    </div>
</body>
</html>
    """
    
    return html_content