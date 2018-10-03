from api.utils.mongo import db
from api.models.User import User

def get_users(request_args):
    result = User.objects.get_or_404()
    return result
    # result_str = json.dumps(list(result))
    # return '{{"users": {}}}'.format(result_str)

def get_user_by_id(id):
    pass

def post_user():
    pass
