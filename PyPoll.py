#The data we need to retrieve.
#1 The total number of votes case
#2 A complete list of candidates who received votes
#3 The percentage of votes each candidate won
#4 The total number of votes each candidate won
#5 The winner of the election based on popular vote

#Add our dependencies
import csv
import os

#Assign a variable for the file to load and the path.
file_to_load= os.path.join("Resources","election_results.csv")

#Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis","election_analysis.txt")

#1. Initialize a total vote counter.
total_votes=0

#Candidate Options
candidate_options=[]

#Declare the empty dictionary.
candidate_votes={}

#Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count=0
winning_percentage=0

#Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader=csv.reader(election_data)

    #Read and Print the header row.
    headers = next(file_reader)

    #Print each row in CSV file
    for row in file_reader:
        #2. Add to the total vote count.
        total_votes+=1

        #Print the candidate name from each row.
        candidate_name=row[2]

        #If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

            #Add the candidatie name to the candidate list
            candidate_options.append(candidate_name)

            #Begin tracking that candidate's vote count.
            candidate_votes[candidate_name]=0

        #Add a vote to that candidate's count.
        candidate_votes[candidate_name]+=1

#Determine the percentage of votes for each candidate by looping through.
#Iterate through the candidate list.
for candidate_name in candidate_votes:

    #Retrive vote count of a candidate.
    votes=candidate_votes[candidate_name]

    #Calculate the percentage of votes.
    vote_percentage=float(votes)/float(total_votes) *100

    #Print out candidates's name, vote count, and percentage of votes to the terminal
    print(f"{candidate_name}: {vote_percentage: .1f}% ({votes:,})\n")

    #Determine if the votes is greater than the winning count.
    if(votes>winning_count) and (vote_percentage>winning_percentage):

        #If True
        winning_count=votes

        #If true
        winning_percentage=vote_percentage

        #Set the wining candidate equal to the candidate's name
        winning_candidate=candidate_name

winning_candidate_summary=(
    f"------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"---------------------\n")

print(winning_candidate_summary)

#Print the candidate name and percentage of votes.
print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")

#Print the candidate vote dictionary
print(candidate_votes)

#Print the candidiate list.
print(candidate_options)

#3. Print the total votes.
print(total_votes)


#Using the with statement open the file as a text file.
with open(file_to_save,"w") as txt_file:

    #Write some data to the file.
    txt_file.write("Counties in the Election\n\nArapahoe\nDenver\nJefferson")
    

#Close the file.
election_data.close()