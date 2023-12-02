#need question class
#need game function
#need to make the questions
#separate function for answering the questions(?)
import random

class QnA:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
    def getQuestion(self):
        return self.question
    def getAnswer(self):
        return self.answer
    
class Category:
    def __init__(self, category, desc):
        self.category = category
        self.desc = desc
    def getCategory(self):
        return self.category
    def getDesc(self):
        return self.desc
    
def categories():
    category = {("Eighties Lyrics", "The answers is the name of the song the lyrics are from."), 
                ("Some Nostaglia For Ya", "All answers will pertain to things during the 2000s and early 2010s."),
                ("Be a Good Sport", "All answers will pertain to sports."),
                ("Astronomy", "All answers will pertain to astronomy."),
                ('''Sorry, I Have a "Nut" Allergy''', '''All answers will contain the word "nut".'''),
                ("The Apple of my Eye", "All answers pertain to apples."),
                ("Discrete Math", "No, not Discreet. All answers have to do with discrete math. Sorry Com Sci kids."),
                ("Finish the Phrase", "All answers will be the missing part of the phrase."),
                ("Geology in Geography", "All answers will be the location of the mentioned geological formation or event."),
                ("HOMES Sweet HOMES", "All answers pertain to the Great Lakes from Michigan."),
                ("Shocking!", "All answers pertain to weather, specifically thunderstorms."),
                ("Dog", "All answers will pertain to dogs.")
                }
    return category

def sport():
    sportQuestions = {
        ("Fenway Park, home of the Boston Red Sox (boooo), also became the main stadium to play this professional sport from 1936 to 1968.",
         "football"),
        ("We all know NASCAR, but what we hopefully know is it's an acronym for this.",
         "national association for stock car auto racing"),
        ("In soccer, a yellow card means a player has been cautioned. In field hockey, it means a player must sit out for a minimum of this many minutes."
         "five"),
        ("Former Chicago Bears defensive tackle William Perry was given this nickname by a college teammate struggling to get into the same elevator as him. Cold!",
         "refrigerator"),
        ("Ha, nice: this number is forbidden to be used on a jersey in the NBA.",
         "sixty-nine"),
        ("Goalies don't score goals, right? Wrong. In 1979, this NY Islanders goalie was credited as being the first goaltender to score a goal in hockey.",
         "billy smith")
    }
    return sportQuestions

def nostalgia():
    nostalgiaQuestions = {
        ("This soft, colorful toy may have sounded edible, but it is, in fact, not. However, you could mold it into tasty foods.", 
         "play-doh"),
        ("Spinning-top toys ha,ve always been a classic, but this toy turned them into things you could use to battle other people in a plastic arena.",
         "beyblade")
        ("The phone is ringing! This kids show that ended in 2016 followed a trio of animals rescuing other animals.",
          "wonder pets"),
        ()

        
    }
# insert more categories below this after further testing

def dailyDouble():
    print("yeye")

def getGuess():
    valid = True
    while valid:
        guess = input("Enter your answer: ")
        try:
            assert "what is" in guess.lower() or "who is" in guess.lower()
            valid = False
        except:
            print('''Answer must contain "Who is" or "What is"''')
    return guess


def game():
    guess = getGuess()
    print(guess)

game()