from rest_framework.permissions import BasePermission


class IsCompanyOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.is_company_owner:
            return True
        else:
            return False
