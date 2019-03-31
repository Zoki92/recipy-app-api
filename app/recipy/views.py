from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Tag, Ingredient
from recipy import serializers


class BaseRecipeAttrViewSet(viewsets.GenericViewSet,
                            mixins.ListModelMixin,
                            mixins.CreateModelMixin):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('-name')


class TagViewSet(BaseRecipeAttrViewSet):
    # Manage tags in the database
    serializer_class = serializers.TagSerializer
    queryset = Tag.objects.all()

    def perform_create(self, serializer):
        # Create new tag
        serializer.save(user=self.request.user)


class IngredientViewSet(BaseRecipeAttrViewSet):
    # Manage ingredients in the database
    serializer_class = serializers.IngredientSerializer
    queryset = Ingredient.objects.all()

    def perform_create(self, serializer):
        # Create a new ingredient
        serializer.save(user=self.request.user)
