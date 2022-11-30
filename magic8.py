import random

name = "Zakaria"
question = "Will I attain untold riches?"
answer = ""
random_number = random.randint(1, 12)

if random_number == 1:
  answer = "Yes - and I'm not lying also."
elif random_number == 2:
  answer = "United States congress says yes."
elif random_number == 3:
  answer = "What does Y-E-S spell out? That's your answer!"
elif random_number == 4:
  answer = "The purple haze has risen, try again."
elif random_number == 5:
  answer = "On vacation. Ask again later."
elif random_number == 6:
  answer = "Are you a snowflake? Better not tell you now."
elif random_number == 7:
  answer = "Got a guy in a corner, they say no."
elif random_number == 8:
  answer = "Microsoft Outlook not so good."
elif random_number == 9:
  answer = "Very, very, very, very doubtful."
elif random_number == 10:
  answer = "Look towards the stars - you'll find your answers there."
elif random_number == 11:
  answer = "Take a long walk - maybe then you'll find your answer."
elif random_number == 12:
  answer = "Nothing to see here - move it along."
else:
  answer = "Error!"

print(name + " asks: " + question)
print("Magic 8-Ball's answer: " + answer)

# Below consists if / else code in regards if the asker does not provide a name,
# such that the value of name is an empty string and if the question string is empty.

#if name == "":
#  print("Question: " + question)
#else:
#  print(name + " asks: " + question)

#if question == "":
#  print("The Magic 8-Ball cannot provide a #fortune unless you ask it something.")
#else:
#  print(name + " asks: " + question)
#  print("Magic 8-Ball's answer: " + answer)