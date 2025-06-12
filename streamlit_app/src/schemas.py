class Texts:
    start_text = """

    <style>
        
        li {
            font-size: xx-large;
            text-align: center;
            list-style: none;
        }
        
        .first-header {
            text-align: center;
        }

        .who-we-are-header {
            text-align: center;
            font-size: xxx-large;
        }

        .start {
            color: #F97A00;
        }

        .countries {
            color: #129990;
        }

        .satellites {
            color: #E50046;
        }

        .agency {
            color: #E83F25;
        }

        .orbit-kind {
            color: #3674B5;
        }

        .us-info {
            text-align: center;
            font-size: x-large;
        }

    </style>

    <h1 class='first-header'>Para Navegar por el sitio, hagalo por las diferentes pestañas:</h1>
    <ul>
        <li class='start'>Inicio</li>
        <li class='countries'>Paises</li>
        <li class='satellites'>Satelites</li>
        <li class='agency'>Agencia</li>
        <li class='orbit-kind'>Tipo de orbita</li>
    </ul>
    
    <h2 class='who-we-are-header'>¿Quiénes somos?</h3>
    <p class='us-info'>Somos dos estudiantes entusiastas y amantes por la programacion y por la Ciencia de Datos, que dicho sea de paso, estudiamos esta maravillosa y hermosa carrera en la Universidad de La Habana.</p>
    <br>
    <h2 class='who-we-are-header'>¿Qué es esto?</h2>
    <p class='us-info'>Pues esto es nuestro proyecto de la asignatura Comunicacion en la Ciencia de Datos, donde nos toco el tema de Los Satelites.<br>Analizaremos y te comunicaremos de forma eficiente y divertida, la increible relacion entre los satelites y los datos.</p>
"""

    dataproduct_header = """
    <style>
    a {
        text-decoration: None;
        color: #7F55B1;
    }
    .dataproduct {
        text-align: center;
        font-size: xx-large;
    }
    </style>


    <h1 class='dataproduct'>DataProduct de <a href='https://github.com/mklaudia06/Satellite-Work'>Satellite-Work</a></h1>
    """

    satelliteQuiz_header = """
    <style>
    h2 {
        text-align: center;
    }

    .quiz-link {
        text-decoration:None; 
        color: #7F55B1;
    }
    </style>

    <h2>¿Acaso ya te probaste ante nuestro <a class='quiz-link' href='https://satellite-quiz.vercel.app/' target=_blank>Satellite Quiz</a>?</h2>
    """
    
    h1_country_map = "<h1 style='text-align: center;'>Todos los paises que han lanzado satelites desde 1957 hasta 2024</h1>"
    

class Countries:
    countries = {
        'Algeria': 'Algeria', 
        'Angola': 'Angola', 
        'Argentina': 'Argentina', 
        'Australia': 'Australia', 
        'Austria': 'Austria', 
        'Azerbaiyán': 'Azerbaijan', 
        'Bangladesh': 'Bangladesh', 
        'Bielorrusia': 'Belarus',
        'Bélgica': 'Belgium',
        'Bolivia': 'Bolivia',
        'Brasil': 'Brazil',
        'Bulgaria': 'Bulgaria',
        'Canadá': 'Canada',
        'Chile': 'Chile',
        'China': 'China',
        'Colombua': 'Colombia', 
        'República Checa': 'Czech Republic',
        'Dinamarca': 'Denmark',
        'Ecuador': 'Ecuador',
        'Egipto': 'Egypt',
        'Estonia': 'Estonia',
        'Etiopía': 'Ethiopia',
        'Finlandia': 'Finland',
        'Francia': 'France',
        'Alemania': 'Germany',
        'Grecia': 'Greece',
        'Hungría': 'Hungary',
        'India': 'India',
        'Indonesia': 'Indonesia',
        'Irán': 'Iran',
        'Iraq': 'Iraq',
        'Israel': 'Israel',
        'Italia': 'Italy',
        'Japón': 'Japan',
        'Jordania': 'Jordan',
        'Kazajistán': 'Kazakhstan',
        'Kenia': 'Kenya',
        'Kuwait': 'Kuwait',
        'Laos': 'Laos',
        'Lituania': 'Lithuania',
        'Luxemburgo': 'Luxembourg',
        'Malasia': 'Malaysia',
        'México': 'Mexico',
        'Mónaco': 'Monaco',
        'Marruecos': 'Morocco',
        'Nepal': 'Nepal',
        'Países Bajos (Holanda)': 'Netherlands',
        'Nueva Zelanda': 'New Zealand',
        'Nigeria': 'Nigeria',
        'Noruega': 'Norway',
        'Pakistán': 'Pakistan', 
        'Perú': 'Peru',
        'Polonia': 'Poland',
        'Rusia': 'Russia',
        'Arabia Saudita': 'Saudi Arabia',
        'Singapur': 'Singapore',
        'Eslovenia': 'Slovenia',
        'Sudáfrica': 'South Africa',
        'Korea del Sur': 'South Korea',
        'España': 'Spain',
        'Sudán': 'Sudan',
        'Suecia': 'Sweden', 
        'Suiza': 'Switzerland',
        'Taiwán': 'Taiwan',
        'Tailandia': 'Thailand',
        'Túnez': 'Tunisia',
        'Turquía': 'Turkey',
        'Estados Unidos': 'USA',
        'Ucrania': 'Ukraine',
        'Emiratos Árabes Unidos': 'United Arab Emirates',
        'Reino Unido': 'United Kingdom',
        'Venezuela': 'Venezuela',
        'Vietnam': 'Vietnam'
    }