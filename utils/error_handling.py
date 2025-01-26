import logging

from rest_framework.exceptions import ValidationError

logger = logging.getLogger(__name__)


def handle_database_error(exception):
    logger.error(f'Database error: {exception}')
    raise ValidationError({'detail': 'Database error'}) from exception


def handle_integrity_error(exception):
    logger.exception('IntegrityError: possible duplicate')
    raise ValidationError({'detail': 'possible duplicate'}) from exception


def handle_object_does_not_exist_error(exception):
    logger.error(f'Object not found: {exception}')
    raise ValidationError({'detail': 'Object not found'}) from exception


def handle_generic_database_error(exception, context=''):
    logger.error(f'Database error in {context}: {exception}')
    raise ValidationError(
        {'detail': f'Database error in {context}'}
    ) from exception
