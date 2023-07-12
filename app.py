from flask import Flask, render_template, request

app = Flask(__name__)

categorias = {
    'camisas': 'Camisas',
    'pantalones': 'Pantalones',
    'zapatos': 'Zapatos'
}

productos = {
    'camisas': [
        {
            'nombre': 'Camisa de algodón a rayas',
            'descripcion': 'Esta camisa es de manga larga y está confeccionada en algodón suave y transpirable. Tiene un diseño a rayas verticales en tonos azules y blancos. Cuenta con cuello clásico y cierre de botones en la parte frontal. Es una prenda versátil que se puede usar tanto en ocasiones casuales como en eventos más formales.',
            'precio': 29.99,
            'imagen': 'camisa-rayas-para-nino.jpg'
        },
        {
            'nombre': 'Camisa estampada de flores',
            'descripcion': 'Esta camisa de estilo tropical está hecha de una mezcla de algodón y poliéster, lo que la hace ligera y resistente. Tiene un estampado de flores de colores vibrantes sobre un fondo negro. Presenta un corte slim fit, cuello italiano y cierre de botones ocultos. Es perfecta para lucir un aspecto moderno y llamativo en días soleados.',
            'precio': 24.99,
            'imagen': 'image.jpeg'
        },
        {
            'nombre': 'Camisa de lino de manga corta',
            'descripcion': 'Esta camisa de lino es ideal para climas cálidos. Tiene mangas cortas y está confeccionada en lino transpirable de alta calidad. Tiene un color blanco clásico y un corte regular fit para mayor comodidad. Cuenta con un cuello de solapa y cierre frontal de botones. Es una opción elegante y fresca para eventos informales de verano.',
            'precio': 19.99,
            'imagen': '47040126_08.png'
        }
    ],
    'pantalones': [
        {
            'nombre': 'Pantalones chinos de color caqui',
            'descripcion': ' Estos pantalones chinos son de estilo clásico y están confeccionados en algodón resistente. Tienen un corte recto y un color caqui versátil que combina fácilmente con diferentes prendas. Cuentan con bolsillos delanteros y traseros, trabillas para cinturón y cierre de botón y cremallera. Son una opción elegante y casual que se adapta a diversas ocasiones.',
            'precio': 39.99,
            'imagen': 'pantalon-chino-vestir-caqui.jpg'
        },
        {
            'nombre': 'Pantalones vaqueros ajustados',
            'descripcion': 'Estos pantalones vaqueros ajustados están hechos de mezclilla de alta calidad. Tienen un corte ceñido al cuerpo que resalta la figura y proporciona un aspecto moderno. Vienen en un tono azul oscuro clásico con efecto desgastado en ciertas áreas. Cuentan con bolsillos delanteros y traseros, detalles de costuras y cierre de botón y cremallera. Son una opción versátil que se puede usar tanto de forma casual como en ocasiones más informales.',
            'precio': 49.99,
            'imagen': '31Lh1O-tQeL._SL500_.jpg'
        },
        {
            'nombre': 'Pantalones deportivos de tela técnica',
            'descripcion': 'Estos pantalones deportivos están fabricados con tela técnica de alta tecnología que ofrece comodidad y flexibilidad. Tienen un diseño moderno con un ajuste relajado y elástico en la cintura. Vienen en un tono negro. Cuentan con bolsillos laterales con cremallera y puños elásticos en los tobillos. Son ideales para actividades deportivas o para lucir un estilo deportivo y cómodo en tu día a día..',
            'precio': 14.99,
            'imagen': 'jogger-pantalones-chandal-moda-t.png'
        }
    ],
    'zapatos': [
        {
            'nombre': 'Zapatos Oxford de cuero',
            'descripcion': 'Estos zapatos Oxford están hechos de cuero genuino de alta calidad. Tienen un diseño clásico y elegante, con cierre de cordones y puntera redondeada. Vienen en color negro y cuentan con detalles de perforaciones en el empeine y costuras finas. Son ideales para ocasiones formales y se pueden combinar con trajes o atuendos más sofisticados.',
            'precio': 79.99,
            'imagen': 'oxford02.jpg'
        },
        {
            'nombre': 'Zapatillas deportivas de running',
            'descripcion': 'Estas zapatillas deportivas están diseñadas para correr y ofrecer un alto rendimiento. Tienen una parte superior de malla transpirable que proporciona ventilación y comodidad. La suela intermedia cuenta con tecnología de amortiguación para absorber impactos, y la suela exterior de goma ofrece tracción y durabilidad. Vienen en varios colores vibrantes y presentan detalles reflectantes para mayor visibilidad en condiciones de poca luz.',
            'precio': 59.99,
            'imagen': '99-thickbox_default-Michel-Holger.jpg'
        },
        {
            'nombre': 'Zapatos mocasines de ante',
            'descripcion': 'Estos zapatos mocasines están confeccionados en ante suave y flexible. Tienen un estilo casual y versátil, con una silueta sin cordones y detalles de costuras en el empeine. Vienen en un tono marrón claro y cuentan con una suela de goma flexible y antideslizante. Son perfectos para lucir un aspecto relajado pero sofisticado en ocasiones informales.',
            'precio': 34.99,
            'imagen': '319088057_830885034831807_3100388459411120041_n-1.jpg'
        }
    ]
}

@app.route('/')
def home():
    return render_template('index.html', categorias=categorias)

@app.route('/productos', methods=['GET'])
def mostrar_productos():
    categoria = request.args.get('categoria')
    busqueda = request.args.get('busqueda')
    
    if categoria in productos:
        productos_categoria = productos[categoria]
    elif busqueda:
        productos_categoria = []
        for _, productos_categoria in productos.items():
            productos_categoria.extend([producto for producto in productos_categoria if busqueda.lower() in producto['categoria'].lower()])
    else:
        productos_categoria = None
    
    return render_template('productos.html', productos=productos_categoria, categoria=categorias.get(categoria))

if __name__ == '__main__':
    app.run()

