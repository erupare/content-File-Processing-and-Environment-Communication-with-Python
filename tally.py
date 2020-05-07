import logging

def tally_votes(data):
    """ 
    the example voting data and operations are in the __main__ section
    write code that will ask for user input for item number being voted on
    create a log file named <voting item>.log 
    tally votes and log each vote
    using: tally = f"Item: {voting_item} Yes: {yes} No: {no}"
    return tally
    """

    pass # student code goes here

if __name__ == "__main__":
    voting_data = ["y", "n", "y", "y", "y", "n"]
    tally = tally_votes(voting_data)
    print(tally)
    