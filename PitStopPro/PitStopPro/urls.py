"""
URL configuration for PitStopPro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from Home import views as homeViews
from Calendar import views as calendarViews
from Inventory import views as inventoryViews
from Employees import views as employeeViews
from Invoicing import views as invoiceViews
from Authentication import views as authViews
from userSettings import views as settingViews
from Pricing import views as pricingViews
from ContactUs import views as contactViews
from CustomerContact import views as customerViews
from Jobs import views as jobViews
from Customers import views as customerRewardsViews

urlpatterns = [
            # LOGIN URLS
    path("", authViews.signin, name = "login/"),
    path("login/", authViews.signin, name = "login/"),
    path("",include('django.contrib.auth.urls')),
    path("login/",include('django.contrib.auth.urls')),
    path("signup/", authViews.signup, name = "signup/"),
    path("settings/", settingViews.settings, name = "settings/"),
            # HOME , ADMIN and DEBUG URLS
    path("home/", homeViews.Home,name="home"),
    path("admin/", admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
            # CALENDAR URLS
    path('calendar/', calendarViews.CalendarView.as_view(), name='calendar'),
    path('event/new/', calendarViews.event, name='event_new'),
    path('event/edit/(?P<event_id>\d+)/', calendarViews.event, name='event_edit'),
            #INVENTORY URLS
    path('inventory/', inventoryViews.inventory, name='inventory'),
    path('inventory/new/',inventoryViews.new_inventory,name="new_inventory"),
    path('inventory/edit/(?P<inventory_id>\d+)',inventoryViews.new_inventory,name="edit_inventory"),
    path('inventory/delete/(?P<inventory_id>\d+)',inventoryViews.delete_inventory,name="delete_inventory"),
            # EMPLOYEES URLS
    path('employees/', employeeViews.employee_list, name='employee_list'),
    path('employees/view.(?P<employee_id>\d+)/', employeeViews.employee_detail, name='employee_detail'), # THIS ONE
    path('payroll/', employeeViews.payroll_list, name='payroll_list'),
    path('payroll/<int:payroll_id>/', employeeViews.payroll_detail, name='payroll_detail'),
    path('employees/delete/(?P<employee_id>\d+)', employeeViews.delete_employee, name='delete_employee'),
    path('employees/add/payroll', employeeViews.addPayroll, name='add_payroll'),
            # INVOICING URLS
    path('createinvoice/', invoiceViews.createInvoice, name='createinvoice'),
    path('invoicing/', invoiceViews.viewInvoices, name='invoicing'),
    path('jobs/delete/<int:jobs_id>',invoiceViews.deleteInvoice, name="delete_invoice"),
    path('jobs/download/<int:jobs_id>/pdf', invoiceViews.downloadInvoice, name='download_invoice'),
            # PRICING CONTACTS
    path('pricing/', pricingViews.viewPricing, name='pricing'),
    path('contactus/', contactViews.Contact,name="contact"),
            # EARNINGS URLS
    path('earnings/', include('Earnings.urls'), name="earnings"),
            # CUSTOMER CONTACT URLS
    path('CustomerContact/', customerViews.CustomerContact, name="customerContact"),
    path('CustomerContact/message/(?P<clientID>\d+)', customerViews.sendMessage, name="sendMessage"),
    path('CustomerContact/message/ALL',customerViews.sendToAll, name="sendtoall"),
            # JOBS URLS
    path('jobs/',jobViews.viewJobs,name="jobs" ),
    path('jobs/new/',jobViews.createJob,name="createjobs"),
    path('jobs/addClient',jobViews.addClient, name="addclient"),
    path('jobs/addVehicle',jobViews.addVehicle, name="addvehicle"),
    path('jobs/delete/<int:jobs_id>',jobViews.deleteJob, name="delete_job"),
            # CUSTOMER REWARDS URLS
    path('customers/', customerRewardsViews.Customers, name='customers'),
    path('privacy-policy/', authViews.privacy_policy, name='privacy-policy'),
    path('terms-and-conditions/', authViews.terms_and_conditions, name='terms-and-conditions'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
