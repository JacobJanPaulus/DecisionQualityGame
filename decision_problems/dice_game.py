from decision_problems.question_type import QuestionType

dice_game = {
        # Display unique name of the game
        "name": "Dice game",
        
        # Text for the info button
        "summary": "You are asked to participate in a game of dice. The croupier will roll a regular dice two times "
                                "and if the product of the resulting pips is at least 19, you get a pay-off of 36€. The stake for the game is 9€.\n\n"
                                "When the croupier sees your hesitance to play, you are offered to see the result of the first roll for 4€, "
                                "before paying additional 6€ to continue to the second dice roll.\n\n"
                                "What will you do to maximize your result?",
                                
        # List of all levels - Levels are played in the given order
        "levels": [
            {
                # Name of the level
                "name": "Game introduction",
                
                # Each level is one of the predefined types
                "type": QuestionType.NONE.name,

                # Every level must have a discription
                "description": "You are asked to participate in a game of dice. The croupier will roll a regular dice two times "
                                "and if the product of the resulting pips is at least 19, you get a pay-off of 36€. The stake for the game is 9€.\n\n"
                                "When the croupier sees your hesitance to play, you are offered to see the result of the first roll for 4€, "
                                "before paying additional 6€ to continue to the second dice roll.\n\n"
                                "What will you do to maximize your result?",
                
                # Score if the player gives the correct answer
                "score": 1,
            },
            {
                # Name of the level
                "name": "Framing",
                
                # Each level is one of the predefined types
                "type": QuestionType.OPTIONS.name,

                # Every level must have a discription
                "description": "To help the decision-making process we should be clear on the framing;\n\n"
                                "What can be considered as 'given', and is out of scope for the decision at hand?\n"
                                "What is to be decided 'later' and not important for now?\n"
                                "What is actually a decision to take now and is 'in scope'?",
                
                # List the questions in a dict with keys:  "question", "answers", "hint", and for this questiontype "options" list
                "questions": [
                    {
                        'question' : "Let the crourpier role one or two dice", 
                        'answer': "in scope",
                        'hint': "Does this effect how you play the game and its outcome?",
                        'options': ['given', 'in scope', 'later', 'not a decision'],
                    },
                    { 
                        'question' : "Play the game a second time or not", 
                        'answer': "later",
                        'hint': "Does this effect how you play the first game?" ,
                        'options': ['given', 'in scope', 'later', 'not a decision'],
                    },
                    {
                        'question' : "Participate in playing the game or not", 
                        'answer': "in scope",
                        'hint': "Does this effect the outcome? How much you win or lose?",
                        'options': ['given', 'in scope', 'later', 'not a decision'],
                    },
                    { 
                        'question' : "You like to play games", 
                        'answer': "not a decision",
                        'hint': "This is not a dicision but a value that might influence your decision making" ,
                        'options': ['given', 'in scope', 'later', 'not a decision'],
                    },
                ],
                
                "score": 10
            },
            {
                # Name of the level
                "name": "Values",

                # Each level is one of the predefined types
                "type": QuestionType.NONE.name,

                # Every level must have a discription
                "description": "Before making the decision you need to identify what matters to you, which values should be considered.\n\n"
                                "From the problem description the only value that arrises is the the financial outcome. What could be other values that play a role here?\n"
                                "Example: 'You like playing games', 'You hate taking risks'",

                "score": 1
            },
            {
                # Name of the level
                "name": "Alternatives",

                # Each level is one of the predefined types
                "type": QuestionType.NONE.name,

                # Every level must have a discription
                "description": "The alternatives are the options that are under the decision maker controle. ...",

                "score": 10
            },
            {
                # Name of the level
                "name": "Decision tree (Step 1)",

                # Each level is one of the predefined types
                "type": QuestionType.NUMERIC.name,

                # Every level must have a discription
                "description": "Add to the decision tree the probabilities, cost and pay-out",

                # Optional image
                "image": "dice_game_decision_tree1.jpg",

                # List the questions. A tuple of "question", "answers", "hint"
                "questions": [
                    { 
                        'question' : "What is the probability p1?", 
                        'answer': 0.778,
                        'hint': "There are 6 x 6 possible combinations of two dice. 8 have a product of pips being 19 or higher." ,
                    },
                    { 
                        'question' : "What is the probability p2?", 
                        'answer': 0.222,
                        'hint': "There are 6 x 6 possible combinations of two dice. 8 have a product of pips being 19 or higher." ,
                    },
                    { 
                        'question' : "The is the cost c1 and c2?", 
                        'answer': 9,
                        'hint': "" ,
                    },
                    { 
                        'question' : "The is the cost c3?", 
                        'answer': 0,
                        'hint': "" ,
                    },
                    { 
                        'question' : "The is the pay-out v1?", 
                        'answer': 0,
                        'hint': "" ,
                    },
                    { 
                        'question' : "The is the pay-out v2?", 
                        'answer': 36,
                        'hint': "" ,
                    },
                    { 
                        'question' : "The is the pay-out v3?", 
                        'answer': 0,
                        'hint': "" ,
                    },
                ],

                "score": 10
            },
            {
                # Name of the level
                "name": "Decision tree (Step 2)",

                # Each level is one of the predefined types
                "type": QuestionType.NUMERIC.name,

                # Every level must have a discription
                "description": "Add to the decision tree the probabilities, cost and pay-out",

                # Optional image
                "image": "dice_game_decision_tree2.jpg",

                 # List the questions. A tuple of "question", "answers", "hint"
                "questions": [
                    { 
                        'question' : "What is the probability p1?", 
                        'answer': 0.5,
                        'hint': "" ,
                    },
                    { 
                        'question' : "What is the probability p2?", 
                        'answer': 1,
                        'hint': "" ,
                    },
                    { 
                        'question' : "What is the probability p3?", 
                        'answer': 0,
                        'hint': "" ,
                    },
                    { 
                        'question' : "The is the cost c1 and c2?", 
                        'answer': 10,
                        'hint': "" ,
                    },
                    { 
                        'question' : "The is the cost c3?", 
                        'answer': 4,
                        'hint': "" ,
                    },
                    { 
                        'question' : "The is the pay-out v1, v2 and v3?",
                        'answer': 0,
                        'hint': "" ,
                    },
                ],

                "score": 10
            },
            {
                # Name of the level
                "name": "Decision tree (Step 3)",

                # Each level is one of the predefined types
                "type": QuestionType.NUMERIC.name,

                # Every level must have a discription
                "description": "Add to the decision tree the probabilities, cost and pay-out",

                # Optional image
                "image": "dice_game_decision_tree3.jpg",

                 # List the questions. A tuple of "question", "answers", "hint"
                "questions": [
                    { 
                        'question' : "What is the probability p1?", 
                        'answer': 0.167,
                        'hint': "" ,
                    },
                    { 
                        'question' : "What is the probability p2?", 
                        'answer': 0.667,
                        'hint': "" ,
                    },
                    { 
                        'question' : "What is the probability p3?", 
                        'answer': 0.333,
                        'hint': "" ,
                    },
                    { 
                        'question' : "The is the cost c1 and c2?", 
                        'answer': 10,
                        'hint': "" ,
                    },
                    { 
                        'question' : "The is the cost c3?", 
                        'answer': 4,
                        'hint': "" ,
                    },
                    { 
                        'question' : "The is the pay-out v1?",
                        'answer': 0,
                        'hint': "" ,
                    },
                    { 
                        'question' : "The is the pay-out v2?",
                        'answer': 36,
                        'hint': "" ,
                    },
                    { 
                        'question' : "The is the pay-out v3?",
                        'answer': 0,
                        'hint': "" ,
                    },
                ],

                "score": 10
            },
            {
                # Name of the level
                "name": "Decision tree (Step 4)",

                # Each level is one of the predefined types
                "type": QuestionType.NUMERIC.name,

                # Every level must have a discription
                "description": "Add to the decision tree the probabilities, cost and pay-out",

                # Optional image
                "image": "dice_game_decision_tree4.jpg",

                 # List the questions. A tuple of "question", "answers", "hint"
                "questions": [
                    { 
                        'question' : "What is the probability p1?", 
                        'answer': 0.333,
                        'hint': "" ,
                    },
                    { 
                        'question' : "What is the probability p2?", 
                        'answer': 0.5,
                        'hint': "" ,
                    },
                    { 
                        'question' : "What is the probability p3?", 
                        'answer': 0.5,
                        'hint': "" ,
                    },
                    { 
                        'question' : "The is the cost c1 and c2?", 
                        'answer': 10,
                        'hint': "" ,
                    },
                    { 
                        'question' : "The is the cost c3?", 
                        'answer': 4,
                        'hint': "" ,
                    },
                    { 
                        'question' : "The is the pay-out v1?",
                        'answer': 0,
                        'hint': "" ,
                    },
                    { 
                        'question' : "The is the pay-out v2?",
                        'answer': 36,
                        'hint': "" ,
                    },
                    { 
                        'question' : "The is the pay-out v3?",
                        'answer': 0,
                        'hint': "" ,
                    },
                ],

                "score": 10
            },
            {
                # Name of the level
                "name": "Decision tree (Step 5)",

                # Each level is one of the predefined types
                "type": QuestionType.OPTIONS.name,

                # Every level must have a discription
                "description": "Make a decision such that the expected outcome is maximized.",

                # Optional image
                "image": "dice_game_decision_tree5.jpg",

                 # List the questions. A tuple of "question", "answers", "hint"
                "questions": [
                    { 
                        'question' : "What is the best option?", 
                        'answer': 'Roll first die',
                        'hint': "Which decision has the highest expected value on Pay-off minus Cost?" ,
                        'options' : ['Play', 'Roll first die', 'Don\'t play']
                    }
                ],

                "score": 10
            }
        ]
    }