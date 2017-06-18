from django import template
register = template.Library()

@register.assignment_tag
def defineAlign(val=None):
  return "http://imgs.neverfate.ru/aligns/align" + val + ".png"

@register.assignment_tag
def defineClanIcon(val=None):
  return "http://imgs.neverfate.ru/clans/" + val + ".gif"

@register.assignment_tag
def defineInfoUrl(val=None):
  return "http://neverfate.ru/inf.php?cid=" + val

@register.assignment_tag
def defineClan(val=None):
  return val