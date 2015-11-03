# questions for this game are taken from tutorials point python basic tutorial
disclaimer = 'http://www.tutorialspoint.com/python/index.htm is the source for these questions about python.'

# array containing unguessed gameString, questions, and answers for easy level
easyGameComplete = {'gameString': '\nPython Identifiers: A Python __1__ is a name used to identify a variable,\
 function, class, module or other object. An __1__ starts with a letter A to Z or a to z or an underscore (_)\
 followed by zero or more letters, underscores and digits (0 to 9).  Python does not allow __2__ characters\
 such as @, $, and % within __1__. Python is a __3__ sensitive programming language. Thus, Manpower and manpower\
  are two different __1__s in Python.  Class names start with an uppercase letter. All other __1__ start with\
  a __4__ letter.  Certain words in Python are __5__s. These are reserved words and you cannot use them as constant\
 or variable or any other identifier names. All the Python __5__s contain lowercase letters only.\n', 
'questions': {
'q1': {'blank': '__1__', 'value': 'identifier'},
'q2': {'blank': '__2__', 'value': 'punctuation'},
'q3': {'blank': '__3__', 'value': 'case'},
'q4': {'blank': '__4__', 'value': 'lowercase'},
'q5': {'blank': '__5__', 'value': 'keyword'}
  } 
}

# array containing unguessed gameString, questions, and answers for medium level
mediumGameComplete = {
  'gameString': '\nPython Variables and Data Types:__1__s are nothing but reserved\
   memory locations to store values. This means that when you create a __1__ you reserve some space in memory.\
   The equal sign (=) is used to assign values to __1__s.  Python has five standard data types: __2__,\
   __3__, __4__, __5__, __6__.  __2__ data types store numeric values.\
   __3__s in Python are identified as a contiguous set of characters represented in the quotation marks.\
   __4__s are the most versatile of Python\'s compound data types. A __4__ contains items separated\
   by commas and enclosed within square brackets ([]). A __5__ is another sequence data type that \
   is similar to the __4__. A __5__ consists of a number of values separated by commas. Unlike __4__s,\
   however, __5__s are enclosed within parentheses and cannot be updated. __5__s can be thought of as \
   read-only __4__s.  A __6__ is a kind of hash table type. They work like associative arrays or hashes.\
    __6__ key can be almost any Python type, but are usually __2__s or __3__s. Values, on the\
     other hand, can be any arbitrary Python object.\n', 
  'questions': {
  'q1': {'blank': '__1__', 'value': 'variable'},
  'q2': {'blank': '__2__', 'value': 'number'},
  'q3': {'blank': '__3__', 'value': 'string'},
  'q4': {'blank': '__4__', 'value': 'list'},
  'q5': {'blank': '__5__', 'value': 'tuple'},
  'q6': {'blank': '__6__', 'value': 'dictionary'}
  }
}

# array containing unguessed gameString, questions, and answers for hard level
hardGameComplete = {
  'gameString': '\nPython Loops: The __1__ loop repeats a statement or group of statements\
  __1__ a given condition is TRUE. It tests the condition before executing the loop body. \
  The __2__ loop executes a sequence of statements multiple times and abbreviates the code that manages the loop variable.\
  With __3__ loops you can use one or more loop inside any another while.\
  Loop control statements change execution from its normal sequence.  The __4__ statment\
  terminates the loop statement and transfers execution to the statement immediately following the loop.\
  A __5__ statement causes the loop to skip the remainder of its body and immediately\
  retest its condition prior to reiterating.  The pass statement in Python is used when\
   a statement is required syntactically but you do not want any command or code to execute.\n',
  'questions': {
  'q1': {'blank': '__1__', 'value': 'while'},
  'q2': {'blank': '__2__', 'value': 'for'},
  'q3': {'blank': '__3__', 'value': 'nested'},
  'q4': {'blank': '__4__', 'value': 'break'},
  'q5': {'blank': '__5__', 'value': 'continue'}
  }
}

levelsArray = [easyGameComplete, mediumGameComplete, hardGameComplete]

def getLevel(levelsArray):
# asks user for level to play, returns the unguessed string
# and array of questions related answers for that level
  level = raw_input('Please choose a level: easy, medium, or hard. \n\n')
  if level == 'easy':
    gameString = levelsArray[0]['gameString']
    qArray = levelsArray[0]['questions']
  elif level == 'medium':
    gameString = levelsArray[1]['gameString']
    qArray = levelsArray[1]['questions']
  elif level == 'hard':
    gameString = levelsArray[2]['gameString']
    qArray = levelsArray[2]['questions']
  return gameString, qArray

def getAnswer(gameString, question):
# given a game string and question, prompts user with unguessed
# string and question.  If user guess correctly, returns guessed string
# after 3rd incorrect guess, answer revealed
  i = 0
  print gameString
  while i < 3:
    user_input = raw_input('What goes in blank ' + question['blank'] + '?')
    if user_input == question['value']:
      print 'Nice job!  '
      gameString = gameString.replace(question['blank'], question['value'])
      return gameString
    else:
      print 'Sorry, please try again.'
    i +=1
  print 'Sorry, the answer is ' + str(question['value'])
  gameString = gameString.replace(question['blank'], question['value'])
  return gameString

def playGame(levelsArray):
# asks for level, cycles through questions for that level
  print disclaimer
  gameString, qArray = getLevel(levelsArray)
  i = 0
  while i < len(qArray):
    gameString = getAnswer(gameString, qArray['q' + str(i + 1)])
    i += 1
  print 'Great!  You finished the game!'
  return gameString

print playGame(levelsArray)

