def check_role(user, roles):
    if user.role not in roles:
        raise Exception("Access denied")