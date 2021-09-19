import csv
import os
# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources","election_results.csv")

#Assign a variable to save the file to a path
file_to_save = os.path.join("analysis","election_analysis.txt")

# Using the with statement open the file as a text file
## Open the election results and read the file
with open(file_to_save,"w") as txt_file:
    # Write some data to the file
    txt_file.write("Counties in the Election")
    txt_file.write("\n-------------------------\n")
    txt_file.write("\nArapahoe\nDenver\nJefferson")

# Initialize a total vote counter
total_votes = 0

# New list of candidates
candidate_options=[]

# Declaring an empty dictionary
candidate_votes ={}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Print the header row
    headers = next(file_reader)
  
    # Print each row in the CSV file
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1

        # Print the candidate name from each row
        candidate_name=row[2]

        # If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            # Add it to the list of candidates
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name]=0

        # Add a vote to that candidate's name
        candidate_votes[candidate_name]+=1

# Determine the percentage of votes for each candidate by looping through the counts
## Iterate through the candidate list
for candidate_name in candidate_votes:
    # Retreive vote count of a candiate
    votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes
    vote_percentage=round((float(votes)/float(total_votes))*100,1)

    #  To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes>winning_count) and (vote_percentage > winning_percentage):
        # If true then set winning_count = votes and winning_percent =
        # vote_percentage.
        winning_count=votes
        winning_percentage = vote_percentage
        # And set the winning_candidate equal to the candidates name
        winning_candidate = candidate_name

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)






