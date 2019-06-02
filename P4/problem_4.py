class Group:
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.get_users():
        return True
    for sub_group in group.get_groups():
        return is_user_in_group(user, sub_group)
    return False

def main():
    tc_1()
    tc_2()
    tc_3()

# empty group
def tc_1():
    parent = Group('parent')
    print(is_user_in_group('parent_user', parent))
    # prints False

# user not in the group
def tc_2():
    parent = Group('parent')
    child = Group("child")
    sub_child = Group("subchild")
    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)
    child.add_group(sub_child)
    parent.add_group(child)
    print(is_user_in_group('parent_user', parent))
    # prints False

# default example from assignment
def tc_3():
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")
    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)
    child.add_group(sub_child)
    parent.add_group(child)
    print(is_user_in_group('sub_child_user', parent))
    # prints True

if __name__ == "__main__":
    main()
