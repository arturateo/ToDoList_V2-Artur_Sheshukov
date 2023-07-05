from to_do_list_v2.models import TYPE_TASKS, STATUS


def get_context_constants(request):
    return {'type_tasks': TYPE_TASKS, 'statuses': STATUS}
