# How to define your own game in the Decision Quality Game Platform
Each game is defined via a ```json``` formatted file, optionally complemented with a number of images. In this game definition file the different type of 'levels' (webpages the player goes through) are described one by one. There are 3 different types of levels.
1. Levels without questions, to be used to explain the decision problem to be solved and to guide players through decision quality concepts.
2. Levels with drop down question, where the player see one or more questions and needs to select for each question the right answer from a drop down list.
3. Levels with numeric questions, where the player must enter the right numerical answer to the question.

## Where to define a new game
Games are defined in the folder `\static\decision_problems\`.

Start by creating a new subfolder in this directory to get `static\decision_problems\<my_game_name>`, and place within this folder a new file called `<my_game_name>.json`. 

The game platform automatically checks the content of `\static\decision_problems\` to make the games available.

## Creating the content of the game
A game is specified by the content of the `<my_game_name>.json`. This content must follow a the predefined structure. 

### General content
At the top level in the `json` file you are request to fill 3 labels:
1. `"name"`, a mandatory short descriptive name of your game.
2. `"summary"`, a mandatory summary of the decision problem. This summary is available to the player in each level via the info icon ℹ️.
3. `"levels'"`, a mandatory list of levels. (See further below for how to specify levels.)

<b>Example</b>:
```json
{
    "name": "Dice game",
    "summary": "You are asked to participate in a game of dice. The croupier will roll a regular dice two times and if the product of the resulting pips is at least 19, you get a pay-off of 36€. The stake for the game is 9€.\n\nWhen the croupier sees your hesitance to play, you are offered to see the result of the first roll for 4€, before paying additional 6€ to continue to the second dice roll.\n\nWhat will you do to maximize your result?",
    "levels": [ 
        {
            ...
        },
        {
            ...
        }
    ]
}
```

### Level content
A level is specified as follows:
1. `"name"`, a mandatory name of the level. This appears at the top of the webpage for the level.
2. `"type"`, a mandatory type of the level. This can be either `"NONE"` (if the level has no questions), `"OPTIONS"` (if the level has questions with options to select from), or `"NUMERIC"` (if the level has questions with numeric answers). Note that it is not (yet) possible to have in one level a mix of numeric and option questions.
3. `"description"`, an optional description on the webpage of the level. Use this to explain concepts and describe the decision problem at hand. 
4. `"image"`, an optional image name to show on the webpage of the level. This image must be placed in the same directory as the `<my_game_name>.json`.
5. `"questions"`, an optional list of questions. 
    * If level type is `"NONE"`, no questions are specified. For other types at least one question needs to be specified.
    * For level type `"OPTIONS"`, a question consists of the labels `"question"` (text stating the question), `"answer"` (the answer of the question - must be listed in the options), `"hint"` (this hint is shown to the player after a wrong answer is given), `"OPTIONS"` (a list of options to appear in the drop down to select from).
    * For level type `"NUMERIC"`, a question consists of the labels `"question"` (text stating the question), `"answer"` (the answer of the question - a numeric value), `"hint"` (this hint is shown to the player after a wrong answer is given).
6. `"score"`, a mandatory integer value specifying the number of points the player gets upon completing the level. Note that each time the player submits a wrong anwser his score for that level is decreased by 1 point.

#### Example level of type `"NONE"`
```json
{
    "name": "Game introduction",
    "type": "NONE",
    "description": "You are asked to participate in a game of dice. The croupier will roll a regular dice two times and if the product of the resulting pips is at least 19, you get a pay-off of 36€. The stake for the game is 9€.\n\nWhen the croupier sees your hesitance to play, you are offered to see the result of the first roll for 4€, before paying additional 6€ to continue to the second dice roll.\n\nWhat will you do to maximize your result?",
    "score": 1
}
```

#### Example level of type `"OPTIONS"`, with 2 questions
```json
 {
    "name": "Framing",
    "type": "OPTIONS",
    "description": "To help the decision-making process we should be clear on the framing;\n\nWhat can be considered as 'given', and is out of scope for the decision at hand?\nWhat is to be decided 'later' and not important for now?\nWhat is actually a decision to take now and is 'in scope'?",
    "questions": [
        {
            "question" : "Let the crourpier role one or two dice", 
            "answer": "in scope",
            "hint": "Does this effect how you play the game and its outcome?",
            "options": ["given", "in scope", "later", "not a decision"]
        },
        { 
            "question" : "Play the game a second time or not", 
            "answer": "later",
            "hint": "Does this effect how you play the first game?" ,
            "options": ["given", "in scope", "later", "not a decision"]
        }
    "score": 10
}
```

#### Example level of type `"NUMERIC"` including an image
```json
{
    "name": "Decision tree (Step 1)",
    "type": "NUMERIC",
    "description": "Add to the decision tree the probabilities, cost and pay-out",
    "image": "dice_game_decision_tree1.jpg",
    "questions": [
        { 
            "question" : "What is the probability p1?", 
            "answer": 0.778,
            "hint": "There are 6 x 6 possible combinations of two dice. 8 have a product of pips being 19 or higher."
        },
        { 
            "question" : "What is the probability p2?", 
            "answer": 0.222,
            "hint": "There are 6 x 6 possible combinations of two dice. 8 have a product of pips being 19 or higher."
        },
    ],
    "score": 15
}
```
