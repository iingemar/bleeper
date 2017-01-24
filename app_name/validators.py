from django.core.exceptions import ValidationError


def validate_content(content):
    if content == 'abcde':
        raise ValidationError('Content cannot be abcde. / validators.validate_content')
    return content