from rest_framework.permissions import BasePermission


class IsManager(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        return False


class IsOwner(BasePermission):
    def has_permission(self, request, view):
        if request.user == view.get_object().user:
            return True
        return False
