import smtplib
import colors as color
import os
import set_environ

def send(to_addr, subject, text):

    # Message parameters
    from_addr = os.environ.get("my_gmail")

    #  Server settings
    out = "smtp.gmail.com"
    port = 587
    user = os.environ.get("my_gmail")
    passwd = os.environ.get("my_gmail_pass")

    # Compile the message
    message = "From: " + from_addr + "\nTo: " + to_addr + "\nSubject: " + subject + "\n\n" + text

    # Send the message
    server = smtplib.SMTP(out, port)
    server.ehlo()
    server.starttls()
    server.login(user, passwd)
    server.sendmail(from_addr, to_addr, message)
    server.close()
    print(color.yellow, color.bold, "Email sent!", color.reset, sep="")

if __name__ == '__main__':
    send(os.environ.get("my_icloud"), "Test Email", "Hello, World!")
    