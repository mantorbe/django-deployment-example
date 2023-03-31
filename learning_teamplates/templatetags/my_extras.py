from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
	'''
	THis cuts out all values of 'arg' form the string
	'''
	return value.replace(arg, '')
#Esta es una forma de registrar el filtro, la otra es con el decorador que esta arriba de la funcion de
#register.filter('cut', cut)