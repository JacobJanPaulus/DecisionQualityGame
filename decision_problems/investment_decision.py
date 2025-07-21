from decision_problems.question_type import QuestionType


investment_decision= {
    "name": "R&D Investment",
    "levels": [
        {
            "name": "Game intro",
            "description": "Find the best R&D investment strategy: Consider a company that sells tools in a market that has upturns and downturns.  Downturns and upturns both last 2 years. "
                            "An upturn is always followed by a downturn and vice versa.\n\n...",
                
                # Each level is one of the predefined types
            "type": QuestionType.NONE.name,

            "score": 1
        },
        {
            "name": "Framing",
            # Each level is one of the predefined types
            "type": QuestionType.OPTIONS.name,
            "description": "Classify the following items as 'given', 'in scope', 'later', 'not a decision'.",
            "score": 1
        },
        {
            "name": "Alternatives",
                # Each level is one of the predefined types
            "type": QuestionType.NONE.name,
            "description": "Define the alternatives for the decision problem.",
            "score": 1
        },
        {
            "name": "Decision tree",
                # Each level is one of the predefined types
            "type": QuestionType.NUMERIC.name,
            "description": "Evaluate the outcome of the alternatives.",
            "score": 1
        }
    ]
}
