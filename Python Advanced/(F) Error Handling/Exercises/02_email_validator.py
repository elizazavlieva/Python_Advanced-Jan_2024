import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


name_pattern = r'^\w+'
symbol_pattern = r'@'
domain_pattern = r'\.(com|bg|org|net)$'
email_min_len = 5


email = input()
while email != 'End':

    name = re.findall(name_pattern, email)
    symbol = re.findall(symbol_pattern, email)
    domain = re.findall(domain_pattern, email)

    if len(name[0]) < email_min_len:
        raise NameTooShortError('Name must be more than 4 characters')

    elif not symbol:
        raise MustContainAtSymbolError('Email must contain @')

    elif not domain:
        raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')

    else:
        print('Email is valid')

    email = input()
