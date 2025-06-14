class Texts:
    start_text = """
    <style>
        .start-page li {
            font-size: xx-large;
            text-align: center;
            list-style: none;
        }
        
        .start-page .first-header {
            text-align: center;
        }

        .start-page .who-we-are-header {
            text-align: center;
            font-size: xxx-large;
        }

        .start-page .start { color: #F97A00; }
        .start-page .countries { color: #129990; }
        .start-page .satellites { color: #E50046; }
        .start-page .agency { color: #E83F25; }
        .start-page .orbit-kind { color: #3674B5; }

        .start-page .us-info {
            text-align: center;
            font-size: x-large;
        }
    </style>

    <div class="start-page">
        <h1 class='first-header'>Para Navegar por el sitio, hágalo por las diferentes pestañas:</h1>
        <ul>
            <li class='start'>Inicio</li>
            <li class='countries'>Países</li>
            <li class='satellites'>Satélites</li>
            <li class='agency'>Agencia</li>
            <li class='orbit-kind'>Tipo de órbita</li>
        </ul>
        
        <h2 class='who-we-are-header'>¿Quiénes somos?</h3>
        <p class='us-info'>Somos dos estudiantes entusiastas y amantes por la programación y por la Ciencia de Datos, que dicho sea de paso, estudiamos esta carrera en la Universidad de La Habana.</p>
        <br>
        <h2 class='who-we-are-header'>¿Qué es esto?</h2>
        <p class='us-info'>Pues esto es nuestro proyecto de la asignatura Comunicación en la Ciencia de Datos, donde nos tocó el tema de Los Satélites.<br>Analizaremos y te comunicaremos de forma eficiente y divertida, la increíble relación entre los satélites y los datos.</p>
    </div>
    """

    dataproduct_header = """
    <style>
        .start-page a {
            text-decoration: None;
            color: #7F55B1;
        }
        .start-page .dataproduct {
            text-align: center;
            font-size: xx-large;
        }
    </style>

    <div class="start-page">
        <h1 class='dataproduct'>DataProduct de <a href='https://github.com/mklaudia06/Satellite-Work'>Satellite-Work</a></h1>
    </div>
    """

    satelliteQuiz_header = """
    <style>
        .start-page h2 {
            text-align: center;
        }
        .start-page .quiz-link {
            text-decoration:None; 
            color: #7F55B1;
        }
    </style>

    <div class="start-page">
        <h2>¿Acaso ya te probaste ante nuestro <a class='quiz-link' href='https://satellite-quiz.vercel.app/' target=_blank>Satellite Quiz</a>?</h2>
    </div>
    """
    
    h1_country_map = "<h1 style='text-align: center;'>Todos los paises que han lanzado satélites desde 1957 hasta 2024</h1>"
    

class Countries:
    countries = {
        'Alemania': 'Germany',
        'Algeria': 'Algeria',
        'Arabia Saudita': 'Saudi Arabia',
        'Argentina': 'Argentina', 
        'Australia': 'Australia',
        'Azerbaiyán': 'Azerbaijan',
        'Bielorrusia': 'Belarus',
        'Bélgica': 'Belgium',
        'Bolivia': 'Bolivia',
        'Brasil': 'Brazil',
        'Canadá': 'Canada',
        'Chile': 'Chile',
        'China': 'China',
        'Colombia': 'Colombia', 
        'Dinamarca': 'Denmark',
        'Ecuador': 'Ecuador',
        'Egipto': 'Egypt',
        'Estados Unidos': 'USA',
        'Estonia': 'Estonia',
        'Eslovenia': 'Slovenia',
        'España': 'Spain',
        'Etiopía': 'Ethiopia',
        'Finlandia': 'Finland',
        'Francia': 'France',
        'Grecia': 'Greece',
        'Hungría': 'Hungary',
        'India': 'India',
        'Indonesia': 'Indonesia',
        'Irán': 'Iran',
        'Israel': 'Israel',
        'Italia': 'Italy',
        'Japón': 'Japan',
        'Kazajistán': 'Kazakhstan',
        'Korea del Sur': 'South Korea',
        'Lituania': 'Lithuania',
        'Luxemburgo': 'Luxembourg',
        'Malasia': 'Malaysia',
        'México': 'Mexico',
        'Marruecos': 'Morocco',
        'Nueva Zelanda': 'New Zealand',
        'Nigeria': 'Nigeria',
        'Países Bajos (Holanda)': 'Netherlands',
        'Pakistán': 'Pakistan', 
        'Perú': 'Peru',
        'Emiratos Árabes Unidos': 'United Arab Emirates',
        'Polonia': 'Poland',
        'Reino Unido': 'UK',
        'República Checa': 'Czech Republic',
        'Rusia': 'Russia',
        'Singapur': 'Singapore',
        'Sudáfrica': 'South Africa',
        'Suecia': 'Sweden', 
        'Suiza': 'Switzerland',
        'Taiwán': 'Taiwan',
        'Tailandia': 'Thailand',
        'Túnez': 'Tunisia',
        'Turquía': 'Turkey',
        'Ucrania': 'Ukraine',
        'URSS': 'USSR',
        'Venezuela': 'Venezuela',
        'Vietnam': 'Vietnam',
    }