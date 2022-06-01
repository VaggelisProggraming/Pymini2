try:
    import webbrowser
    import calendar 
    import datetime
    from tqdm import tqdm, trange
    from tqdm import tqdm
    import time
    import os
    import random
    import sys
    import images
    from PIL import Image

    class color() :
            black = '\033[30m'
            red = '\033[31m'
            green = '\033[32m'
            yellow = '\033[33m'
            blue = '\033[34m'
            magenta = '\033[35m'
            cyan = '\033[36m'
            white = '\033[37m'
            lightblue = '\033[94m'
            reset = '\033[37m'
    
    class Background() :
            black = '\033[40m'
            red = '\033[41m'
            green = '\033[42m'
            yellow = '\033[43m'
            blue = '\033[44m'
            magenta = '\033[45m'
            cyan = '\033[46m'
            white = '\033[47m'
            reset = '\033[49m'

    for i in range(100):
        print('\n\n\n')
    print(color.yellow+images.MainBg)

    Q1 = input("""
    What Would You Like To Do?
    [1]. Sign In To Current Account.
    [2]. Sign Up (Will Replace Old User If An Account Is Already Set-Up)
    """)

    if Q1 == '2':
        Password = input('Please Enter Your Password: ')
        while True:
            def doesFileExists(filePathAndName):                            
                return os.path.exists(filePathAndName)

            if doesFileExists('./Password.txt'):
                with open('Password.txt') as f:
                    contents = f.read()
                if contents == Password:
                    UserNameS = input('Please Enter Your New Username: ')
                    PasswordS = input('Please Enter Your New Password: ')
                    with open('Username.txt', 'w') as f:
                        f.write(UserNameS)
                    with open('Password.txt', 'w') as f:
                        f.write(PasswordS)
                        break
            else:
                with open('Password.txt', 'w') as f:
                    f.write(Password)
                print('Password.txt Was Created! The Program will Now Shutdown')
                time.sleep(1.10)
                exit()




    if Q1 == '1':
        Password = input('Please Enter Your Password: ')


        with open('Password.txt') as f:
            contents = f.read()
    while True:
        if contents == Password:
            print('Login Successful')
            time.sleep(1)
            print('Welcome To PyminiOS')
            MainMenu = input("""
                    What Would You Like To Do?
                    
                    [1]. Exit.
                    [2]. Games.
                    [3]. Calculator.
                    [4]. Calender.
                    [5]. Terminal.
                    [6]. browers.
                    [7]. About System.
                    [8]. Proggram Stuff
                    
                    """)
            if MainMenu.lower() == "1":
                print("Gonna Exit.")
                exit()
            if MainMenu.lower() == "2":
                GameC = input(color.red+"""
                [1]. Rock Paper Scissors.
                [2]. Guess The word.
                [3]. Guess the number.
                [4]. Typing Test.
                [5]. Math Game.
                [6]. Proggraming Quiz.
                [7]. Reaction Game.
                [8]. Adventure Game.
                [9]. Gambling Game.
                """)
                if GameC == '1':
                     while True:
                        print(images.RPStext)
                        ROPESC = ['rock', 'paper', 'scissors']
                        RPS = random.choice(ROPESC)
                        rps = input(f"What's your choice {ROPESC} : ")
                        print('the bot chose', RPS)
                        if rps == 'l': 
                            print('You left!')
                            break
                if GameC == '2':
                    while True:
                        print(images.WTWtext)
                        Choices = ["easy", "chest", "value", "noise", "friend", "bus", "child", "developers", "power", "use"]
                        CompChoice = random.choice(Choices)
                        if CompChoice == "easy":
                            print("Python is ... That's why a lot of people lern the language")
                            time.sleep(0.1)
                            print("I don't like hard thing I like ... things")
                            time.sleep(0.1)
                            print("People say that java is hard and I agree but some other say it's ....")
                            stopwatch = time.time()
                            UsrChoice = input("What's The word? : ")
                            End = time.time() - stopwatch
                            if UsrChoice == "easy":
                                print(f"YES! This took you {round(End)}")
                            if UsrChoice == "l":
                                print("Ok leaving")
                            else:
                                print(f"NO!")
                        if CompChoice == "chest":
                            print("This is a bit hard :")
                            print("So This maybe completly useless but for those who have played minecraft we store things in ..... witch are easy to make")
                            time.sleep(0.1)
                            print("If you go to your grandpa's attic you may find c....s")
                            time.sleep(0.1)
                            print("We can store stuff in there what is it?")
                            stopwatch = time.time()
                            UsrChoice = input("What is it? : ")
                            EndingTime = time.time() - stopwatch
                            if UsrChoice == "chest":
                                print("YES!! you did it it took you", round(EndingTime))
                            if UsrChoice == "l":
                                print("Ok leaving")
                            else:
                                print("wrong Maybe the next time "+images.sadFace)
                        if CompChoice == "value":
                            print("Money has ..... because the bank says it!")
                            UsrChoice = input("Enter what it is : ")
                            if UsrChoice == "value":
                                print("Correct")
                            if UsrChoice == "l":
                                print("Ok leaving")
                            else:
                                print("Wrong")
                        if CompChoice == "noise":
                            print("Some headphones have n...e cancelation")
                            time.sleep(0.1)
                            print("What's all that n.i..?")
                            stopwatch = time.time()
                            UsrChoice = input("Enter what it is : ")
                            End = time.time() - stopwatch
                            if UsrChoice == "noise":
                                print("You Got it! It took you " + End + " to complete")
                            if UsrChoice == "l":
                                print("Ok leaving")
                            else:
                                print("Wrong "+images.sadFace)
                        if CompChoice == "friend":
                            print("Your f...d. are those who might help you when you're sad")
                            time.sleep(0.1)
                            print("If you are not an extrovert in shool when you are on recess you will probably be with your frieneds")
                            Start = time.time()
                            UsrChoice = input("Enter what it is : ")
                            End = time.time() - Start
                            if UsrChoice == "friend":
                                print("Got it! it took you " + End)
                            if UsrChoice == "l":
                                print("Ok leaving")
                            else:
                                print(f"Wrong {images.sadFace}")
                        if CompChoice == "bus":
                            print("Ok so if you are in shcool how you get to shcool is probably by a b..")
                            time.sleep(0.1)
                            print("What is it?")
                            Start = time.time()
                            UserChoice = input("What is it? : ")
                            End = time.time() - Start
                            if UserChoice == "bus":
                                print("Got it! it took you " + End)
                            if UsrChoice == "l":
                                print("Ok leaving")
                            else:
                                print("wrong choice")
                        if CompChoice == "child":
                                print("a c..l. needs to play!")
                                time.sleep(0.1)
                                print(".h...ren go to shcool to learn things and see their friends")
                                Start = time.time()
                                UsrChoice = input("Enter what it is : ")
                                End = time.time() - Start
                                if UsrChoice.lower() == "child" or UsrChoice.lower() == "children":
                                    print("Got it! it took you" + End)
                                if UsrChoice == "l":
                                    print("Ok leaving")
                                else:
                                    print(f"Wrong {images.sadFace}")
                        if CompChoice == "developers":
                                print("Dev......s code things")
                                Start = time.time()
                                UsrChoice = input("What is it? :")
                                End = time.time() - Start
                                if UsrChoice == "developers":
                                    print("Correct! it took you " + End + " seconds")
                                if UsrChoice == "l":
                                    print("Ok leaving")
                                else:
                                    print("Wrong!")
                        if CompChoice == "power":
                            print("I have all the p...r in my hands")
                            time.sleep(0.1)
                            Start = time.time()
                            UserChoice = input("Enter what it is: ")
                            End = time.time() - Start
                            if UserChoice == "power":
                                print("Correct! it took you " + End + " seconds")
                            if UsrChoice == "l":
                                print("Ok leaving")
                            else:
                                print("Wrong!" + images.sadFace)
                        if CompChoice == "use":
                            print("I u.e an computer")
                            time.sleep(0.1)
                            Start = time.time()
                            UsrChoice = input("what is it? : ")
                            End = time.time() - Start
                            if UserChoice == "use":
                                print("Correct! it took you " + End + " seconds")
                            if UsrChoice == "l":
                                print("Ok leaving")
                                break
                            else:
                                print("Wrong!" + images.sadFace)
                
                
                if GameC == '3':
                    print(images.GTNtext)
                    while True:
                        CompChoice = random.randint(0, 20)
                        UsrGuess = input("Enter what you think it is: ")
                        if UsrGuess == CompChoice:
                            print("Correct!")
                        if UsrGuess.lower() == "l":
                            print("Ok leaving")
                            break
                        if UsrGuess == "Change":
                            UsrIntChoice = int(input("Ok what number do you want your limit to be? :"))
                            while True:
                                CompChoice = random.randint(1, UsrIntChoice)
                                UserChoice = int(input("What is the number? :"))
                                if UserChoice == CompChoice:
                                    print("Correct")
                                if UsrChoice.lower() == "l":
                                    print("Ok leaving you need to type one more time l thought")
                                    break
                                if UserChoice == "Change":
                                    while True:
                                        CompChoice = random.randint(1, UsrIntChoice)
                                        UserChoice = int(input("What is the number? :"))
                                        if UserChoice == CompChoice:
                                            print("Correct")
                                        if UsrChoice.lower() == "l":
                                            print("Ok leaving you need to type one more time l thought")
                                            break
                if GameC == '4':
                    import typing

                if GameC == '5':
                    Symbols = ['+', '-', 'x', ':']

                    symbols = random.choice(Symbols)
                    maths = random.randint(0,100)
                    maths2 = random.randint(0, 100)
                    print('Starting in ')
                    time.sleep(1)
                    print(3)
                    time.sleep(1)
                    print(2)
                    time.sleep(1)
                    print(1)
                    time.sleep(1)
                    print('GO!')
                    start_time = time.time()
                    print('Your porblem is', maths, symbols, maths2, '=')
                    maths = input()
                    fin_time = time.time() - start_time
                    print("This took ", fin_time, ' seconds')

                if GameC == '6':
                    class Question() :
                        def __init__(self, prompt, answer):
                            self.prompt = prompt
                            self.answer = answer

                    question_prompts = [
                        "What color are apples?\n(a) Red/Green\n(b)Orange",
                        "What color are bananas?\n(a) Red/Green\n(b)Yellow",
                    ]

                    questions = [
                        Question(question_prompts[0], "a"),
                        Question(question_prompts[1], "b"),
                    ]

                    def run_quiz(questions):
                        score = 0
                        for question in questions:
                            answer = input(question.prompt)
                            if answer == question.answer:
                                score += 1
                        print("you got", score, "out of", len(questions))

                    run_quiz(questions)
                if GameC == '7':
                    print(color.magenta+images.ReactingTime)
                    points = {}
                    player_1 = input("Player one: ")
                    player_2 = input("Player two: ")
                    points[player_1] = 0
                    points[player_2] = 0
                    rounds = int(input("Rounds: "))
                    while rounds % 2 != 0:
                        print("Sorry, you have to give me an even number!")
                        rounds = int(input("Rounds: "))
                    turn = random.randint(0, 1)
                    for r in range(0, rounds):
                        if turn == 0:
                            print("It's {}'s turn!".format(player_1))
                        else:
                            print("It's {}'s turn!".format(player_2))
                        time.sleep(0.5)
                        print("Get ready..")
                        time.sleep(random.randint(1,12))
                        then = datetime.datetime.now()
                        t = input("GO!! ")
                        now = datetime.datetime.now()
                        diff = then-now
                        reaction_time = round(abs(diff.total_seconds()), 2)
                        if turn == 0:
                            points[player_1] += reaction_time
                            turn += 1
                        else:
                            points[player_2] += reaction_time
                            turn -= 1
                        print("Reaction time: {} seconds".format(reaction_time))
                    winner = min([points[player_1], points[player_2]])
                    print("The winner is..")
                    time.sleep(0.5)
                    print(player_1+"!")
                if GameC == '8':
                    print(images.Adventure)
                    import adventure
                if GameC == '9':
                    def intro_banner():
                        s = color.green+images.GAMBLING
                        
                        print(s)
                    def game_over():
                        s = "Game Over. Bye!"

                        print(s)
                        
                    def main():
                        intro_banner()

                        playername = input('Player Name : ')
                        money = 50
                        print("Welcome to the game, " + playername + ". Your starting amount is " + str(money) + ' Gold.')

                        keepplaying = True
                        while keepplaying:
                            bet = input("Place your bet >> ")
                            isbetnotvalid = int(bet) > money or int(bet) < -1
                            while isbetnotvalid:
                                print("Please enter a valid bet.")
                                bet = input("Place fix your bet >> ")
                                isbetnotvalid = int(bet) > money or int(bet) < -1

                            bet = int(bet)

                            player_card = random.randint(1, 12)
                            cpu_card = random.randint(1, 12)

                            print("Your card is " + str(player_card) + ". CPU card is " + str(cpu_card) + ".")

                            if player_card == cpu_card:
                                print("It's a DRAW! CPU wins because that's how it is.")
                                money = money - bet
                            elif player_card > cpu_card:
                                print("You win " + str(bet) + " Gold!")
                                money = money + bet
                            else:
                                print("CPU wins! You lose " + str(bet) + " Gold!")
                                money = money - bet

                            if money < 0:
                                print("You're out of money!")
                                game_over()
                                keepplaying = False
                            else: 
                                print("Your money is now " + str(money) + " Gold.")
                                ask = input("Do you want to keep playing? [y/N] >> ")
                                if ask == 'y' or ask == 'Y':
                                    keepplaying = True
                                else:
                                    print("You're leaving with " + str(money) + " Gold. Bye.")
                                    game_over()
                                    keepplaying = False
                    main()
            if MainMenu.lower() == "3":
                print(images.Calculator,
                
                        images.CalculatorKeys)     
                for i in range(5):
                    time.sleep(1)
                    print('type 12345678910 or 1234.003 if you want to leave the calculator please enter it on the first number (you have to pass every number thought!)')
                    num = float(input("Your number "))
                    num2 = float(input("Your second number "))
                    # num3 = input("Your third number ")
                    num4 = input('do you want "+ - * multiply or / for devide" ')
                    if num4 == '+':
                        print('the result of', num, '+', num2, 'is', (num) + (num2))
                    if num4 == '-':
                        print('The result is', (num) - (num2))
                    if num4 == '*':
                        print("the result is", (num) * (num2))
                    if num4 == '/':
                        print('the result is', (num) / (num2))
                    symbols = ['+', '-', '*', '/']
            
                    nums = num, num2
                    if num4 != symbols or nums != int:
                        print('Invalaid input')
            if MainMenu.lower() == "4":
                print(images.Calendar)

                print("Your Calender\n \n ")

                y = int(input("Enter the Year : "))
                m = int(input("Enter the month : "))
                try:
                    mycalender = calendar.month(y , m)
                    print("\n", mycalender)
                    stay = input("Leave (press anything): ")
                except IndexError:
                    print("Its out of range")
            if MainMenu.lower() == "5":
                class Background() :
                    black = '\033[40m'
                    red = '\033[41m'
                    green = '\033[42m'
                    orange = '\033[43m'
                    blue = '\033[44m'
                    magenta = '\033[45m'
                    cyan = '\033[46m'
                    lightgray = '\033[47m'
                    darkgray = '\033[100m'
                    lightred = '\033[101m'
                    lightgreen = '\033[102m'
                    yellow = '\033[102m'
                    lightblue = '\033[102m'
                    lightpurple = '\033[102m'
                    Teal = '\033[106m'
                    white = '\033[107m'
                    reset = '\033[49m'
                Q1 = input("Do you want to Open [1] Ult CMD or [2] Command Prompt  : ")
                if Q1 == '2':
                    os.startfile("pyminiOS\Command Prompt.lnk")
                if Q1 == '1':
                    while True:
                        Ult = input(f"{color.green+os.path.expanduser('~')}~{color.red}$ ").strip()
                        print(color.reset)
                        if "echo " in Ult:
                            print(Ult[5:])
                        elif "input" in Ult:
                            x = input(Ult[6:], " : ")
                        elif "tree C" in Ult:
                            os.system("tree C:/")
                        elif "canvas.Create.content." in Ult:
                            print("Opening image " + Ult[22:])
                            PathImg = input("what's the path :  ")
                            im = Image.open(f"{PathImg}")
                            im.show()

                        elif Ult == 'break.sys':
                            print("Leaving ULT CMD")
                            break
                        if Ult == 'help':
                            print("""echo hello, world!
                            results: hello, world!
                            warning: use echo one space this is really important because is you do with two spaces
                            results: ello world
                            results(three spaces) : llo world\n\n\n
                            """)
                            print("""
                            input lorem insprum
                            results: lorem insprum : 
                            warning: dont type (:) because ult comes with it. If you don't want it type
                            raw.input lorem insprum
                            results: lorem insprum
                            second problem : same with printing
                            """)
                            print("""
                            echo leaving
                            break.sys
                            results:( leaving\n back to main screen)
                            """)
                        else:
                            print('Invalid Command.')
            if MainMenu.lower() == "6":
                Question = input("What searching engine do you want to use? : ")
                if Question.lower() == "duck duck go":
                    webbrowser.open("https://duckduckgo.com/")
                if Question.lower() == "google":
                    webbrowser.open("https://google.com/")
                if Question.lower() == "bing":
                    webbrowser.open("https://www.bing.com/")
                if Question.lower() == 'yahoo':
                    webbrowser.open("https://gr.yahoo.com/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAEOOS5WGS-HvCDmcm2L1ilEec8F7nl4QtCk-NP5I3c1Opxks70fwKtmoeeBwnFu3qw7OlM5cIbR0gXtEbfP6PX8U4MLb5VZyUQQAA5xv14O19UBp7gb4cbDLyvQ9PH-MrpZH-cGUPHShURACqNb3-fn0D_W3bJEf0nY9nzebw7m1")
                else:
                    print("sorry I don't know that search engine")
            
            if MainMenu.lower() == '7':
                lang = 'python 3.9'
                __version__ = "2.0.0"
                print(f"System version: {__version__}")
                print(f"language writen in {lang}")

            if MainMenu.lower() == '8':
                print("Opening pyminiIDE you can code in python")
                import pyminiIDE

            if MainMenu.lower() == 'background':
                BGcolor = input("""
                What color do you want your background to be:

                    [1]. black
                    [2]. red
                    [3]. Green
                    [4]. Yellow
                    [5]. blue
                    [6]. magenta
                    [7]. cyan
                    [8]. white
                    [9]. reset
                    
                """)
                if BGcolor == '1':
                    print(Background.black)
                if BGcolor == '2':
                    print(Background.red)
                if BGcolor == '3':
                    print(Background.green)
                if BGcolor == '4':
                    print(Background.yellow)
                if BGcolor == '5':
                    print(Background.blue)
                if BGcolor == '6':
                    print(Background.magenta)
                if BGcolor == '7':
                    print(Background.cyan)
                if BGcolor == '8':
                    print(Background.white)
                if BGcolor == '9':
                    print(Background.reset)
                
            if MainMenu.lower() == 'text colors':
                FGcolor = input("""
                What colors do you want? :

                [1]. black
                [2]. red
                [3]. green
                [4]. yellow
                [5]. blue
                [6]. magenta
                [7]. cyan
                [8]. white
                [9]. light blue
                [10]. reset

                """)
                if FGcolor == '1':
                    print(color.black)
                elif FGcolor == '2':
                    print(color.red)
                elif FGcolor == '3':
                    print(color.green)
                elif FGcolor == '4':
                    print(color.yellow)
                elif FGcolor == '5':
                    print(color.blue)
                elif FGcolor == '6':
                    print(color.magenta)
                elif FGcolor == '7':
                    print(color.cyan)
                elif FGcolor == '8':
                    print(color.white)
                elif FGcolor == '9':
                    print(color.lightblue)
                else:
                    print("sorry don't know that color'")

            if MainMenu.lower() == 'Open amazon':
                webbrowser.open("https://www.amazon.com/")
            if MainMenu.lower() == 'Open Typing tests':
                webbrowser.open("https://www.speedtypingonline.com/typing-test")
            if MainMenu.lower() == 'Open github':
                webbrowser.open("https://github.com/")
            if MainMenu.lower() == "Download UCube":
                webbrowser.open("https://vaggelisproggraming.github.io/UCube/")
            if MainMenu.lower() == 'Download UFPS':
                webbrowser.open("https://vaggelisproggraming.itch.io/ufps")
            if MainMenu.lower() == 'Code a website':
                webbrowser.open("https://codepen.io/trending")
            if MainMenu.lower == 'code in replt':
                webbrowser.open("https://replit.com/~")
            if MainMenu.lower() == 'orginize':
                webbrowser.open("https://trello.com")
            

                


            if MainMenu == "emojis":
                print("Found an easter egg huh")
                print("Ok")
                print("""
                ( ͡° ͜ʖ ͡°)
                ( ͠° ͟ʖ ͡°)
                ( ͡°👅 ͡°)
                \( ᵔ︠ ͜ʖ ︡ᵔ)/
                ( ͡⊙ ͜ʖ ͡⊙)
                ( ͡◉ ͜ʖ ͡◉)
                ( ಠ ͜ʖಠ)
                ( ͡° ʖ̯ ͡°)
                ¯\_( ͡° ͜ʖ ͡°)_/¯
                (っ＾▿＾)💨
                (╯ ͠° ͟ʖ ͡°)╯┻━┻
                (ง ͠° ͟ل͜ ͡°)ง
                ( ͡▧ ͜ʖ ͡▧)
                ( ◣︡ ͜ʖ ◢︠ )
                (っ ◣︡ ͜ʖ ◢︠ )っ🎔
                (╥︣﹏᷅╥᷅)
                ಥ_ಥ
                💪 (•︡益︠•) 👊
                (¬‿¬)
                """)
                    
                        


                        

        else:
            print('Access Denied')
            print('The Program Will Now Shutdown!')
            time.sleep(1.15)
            exit()


except Exception as inst:
    print(type(inst))    # the exception instance
    print(inst.args)     # arguments stored in .args
    print(inst)          # __str__ allows args to be printed directly,
                          # but may be overridden in exception subclasses
    x, y = inst.args     # unpack args
    print('x =', x)
    print('y =', y)
    print(color.blue)
    for i in tqdm([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
        time.sleep(0.2)
    print(images.ErrorScreen)
    time.sleep(1.5)
    import Main
except KeyboardInterrupt:
    print("Keyboard Interrupt")


__version__ = "2.0.0"
__name__ = "Pymini 2"