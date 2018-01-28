# -*- coding:utf-8 -*-
__author__ = 'qiuyyb'

from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home/$', views.home, name='home'),
    url(r'^login/$', views.log_in, name='login'),
    url(r'^logout/$', views.log_out, name='logout'),
    url(r'^console/$', views.console, name='console'),
    url(r'^asset/$', views.asset, name='asset'),
    url(r'^fpcy_stat/$', views.fpcy_stat, name='fpcy_stat'),
    url(r'^fpcy_request_log/$', views.fpcy_request_log, name='fpcy_request_log'),
    url(r'^get_user_asset/$', views.get_user_asset, name='get_user_asset'),
    url(r'^asset/add/$', views.asset_add, name='asset_add'),
    url(r'^asset/(?P<asset_id>[0-9]+)/change/$', views.asset_change, name='asset_change'),
    url(r'^asset/(?P<asset_id>[0-9]+)/delete/$', views.asset_delete, name='asset_delete'),
    url(r'^host_connect/(?P<asset_id>[0-9]+)/$', views.host_connect, name='host_connect'),
    url(r'^get_auth_obj/$', views.get_auth_obj, name='get_auth_obj'),
    url(r'^get_free_asset/$', views.get_free_asset, name='get_free_asset'),
    url(r'^get_database/$', views.get_database, name='get_database'),
    url(r'^get_max_port/$', views.get_max_port, name='get_max_port'),
    url(r'^app/deploy/$', views.app_deploy, name='apps_deploy'),
    url(r'^app/$', views.apps, name='apps_list'),
    url(r'^access_log/$', views.access_log, name='access_log'),
    url(r'^app/start/$', views.start_app, name='start_app'),
    url(r'^app/stop/$', views.stop_app, name='stop_app'),
    url(r'^app/reload/$', views.reload_app, name='reload_app'),
    url(r'^app/update/$', views.update_app, name='update_app'),
    url(r'^help/$', views.help, name='help'),
    url(r'^http_data/$', views.http_data, name='http_data'),
    url(r'^message/$', views.message, name='message'),
    url(r'^monitor/$', views.monitor, name='monitor'),
    url(r'^upload/$', views.upload_file, name='upload'),
    url(r'^upload_file_list/$', views.upload_file_list, name='upload_file_list'),
    url(r'^ksbm_oss_file_update/$', views.ksbm_oss_file_update, name='ksbm_oss_file_update'),
    url(r'^task/$', views.task_list, name='task_list'),
    url(r'^config_file/$', views.config_file, name='config_file'),
    url(r'^config_file/add/$', views.config_file_add, name='config_file_add'),
    url(r'^config_file/(?P<app_name>[\w\-]+)/(?P<env>[\w]+)/(?P<file_path>.+)/(?P<file_name>.+)/editor/$',
        views.config_file_editor, name='config_file_editor'),
    url(r'^deny/$', views.deny, name='deny'),
    url(r'^sql_submit/$', views.sql_submit, name='sql_submit'),
    url(r'^sql_list/$', views.sql_list, name='sql_list'),
    url(r'^sql_exec/$', views.sql_exec, name='sql_exec'),
    url(r'^shell/$', views.shell, name='shell'),
    url(r'^log/$', views.get_log, name='get_log'),
    url(r'^get_log_handle/(?P<start_line>[0-9]+)/(?P<end_line>[0-9]+)/$', views.get_log_handle, name='get_log_handle'),
]