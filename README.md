# Utilizar el proxy model en el modelo en Django

Este es un tutorial hecho en mi web, para verlo podéis pinchar aquí [https://cosasdedevs.com/posts/como-utilizar-el-proxy-model-de-django/](https://cosasdedevs.com/posts/como-utilizar-el-proxy-model-de-django/)

Para utilizarlo tenéis que crear el entorno virtual y lanzar el siguiente comando para instalar las librerías:

```
pip install -r requirements.txt
```

Una vez hecho esto podéis hacer pruebas lanzando el siguiente comando que os abrirá una consola:

```
python manage.py shell_plus --ipython
```

Un ejemplo para utilizar las funciones que hemos creado en el ejemplo:

```python
c = ExtensionContacto.objects.all()

for contact in c:
	contact.get_edad()
	contact.get_datos_contacto()
```