from decision_problems.question_type import QuestionType

test_example = {
    # Display unique name of the game
    "name": "Test Example",

    # Text for the info button
    "summary": "This is just an example...",

    # List of all levels, which are played in the given order
    "levels": [
        {
            # Name of the level
            "name": "Game introduction",
            
            # Each level is one of the predefined types
            "type": QuestionType.NONE.name,

            # Every level must have a discription
            "description": "Example of a game introduction description. Just press next to continue",

            # Score if the player gives the correct answer
            "score": 1,
        },
        {
            # Name of the level
            "name": "Exampele leve 1",
            
            # Each level is one of the predefined types
            "type": QuestionType.OPTIONS.name,

            # Every level must have a discription
            "description": "Example level 1. Select Yes as the answer",

            # List the questions in a dict with keys:  "question", "answers", "hint", and for this questiontype "options" list
            "questions": [
                {
                    'question' : "Select 'Yes'", 
                    'answer': "Yes",
                    'hint': "Select Yes",
                    'options': ['Yes', 'No'],
                },
            ],

            # Score if the player gives the correct answer
            "score": 5,
        },
        {
            # Name of the level
            "name": "Exampele leve 2",
            
            # Each level is one of the predefined types
            "type": QuestionType.OPTIONS.name,

            # Every level must have a discription
            "description": "Example level 2. Select Yes as the answer",

            # List the questions in a dict with keys:  "question", "answers", "hint", and for this questiontype "options" list
            "questions": [
                {
                    'question' : "Select 'Yes'", 
                    'answer': "Yes",
                    'hint': "Select Yes",
                    'options': ['Yes', 'No'],
                },
            ],

            # Score if the player gives the correct answer
            "score": 10,
        },
    ]
}