import graphene
from graphene_django.types import DjangoObjectType

from apps.biz.models import Biz


class BizType(DjangoObjectType):
    class Meta:
        model = Biz
        fields = ('uuid', 'title', 'description', 'address', 'city', 'phone', 'is_claimed')


class Query(graphene.ObjectType):
    all_biz = graphene.List(BizType)

    def resolve_all_biz(root, info):
        return Biz.objects.all()


schema = graphene.Schema(query=Query)
