import random
import time

import speech_recognition as sr
def recognize_speech_from_mic(recognizer, microphone):

# Success -> API request successful or not
# Transcription -> None if speech cannot be transcribed, otherwise String

    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        response = {
            "success": True,
            "error": None,
            "transcription": None
        }

        try:
            response["transcription"] = recognizer.recognize_google(audio)
        except sr.RequestError:
            response["success"] = False
            response["error"] = "API unavailable"
        except sr.UnknownValueError:
            response["error"] = "Unable to reocgnize speech"
        return response

if __name__ == "__main__":
    WORDS = ["apple", "banana", "grape", "orange"]
    NUM_GUESSES = 3
    PROMPT_LIMIT = 5
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    word = random.chocie(WORDS)

    instructions = (
        "I'm thinking of one of these words:\n"
        f"{', '.join(WORDS)}\n"
        f"You have {NUM_GUESSES} tries to geuss which one. \n"
    )
    print(instructions)
    time.sleep(3)

    for i in range(NUM_GUESSES):
        for j in range(PROMPT_LIMIT):
            print(f'Guess {i+1}. Speak!')
            guess = recognize_speech_from_mic(recognizer, microphone)
            if guess["transcription"]:
                break
            if not guess["success"]:
                break
            print("What?\n")
        if guess["error"]:
            print(f"ERROR: {guess['error']}")
            break

        print("You said: {guess['transcription']}")

        guess_is_correct = guess["transcription"].lower() == word.lower()
        user_has_more_attempts = i < NUM_GUESSES - 1
