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
    category = [("Some Nostaglia For Ya", "All answers will pertain to things from the 2000s and early 2010s."),
                ("Be a Good Sport", "All answers will pertain to sports."),
                ("Eighties Lyrics", "The answers is the name of the song the lyrics are from."), 
                ("Astronomy", "All answers will pertain to astronomy."),
                ('''Sorry, I Have a "Nut" Allergy''', '''All answers will contain the word "nut".'''),
                ("The Apple of my Eye", "All answers pertain to apples."),
                ("Discrete Math", "No, not Discreet. All answers have to do with discrete math. Sorry Com Sci kids."),
                ("Finish the Phrase", "All answers will be the missing part of the phrase."),
                ("Geology in Geography", "All answers will be the location of the mentioned geological formation or event."),
                ("HOMES Sweet HOMES", "All answers pertain to the Great Lakes from Michigan."),
                ("Shocking!", "All answers pertain to weather, specifically thunderstorms."),
                ("Dog", "All answers will pertain to dogs.")
    ]   
    return category

def sport():
    sportQuestions = [
        ("Fenway Park, home of the Boston Red Sox (boooo), also became the main stadium to play this professional sport from 1936 to 1968.",
         "football"),
        ("The majority of people have heard of NASCAR, but what they hopefully know is it's an acronym for this.",
         "national association for stock car auto racing"),
        ("In soccer, a yellow card means a player has been cautioned. In field hockey, it means a player must sit out for a minimum of this many minutes."
         "five"),
        ("Former Chicago Bears defensive tackle William Perry was given this nickname by a college teammate struggling to get into the same elevator as him. Cold!",
         "refrigerator"),
        ("Ha, nice: this number is forbidden to be used on a jersey in the NBA.",
         "sixty-nine"),
        ("Goalies don't score goals, right? Wrong. In 1979, this NY Islanders goalie was credited as being the first goaltender to score a goal in hockey.",
         "billy smith")
    ]
    return sportQuestions

def nostalgia():
    nostalgiaQuestions = [
        ("This soft, colorful toy may have sounded edible, but it is, in fact, not. However, you could mold it into tasty foods.", 
         "play-doh"),
        ("Spinning-top toys have always been a classic, but this toy turned them into objects you could use to battle other people in a plastic arena.",
         "beyblade"),
        ("The phone is ringing! This kids show that ended in 2016 followed a trio of animals rescuing other animals.",
          "wonder pets"),
        ("One of the most iconic animated movies made in 2001 was actually used as punishment for animators underperforming in a separate project.",
         "shrek"),
        ("In December of 2012, the music video for this song by a South Korean singer became the first video in YouTube history to reach one billion views.",
         "gangnam style"), 
        ("Nothing hit quite harder than seeing your virtual dog and dirt house again in this blocky computer game that was officially released in 2011.",
         "minecraft")
    ]
    return nostalgiaQuestions
# insert more categories below this after further testing

def dailyDouble():
    print("yeye")

def getCatnAns():
    cat = categories()
    qnaList = cat
    return qnaList

def firstRound(categories):
    test = [(categories[0], nostalgia()), (categories[1], sport())]
    candq = {}
    catNum = 1
    for i in range(len(test)):
        cat = random.randint(0, len(test) - 1)
        pointDict = {}
        points = 200
        for e in range(0, 5):
            q = random.randint(0, 5)
            pointDict[points] = test[cat][1][q]
            points+=200
        tup = (test[cat][0], pointDict)
        candq[catNum] = tup
        t = categories[cat]
        categories.remove(t)
        test.pop(cat)
        catNum+=1
    candq[0] = categories
    return candq
    

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
    print("Jeopardy rules yadda yadda yadda")
    #p1 = input("Player One, enter your name: ")
    #p2 = input("Player One, enter your name: ")
    #p3 = input("Player One, enter your name: ")
    p1 = "bruh"
    p2 = "man"
    p3 = "ur mom"
    players = {p1: 0, p2: 0, p3: 0}
    pKeys = [p1, p2, p3]
    cna = firstRound(getCatnAns())
    rCats = cna[0]
    del cna[0]
    player = 0
    fr = True
    while fr:
        print("{}, its your turn.".format(pKeys[player]))
        cat = True
        while cat:
            print("Available Categories: ")
            for item in cna:
                print("{}: {}".format(item, cna[item][0][0]))
            cCat = input("Enter the category number: ")
            if(cCat.isdigit() and int(cCat)>0 and int(cCat) in cna.keys()):
                cat = False
            else:
                print("Invalid input. Please try again.")
                continue
        question = True
        while question:
            print("Available Questions:")
            for item in cna[int(cCat)][1]:
                print(item)
            cQuest = input("Enter a point amount: ")
            if(cQuest.isdigit() and int(cQuest)>0 and int(cQuest) in cna[int(cCat)][1].keys()):
                question = False
            else:
                print("Invalid input. Please try again.")
                continue
        
        
game()