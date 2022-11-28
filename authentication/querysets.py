
from collections import namedtuple
from django.db.models import Q
from django.db.models import QuerySet

UserRoles = namedtuple('UserRoles', ['instructor', 'learner'])
role = UserRoles('INS', 'LRN')


class CustomUserQuerySet(QuerySet):

    def active_users(self):
        return self.filter(Q(is_active=True))

    def staff_users(self):
        return self.filter(Q(is_staff=True))

    def instactors(self):
        return self.filter(Q(role=role.instructor))

    def learners(self):
        return self.filter(Q(role=role.learner))











