# Election_Analysis

## Overview of Election Audit
Election audit for the Colorado Board of Elections - the following analysis displays the outcome of a local congressional election. 

## Election-Audit Results
- Total votes casted: 369,711

- Number of votes and the percentage of total votes for each county in the precinct:
  - Jefferson: 10.5% (38,855)
  - Denver: 82.8% (306,055)
  - Arapahoe: 6.7% (24,801)
 
- County with the largest number of votes: Denver

- Number of votes and the percentage of the total votes each candidate received:
  - Charles Casper Stockham: 23.0% (85,213)
  - Diana DeGette: 73.8% (272,892)
  - Raymon Anthony Doane: 3.1% (11,606)

- Winning candidate: Diana DeGette
  - Winning Vote Count: 272,892
  - Winning Percentage: 73.8%

## Election-Audit Summary
The script used for this election analysis is designed to work for any future election. In order for this to work with almost no modification to the script, the columns in the CSV file must be in the same order as election_analysis.csv. Meaning - 'Ballot ID' (index[0]) is the first column, 'County' (index[1]) is the second column and 'Candidate' (index[2]) is the third column. 

If the columns do not come in the same order, all index in the script would need to be modified. 
For example: if columns are rearranged as [County, Candidate, Ballot ID]
  - County becomes index 0
  - Candidate becomes index 1
  - Ballot ID becomes index 2
 
## Resources
- Data source: election_analysis.csv
- Software: Python 3.9.7, Visual Studio Code 1.60.0
