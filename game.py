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
    
    def validateAns(self, guess):
        if(self.answer in guess.lower()):
            return True
        else:
            return False
    
class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0

    def getName(self):
        return self.name
    
    def getPoints(self):
        return self.points
    
    def addPoints(self, add):
        self.points+=add
    
    def removePoints(self, subtract):
        self.points-=subtract
        
def categories():
    category = [("Some Nostaglia For Ya", "All answers will pertain to things from the 2000s and early 2010s."),
                ("Be a Good Sport", "All answers will pertain to sports."),
                ("Eighties Lyrics", "The answers is the name of the song the lyrics are from."), 
                ("Out of this World", "All answers will pertain to astronomy."),
                ('''Sorry, I Have a "Nut" Allergy''', '''All answers will contain the word "nut".'''),
                ("The Apple of my Eye", "All answers pertain to apples."),
                ("Vocabulary Bee", "The answer will be the word that the definition best fits."),
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
        ("In soccer, a yellow card means a player has been cautioned. In field hockey, it means a player must sit out for a minimum of this many minutes.",
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

def eighties():
    eightiesQuestions = [
        ('''"We're no strangers to love/You know the rules, and so do I"; 1987''',
         "never gonna give you up"),
        ('''"Money's the matter/If you're in it for love, you ain't gonna get too far"; 1982''',
         "maneater"),
        ('''"I'm never gonna dance again/Guilty feet have got no rhythm"; 1984''',
         "careless whisper"),
        ('''"People always told me be careful what you do/And don't go around breaking young girl's hearts"; 1982''',
         "billie jean"),
        ('''"It ain't much I'm asking, if you want the truth/Here's to the future for the dreams of youth"; 1989''',
         "i want it all"),
        ('''"Gina dreams of running away/When she cries in the night, Tommy whispers/'Baby, it's okay, someday'"; 1987''',
         "livin on a prayer")
    ]
    return eightiesQuestions

def world():
    worldQuestions = [
        ("In 2019, the Event Horizon Telescope released the very first image of this region of spacetime, best known for being so dense not even light can escape it.", 
         "black hole"),
        ("There are typically two full moons per month. However, a third full moon within that month is known as this.",
         "blue moon"),
        ("This solar phenomena are the main reasons for auroras to appear at the Earth's poles. If strong enough, it could also severely disrupt technology.",
          "geomagnetic storms"),
        ("This galaxy, named for the wife of Perseus in Greek mythology, is the only other galaxy(besides the Milky Way) that is visible to the naked eye.",
         "andromeda"),
        ('''"To prevent war, the galaxy is on Orion's belt." Not quite...but Orion's this is south of the belt, also known as a "stellar nursery".''',
         "nebula"), 
        ("When a massive star dies, they tend to go out with a bright, massive bang, otherwise known as this.",
         "supernova")
    ]
    return worldQuestions

def nut():
    nutQuestions = [
        ("60 seconds.",
        "minute"),
        ("Lack of proper nourishment.",
         "malnutrition"),
        ("Not put to use; ends in -ed",
         "unutilized"),
        ("A ring-shaped sweet fried dough; five letter",
         "donut"),
        ("A legume crop with edible seeds; also known as a goober.",
         "peanut")
        ("Useless; pointless",
         "unutile")
    ]
    return nutQuestions

def apple():
    appleQuestions = [
        ("The origins of the caramel apple stem from this city in New Jersey, currently known for having one of the busiest airports in the world.",
         "Newark"),
        ("This man, best known as Johnny Appleseed, introduced apple trees into states like Pennsylvania and Illinois.",
         "John Chapman"),
        ("Despite apples being promiment in the United States, only this type of apple is native to the country.",
         "crabapple")
        ("Growing apples is actually a science! It's a branch of botany called this, which also encompasses all other fruits like a pear.",
         "pomology"),
        ("Be careful when consuming apple seeds. They contain traces of this dangerous chemical, known for having a bitter almond scent.",
         "cyanide"),
        ("Apples trees produce beautiful flowers, so it's no surprise that the fruit is in the same family as this romantic flower.",
         "rose")
    ]
    return appleQuestions

def vocab():
    vocabQuestions = [
        ("A ghost; starts with s",
         "specter"),
        ("Infection, or a hidden program that harms a computer",
         "virus")
        ("A student, or the centermost part of the eye",
         "pupil")
        ("Nonprofessional, or someone who is inept at a particular activity; starts with a",
         "amateur")
        ("Magical or medicinal potion",
         "elixir")
        ("Picturesque, or extremely happy and peaceful; starts with i",
         "idyllic")
    ]
    return vocabQuestions

def phrase():
    phraseQuestions = [
        ("Jack of all trades",
         "master of none"),
        ("You can lead a horse to water",
         "but you cannot make it drink"),
        ("Those who live in glass houses",
         "should not throw stones"),
        ("The early bird",
         "gets the worm"),
        ("An eye for an eye",
         "makes the whole world blind"),
        ("All work and no play",
         "makes jack a dull boy")
    ]
    return phraseQuestions

def gng():
    gngQuestions = [
        ("The Mount Tambora Eruption of April 1815; country in Southeast Asia and Oceania",
         "indonesia"),
        ("Vadivia Earthquake, with a record 9.5 magnitude; country in western South America",
         "chile"),
        ("Mount Elbert, the highest point in the Rockies; U.S. state in the west",
         "colorado"),
        ("Petrified forest, a national park full of petrified wood; U.S. state in the southwest",
         "arizona"),
        ("Lituya Bay megatsunami, with about 1700 foot waves; U.S. state in the northwest",
         "alaska"),
        ("The Matterhorn, the world's most photogenic mountain; country in Central Europe",
         "switzerland")
    ]
    return gngQuestions

def homes():
    homesQuestions = [
        ("Lake Erie is allegedly home to a folkloreish monster with this nickname. It had been spotted on multiple occassions over the course of decades.",
         "bessie"),
        ("The lakes have their own area of unexplained plane and boat disappearances, quite similar to this region in the North Atlantic Ocean.",
         "bermuda triangle"),
        ('''The Lake Michigan shoreline is the only place you can find this type of stone, best known for its "rays of the rising sun" pattern.''',
         "petoskey"),
        ("This large island based in Lake Superior contains several smaller lakes within it. A lake on a lake, how about that.",
         "isle royale")
        ("Lake Michigan and Lake Huron are, hydrologically speaking, one lake because they share the same water and are connected by this narrow passage of water.",
         "strait")
        ("When this record-breaking heavy hitter from the Yankees hit his first home run in Toronto, it it believed that the ball landed in Lake Ontario.",
         "babe ruth")
    ]
    return homesQuestions

def shocking():
    shockingQuestions = [
        ("Yes, it is possible for it to rain cats and dogs...literally. In Calagary in 1921, thousands of these amphibians poured from the skies.",
         "frog")
        ("Occassionally, this type of cloud appearing as bulbous pouches will hang underneath the base of a raincloud after a major thunderstorm.",
         "mammatus"),
        ("There are four types of thunderstorms: single-cell, multi-cell clusturs, multi-cell lines, and this, which is one of the most destructive thunderstorm types.",
         "supercell"),
        ("In 1992, a breeding facility for burmese python was demolished, allowing many of the snakes to escape? How? You have this Category 5 hurricane to thank.",
         "andrew"),
        ("What do you get when you mix snow with a thunderstorm? This rare weather phenomenon, which is more commonly occuring near larger lakes.",
         "thundersnow"),
        ("This type of windstorm can reach wind speeds of up to 58 miles per hour and are incredibly dangerous. In Iowa, it caused over 12 billion dollars worth of damage.",
         "derecho")
    ]
    return shockingQuestions

def dog():
    dogQuestions = [
        ("Even dogs have their own fingerprints! Rather, the print of this bodypart is unique to every dog.",
         "nose"),
        ("The Basenji dog isn't entirely barkless. They can do this, or a form of singing popular in Switzerland.",
         "yodel"),
        ("The Labrador Retriver, one of America's most popular dog, is actually from this country in the far north.",
         "newfoundland"),
        ("There dogs - two Pomeranians and a Pekingese - survived the sinking of this massive passenger liner in 1912.",
         "titanic"),
        ("This type of dog could beat out a cheetah in a race, as they can run at about 35 miles per hour for an elongated period of time.",
         "greyhound"),
        ("A group of pugs is called a this, or a low, rumbling sound made as a noise of complaint.",
         "grumble")
    ]
    return dogQuestions

def dailyDouble(qna, player):
    print("You have earned a daily double!")
    print("Here's how it works:")
    print("You'll input a point wager. The wager cannot be over your current point amount. If you are in the negatives or right at zero, it cannot be over 2000 points.")
    print("After that, you'll be prompted to answer the question. Whether or not you earn those points will depend on if you answer the question correctly.")
    print("You currently have {} points.".format(player.getPoints()))
    w = True
    while w:
        if(player.getPoints() <= 0):
            wager = input("Enter your wager(1 - 2000): ")
            if(int(wager) > 2000) or (int(wager) < 1) or (wager.isdigit() == False):
                print("Invalid input. Please try again.")
                continue
            else:
                w = False
        else:
            wager = input("Enter your wager(1 - {}): ".format(player.getPoints()))
            if(int(wager) > player.getPoints()) or (int(wager) < 1) or (wager.isdigit() == False):
                print("Invalid input. Please try again.")
                continue
            else:
                w = False
    print(qna.getQuestion())
    guess = getGuess()
    correct = qna.validateAns(guess)
    if(correct == True):
        print("That answer is correct! You have earned {} points.".format(wager))
        player.addPoints(int(wager))
    else:
        print("That is incorrect. The correct answer is: {}".format(qna.getAnswer().title()))
        player.removePoints(int(wager))
        

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
            q = random.randint(0, len(test[cat][1])-1)
            pointDict[points] = test[cat][1][q]
            del test[cat][1][q]
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

def getPlayer():
    #p1 = input("Player One, enter your name: ")
    #p2 = input("Player Two, enter your name: ")
    #p3 = input("Player Three, enter your name: ")
    p1 = Player("bruh")
    p2 = Player("man")
    p3 = Player("ur mom")
    return [p1, p2, p3]



def gameone():
    print("Jeopardy rules yadda yadda yadda")
    players = getPlayer()
    cna = firstRound(getCatnAns())
    rCats = cna[0]
    del cna[0]
    player = 0
    dd = 0
    fr = True
    while fr:
        print("{}, its your turn.".format(players[player].getName()))
        cat = True
        while cat:
            print("Available Categories: ")
            for item in cna:
                print("{}: {}".format(item, cna[item][0][0]))
            cCat = input("Enter the category number: ")
            if(cCat.isdigit() and int(cCat)>0 and int(cCat) in cna.keys()):
                cCat = int(cCat)
                cat = False
            else:
                print("Invalid input. Please try again.")
                continue
        print(cna[cCat][0][0])
        print(cna[cCat][0][1])
        question = True
        while question:
            print("Available Questions:")
            for item in cna[int(cCat)][1]:
                print(item)
            cQuest = input("Enter a point amount: ")
            if(cQuest.isdigit() and int(cQuest)>0 and int(cQuest) in cna[cCat][1].keys()):
                cQuest = int(cQuest)
                question = False
            else:
                print("Invalid input. Please try again.")
                continue
        qna = QnA(cna[cCat][1][cQuest][0], cna[cCat][1][cQuest][1])
        if(len(cna) == 1) and (len(cna[cCat][1]) == 1) and (dd == 0):
            dailyDouble(qna, players[player])
        elif(random.randint(1, 10) == 10) and (dd == 0):
            dailyDouble(qna, players[player])
        else:
            print(qna.getQuestion())
            guess = getGuess()
            correct = qna.validateAns(guess)
            if(correct == True):
                print("That answer is correct! You have earned {} points.".format(cQuest))
                players[player].addPoints(cQuest)
            else:
                print("That is incorrect. The correct answer is: {}".format(qna.getAnswer().title()))
                players[player].removePoints(cQuest)
        del cna[cCat][1][cQuest]
        if(len(cna[cCat][1]) == 0):
            del cna[cCat]
        if(len(cna) == 0):
            print("Round one over!")
            fr = False
        player+=1
        if(player > 2):
            player = 0
    print("Here are the current standings: ")
    sorted_players = sorted(players, key=lambda x: x.points)
    print("1. {} with {} points".format(sorted_players[2].getName(), sorted_players[2].getPoints()))
    print("2. {} with {} points".format(sorted_players[1].getName(), sorted_players[1].getPoints()))
    print("3. {} with {} points".format(sorted_players[0].getName(), sorted_players[0].getPoints()))
    return [rCats, players]

        
tranfer_vars = gameone()