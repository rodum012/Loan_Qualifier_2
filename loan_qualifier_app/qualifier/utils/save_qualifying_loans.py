import csv

def save_qualifying_loans(qualifying_loans):
    """Saves the qualifying loans to a CSV file.

    Args:
        qualifying_loans (list of lists): The qualifying bank loans.
    """
    # @TODO: Complete the usability dialog for savings the CSV Files.
    #Creates header for CSV file
    header = ['Lender','Max Loan Amount','Max LTV', 'Max DTI', 'Min Credit Score', 'Interest Rate']
    #Opens new csv file called qualifying_loans.csv
    with open('./data/qualifying_loans.csv','w',newline='') as csvfile: 
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(header)    
        #iterates through each qualifying loans and saves it as a row in the csv file
        for loan in qualifying_loans:
            csvwriter.writerow(loan)