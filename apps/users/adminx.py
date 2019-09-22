import xadmin
from xadmin import views
from .models import EmailVerifyRecord, Banner

class EmailVerifyRecordAdmin(object):
    # 显示的列
    list_display = ['code', 'email', 'send_type', 'send_time']
    # 搜索的字段，不要添加时间搜索
    search_fields = ['code','email','send_type']
    # 过滤
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    list_display = ['title','image','url','index','add_time']
    search_fields = ['title','image','url','index']
    list_filter = ['title','image','url','index','add_time']


class BaseSetting(object):
    '''开启主题功能'''
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    '''修改title'''
    site_title = '雪岭云杉后台管理'
    '''修改footer'''
    site_footer = '雪岭云杉教育科技有限公司'
    '''收起菜单'''
    menu_style = 'accordion'


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)