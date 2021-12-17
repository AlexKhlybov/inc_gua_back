from rest_framework import permissions
from ..models import User


class IsUser(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.pk == request.user.pk


class RejectAll(permissions.BasePermission):

    def has_permission(self, request, view):
        return False


class IsRoleOrReject(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return hasattr(obj, 'role') and obj.role == request.user.role


class IsUnderwriterOrReject(IsRoleOrReject):

    def has_permission(self, request, view):
        return hasattr(request.user, 'role') and request.user.role == User.ROLE.UNDERWRITER

    def has_object_permission(self, request, view, obj):
        return hasattr(request.user, 'role') and request.user.role == User.ROLE.UNDERWRITER


class IsMasterUnderwriterOrReject(IsRoleOrReject):

    def has_permission(self, request, view):
        return hasattr(request.user, 'role') and request.user.role == User.ROLE.MASTER_UNDERWRITER

    def has_object_permission(self, request, view, obj):
        return hasattr(request.user, 'role') and request.user.role == User.ROLE.UNDERWRITER


class IsPrincipalOrReject(IsRoleOrReject):

    def has_permission(self, request, view):
        return hasattr(request.user, 'role') and request.user.role == User.ROLE.PRINCIPAL

    def has_object_permission(self, request, view, obj):
        return hasattr(request.user, 'role') and request.user.role == User.ROLE.UNDERWRITER


class IsAgentOrReject(IsRoleOrReject):

    def has_permission(self, request, view):
        return hasattr(request.user, 'role') and request.user.role == User.ROLE.AGENT

    def has_object_permission(self, request, view, obj):
        return hasattr(request.user, 'role') and request.user.role == User.ROLE.UNDERWRITER


class IsBankOrReject(IsRoleOrReject):

    def has_permission(self, request, view):
        return hasattr(request.user, 'role') and request.user.role == User.ROLE.BANK

    def has_object_permission(self, request, view, obj):
        return hasattr(request.user, 'role') and request.user.role == User.ROLE.UNDERWRITER
