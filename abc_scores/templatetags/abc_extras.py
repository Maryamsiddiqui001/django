from django import template
from django.core.files import File

register = template.Library()

@register.filter
def print_file_content(file_path):
  f = open(file_path, 'r') 
  content = f.read()
  f.close()
  return content
  
  
