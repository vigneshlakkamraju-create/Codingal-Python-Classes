class Cricket:
    def __init__(self, player, score):
        self.__player = player
        self.__score = score

    def info(self):
        print(f"Player: {self.__player}, Score: {self.__score}")

    def play(self):
        print(f"{self.__player} hits a six!")

    def get_score(self):
        return self.__score

    def set_score(self, new_score):
        if new_score >= 0:
            self.__score = new_score
        else:
            print("Score cannot be negative.")


class Football:
    def __init__(self, player, goals):
        self.__player = player
        self.__goals = goals

    def info(self):
        print(f"Player: {self.__player}, Goals: {self.__goals}")

    def play(self):
        print(f"{self.__player} scores a goal!")

    def get_goals(self):
        return self.__goals

    def set_goals(self, new_goals):
        if new_goals >= 0:
            self.__goals = new_goals
        else:
            print("Goals cannot be negative.")

cricket = Cricket("Virat Kohli", 75)
football = Football("Lionel Messi", 3)

print("=== Sports Scoreboard ===\n")
for sport in (cricket, football):
    sport.info()
    sport.play()
    print()  

print("---Direct change attempt---")
cricket.__score = 100
print(f"Directly changed cricket score to: {cricket.__score} (should not affect the actual score)")


print("=== Updating Scores ===\n")
cricket.set_score(80)
football.set_goals(4)