"""
Views for Recipe APIs
"""

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Recipe
from recipe import serializers


class RecipeViewSet(viewsets.ModelViewSet):
    """View for manage recipe APIs"""
    serializer_class = serializers.RecipeSerializer
    queryset = Recipe.objects.all()

    # all users must be authenticated
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # we want to make sure the recipes are get by the authenticated user
    def get_queryset(self):
        """Retrieve recopes for authenticated user"""
        return self.queryset.filter(user=self.request.user).order_by('-id')
