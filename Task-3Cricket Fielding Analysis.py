
import pandas as pd

def calculate_performance_score(row):
    """Calculates the Performance Score (PS) for a single fielding event."""
    C = row['Catches']
    RO = row['Run Outs']
    ST = row['Stumpings']
    WRO_good = row['Good Throws']  # Assuming 'Good Throws' contributes positively
    WRO_bad = row['Bad Throws']    # Assuming 'Bad Throws' contribute negatively
    MRO = row['Missed Run Outs']
    CT = row['Difficult Catches Taken']
    CD = row['Difficult Catches Dropped']
    RS = row['Runs Saved']
    RC = row['Runs Conceded']

    ps = (C + RO + ST + 0.5 * WRO_good - 0.5 * WRO_bad - 0.5 * MRO + CT - 0.5 * CD + RS - RC)
    return ps

# Load the fielding data from the CSV file
try:
    fielding_df = pd.read_csv('fielding_data.csv')

    # Calculate the Performance Score for each fielding event
    fielding_df['Performance Score'] = fielding_df.apply(calculate_performance_score, axis=1)

    # You can now work with the DataFrame containing the Performance Scores
    print(fielding_df[['Match', 'Innings', 'Player Name', 'Performance Score']].head())

except FileNotFoundError:
    print("Error: 'fielding_data.csv' not found. Please make sure the file is in the same directory as the script.")
except KeyError as e:
    print(f"Error: Column '{e}' not found in the CSV file. Please check the column names.")