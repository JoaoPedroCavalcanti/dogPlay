from rest_framework.permissions import BasePermission

class IsOwnerOrAdmin(BasePermission):
    
    def has_permission(self, request, view):
        return super().has_permission(request, view)
    
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        if obj.petOwner == None:
            return True
        if obj.petOwner == request.user:
            return True
        return False