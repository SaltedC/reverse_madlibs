gameString = 'this is my string.  __1__.  yeah.  it is awesome!!! __2__.  Let\'s add another blank __3__.'
q1 = {'blank': '__1__', 'value': 'dog', 'answered': False}
q2 = {'blank': '__2__', 'value': 'cat', 'answered': False}
q3 = {'blank': '__3__', 'value': 'horse', 'answered': True}
q_array = [q1, q2, q3]


question = 'b1?'
answer = 'dog'
blank = '__1__'
def getAnswer(question, answer, gameString, blank):
  i = 0
  while i < 3:
    print gameString
    user_input = raw_input(question)
    if user_input == answer:
      gameString = gameString.replace(blank, answer)
      return gameString
    i +=1
  print 'nope, answer is ' + str(answer)

print getAnswer(question, answer, gameString, blank) 





# def get_question(q_array, guessed_string):
#   """returns index of question if q is not answered"""
#   index = 0
#   while index < len(q_array):
#     if q_array[index]['answered'] == False:
#       print guessed_string
#       user_input = raw_input('What is # ' + str(index + 1) + '?')
#       """asks user for answer and returns guessed_string"""
#       if user_input == q_array[index]['value']:
#         guessed_string = guessed_string.replace(q_array[index]['blank'], q_array[index]['value'])
#         print guessed_string
#         # maybe i could use a while loop here to continue asking for answer until user input == value
#     index += 1
#   print "you got it!  " + str(guessed_string)


# print get_question(q_array, gameString)

# def play_game(gameString, q_array):
#   index = 0
#   play = True
#   while index < len(q_array):
#     if q_array[index]['hidden'] == True:
#       user_input = raw_input('What goes in blank number ' + str(index + 1))
#       if user_input == q_array[index]['value']:

#     index += 1

# def get_answer(q_array, guessed_string):
#   user_input = raw_input("What goes in blank " + str(q_array[index + 1]) + "?")
#   if user_input == q_array[index]['value']:
#     guessed_string = guessed_string.replace(q_array[index]['blank'], q_array[index])
# if q1['hidden'] == False:
#   gameString = gameString.replace(q1['blank'], q1['value'])
# else:
#   user_input = raw_input("What goes in blank 1?")
#   if user_input == q1['value']:
#     print 'Good job!'
#     gameString = gameString.replace(q1['blank'], q1['value'])
#   else: 
#     user_input = raw_input("I\'m sorry.  What goes in blank 1?")


