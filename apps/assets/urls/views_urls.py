# coding:utf-8
from django.conf.urls import url
from .. import views

app_name = 'assets'

urlpatterns = [
    # Resource asset url
    url(r'^$', views.AssetListView.as_view(), name='asset-index'),
    url(r'^asset/$', views.AssetListView.as_view(), name='asset-list'),
    url(r'^asset/create/$', views.AssetCreateView.as_view(), name='asset-create'),
    url(r'^asset/export/$', views.AssetExportView.as_view(), name='asset-export'),
    url(r'^asset/import/$', views.BulkImportAssetView.as_view(), name='asset-import'),
    url(r'^asset/(?P<pk>[0-9a-zA-Z\-]{36})/$', views.AssetDetailView.as_view(), name='asset-detail'),
    url(r'^asset/(?P<pk>[0-9a-zA-Z\-]{36})/update/$', views.AssetUpdateView.as_view(), name='asset-update'),
    url(r'^asset/(?P<pk>[0-9a-zA-Z\-]{36})/delete/$', views.AssetDeleteView.as_view(), name='asset-delete'),
    url(r'^asset/update/$', views.AssetBulkUpdateView.as_view(), name='asset-bulk-update'),

    # asset more details by litian 20180409
    url(r'^asset/(?P<asset_id>[0-9a-zA-Z\-]{36})/more_detail/(?P<node>[0-9]+)$', views.asset_more_detail_view, name='asset-more-detail'),
    url(r'^asset/(?P<asset_id>[0-9a-zA-Z\-]{36})/more_detail/update$', views.asset_more_detail_update, name='asset-more-detail-update'),

    # User asset view
    url(r'^user-asset/$', views.UserAssetListView.as_view(), name='user-asset-list'),

    # Resource admin user url
    url(r'^admin-user/$', views.AdminUserListView.as_view(), name='admin-user-list'),
    url(r'^admin-user/create/$', views.AdminUserCreateView.as_view(), name='admin-user-create'),
    url(r'^admin-user/(?P<pk>[0-9a-zA-Z\-]{36})/$', views.AdminUserDetailView.as_view(), name='admin-user-detail'),
    url(r'^admin-user/(?P<pk>[0-9a-zA-Z\-]{36})/update/$', views.AdminUserUpdateView.as_view(), name='admin-user-update'),
    url(r'^admin-user/(?P<pk>[0-9a-zA-Z\-]{36})/delete/$', views.AdminUserDeleteView.as_view(), name='admin-user-delete'),
    url(r'^admin-user/(?P<pk>[0-9a-zA-Z\-]{36})/assets/$', views.AdminUserAssetsView.as_view(), name='admin-user-assets'),

    # Resource system user url
    url(r'^system-user/$', views.SystemUserListView.as_view(), name='system-user-list'),
    url(r'^system-user/create/$', views.SystemUserCreateView.as_view(), name='system-user-create'),
    url(r'^system-user/(?P<pk>[0-9a-zA-Z\-]{36})/$', views.SystemUserDetailView.as_view(), name='system-user-detail'),
    url(r'^system-user/(?P<pk>[0-9a-zA-Z\-]{36})/update/$', views.SystemUserUpdateView.as_view(), name='system-user-update'),
    url(r'^system-user/(?P<pk>[0-9a-zA-Z\-]{36})/delete/$', views.SystemUserDeleteView.as_view(), name='system-user-delete'),
    url(r'^system-user/(?P<pk>[0-9a-zA-Z\-]{36})/asset/$', views.SystemUserAssetView.as_view(), name='system-user-asset'),

    url(r'^label/$', views.LabelListView.as_view(), name='label-list'),
    url(r'^label/create/$', views.LabelCreateView.as_view(), name='label-create'),
    url(r'^label/(?P<pk>[0-9a-zA-Z\-]{36})/update/$', views.LabelUpdateView.as_view(), name='label-update'),
    url(r'^label/(?P<pk>[0-9a-zA-Z\-]{36})/delete/$', views.LabelDeleteView.as_view(), name='label-delete'),

    url(r'^domain/$', views.DomainListView.as_view(), name='domain-list'),
    url(r'^domain/create/$', views.DomainCreateView.as_view(), name='domain-create'),
    url(r'^domain/(?P<pk>[0-9a-zA-Z\-]{36})/$', views.DomainDetailView.as_view(), name='domain-detail'),
    url(r'^domain/(?P<pk>[0-9a-zA-Z\-]{36})/update/$', views.DomainUpdateView.as_view(), name='domain-update'),
    url(r'^domain/(?P<pk>[0-9a-zA-Z\-]{36})/delete/$', views.DomainDeleteView.as_view(), name='domain-delete'),
    url(r'^domain/(?P<pk>[0-9a-zA-Z\-]{36})/gateway/$', views.DomainGatewayListView.as_view(), name='domain-gateway-list'),

    url(r'^domain/(?P<pk>[0-9a-zA-Z\-]{36})/gateway/create/$', views.DomainGatewayCreateView.as_view(), name='domain-gateway-create'),
    url(r'^domain/gateway/(?P<pk>[0-9a-zA-Z\-]{36})/update/$', views.DomainGatewayUpdateView.as_view(), name='domain-gateway-update'),
]

