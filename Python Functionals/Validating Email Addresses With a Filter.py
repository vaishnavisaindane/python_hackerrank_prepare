def fun(email):
     try:
        username, url = email.split('@')
        website, extension = url.split('.')
     except ValueError:
        return False

     if username.replace('-', '').replace('_', '').isalnum() is False:
        return False
     elif website.isalnum() is False:
        return False
     elif len(extension) > 3:
        return False
     else:
        return True
    # return True if s is a valid email, else return False

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)



https://youtu.be/ymo0YaMrc6s?si=ypiC63Ul2lx4yTQD
