import logging

from rest_framework.exceptions import ValidationError

logger = logging.getLogger(__name__)


class ErrorHandler:
    @classmethod
    def handle_database_error(cls, exception):
        """Handle database errors."""
        logger.error(f'Database error: {exception}')
        raise ValidationError({'detail': 'Database error'}) from exception

    @classmethod
    def handle_integrity_error(cls, exception):
        """Handle integrity errors."""
        logger.exception('IntegrityError: possible duplicate')
        raise ValidationError({'detail': 'possible duplicate'}) from exception

    @classmethod
    def handle_object_does_not_exist_error(cls, exception):
        """Handle object does not exist errors."""
        logger.error(f'Object not found: {exception}')
        raise ValidationError({'detail': 'Object not found'}) from exception

    @classmethod
    def handle_generic_database_error(cls, exception, context=''):
        """Handle generic database errors."""
        logger.error(f'Database error in {context}: {exception}')
        raise ValidationError(
            {'detail': f'Database error in {context}'}
        ) from exception
