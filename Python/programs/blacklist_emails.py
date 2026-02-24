"""
Imagine we're responsible for the security of a website, and we need to check a list of email addresses
against a blacklist. If an address is found on the blacklist, we need to stop checking immediately.

Create a function check_emails_against_blacklist that:

Takes a list of emails and a blacklist.
Iterates through the emails using a for loop.
If the current address is in the blacklist, returns it and stops checking with break.
If emails is empty or isn't present in the blacklist, an empty string should be returned.
"""
def check_emails_against_blacklist(emails: list[str], blacklist: set) -> str:
    rtn_email = ""
    blk_ctr=0
    for email in emails:
        for blocked in blacklist:
            if email == blocked:
                print(f"Blocked email found: {email}")
                rtn_email = blocked
                blk_ctr+=1
                break
    print(f"Blocked emails found: {blk_ctr}")
    return(rtn_email)


emails = ["user@example.com", "banneduser@example.com","spam@blacklist.com", "anotheruser@example.com"]
#emails = ["user@example.com", "anotheruser@example.com"]
blacklist = {"spam@blacklist.com", "banneduser@example.com"}
check_emails_against_blacklist(emails, blacklist) # "spam@blacklist.com"
