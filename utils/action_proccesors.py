from actions.models import Action


def last_actions_following(request):
    if not request.user.is_anonymous:
        return {'last_actions_list': Action.objects.filter(user__in=request.user.following.all())[:3]}
    else:
        return {'last_actions_list': 'Hui'}
