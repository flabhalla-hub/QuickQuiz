from app import app, db, Question

with app.app_context():
    db.create_all()
#HTML :    
    q1 = Question(category="HTML", 
                  question="Que signifie HTML ?",
                  choice1="Hyper Text Markup Language", 
                  choice2="High Text Machine Language", 
                  choice3="Hyperlinks Text Mark Language",
                  answer="Hyper Text Markup Language")
             
    q2 = Question(category="HTML", 
                  question="Quelle balise est utilisée pour les images ?",
                  choice1="<img>", 
                  choice2="<image>", 
                  choice3="<pic>",
                  answer="<img>")    
    q3 = Question(category="HTML", 
                  question="Quelle balise crée un lien ?",
                  choice1="<a>", 
                  choice2="<link>", 
                  choice3="<href>",
                  answer="<a>")

    q4 = Question(category="HTML", 
                  question="Quelle balise pour un paragraphe ?",
                  choice1="<p>", 
                  choice2="<para>", 
                  choice3="<text>",
                  answer="<p>")  
    q5 = Question(category="HTML", 
                  question="Quelle balise pour les titres ?",
                  choice1="<h1>", 
                  choice2="<head>", 
                  choice3="<title>",
                  answer="<h1>")

    q6 = Question(category="HTML", 
                  question="HTML est ?",
                  choice1="Un langage de balisage", 
                  choice2="Un langage de programmation", 
                  choice3="Une base de données",
                  answer="Un langage de balisage")

    q7 = Question(category="HTML", 
                  question="Quelle balise pour les listes ?",
                  choice1="<ul>", 
                  choice2="<list>", 
                  choice3="<lii>",
                  answer="<ul>")

    q8 = Question(category="HTML", 
                  question="Quelle balise pour un saut de ligne ?",
                  choice1="<br>", choice2="<break>", choice3="<lb>",
                  answer="<br>")    
    q9 = Question(category="HTML", 
                  question="Quelle balise contient les métadonnées ?",
                  choice1="<head>", choice2="<body>", choice3="<meta>",
                  answer="<meta>")

    q10 = Question(category="HTML", 
                   question="Quelle balise contient le contenu principal ?",
                   choice1="<body>", choice2="<main>", choice3="<content>",
                   answer="<body>")
    
    #CSS
    q11 = Question(category="CSS", 
                   question="Que signifie CSS ?",
                   choice1="Cascading Style Sheets", choice2="Computer Style Sheets", choice3="Creative Style System",
                   answer="Cascading Style Sheets")

    q12 = Question(category="CSS", 
                   question="Quelle propriété change la couleur du texte ?",
                   choice1="color", choice2="background", choice3="font",
                   answer="color")
    q13 = Question(category="CSS", 
                  question="Quelle propriété change la couleur de fond ?",
                  choice1="background-color", choice2="color", choice3="bg",
                  answer="background-color")

    q14 = Question(category="CSS", 
                   question="CSS est utilisé pour ?",
                   choice1="Le design", choice2="La logique", choice3="La base de données",
                   answer="Le design")

    q15 = Question(category="CSS", 
                   question="Comment sélectionner une classe ?",
                   choice1=".classe", choice2="#classe", choice3="classe",
                   answer=".classe")
    q16 = Question(category="CSS",
                   question="Quelle valeur de display pour un élément flexible ?",
                   choice1="flex", choice2="block", choice3="inline",
                   answer="flex")
    q17 = Question(category="CSS",
                   question="Quelle propriété change la taille du texte ?",
                   choice1="font-size", choice2="text-size", choice3="size",
                   answer="font-size")

    q18 = Question(category="CSS", 
                   question="Quelle propriété ajoute un espace interne ?",
                   choice1="padding", choice2="margin", choice3="space",
                   answer="padding")

    q19 = Question(category="CSS", 
                   question="Quelle propriété ajoute un espace externe ?",
                   choice1="margin", choice2="padding", choice3="border",
                   answer="margin")

    q20 = Question(category="CSS", 
                   question="Extension d’un fichier CSS ?",
                   choice1=".css", choice2=".style", choice3=".design",
                   answer=".css")
    
  #FLASK :
    q21 = Question(category="Flask", 
                   question="Flask est écrit en ?",
                   choice1="Python", choice2="Java", choice3="C++",
                answer="Python")

    q22 = Question(category="Flask",
                  question="Quelle commande installe Flask ?",
                  choice1="pip install flask", 
                  choice2="npm install flask", 
                  choice3="apt install flask",
                  answer="pip install flask")

    q23 = Question(category="Flask", 
                   question="Quelle fonction lance l'application ?",
                   choice1="app.run()", choice2="run()", choice3="start()",
                   answer="app.run()")

    q24 = Question(category="Flask", 
                   question="Comment définir une route ?",
                   choice1="@app.route", choice2="@route", choice3="@url",
                   answer="@app.route")

    q25 = Question(category="Flask", 
                   question="Quel moteur de template utilise Flask ?",
                   choice1="Jinja2", choice2="HTML", choice3="CSS",
                   answer="Jinja2")

    q26 = Question(category="Flask", 
                   question="Quel objet gère les requêtes ?",
                   choice1="request", choice2="response", choice3="session",
                   answer="request")

    q27 = Question(category="Flask", 
                   question="Quelle fonction fait une redirection ?",
                   choice1="redirect()", choice2="move()", choice3="goto()",
                   answer="redirect()")

    q28 = Question(category="Flask", 
                   question="Quel objet stocke la session ?",
                   choice1="session", choice2="cookie", choice3="cache",
                   answer="session")

    q29 = Question(category="Flask", 
                   question="Quelle fonction affiche HTML ?",
                   choice1="render_template", choice2="send_html", choice3="render",
                   answer="render_template")

    q30 = Question(category="Flask", 
                   question="Port par défaut de Flask ?",
                   choice1="5000", choice2="8000", choice3="3000",
                   answer="5000") 
    
   # JINJA2 :
    q31 = Question(category="Jinja2",
                   question="Jinja2 est utilisé pour ?",
                   choice1="Les templates", choice2="La base de données", choice3="Le CSS",
                   answer="Les templates")

    q32 = Question(category="Jinja2", 
                   question="Comment afficher une variable ?",
                   choice1="{{ }}", choice2="{ }", choice3="< >",
                   answer="{{ }}")

    q33 = Question(category="Jinja2", 
                   question="Syntaxe d'une boucle ?",
                   choice1="{% for %}", choice2="{{ for }}", choice3="<for>",
                   answer="{% for %}")

    q34 = Question(category="Jinja2", 
                   question="Syntaxe d'une condition ?",
                   choice1="{% if %}", choice2="{{ if }}", choice3="<if>",
                   answer="{% if %}")

    q35 = Question(category="Jinja2", 
                   question="Fin d'une boucle ?",
                   choice1="{% endfor %}", choice2="{% stop %}", choice3="{% end %}",
                   answer="{% endfor %}")

    q36 = Question(category="Jinja2",
                  question="Comment appliquer un filtre sur une variable ?",
                  choice1="{{ variable|upper }}", 
                  choice2="{{ variable.upper }}", 
                  choice3="{% filter variable %}",
                  answer="{{ variable|upper }}")

    q37 = Question(category="Jinja2", 
                   question="Syntaxe des commentaires ?",
                   choice1="{# #}", choice2="//", choice3="<!-- -->",
                   answer="{# #}")

    q38 = Question(category="Jinja2", 
                   question="Héritage de template ?",
                   choice1="{% extends %}", choice2="{% include %}", choice3="{% use %}",
                   answer="{% extends %}")

    q39 = Question(category="Jinja2", 
                   question="Inclure un fichier ?",
                   choice1="{% include %}", choice2="{% import %}", choice3="{% add %}",
                   answer="{% include %}")

    q40 = Question(category="Jinja2",
                  question="Comment définir un bloc dans Jinja2 ?",
                  choice1="{% block %}", 
                  choice2="{{ block }}", 
                  choice3="{% define %}",
                  answer="{% block %}") 
    
  #SQL ALCHEMY :
    q41 = Question(category="SQLAlchemy", 
                   question="SQLAlchemy est ?",
                   choice1="Un ORM", choice2="Un framework", choice3="Un langage",
                   answer="Un ORM")

    q42 = Question(category="SQLAlchemy", 
                   question="Créer les tables ?",
                   choice1="db.create_all()", choice2="create()", choice3="make_table()",
                   answer="db.create_all()")

    q43 = Question(category="SQLAlchemy", 
                   question="Ajouter un enregistrement ?",
                   choice1="db.session.add()", choice2="insert()", choice3="add_row()",
                   answer="db.session.add()")

    q44 = Question(category="SQLAlchemy", 
                   question="Sauvegarder les changements ?",
                   choice1="db.session.commit()", choice2="save()", choice3="commit_db()",
                   answer="db.session.commit()")

    q45 = Question(category="SQLAlchemy", 
                   question="Faire une requête ?",
                   choice1="Model.query", choice2="get()", choice3="fetch()",
                   answer="Model.query")

    q46 = Question(category="SQLAlchemy",
                   question="Filtrer les données ?",
                   choice1="filter_by()", choice2="where()", choice3="find()",
                   answer="filter_by()")

    q47 = Question(category="SQLAlchemy", 
                   question="Clé primaire ?",
                   choice1="primary_key=True", choice2="key=True", choice3="main=True",
                   answer="primary_key=True")

    q48 = Question(category="SQLAlchemy", 
                   question="Type String ?",
                   choice1="db.String", choice2="db.Text", choice3="db.Char",
                   answer="db.String")

    q49 = Question(category="SQLAlchemy", 
                   question="Supprimer les tables ?",
                   choice1="db.drop_all()", choice2="delete()", choice3="remove_all()",
                   answer="db.drop_all()")

    q50 = Question(category="SQLAlchemy",
                  question="Comment récupérer tous les enregistrements ?",
                  choice1="Model.query.all()", 
                  choice2="Model.query.get()", 
                  choice3="Model.query.first()",
                  answer="Model.query.all()")


    db.session.add_all([
          q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,
          q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,
          q21,q22,q23,q24,q25,q26,q27,q28,q29,q30,
          q31,q32,q33,q34,q35,q36,q37,q38,q39,q40,
          q41,q42,q43,q44,q45,q46,q47,q48,q49,q50
               ])

    db.session.commit()
   