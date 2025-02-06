# import random
# import sys
# import time
# from typing import List, Optional

# class SquidGame:
#     def __init__(self):
#         self.players: List[str] = []
#         self.prize_money: int = 45600000000  # 45.6 billion won
#         self.current_players: int = 0
        
#     def start_game(self) -> None:
#         print("\n=== Welcome to Squid Game ===")
#         print("Your life is on the line. Will you survive?")
        
#         player_name = input("\nEnter your name to join the game: ")
#         self.players.append(player_name)
#         self.current_players = len(self.players)
        
#         self.play_red_light_green_light()
        
#     def play_red_light_green_light(self) -> None:
#         print("\n=== Game 1: Red Light, Green Light ===")
#         print("Rules: Move when it's 'Green Light', stop when it's 'Red Light'")
#         print("You have 30 seconds to reach the finish line!")
        
#         input("\nPress Enter to start...")
        
#         for _ in range(3):  # Three rounds
#             light = random.choice(["Red", "Green"])
#             print(f"\n{light} Light!")
#             time.sleep(2)
            
#             if light == "Red":
#                 action = input("Quick! Type 'stop' to freeze: ").lower()
#                 if action != "stop":
#                     print("\n🔫 You moved during Red Light! Game Over!")
#                     sys.exit()
#             else:
#                 action = input("Type 'run' to move forward: ").lower()
#                 if action != "run":
#                     print("\n⚠️ You didn't move! You're running out of time!")
        
#         print("\n🎉 Congratulations! You survived Red Light, Green Light!")
#         self.play_honeycomb_game()
        
#     def play_honeycomb_game(self) -> None:
#         print("\n=== Game 2: Honeycomb Game ===")
#         print("Rules: Carefully trace the pattern without breaking it")
        
#         patterns = ["circle", "triangle", "star", "umbrella"]
#         pattern = random.choice(patterns)
        
#         print(f"\nYour pattern is: {pattern}")
#         print("You must 'cut' around it carefully...")
        
#         attempts = 3
#         while attempts > 0:
#             pressure = int(input("\nChoose cutting pressure (1-10): "))
#             if pressure > 7:
#                 print("\n💥 Too much pressure! The honeycomb broke! Game Over!")
#                 sys.exit()
#             elif pressure < 4:
#                 print("\n⚠️ Too gentle! You need more pressure!")
#                 attempts -= 1
#             else:
#                 print("\n🎉 Perfect! You successfully carved the pattern!")
#                 break
                
#         if attempts == 0:
#             print("\n⏰ You ran out of attempts! Game Over!")
#             sys.exit()
            
#         print("\n🏆 Congratulations! You've survived the games!")
#         print(f"You won {self.prize_money:,} won!")

# if __name__ == "__main__":
#     game = SquidGame()
#     game.start_game()




# Modified Squid Game

import random
import sys
import time
import os
from typing import List, Optional

from colorama import init, Fore, Back, Style

