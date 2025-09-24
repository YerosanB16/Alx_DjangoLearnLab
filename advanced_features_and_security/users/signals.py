from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group, Permission
from django.dispatch import receiver
from django.apps import apps

@receiver(post_migrate)
def create_user_groups(sender, **kwargs):
    if sender.name == 'users':
        groups = {
            "Admins": ['can_view', 'can_create', 'can_edit', 'can_delete'],
            "Editors": ['can_view', 'can_create', 'can_edit'],
            "Viewers": ['can_view']
        }

        for group_name, perms in groups.items():
            group, created = Group.objects.get_or_create(name=group_name)
            for perm_codename in perms:
                try:
                    perm = Permission.objects.get(codename=perm_codename)
                    group.permissions.add(perm)
                except Permission.DoesNotExist:
                    print(f"Permission {perm_codename} not found")
