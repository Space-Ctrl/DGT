import requests
from catagorys import topics, difficulties
# Use the Open Trivia DB API to get data from the API

amount = int(input("How many questions do you want? "))
for i in range(len(difficulties)):
    print(f"{i+1}. {difficulties[i]}")

topic = topics[input("What topic do you want? ")]
print("easy [1], medium [2], hard [3]]")
difficulty = difficulties[int(input("What difficulty do you want?  "))-1]

response = requests.get(url="https://opentdb.com/api.php?amount={amount}&category={topic}&difficulty={difficulty}&type=multiple")
question_data = response.json()["results"]