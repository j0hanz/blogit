from rest_framework import serializers


def validate_actor_and_recipient(data):
    if data['actor'] == data['recipient']:
        msg = 'Actor and recipient cannot be the same.'
        raise serializers.ValidationError(msg)
    return data


def validate_followed_user(request_user, value):
    if request_user == value:
        msg = 'You cannot follow yourself.'
        raise serializers.ValidationError(msg)
    return value


def validate_like_post(request_user, value):
    if request_user.likes.filter(post=value).exists():
        msg = 'You have already liked this post.'
        raise serializers.ValidationError(msg)
    return value
