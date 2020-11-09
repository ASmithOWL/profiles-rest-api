from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile

    Args:
        permissions (lib): django rest_framework library that contains the BasePermissions class
    """

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile

        Args:
            request (str): The HTTP request with update data
            view (class): The Django api viewset
            obj (object): the object being updated
        """

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
