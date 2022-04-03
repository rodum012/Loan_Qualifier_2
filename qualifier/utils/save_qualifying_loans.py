import csv
import questionary
import sys

def save_qualifying_loans(qualifying_loans):
    """Saves the qualifying loans to a CSV file.

    Args:
        qualifying_loans (list of lists): The qualifying bank loans.
    """
    # @TODO: Complete the usability dialog for savings the CSV Files.
    #Checks to see if the number of qualifying loans is greater than 0 and if it is not, then it ecits the program
    if len(qualifying_loans) <= 0:
        sys.exit()
    else:
        #Asks user if they would like to save the results of the loans they qualiff for
        user_answer = questionary.confirm("Would you like to save your qualifying loans?").ask()
        #checks if the user responded 'yes', and runs the below code if they did
        if user_answer == True:
            #Creates header for CSV file
            header = ['Lender','Max Loan Amount','Max LTV', 'Max DTI', 'Min Credit Score', 'Interest Rate']
            file_path = questionary.text("Input the filepath (including the name of the file.csv) for where you would like the results saved to (ex: ./data/qualifying_loans.csv): ").ask()
            file_path = str(file_path)
            #Opens new csv file called qualifying_loans.csv
            with open(file_path,'w',newline='') as csvfile: 
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(header)    
                #iterates through each qualifying loans and saves it as a row in the csv file
                for loan in qualifying_loans:
                    csvwriter.writerow(loan)