class SquidGame:
    def __init__(self):
        init()  # Initialize colorama
        self.players: List[dict] = []
        self.prize_money: int = 45600000000  # 45.6 billion won
        self.current_players: int = 0
        self.player_health: int = 100
        self.player_stamina: int = 100
        self.difficulty: str = 'normal'
        
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def display_stats(self):
        print(f"\n{Fore.CYAN}=== Player Stats ==={Style.RESET_ALL}")
        print(f"Health: {'♥' * (self.player_health // 10)}")
        print(f"Stamina: {'⚡' * (self.player_stamina // 10)}")
        
    def start_game(self) -> None:
        self.clear_screen()
        print(f"\n{Fore.RED}=== Welcome to Squid Game ==={Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Your life is on the line. Will you survive?{Style.RESET_ALL}")
        
        player_name = input(f"\n{Fore.GREEN}Enter your name to join the game: {Style.RESET_ALL}")
        self.difficulty = input(f"Choose difficulty (easy/normal/hard): ").lower()
        
        player = {
            'name': player_name,
            'alive': True,
            'wins': 0
        }
        self.players.append(player)
        self.current_players = len(self.players)
        
        self.main_game_loop()
        
    def main_game_loop(self):
        games = [
            self.play_red_light_green_light,
            self.play_honeycomb_game,
            self.play_tug_of_war,
            self.play_marbles,
            self.play_glass_bridge,
            self.play_final_squid
        ]
        
        for game_number, game in enumerate(games, 1):
            self.clear_screen()
            self.display_stats()
            if self.player_health <= 0:
                self.game_over("You ran out of health!")
                return
            
            print(f"\n{Fore.YELLOW}=== Game {game_number} of {len(games)} ==={Style.RESET_ALL}")
            time.sleep(2)
            game()
            
            # Recover some stamina between games
            self.player_stamina = min(100, self.player_stamina + 30)
            time.sleep(3)
            
    def play_red_light_green_light(self) -> None:
        print(f"\n{Fore.GREEN}=== Game 1: Red Light, Green Light ==={Style.RESET_ALL}")
        print("Rules: Move when it's 'Green Light', stop when it's 'Red Light'")
        
        distance = 0
        target_distance = 100
        time_limit = 30
        start_time = time.time()
        
        while distance < target_distance and (time.time() - start_time) < time_limit:
            light = random.choice(["Red", "Green"])
            print(f"\n{Fore.RED if light == 'Red' else Fore.GREEN}{light} Light!{Style.RESET_ALL}")
            
            reaction_start = time.time()
            action = input("Type 'stop' or 'run': ").lower()
            reaction_time = time.time() - reaction_start
            
            if reaction_time > (1.5 if self.difficulty == 'hard' else 2.0):
                self.player_health -= 20
                print(f"{Fore.RED}Too slow! You lose health!{Style.RESET_ALL}")
                
            if light == "Red" and action != "stop":
                self.game_over("You moved during Red Light!")
            elif light == "Green" and action == "run":
                move_distance = random.randint(10, 20)
                distance += move_distance
                self.player_stamina -= 10
                print(f"You moved forward {move_distance}m! ({distance}/{target_distance}m)")
                
            self.display_stats()
            time.sleep(1)
            
        if distance >= target_distance:
            print(f"\n{Fore.GREEN}🎉 Congratulations! You survived Red Light, Green Light!{Style.RESET_ALL}")
        else:
            self.game_over("Time's up!")

    def play_honeycomb_game(self) -> None:
        print(f"\n{Fore.GREEN}=== Game 2: Honeycomb Game ==={Style.RESET_ALL}")
        patterns = {
            "circle": "⭕",
            "triangle": "△",
            "star": "★",
            "umbrella": "☂"
        }
        pattern = random.choice(list(patterns.keys()))
        
        print(f"Your pattern is: {patterns[pattern]}")
        print("You must trace it carefully...")
        
        time_limit = 30 if self.difficulty == 'hard' else 45
        start_time = time.time()
        success_points = 0
        needed_points = 5
        
        while success_points < needed_points and (time.time() - start_time) < time_limit:
            pressure = int(input("\nChoose cutting pressure (1-10): "))
            angle = int(input("Choose cutting angle (1-10): "))
            
            ideal_pressure = random.randint(4, 7)
            ideal_angle = random.randint(4, 7)
            
            if abs(pressure - ideal_pressure) <= 1 and abs(angle - ideal_angle) <= 1:
                success_points += 1
                print(f"{Fore.GREEN}Perfect cut! Progress: {success_points}/{needed_points}{Style.RESET_ALL}")
            elif abs(pressure - ideal_pressure) <= 2 and abs(angle - ideal_angle) <= 2:
                success_points += 0.5
                print(f"{Fore.YELLOW}Decent cut! Progress: {success_points}/{needed_points}{Style.RESET_ALL}")
            else:
                self.player_health -= 20
                print(f"{Fore.RED}Bad cut! You lose health!{Style.RESET_ALL}")
            
            self.display_stats()
            
        if success_points >= needed_points:
            print(f"\n{Fore.GREEN}🎉 You successfully carved the pattern!{Style.RESET_ALL}")
        else:
            self.game_over("Failed to complete the pattern in time!")

    def play_tug_of_war(self) -> None:
        print(f"\n{Fore.GREEN}=== Game 3: Tug of War ==={Style.RESET_ALL}")
        rope_position = 50  # Middle position
        winning_position = 70  # Need to pull to this position to win
        losing_position = 30  # If rope goes below this, you lose
        
        while True:
            print("\n" + "=" * rope_position + "🔴" + "=" * (100 - rope_position))
            
            action = input("Choose action (pull/brace/rest): ").lower()
            
            if action == "pull":
                if self.player_stamina >= 10:
                    pull_power = random.randint(5, 15)
                    rope_position += pull_power
                    self.player_stamina -= 10
                else:
                    print(f"{Fore.RED}Too exhausted to pull!{Style.RESET_ALL}")
            elif action == "brace":
                enemy_pull = random.randint(3, 8)
                rope_position -= enemy_pull
                self.player_stamina += 5
            elif action == "rest":
                self.player_stamina += 15
                enemy_pull = random.randint(5, 10)
                rope_position -= enemy_pull
            
            self.display_stats()
            
            if rope_position >= winning_position:
                print(f"\n{Fore.GREEN}🎉 Victory! You won the tug of war!{Style.RESET_ALL}")
                break
            elif rope_position <= losing_position:
                self.game_over("You lost the tug of war!")
                
    def play_marbles(self) -> None:
        print(f"\n{Fore.GREEN}=== Game 4: Marbles ==={Style.RESET_ALL}")
        player_marbles = 10
        opponent_marbles = 10
        
        while player_marbles > 0 and opponent_marbles > 0:
            print(f"\nYour marbles: {player_marbles}")
            print(f"Opponent's marbles: {opponent_marbles}")
            
            bet = int(input("How many marbles do you bet? "))
            guess = input("Odd or Even? ").lower()
            
            if bet > player_marbles:
                self.game_over("You bet more marbles than you have!")
            
            opponent_number = random.randint(1, min(opponent_marbles, 5))
            is_odd = opponent_number % 2 == 1
            
            print(f"\nOpponent had {opponent_number} marbles!")
            
            if (is_odd and guess == "odd") or (not is_odd and guess == "even"):
                player_marbles += bet
                opponent_marbles -= bet
                print(f"{Fore.GREEN}You won this round!{Style.RESET_ALL}")
            else:
                player_marbles -= bet
                opponent_marbles += bet
                print(f"{Fore.RED}You lost this round!{Style.RESET_ALL}")
                
        if player_marbles <= 0:
            self.game_over("You lost all your marbles!")
        else:
            print(f"\n{Fore.GREEN}🎉 You won the marble game!{Style.RESET_ALL}")

    def play_glass_bridge(self) -> None:
        print(f"\n{Fore.GREEN}=== Game 5: Glass Bridge ==={Style.RESET_ALL}")
        bridge_length = 18
        current_position = 0
        
        print("\nCross the bridge by choosing the correct glass panel!")
        print("One will support you, the other will break!")
        
        while current_position < bridge_length:
            print(f"\nStep {current_position + 1}/{bridge_length}")
            print("Left (L) or Right (R)?")
            
            safe_panel = random.choice(['L', 'R'])
            choice = input("Choose: ").upper()
            
            if choice == safe_panel:
                current_position += 1
                print(f"{Fore.GREEN}Safe step!{Style.RESET_ALL}")
                time.sleep(1)
            else:
                damage = 40 if self.difficulty == 'hard' else 30
                self.player_health -= damage
                print(f"{Fore.RED}The glass breaks! You barely hang on!{Style.RESET_ALL}")
                if self.player_health <= 0:
                    self.game_over("You couldn't hold on!")
                    
            self.display_stats()
            
        print(f"\n{Fore.GREEN}🎉 You made it across the bridge!{Style.RESET_ALL}")

    def play_final_squid(self) -> None:
        print(f"\n{Fore.GREEN}=== Final Game: Squid Game ==={Style.RESET_ALL}")
        player_position = 0
        finish_line = 10
        opponent_position = 0
        
        while player_position < finish_line and opponent_position < finish_line:
            print(f"\nYour position: {'🏃' * player_position}{'_' * (finish_line - player_position)}")
            print(f"Opponent: {'🏃' * opponent_position}{'_' * (finish_line - opponent_position)}")
            
            print("\nChoose your action:")
            print("1. Attack (risky but can push opponent back)")
            print("2. Defend (safe but slower)")
            print("3. Sprint (fast but drains stamina)")
            
            action = input("Action (1-3): ")
            
            if action == "1":
                if random.random() > 0.5:
                    opponent_position = max(0, opponent_position - 2)
                    player_position += 1
                    print(f"{Fore.GREEN}Successful attack!{Style.RESET_ALL}")
                else:
                    self.player_health -= 20
                    print(f"{Fore.RED}Attack failed!{Style.RESET_ALL}")
            elif action == "2":
                player_position += 1
                if random.random() > 0.7:
                    opponent_position += 1
            elif action == "3":
                if self.player_stamina >= 20:
                    player_position += 2
                    self.player_stamina -= 20
                else:
                    print(f"{Fore.RED}Not enough stamina!{Style.RESET_ALL}")
                    
            opponent_position += random.randint(0, 1)
            self.display_stats()
            
            if self.player_health <= 0:
                self.game_over("You've been defeated!")
                return
                
        if player_position >= finish_line:
            self.victory()
        else:
            self.game_over("Your opponent reached the finish first!")

    def game_over(self, reason: str) -> None:
        print(f"\n{Fore.RED}💀 GAME OVER: {reason}{Style.RESET_ALL}")
        print(f"{Fore.RED}You have been eliminated.{Style.RESET_ALL}")
        sys.exit()
        
    def victory(self) -> None:
        print(f"\n{Fore.GREEN}🏆 CONGRATULATIONS! YOU WON THE SQUID GAME!{Style.RESET_ALL}")
        print(f"You won {self.prize_money:,} won!")
        sys.exit()

if __name__ == "__main__":
    game = SquidGame()
    game.start_game()
