```python
from  rest_framework  import  viewsets
from app.models import Example
from app.serializer import ExampleSerializer
```
**using models as a db**
```python
class  ExampleViewSet(viewsets.ModelViewSet):
	serializer_class  = ExampleSerializer
	def  get_queryset(self):
		ex  = Example.object.all()
		return  ex
		
	def  retrieve(self, request, *args, **kwargs):
		params  =  kwargs
		query  = Example.objects.filter(db_field  =  params['pk'])
		serializer  =  ExampleSerializer(query, many=True)
		return  Response(serializer.data)
```
**using with a external a db**

```python
class  ExampleViewSet(viewsets.ModelViewSet):	
	def  retrieve(self, request, *args, **kwargs):
		params  =  kwargs['pk']		
		return  JsonResponse('''{dict}''')
```

