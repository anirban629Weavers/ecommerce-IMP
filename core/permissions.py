from rest_framework import permissions
from core.models import User

class IsStaffPermission(permissions.BasePermission):
    """
        Custom permission to only allow staff members.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)

