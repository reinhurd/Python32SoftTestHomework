from model.userinfo import UserInfo
import random
from model.group import Group


def test_del_user_from_group(app, orm):
    if app.user.count() == 0:
        app.user.create(UserInfo(firstname="Test", lastname="TEST"))
    if app.group.count() == 0:
        app.group.create(Group(name="Test", header="", footer=""))
    ##Выберем случайную группу из существующих
    groups = orm.get_group_list()
    group = random.choice(groups)
    ##Найден в ней всех пользователей
    users_in_group = orm.get_userinfo_in_group(group)
    ##Если пользователей в группе нет, добавим нового
    if len(users_in_group) == 0:
        all_users = orm.get_userinfo_list()
        user = random.choice(all_users)
        app.user.add_user_to_group(user.id, group.id)
    users_in_group = orm.get_userinfo_in_group(group)
    user_to_del = random.choice(users_in_group)
    app.user.del_user_from_group(user_to_del.id, group.id)
    new_users = orm.get_userinfo_in_group(group)
    assert user_to_del not in new_users
