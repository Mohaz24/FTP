fn = input('Enter a file:')
fh = open(fn,'r')
most_sent_emails_user = dict()
# READING EMAIL FILES
for email in fh :
    if email.startswith('From') :
    # Create string collection
     split_emails = email.split()
    # Extract all the users
     extract_users = split_emails[1]
    # Use the dic to count the most sent email  
     most_sent_emails_user[extract_users] = most_sent_emails_user.get(extract_users, 0) + 1
# Loop through all the emails by converting the data to tuples 
for key,value in most_sent_emails_user.items() : 
#  Find the number which user sent the emails by checking with conditional statement.
#  If the tuple value is greater or equal.
   if value >= 10:
    # Print out the most email sent by a user
    print(f"The most sent email by user: {key} by {value} emails")
  