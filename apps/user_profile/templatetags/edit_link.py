from django import template
from django.core.urlresolvers import reverse


register = template.Library()


@register.simple_tag
def get_path(obj):
    return reverse('admin:%s_%s_change' % (
                    obj._meta.app_label,
                    obj._meta.module_name
                ), args=(obj.id,))


class EditLinkNode(template.Node):
    def __init__(self, obj):
        self.object = template.Variable(obj)

    def render(self, context):
        _object = self.object.resolve(context)
        path = get_path(_object)
        return u'<a href="%s">(admin)</a>' % path


@register.tag(name="edit_link")
def do_edit_link(parser, token):
    token = token.split_contents()
    try:
        obj = token.pop(1)
    except IndexError:
        raise template.TemplateSyntaxError, \
            '%s tag requires at least an object as first argument' % token[0]
    return EditLinkNode(obj)
