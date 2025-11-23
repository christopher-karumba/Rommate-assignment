class Roommate:
    def __init__(self, name, age, hobby, personality,course):
        self.name = "Terry odhiambo"
        self.age = 26
        self.hobby ="listening to music,writing and singing songs,watching latest movie series which i can say its his best hobby,especially the comedian and the action movies,he also likes doing atheletics especially in the mornings he usually wakes up early to take the morning runs"
        self.personality = "Is that he is really calm,good,hardworking and very talkative at times"
        self.course = "Architecture"

    def description(self):
        print(f"\n--- About My Roommate ---")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Hobby: {self.hobby}")
        print(f"Personality: {self.personality}")
        print(f"course:{self.course}")

    def about(self):
        print(f"\nMy roommate name is, {self.name} and he is currently at the age of {self.age}. years old")
        print(f"He is currently in school like  i am doing a course in {self.course} which he is finalising currently in the sixth year here at jkuat though curently he does not have lots of classes he does some projects stuff and earns some money")
        print(f"Everyday he wakes up at around seven in the morning and does some chores at the room,studies and while done he does what he loves which is {self.hobby}")
        print(f"all i can say of him is that his a good person and {self.personality}")      

my_roommate.description()
my_roommate.about()