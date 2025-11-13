"""Senacmon URL configuration."""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("accounts/", include(("accounts.urls", "accounts"), namespace="accounts")),
    path("game/", include(("game.urls", "game"), namespace="game")),
    path("wallet/", include(("wallet.urls", "wallet"), namespace="wallet")),
]

# Servir arquivos estáticos em modo DEBUG (CSS do admin, etc.)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
