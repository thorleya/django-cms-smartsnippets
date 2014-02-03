from django.conf import settings
from collections import OrderedDict


shared_sites = getattr(settings, 'SMARTSNIPPETS_SHARED_SITES', [])
include_orphan = getattr(settings, 'SMARTSNIPPETS_INCLUDE_ORPHAN', True)
restrict_user = getattr(settings, 'SMARTSNIPPETS_RESTRICT_USER', False)

snippet_caching_time = getattr(settings, 'SMARTSNIPPETS_CACHING_TIME', 300)
caching_enabled = snippet_caching_time != 0

PRESET_COLORPICKER_SCHEMES = [OrderedDict([
        ('main_color', '#efa80e'),
        ('background', '#ffffff'),
        ('button_color', '#ef850d'),
        ('light_accent', '#0087bb'),
        ('darker_accent', '#016e97'),
        ('name', 'Yellow Theme'),
        ('id', 'yellow')    
    ]),OrderedDict([
        ('main_color', '#589846'),
        ('background', '#f3f4ee'),
        ('button_color', '#ef850f'),
        ('light_accent', '#7eb750'),
        ('darker_accent', '#1f6038'),
        ('name', 'Green Theme'),
        ('id', 'green')   
    ]),OrderedDict([
        ('main_color', '#ee4a2f'),
        ('background', '#f1f0ec'),
        ('button_color', '#9a8783'),
        ('light_accent', '#27314c'),
        ('darker_accent', '#ff3d1f'),
        ('name', 'Red Theme'),
        ('id', 'red')  
    ]),OrderedDict([
        ('main_color', '#5d3b6d'),
        ('background', '#f8f3f0'),
        ('button_color', '#7e5a88'),
        ('light_accent', '#a69ca7'),
        ('darker_accent', '#46324b'),
        ('name', 'Purple Theme'),
        ('id', 'purple')   
    ]),OrderedDict([
        ('main_color', '#ee6225'),
        ('background', '#f8f3f0'),
        ('button_color', '#d24a10'),
        ('light_accent', '#20639a'),
        ('darker_accent', '#0b3a64'),
        ('name', 'Orange Theme'),
        ('id', 'orange')   
    ]),OrderedDict([
        ('main_color', '#c1ad94'),
        ('background', '#ffffff'),
        ('button_color', '#404955'),
        ('light_accent', '#8697a5'),
        ('darker_accent', '#687a92'),
        ('name', 'Neutral Theme'),
        ('id', 'neutral')  
    ]),OrderedDict([
        ('main_color', '#541357'),
        ('background', '#fffdf1'),
        ('button_color', '#635262'),
        ('light_accent', '#f18c09'),
        ('darker_accent', '#332244'),
        ('name', 'Orange/Purple Theme'),
        ('id', 'orangepurple')
    ])]
