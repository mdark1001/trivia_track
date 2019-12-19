{
    'name': "Trivia track",

    'summary': """
      Tablero de Indicadores
    """,

    'description': """
       Trivia-Track
    """,

    'author': "@MiguelCabrera1001",
    'website': "",

    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'generar_folios'
                ],
    'data': [
        'security/ir.model.access.csv',
        'views/trivia_track.xml',
        'views/page_trivia.xml',
        'views/rifa.xml',
        'data/data.xml',
        'views/menu.xml',
        'views/trivia_rifa.xml',

    ],
    'qweb': ['static/src/xml/*.xml'],
}
