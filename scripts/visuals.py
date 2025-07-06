# Find interesting fact (provided)
def find_interesting_fact(df, metrics):
    metrics['xG_Diff'] = metrics['gf'] - metrics['xg']
    most_overperforming = metrics.loc[metrics['xG_Diff'].idxmax()]
    return {
        'team': most_overperforming['team'],
        'xG_Diff': most_overperforming['xG_Diff'].round(2),
        'gf': most_overperforming['gf'].round(2),
        'xg': most_overperforming['xg'].round(2)
    }

# Fixed generate visualizations (corrected from provided code)
def generate_visualizations(df, metrics):
    plots = []
    top_teams = metrics.sort_values('gf', ascending=False).head(5)['team'].tolist()
    
    # Bar Chart: Average Goals Scored and Conceded
    plt.figure(figsize=(14, 6))
    bar_width = 0.35
    index = np.arange(len(metrics))
    plt.bar(index - bar_width/2, metrics['gf'], bar_width, label='Goals Scored', color='skyblue')
    plt.bar(index + bar_width/2, metrics['ga'], bar_width, label='Goals Conceded', color='salmon')
    plt.xlabel('Team')
    plt.ylabel('Average Goals')
    plt.title('Average Goals Scored and Conceded per Team')
    plt.xticks(index, metrics['team'], rotation=90)
    plt.legend()
    plt.tight_layout()
    img = io.BytesIO()
    plt.savefig(img, format='png', bbox_inches='tight')
    img.seek(0)
    plots.append(base64.b64encode(img.getvalue()).decode('utf-8'))
    plt.close()
    
    # Pie Charts: Win/Loss/Draw for top 5 teams
    for team in top_teams:
        team_data = metrics[metrics['team'] == team]
        sizes = [team_data['Wins'].iloc[0], team_data['Draws'].iloc[0], team_data['Losses'].iloc[0]]
        labels = ['Wins', 'Draws', 'Losses']
        plt.figure(figsize=(6, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=['#66b3ff', '#ffcc99', '#ff9999'])
        plt.title(f'Win/Loss/Draw Distribution for {team}')
        img = io.BytesIO()
        plt.savefig(img, format='png', bbox_inches='tight')
        img.seek(0)
        plots.append(base64.b64encode(img.getvalue()).decode('utf-8'))
        plt.close()
    
    # Scatter Plot: xG vs Actual Goals
    plt.figure(figsize=(10, 6))
    for team in metrics['team']:
        team_df = df[df['team'] == team]
        plt.scatter(team_df['xg'], team_df['gf'], label=team, alpha=0.6)
    plt.plot([0, 8], [0, 8], 'k--', label='Perfect Correlation')
    plt.xlabel('Expected Goals (xG)')
    plt.ylabel('Actual Goals Scored')
    plt.title('Expected Goals vs Actual Goals Scored')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    img = io.BytesIO()
    plt.savefig(img, format='png', bbox_inches='tight')
    img.seek(0)
    plots.append(base64.b64encode(img.getvalue()).decode('utf-8'))
    plt.close()
    
    # Box Plot: Goal Distribution
    plt.figure(figsize=(14, 6))
    sns.boxplot(x='team', y='gf', data=df)
    plt.xlabel('Team')
    plt.ylabel('Goals Scored')
    plt.title('Goal Distribution by Team')
    plt.xticks(rotation=90)
    plt.tight_layout()
    img = io.BytesIO()
    plt.savefig(img, format='png', bbox_inches='tight')
    img.seek(0)
    plots.append(base64.b64encode(img.getvalue()).decode('utf-8'))
    plt.close()

    # Correlation Heatmap
    cmap = sns.diverging_palette(10, 220, as_cmap=True)
    df['result_num'] = df['result'].map({'W': 2, 'D': 1, 'L': 0})
    df['venue_num'] = df['venue'].map({'Home': 1, 'Away': 0})
    plt.figure(figsize=(10, 8))
    sns.heatmap(df[['gf', 'ga', 'xg', 'xga', 'poss', 'sh', 'sot', 'dist', 'fk', 'pk', 'pkatt', 'result_num']].corr(), annot=True, cmap=cmap)
    plt.title('Feature Correlation Heatmap')
    img = io.BytesIO()
    plt.savefig(img, format='png', bbox_inches='tight')
    img.seek(0)
    plots.append(base64.b64encode(img.getvalue()).decode('utf-8'))
    plt.close()
    
    # Radar Chart
    teams = ['Barcelona', 'Girona', 'Real Madrid', 'Atletico Madrid', 'Villarreal', 'Sevilla', 'Athletic Club']
    stats = ['gf', 'ga', 'xg', 'xga', 'poss', 'sh', 'sot']
    radar_df = (metrics.set_index('team')[stats] - metrics[stats].min()) / (metrics[stats].max() - metrics[stats].min())
    categories = stats
    N = len(categories)
    angles = [n / float(N) * 2 * pi for n in range(N)] + [0]
    plt.figure(figsize=(7, 7))
    for team in teams:
        values = radar_df.loc[team].tolist() + [radar_df.loc[team].tolist()[0]]
        plt.polar(angles, values, label=team, linewidth=2)
    plt.xticks(angles[:-1], categories)
    plt.title('Team Performance Radar Chart')
    plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
    plt.tight_layout()
    img = io.BytesIO()
    plt.savefig(img, format='png', bbox_inches='tight')
    img.seek(0)
    plots.append(base64.b64encode(img.getvalue()).decode('utf-8'))
    plt.close()
    
    return plots, top_teams