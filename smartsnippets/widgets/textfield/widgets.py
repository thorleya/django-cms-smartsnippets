from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
from smartsnippets.widgets_pool import widget_pool
from smartsnippets.widgets_base import SmartSnippetWidgetBase


class TextField(SmartSnippetWidgetBase):
    name = 'Text Field'

    def render(self):
        return render_to_string('smartsnippets/widgets/textfield/widget.html',
                                    {'field': self})

widget_pool.register_widget(TextField)