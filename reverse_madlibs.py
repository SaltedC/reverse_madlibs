gameString = 'this is my string.  __1__.  yeah.  it is awesome!!! __2__.  __3__'
q1 = {'blank': '__1__', 'value': 'dog', 'hidden': True}
q2 = {'blank': '__2__', 'value': 'cat', 'hidden': True}
q3 = {'blank': '__3__', 'value': 'horse', 'hidden': True}
qArray = [q1, q2, q3]


def getAnswer(question, gameString):
  i = 0
  print gameString
  while i < 3:
    user_input = raw_input('What goes in blank ' + question['blank'] + '?')
    if user_input == question['value']:
      gameString = gameString.replace(question['blank'], question['value'])
      return gameString
    else:
    	print 'Sorry, please try again.'
    i +=1
  print 'Sorry, the answer is ' + str(question['value'])
  gameString = gameString.replace(question['blank'], question['value'])
  return gameString


def playGame(qArray, gameString):
  i = 0
  while i < len(qArray):
    gameString = getAnswer(qArray[i], gameString)
    i += 1
  return gameString

print playGame(qArray, gameString)

