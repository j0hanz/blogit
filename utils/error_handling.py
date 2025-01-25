import logging

from rest_framework.exceptions import ValidationError

logger = logging.getLogger(__name__)


def handle_database_error(exception):
    logger.error(f'Database error: {exception}')
    raise ValidationError({'detail': 'Database error'}) from exception


def handle_integrity_error(exception):
    logger.exception('IntegrityError: possible duplicate')
    raise ValidationError({'detail': 'possible duplicate'}) from exception
