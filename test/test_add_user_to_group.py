from model.userinfo import UserInfo
import random
from model.group import Group


def test_add_user_to_group(app, orm):
    if app.user.count() == 0:
        app.user.create(UserInfo(firstname="Test", lastname="TEST"))
    if app.group.count() == 0:
        app.group.create(Group(name="Test", header="", footer=""))
    all_users = orm.get_userinfo_list()
    user = random.choice(all_users)

    ##Выберем случайную группу из существующих
    groups = orm.get_group_list()
    group_id = random.choice(groups).id
    app.user.add_user_to_group(user.id, group_id)
    new_users = orm.get_userinfo_in_group(Group(id=group_id))
    assert user in new_users


