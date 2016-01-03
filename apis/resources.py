from tastypie.authorization import Authorization
from tastypie.authentication import Authentication
from tastypie.resources import ModelResource
from apis.models import PackageGeneric, PackageGenericEdu, PackageCinnamon, PackageCinnamonEdu, PackageMate, PackageMateEdu

API_LIMIT_PER_PAGE = 0

class PackageGenericResource(ModelResource):
    class Meta:
        #Query que va a mostarar la api
        queryset = PackageGeneric.objects.all()
        #El limite de registro que tendra la api, en este caso es 0 infinitos
        limit = 0
        #Nombre por el cual van acceder a la api
        resource_name = 'paquetes-generic'
        #Metodos que va a permitir la api
        list_allowed_methods = ['get', 'post', 'put', 'delete']
        always_return_data = True
        authorization = Authorization()

class PackageGenericEduResource(ModelResource):
    class Meta:
        queryset = PackageGenericEdu.objects.all()
        limit = 0
        resource_name = 'paquetes-generic-edu'
        list_allowed_methods = ['get', 'post', 'put', 'delete']
        always_return_data = True
        authorization = Authorization()

class PackageCinnamonResource(ModelResource):
    class Meta:
        queryset = PackageCinnamon.objects.all()
        limit = 0
        resource_name = 'paquetes-cinnamon'
        list_allowed_methods = ['get', 'post', 'put', 'delete']
        always_return_data = True

class PackageCinnamonEduResource(ModelResource):
    class Meta:
        queryset = PackageCinnamonEdu.objects.all()
        limit = 0
        resource_name = 'paquetes-cinnamon-edu'
        list_allowed_methods = ['get', 'post', 'put', 'delete']
        always_return_data = True
        authorization = Authorization()

class PackageMateResource(ModelResource):
    class Meta:
        queryset = PackageMate.objects.all()
        limit = 0
        resource_name = 'paquetes-mate'
        list_allowed_methods = ['get', 'post', 'put', 'delete']
        always_return_data = True
        authorization = Authorization()

class PackageMateEduResource(ModelResource):
    class Meta:
        queryset = PackageMateEdu.objects.all()
        limit = 0
        resource_name = 'paquetes-mate-edu'
        list_allowed_methods = ['get', 'post', 'put', 'delete']
        always_return_data = True
        authorization = Authorization()