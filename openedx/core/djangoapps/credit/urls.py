"""
URLs for the credit app.
"""
from django.conf.urls import patterns, url, include

from openedx.core.djangoapps.credit import views, routers

PROVIDER_ID_PATTERN = r'(?P<provider_id>[^/]+)'

V1_URLS = patterns(
    '',

    # TODO Move to viewset
    url(
        r'^providers/{provider_id}/request/$'.format(provider_id=PROVIDER_ID_PATTERN),
        views.create_credit_request,
        name='create_request'
    ),

    # Move to own view
    url(
        r'^providers/{provider_id}/callback/?$'.format(provider_id=PROVIDER_ID_PATTERN),
        views.credit_provider_callback,
        name='provider_callback'
    ),

    # Move to view
    url(
        r'^eligibility/$',
        views.get_eligibility_for_user,
        name='eligibility_details'
    ),
)

router = routers.SimpleRouter()  # pylint: disable=invalid-name
router.register(r'courses', views.CreditCourseViewSet)
router.register(r'providers', views.CreditProviderViewSet)
V1_URLS += router.urls

urlpatterns = patterns(
    '',
    url(r'^v1/', include(V1_URLS)),
)
