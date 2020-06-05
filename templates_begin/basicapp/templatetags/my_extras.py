from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts out all values of arg from the string!
    """

    return value.replace(arg,'')
#Instead of decorator the below one can be used
#register.filter('cut',cut) #Name of our filter and its function
