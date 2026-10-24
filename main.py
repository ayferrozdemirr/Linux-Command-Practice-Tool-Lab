import json
import os

def load_questions(filename="questions.json"):
    if not os.path.exists(filename):
        print(f"Hata: '{filename}' dosyası bulunamadı!")
        return []
    
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)

def run_quiz():
    questions = load_questions()
    if not questions:
        return

    score = 0
    total_questions = len(questions)

    print("=" * 40)
    print("  Linux Command Practice Tool Lab")
    print("=" * 40)
    print("Sorulara A, B, C veya D şeklinde cevap veriniz.\n")

    for index, q in enumerate(questions, start=1):
        print(f"Soru {index}/{total_questions}: {q['question']}")
        for key, value in q["options"].items():
            print(f"  {key}) {value}")
        
        user_answer = input("\nCevabınız: ").strip().upper()
        
        if user_answer == q["answer"]:
            print(" Doğru!\n")
            score += 1
        else:
            print(f" Yanlış! Doğru cevap: {q['answer']}\n")

    print("-" * 40)
    print(f"Test Bitti! Toplam Skorunuz: {score} / {total_questions}")
    percentage = (score / total_questions) * 100
    print(f"Başarı Oranı: %{percentage:.1f}")
    print("-" * 40)

if __name__ == "__main__":
    run_quiz()