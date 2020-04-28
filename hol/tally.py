import logging

def tally_votes(data):
    voting_item = input("What is the item number for this vote? ")
    file_name = f"{voting_item}.log"

    # start log

    yes = 0
    no = 0
    for vote in data:
        if vote == "y":
            yes = yes + 1
        else:
            no = no + 1
        # log vote
        
    
    tally = f"Item: {voting_item} Yes: {yes} No: {no}"
    
    # log tally
    
    return tally, voting_item

if __name__ == "__main__":
    voting_data = ["y", "n", "y", "y", "y", "n"]
    tally, voting_item = tally_votes(voting_data)
    print(tally)
    