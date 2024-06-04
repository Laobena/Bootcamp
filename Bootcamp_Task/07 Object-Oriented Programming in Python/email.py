class Email:
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False
    
    
    def marked_as_read(self):
        if not self.has_been_read:
            self.has_been_read = True
            return "Marked as read"
    

    def populate_inbox(inbox):
        inbox.append(email_1)
        inbox.append(email_2)
        inbox.append(email_3)
        return inbox
    

    def email_list(inbox):
        for index, email in enumerate(inbox, start=1):
            print(f"{index}  {email.subject_line}")
        
        
    def read_email(inbox):
        Email.email_list(inbox)  
        while True:
            try:
                user_input = int(input("Enter the number of the email you would like to read:\n"))
                if 1 <= user_input <= len(inbox):
                    print(f"Email Address: {inbox[user_input - 1].email_address}")
                    print(f"Subject Line: {inbox[user_input - 1].subject_line}")
                    print(f"Email Content: {inbox[user_input - 1].email_content}")
                    break
                else:
                    print("Invalid input. Please enter a valid email number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

            

inbox = []
email_1 = Email("emanuel@gmail.com", "Good Morning", "Hello what are you doing today?" )
email_2 = Email("Chickenworld@gmail.com", "Selling Chickens", "Hello we are wondering if you would like to buy some chickens")
email_3 = Email("meditationmentor@yahoo.com", "Meditate", "Good moring this is a daily reminder for yo to meditate today.")  
Email.populate_inbox(inbox)

print("Welcome to your email")
print("What would you like to do?: ")
while True:
    try:
        user = int(input("1. Read an email \n2. View unread emails \n3.Quit application: \n"))
        if user == 1:
            Email.read_email(inbox)
        elif user == 2:
            Email.email_list(inbox)
        else:
            exit()
    except ValueError:
                print("Invalid input. Please enter a number.")










