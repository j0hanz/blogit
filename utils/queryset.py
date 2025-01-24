from django.db.models import Count


def annotate_profile_queryset(queryset):
    return queryset.annotate(
        posts_count=Count('owner__posts', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True),
    ).order_by('-created_at')


def annotate_post_queryset(queryset):
    return (
        queryset.select_related('owner')
        .annotate(comments_count=Count('comments'))
        .order_by('-created_at')
    )
