import os
import json

# Definition of games available to play
decision_problems = {}

class DecisionProblemQuestion:
    def __init__(self, type, json_data):
        self._type = type

        # Set the question
        if "question" in json_data:
            self._question: str = json_data["question"]
        else:
            raise ValueError(f"Decision problem question is missing \"question\".")
        
        # Set the answer
        if "answer" in json_data:
            self._answer = json_data["answer"]
            if self._type == "NUMERIC" and (not (isinstance(self._answer,int) or isinstance(self._answer,float))):
                print (self._type)
                print (self._answer) 
                raise ValueError(f"Decision problem question is numeric, but \"answer\" is not.")
        else:
            raise ValueError(f"Decision problem question is missing \"answer\".")
        
        # Set the hint
        if "hint" in json_data:
            self._hint: str = json_data.get("hint","")
        else:
            raise ValueError(f"Decision problem question is missing \"hint\".")

        # Set options
        if self._type == "OPTIONS" and ("options" not in json_data):
            raise ValueError(f"Decision problem question is missing \"hint\".")
        elif self._type == "OPTIONS":
            # Each questions must contain a list of option to select from
            if "options" in json_data:
                self._options = []
                for opt in json_data["options"]:
                    self._options.append(opt)
            # Check if answer is in options listed
            if self._answer not in self._options:
                raise ValueError(f"Decision problem question awnser is not listed in the options.")
    
    def to_dict(self):
        as_dict = {}
        as_dict["question"] = self._question
        as_dict["answer"] = self._answer
        as_dict["hint"] = self._hint
        if self._type == "OPTIONS":
            as_dict["options"] = self._options
        return as_dict

class DecisionProblemLevel:
    def __init__(self, json_data, dir):
        # Set the name
        if "name" in json_data:
            self._name: str = json_data["name"]
        else:
            raise ValueError(f"Decision problem level is missing \"name\".")
        
        # Set the type
        if "type" in json_data:
            self._type: str = json_data["type"]
            if self._type not in ['NONE', 'OPTIONS', 'NUMERIC']:
                raise ValueError(f"Decision problem level has invalid \"type\".")
        else:
            raise ValueError(f"Decision problem level is missing \"type\".")
        
        # Set optional description
        self._description: str = json_data.get("description", None)
        
        # Set optional image
        self._image: str = json_data.get("image", None)
        if self._image:
            self._image = dir + "/" + self._image

        # Set optional questions
        json_questions = json_data.get("questions", None)
        if self._type == "NONE" and json_questions != None:
            raise ValueError("Level type NONE should have no questions specified")
        if self._type != "NONE" and json_questions == None:
            raise ValueError("Level type not equal to NONE must have questions specified")
        self._questions = []
        if json_questions:       
            for q in json_questions:
                self._questions.append( DecisionProblemQuestion(self._type, q) )

        # Set the score
        if "score" in json_data:
            if isinstance(json_data["score"],int):
                self._score: int = json_data["score"]
            else:
                raise ValueError(f"Decistion problem level \"score\" is not integer.")
        else:
            raise ValueError(f"Decision problem level is missing \"score\".")
        
    @property
    def name(self)->str:
        return self._name
    
    @property
    def type(self)->str:
        return self._type
    
    @property
    def description(self)->str:
        return self._description
    
    @property
    def image(self)->str:
        return self._image
    
    @property
    def questions(self)->str:
        questions = []
        for q in self._questions:
            questions.append(q.to_dict())
        return questions
    
    @property
    def score(self) -> int:
        return self._score
    
class DecisionProblem:
    def __init__(self, filepath):
        
        # Derive the game from the input json file
        json_data = self._load_json(filepath)

        # Parse the data from the json file
        self._name = ""
        self._summary = ""
        self._levels = []
        self._parse_data(json_data, dir=os.path.basename(os.path.dirname(filepath)))

    @staticmethod
    def _load_json(filepath) -> str:
        # 1. Check if file has a .json extension
        if not filepath.lower().endswith(".json"):
            raise ValueError(f"File extension is not .json: {filepath}")
    
        # 2. Check the file existence
        if not os.path.isfile(filepath):
            raise FileNotFoundError(f"File does not exist: {filepath}")
        
        # 3. Try to load JSON
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                return json.load(f)  # return parsed JSON
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format in {filepath}: {e}")
        
    def _parse_data(self,json_data, dir) -> None:
        # Set the name
        if "name" in json_data:
            self._name = json_data["name"]
        else:
            raise ValueError(f"Decision problem is missing \"name\".")
        
        # Set the summary
        if "summary" in json_data:
            self._summary = json_data["summary"]
        else:
            raise ValueError(f"Decision problem is missing \"summary\".")

        # Set the levels
        if "levels" in json_data:
            for level in json_data["levels"]:
                lvl = DecisionProblemLevel(level, dir)
                self._levels.append(lvl)
        else:
            raise ValueError(f"Decision problem is missing \"levels\".")

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def summary(self) -> str:
        return self._summary

    @property
    def nr_levels(self)-> int:
        return len(self._levels)

    def get_level(self, level_idx: int) -> DecisionProblemLevel:
        if (level_idx < 0 ) or level_idx >= len(self._levels):
            raise ValueError(f"Level index out of range")
        return self._levels[level_idx]


# Function to load the decision problems from the json files
def load_decision_problems() -> None:

    # Look into directory static/decision_problems to find all subdirs with a valid decision problem
    path = "static/decision_problems"

    # Look in to each subdir
    for dir in os.listdir(path):
        subdir = os.path.join(path,dir)
        if os.path.isdir(subdir):
            
            # Look for each json file
            for file in os.listdir(subdir):
                if file.lower().endswith(".json"):
                    filepath = os.path.join(subdir,file)
                    print( f"Loading file \"{filepath}\" ...")

                    try:
                        decision_problem = DecisionProblem(filepath)
                        decision_problems[decision_problem.name] = decision_problem #TODO make sure it is unique
                    except Exception as e:
                        print( f"Error loading {subdir}: {e}")