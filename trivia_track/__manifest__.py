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
                'board',
                'generar_folios'],
    'data': [
        'views/trivia_track.xml',
        'views/page_trivia.xml',
        'views/trivia_rifa.xml',
        'views/rifa.xml',
        'data/data.xml',
        'views/menu.xml',
    ],
    'qweb': ['static/src/xml/*.xml'],
}
