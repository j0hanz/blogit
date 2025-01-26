from django.db.models import Count


def annotate_profile_queryset(queryset):
    """Annotate profile queryset with counts."""
    return queryset.annotate(
        posts_count=Count('owner__posts', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True),
    ).order_by('-created_at')


def annotate_post_queryset(queryset):
    """Annotate post queryset with counts."""
    return (
        queryset.select_related('owner')
        .annotate(comments_count=Count('comments'))
        .order_by('-created_at')
    )


def annotate_notification_queryset(queryset):
    """Annotate notification queryset."""
    return queryset.select_related('actor', 'recipient')


def annotate_comment_queryset(queryset):
    """Annotate comment queryset."""
    return queryset.select_related('owner', 'post')
