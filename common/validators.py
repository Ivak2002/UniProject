from django.core.exceptions import ValidationError
def number_validator(value):

    if not value.isdigit():
        raise ValidationError('Phone number must contain only digits.')


    if len(value) != 10:
        raise ValidationError('Phone number must be exactly 10 digits long.')


    if not value.startswith('0'):
        raise ValidationError('Phone number must start with 0.')


    valid_prefixes = ['02', '03', '04', '05', '06', '07', '08', '09']
    if value[:2] not in valid_prefixes:
        raise ValidationError('Phone number prefix is not valid for Bulgaria.')