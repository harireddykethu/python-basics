def send_email(email, sender):

    sender(email, 'Hello there!')


def gmail_sender(email, message):
    print(f'Gmail: {message}, {email}')


def outlook_sender(email, message):
    print(f'Outlook: {message}, {email}')


# user here
send_email('someone@domain.com', outlook_sender)

send_email('someone@domain.com', lambda email,
           message: print(f'Lambda: {message}, {email}'))
