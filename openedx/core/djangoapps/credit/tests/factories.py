from factory import DjangoModelFactory

from openedx.core.djangoapps.credit.models import CreditProvider


class CreditProviderFactory(DjangoModelFactory):
    class Meta(object):
        model = CreditProvider
