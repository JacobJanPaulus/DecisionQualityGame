from decision_problems.question_type import QuestionType


investment_decision= {
    # Display the unique name of the game
    "name": "R&D Investeringsbeslissing",

    #Text for the info button
    "summary": "Ga op zoek naar de beste investeringsbeslissing. \n\n"
            "Analyseer een bedrijf dat machines verkoopt op een markt die pieken en dalen kent. Zowel pieken als dalen duren beide 2 jaar. Een piek wordt "
            "altijd gevolgd door een dal en vice versa. Op dit moment bevindt het bedrijf zich in een dal, en met een kans van 50% zal het bedrijf het "
            "komende jaar te maken krijgen met een piek. Het aantal machines dat het bedrijf verkoopt is 10 eenheden tijdens een piek en 5 eenheden tijdens "
            "een dal. De marge op de huidige versie (A) van de machine is 10 miljoen euro per eenheid. Het bedrijf heeft de mogelijkheid om een R&D-project "
            "uit te voeren dat 2 jaar in beslag neemt. Na het eerste jaar resulteert het R&D-project in een verbeterde versie (B) van de machine (zeker). "
            "Na het tweede jaar zal het R&D-project met een kans van 20% een nog betere versie (C) van de machine opleveren. De kosten voor het R&D-project "
            "bedragen 165 miljoen euro. Het project kan niet worden gestopt na het eerste jaar. De marge van versie B van de machine is 15 miljoen euro per \n"
            "eenheid en de marge van versie C van de machine is 20 miljoen euro per eenheid. Het bedrijf heeft ook de optie om eerst een proof of \n"
            "concept-project uit te voeren voordat het R&D-project wordt gestart. Het proof of concept-project kost 30 miljoen euro en duurt 1 jaar om te \n"
            "voltooien. Als het proof of concept-project succesvol is en het bedrijf het R&D project uitvoert, kan het bedrijf een jaar later machine versie \n"
            "B gaan verkopen en machine versie C na twee jaar (zeker). Het R&D-project zal het bedrijf een extra 120 miljoen euro kosten, zodat de totale \n"
            "R&D-kosten in deze situatie 150 miljoen euro bedragen. Als het proof of concept niet succesvol is, weet het bedrijf dat het uitvoeren van het \n"
            "R&D-project alleen mogelijk maakt om machine versie B na één jaar te verkopen, d.w.z. het bedrijf kan nooit machine versie C verkopen. Na het \n"
            "eerste (pilot) jaar kan het bedrijf besluiten om het R&D-project voort te zetten of te stoppen. In het laatste geval blijft het bedrijf machine \n"
            "versie A verkopen. Op het moment dat het bedrijf besluit om het project al dan niet voort te zetten, weet het of het te maken heeft met een dal \n"
            "of een piek. Het bedrijf schat dat de kans op succes voor het proof of concept-project gelijk is aan 80%.",
    
    #list of all levels - Levels are played in given order
    "levels": [
        {
            # Name of the level
            "name": "Spel introductie",

            # Each level is one of the predefined types
            "type": QuestionType.NONE.name,
            
            # Every level must have a description
            "description": "Ga op zoek naar de beste investeringsbeslissing. \n\n"
            "Analyseer een bedrijf dat machines verkoopt op een markt die pieken en dalen kent. Zowel pieken als dalen duren beide 2 jaar. Een piek wordt "
            "altijd gevolgd door een dal en vice versa. Op dit moment bevindt het bedrijf zich in een dal, en met een kans van 50% zal het bedrijf het "
            "komende jaar te maken krijgen met een piek. Het aantal machines dat het bedrijf verkoopt is 10 eenheden tijdens een piek en 5 eenheden tijdens "
            "een dal. De marge op de huidige versie (A) van de machine is 10 miljoen euro per eenheid. Het bedrijf heeft de mogelijkheid om een R&D-project "
            "uit te voeren dat 2 jaar in beslag neemt. Na het eerste jaar resulteert het R&D-project in een verbeterde versie (B) van de machine (zeker). "
            "Na het tweede jaar zal het R&D-project met een kans van 20% een nog betere versie (C) van de machine opleveren. De kosten voor het R&D-project\n"
            "bedragen 165 miljoen euro. Het project kan niet worden gestopt na het eerste jaar. De marge van versie B van de machine is 15 miljoen euro per \n"
            "eenheid en de marge van versie C van de machine is 20 miljoen euro per eenheid. Het bedrijf heeft ook de optie om eerst een proof of \n"
            "concept-project uit te voeren voordat het R&D-project wordt gestart. Het proof of concept-project kost 30 miljoen euro en duurt 1 jaar om te \n"
            "voltooien. Als het proof of concept-project succesvol is en het bedrijf het R&D project uitvoert, kan het bedrijf een jaar later machine versie \n"
            "B gaan verkopen en machine versie C na twee jaar (zeker). Het R&D-project zal het bedrijf een extra 120 miljoen euro kosten, zodat de totale \n"
            "R&D-kosten in deze situatie 150 miljoen euro bedragen. Als het proof of concept niet succesvol is, weet het bedrijf dat het uitvoeren van het \n"
            "R&D-project alleen mogelijk maakt om machine versie B na één jaar te verkopen, d.w.z. het bedrijf kan nooit machine versie C verkopen. Na het \n"
            "eerste (pilot) jaar kan het bedrijf besluiten om het R&D-project voort te zetten of te stoppen. In het laatste geval blijft het bedrijf machine \n"
            "versie A verkopen. Op het moment dat het bedrijf besluit om het project al dan niet voort te zetten, weet het of het te maken heeft met een dal \n"
            "of een piek. Het bedrijf schat dat de kans op succes voor het proof of concept-project gelijk is aan 80%.",
                
            # Score if the player gives the correct answer
            "score": 1
        },
        {
            # Name of the level
            "name": "Raamwerk",

            # Each level is one of the predefined types
            "type": QuestionType.OPTIONS.name,

            # Every level must have a description
            "description": "Geef aan of het item 'gegeven', 'scope', 'later' of 'geen beslissing' is.",

            # List of questions in a dict with keys: "questions", "answers", "hint", and for this questiontype "options" list
            "questions": [
                {
                    'question': "Pieken en dalen duren elk precies 2 jaar",
                    'answer': "Geen beslissing",
                    'hint': "Is dit iets waar het bedrijf over kan beslissen?",
                    'options': [ 'Gegeven', 'Scope', 'Later', 'Geen beslissing'],
                },
                {
                    'question': "Voer het proof of concept uit?",
                    'answer': "Scope",
                    'hint': "Is dit iets waar het bedrijf nu over moet beslissen?",
                    'options': [ 'Gegeven', 'Scope', 'Later', 'Geen beslissing'],
                },
                {
                    'question': "Financieren van de investeringskosten",
                    'answer': "Later",
                    'hint': "Is dit iets dat het bedrijf kan beïnvloeden?",
                    'options': [ 'Gegeven', 'Scope', 'Later', 'Geen beslissing'],
                },
                {
                    'question': "De kans op succes voor de proof of concept is 80%",
                    'answer': "Geen beslissing",
                    'hint': "Is dit iets dat het bedrijf kan beïnvloeden?",
                    'options': [ 'Gegeven', 'Scope', 'Later', 'Geen beslissing'],
                },
                {
                    'question': "Investeringperiode is 5 jaar",
                    'answer': "Gegeven",
                    'hint': "Is dit iets dat het bedrijf kan beïnvloeden?",
                    'options': [ 'Gegeven', 'Scope', 'Later', 'Geen beslissing'],
                },
                {
                    'question': "Mogelijke investering in versie D",
                    'answer': "Later",
                    'hint': "Is dit iets dat het bedrijf kan beïnvloeden?",
                    'options': [ 'Gegeven', 'Scope', 'Later', 'Geen beslissing'],
                },                
                {
                    'question': "Voer R&D investering uit?",
                    'answer': "Scope",
                    'hint': "Is dit iets dat het bedrijf kan beïnvloeden?",
                    'options': [ 'Gegeven', 'Scope', 'Later', 'Geen beslissing'],
                },
                {
                    'question': "Rentevoet is 0%",
                    'answer': "Gegeven",
                    'hint': "Is dit iets dat het bedrijf kan beïnvloeden?",
                    'options': [ 'Gegeven', 'Scope', 'Later', 'Geen beslissing'],
                },
                {
                    'question': "De kosten van het R&D project zijn 165 miljoen euro",
                    'answer': "Geen beslissing",
                    'hint': "Is dit iets dat het bedrijf kan beïnvloeden?",
                    'options': [ 'Gegeven', 'Scope', 'Later', 'Geen beslissing'],
                }
            ],  

            "score": 90
        },
        {
            # Name of the level
            "name": "Alternatief 1: Niks doen",
            
            # Each level is one of the predefined types
            "type": QuestionType.OPTIONS.name,

            # Every level must have a description
            "description": "Defineer de alternatieven voor het besluitvormingsprobleem.",

            # List of questions in a dict with keys: "questions", "answers", "hint", and for this questiontype "options" list
            "questions": [
                {
                    'question': "Voer het proof of concept uit?",
                    'answer': "Nee",
                    'hint': "Is dit echt niks doen?",
                    'options': [ 'Ja', 'Nee', 'Ja/Nee'],
                },
                {
                    'question': "Voer R&D investering uit?",
                    'answer': "Nee",
                    'hint': "Is dit echt niks doen?",
                    'options': [ 'Ja', 'Nee', 'Ja/Nee'],
                }
            ],  


            "score": 10
        },
        {
            # Name of the level
            "name": "Alternatief 2: Voer R&D project uit",
            
            # Each level is one of the predefined types
            "type": QuestionType.OPTIONS.name,

            # Every level must have a description
            "description": "Defineer de alternatieven voor het besluitvormingsprobleem.",

            # List of questions in a dict with keys: "questions", "answers", "hint", and for this questiontype "options" list
            "questions": [
                {
                    'question': "Voer het proof of concept uit?",
                    'answer': "Nee",
                    'hint': "Is dit echt R&D doen?",
                    'options': [ 'Ja', 'Nee', 'Ja/Nee'],
                },
                {
                    'question': "Voer R&D investering uit?",
                    'answer': "Ja",
                    'hint': "Is dit echt R&D doen?",
                    'options': [ 'Ja', 'Nee', 'Ja/Nee'],
                }
            ],  


            "score": 10
        },        
        {
            # Name of the level
            "name": "Alternatief 3: Voer proof of concept uit",
            
            # Each level is one of the predefined types
            "type": QuestionType.OPTIONS.name,

            # Every level must have a description
            "description": "Defineer de alternatieven voor het besluitvormingsprobleem.",

            # List of questions in a dict with keys: "questions", "answers", "hint", and for this questiontype "options" list
            "questions": [
                {
                    'question': "Voer het proof of concept uit?",
                    'answer': "Ja",
                    'hint': "Is dit echt proof of concept doen?",
                    'options': [ 'Ja', 'Nee', 'Ja/Nee'],
                },
                {
                    'question': "Voer R&D investering uit?",
                    'answer': "Ja/Nee",
                    'hint': "Moet dat nu al besloten worden?",
                    'options': [ 'Ja', 'Nee', 'Ja/Nee'],
                }
            ],  


            "score": 10
        },    
        {
            # Name of the level
            "name": "Evaluatie alternatief 1: Niks doen",

            # Each level is one of the predefined types
            "type": QuestionType.NUMERIC.name,

            # Every level must have a description
            "description": "Evalueer de uitkomst van de alternatieven.",

            # Optional image
            "image": "investment_decision.jpg",

            "questions": [
                {
                        'question' : "Wat is de verwachte waarde van alternatief 1", 
                        'answer': 350,
                        'hint': "" ,
                }
            ],

            "score": 20
        }

    ]
}
