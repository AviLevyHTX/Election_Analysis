#The data we need to retrieve/add our dependencies 
import csv
import os 

#Assign a variable for the file to load from a path
file_to_load = os.path.join("Resources","election_results.csv")
#Assign a variable to save the file to a path
file_to_save= os.path.join("analysis","election_analysis.txt")

#Open the election results and read the file using "with" statement
with open(file_to_load) as election_data:
    #To do: read and analyze the data here
    #Read the file object with the reader function
    file_reader= csv.reader(election_data)
    
    #Read and print the header row
    headers=next(file_reader)
    print(headers)

# 1. The total number of votes case
# 2. A complete list of candidates who received vots
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote