from config.wsgi import *

from core.models import Type, Employee

#listar
"""query = Type.objects.all()
print(query)"""

#insercion
##t = Type(name = 'tostada').save()
##t.name = 'nutella'
##t.save()

#actualizacion
"""t = Type.objects.get(pk='4')
t.name = 'Cake'
t.save()"""


#eliminacion
"""try:
    t = Type.objects.get(pk='1')
    t.delete()
except Exception as e:
    print(e)"""

#listar de tipo filter ...icontains para hacer filtro sin importar las mayusculas o minusculas
ob = Employee.objects.filter(type_id=2)


for i in Type.objects.filter(name__endswith='e')[:2]:
    print(i.name)
