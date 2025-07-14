import random
import time
import sys
import threading

# List of Hangul words for the game.
# (Note: For a real game, you would need a much larger list or a way to generate them.)
HANGUL_WORDS = [
    "안녕하세요", "파이썬", "게임", "코딩", "단어", "폭탄",
    "사랑", "행복", "시간", "점수", "생명", "도전"
]

# Game parameters
LIVES = 3
SCORE = 0
TIME_LIMIT = 2.0  # 2 seconds

def get_word():
    """Selects a random Hangul word."""
    return random.choice(HANGUL_WORDS)

def timed_input(prompt, timeout):
    """
    Handles user input with a timeout.
    
    This is a simple implementation and might behave differently 
    depending on the operating system and environment.
    """
    user_input = [None]
    
    def get_input():
        try:
            user_input[0] = input(prompt)
        except EOFError:
            pass

    input_thread = threading.Thread(target=get_input)
    input_thread.start()
    input_thread.join(timeout)
    
    if input_thread.is_alive():
        print("\n시간 초과!")
        return None
    
    return user_input[0]

def game_loop():
    """Main game loop."""
    global LIVES, SCORE

    print("=== 한글 단어 시한폭탄을 해체하라! ===")
    print(f"시작! 생명: {LIVES}, 점수: {SCORE}, 제한 시간: {TIME_LIMIT}초")
    
    while LIVES > 0:
        current_word = get_word()
        print("\n----------------------------------")
        print(f"다음 단어를 입력하세요: {current_word}")
        
        start_time = time.time()
        
        # Get user input with the time limit
        user_input = timed_input("입력: ", TIME_LIMIT)
        
        end_time = time.time()
        elapsed_time = end_time - start_time
        
        # Check if the user input was received (not timed out)
        if user_input is None:
            # Time out occurred (handled in timed_input)
            LIVES -= 1
            print(f"입력 시간 초과! 생명이 감소합니다. 남은 생명: {LIVES}")
        else:
            # Input received, check correctness and time
            user_input = user_input.strip()
            
            if user_input == current_word:
                if elapsed_time <= TIME_LIMIT:
                    # Correct and within time limit: increase score
                    SCORE += 10
                    print(f"정확합니다! (+10점). 현재 점수: {SCORE}")
                else:
                    # Correct but took too long (this scenario is unlikely if timed_input works perfectly, 
                    # but included for robustness)
                    LIVES -= 1
                    print(f"시간 초과! 생명이 감소합니다. 남은 생명: {LIVES}")
            else:
                # Incorrect word: decrease life
                LIVES -= 1
                print(f"틀렸습니다. 생명이 감소합니다. 남은 생명: {LIVES}")

    print("\n----------------------------------")
    print("게임 종료!")
    print(f"최종 점수: {SCORE}")

if __name__ == "__main__":
    game_loop()