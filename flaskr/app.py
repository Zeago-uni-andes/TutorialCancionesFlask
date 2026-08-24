from flaskr import create_app
from .modelos import db, Cancion, Album, Usuario, Medio
from .modelos import AlbumSchema,UsuarioSchema,CancionSchema
from flask_restful import Api
from .vistas import VistaCanciones, VistaCancion, VistaSignIn, VistaLogIn, VistaAlbum, VistaAlbumsUsuario, VistaCancionesAlbum
from flask_jwt_extended import JWTManager

app= create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

api = Api(app)
api.add_resource(VistaCanciones, '/canciones')
api.add_resource(VistaCancion, '/cancion/<int:id_cancion>')
api.add_resource(VistaSignIn, '/signin')
api.add_resource(VistaLogIn, '/login')
api.add_resource(VistaAlbumsUsuario, '/usuario/<int:id_usuario>/albumes')
api.add_resource(VistaAlbum, '/album/<int:id_album>')
api.add_resource(VistaCancionesAlbum, '/album/<int:id_album>/canciones')

jwt = JWTManager(app)

# # 3. Bloque de prueba
# with app.app_context():
#     # Crea las tablas si no existen
#     db.create_all()

#     # Creación de instancias de los modelos
#     u1 = Usuario(nombre_usuario="jzea", contrasena="123456")

#     a1 = Album(
#         titulo="Grandes Éxitos",
#         anio=2024,
#         descripcion="Álbum de prueba",
#         medio=Medio.CD,
#     )

#     c1 = Cancion(
#         titulo="Prueba cancion",
#         minutos=2,
#         segundos=25,
#         interprete="Juan David Zea",
#     )
#     c2 = Cancion(
#         titulo="Prueba cancion 2",
#         minutos=3,
#         segundos=10,
#         interprete="Juan David Zea",
#     )

#     # Agregar a la sesión y guardar cambios
#     db.session.add(u1)
#     db.session.add(a1)
#     db.session.add_all([c1, c2])
#     db.session.commit()

#     # Consultar y mostrar resultados a través de los modelos
#     print("--- Usuarios ---")
#     print(Usuario.query.all())

#     print("--- Álbumes ---")
#     print(Album.query.all())

#     print("--- Canciones ---")
#     print(Cancion.query.all())

# with app.app_context():
#     u =  Usuario(nombre_usuario="jzea", contrasena="123456")
#     a1 = Album(
#         titulo="Grandes Éxitos",
#         anio=2024,
#         descripcion="Álbum de prueba",
#         medio=Medio.CD,
#     )
#     c1 = Cancion(titulo="Prueba cancion",minutos=2,segundos=25,interprete="Juan David Zea")
#     u.albumes.append(a1)
#     a1.canciones.append(c1)
#     db.session.add(u)
#     db.session.add(c1)
#     db.session.commit()
#     # print(Usuario.query.all())
#     # print(Usuario.query.all()[0].albumes)
#     # db.session.delete(u)
#     # print(Usuario.query.all())
#     # print(Album.query.all())
#     print(Album.query.all())
#     print(Cancion.query.all())
#     print(Album.query.all()[0].canciones)
#     db.session.delete(a1)
#     print(Album.query.all())
#     print(Cancion.query.all())

# with app.app_context():
#     album_schema = AlbumSchema()
#     usuario_schema = UsuarioSchema()
#     cancion_schema = CancionSchema()
#     A = Album(titulo="Grandes Éxitos",anio=2024,descripcion="Álbum de prueba",medio=Medio.CD)
#     U = Usuario(nombre_usuario="jzea", contrasena="123456")
#     C = Cancion(titulo="Prueba cancion",minutos=2,segundos=25,interprete="Juan David Zea")
#     db.session.add(A)
#     db.session.add(U)
#     db.session.add(C)
#     db.session.commit()
#     print([album_schema.dumps(album) for album in Album.query.all()])
#     print([usuario_schema.dumps(user) for user in Usuario.query.all()])
#     print([cancion_schema.dumps(cancion) for cancion in Cancion.query.all()])