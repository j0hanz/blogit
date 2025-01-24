from django.core.exceptions import ValidationError

MAX_CONTENT_LENGTH = 500


def validate_content(value, image=None):
    if not value and not image:
        msg = 'You must upload an image or write some content.'
        raise ValidationError(msg)
    if len(value) > MAX_CONTENT_LENGTH:
        msg = f'Content cannot exceed {MAX_CONTENT_LENGTH} characters.'
        raise ValidationError(msg)
    return value
