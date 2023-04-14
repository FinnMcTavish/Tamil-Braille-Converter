import PIL
import easyocr
from PIL import ImageDraw

braille_map = {
    "அ": "⠁",
    "ஆ": "⠜",
    "இ": "⠊",
    "ஈ": "⠔",
    "உ": "⠥",
    "ஊ": "⠳",
    "எ": "⠢",
    "ஏ": "⠑",
    "ஐ": "⠌",
    "ஒ": "⠭",
    "ஓ": "⠕",
    "ஔ": "⠪",
    "க": "⠅",
    "ங": "⠬",
    "ச": "⠉",
    "ஞ": "⠒",
    "ட": "⠾",
    "ண": "⠼",
    "த": "⠞",
    "ந": "⠝",
    "ப": "⠏",
    "ம": "⠍",
    "ய": "⠽",
    "ர": "⠗",
    "ல": "⠇",
    "வ": "⠧",
    "ழ": "⠷",
    "ள": "⠸",
    "ற": "⠻",
    "ன": "⠰",
    "ஜ": "⠚",
    "ஷ": "⠯",
    "ஸ": "⠎",
    "ஹ": "⠓",
    "்": "⠈",
    "ஃ": "⠠",
    'ா':"⠜",
    'ி':"⠊",
    'ீ':"⠔",
    'ு':"⠥",
    'ூ':"⠳",
    'ெ':"⠢",
    'ே':"⠑",
    'ை':"⠌",
    'ொ':"⠭",
    'ோ':"⠪",
    'ௌ':"⠪",
    ' ':" ",
    ",":"⠂",
    ";":"⠆",
    ":":"⠒",
    "!":"⠖",
    "?":"⠦",
    '.':"⠲"
}

num_map = {
    "0":"⠚",
    "1":"⠁",
    "2":"⠃",
    "3":"⠉",
    "4":"⠙",
    "5":"⠑",
    "6":"⠋",
    "7":"⠛",
    "8":"⠓",
    "9":"⠊",
}


def tamil_to_braille(text):
    # Convert each Tamil letter to its corresponding Braille symbol
    braille = ""
    for letter in text:
        braille += braille_map.get(letter, letter)
    return braille


def braille_to_tamil(text):
    tamil_vowels = ['அ', 'ஆ', 'இ', 'ஈ', 'உ', 'ஊ', 'எ', 'ஏ', 'ஐ', 'ஒ', 'ஓ', 'ஔ']
    tamil = ""
    for i in range(len(text)):
        letter = text[i]
        if letter == "⠼":
            i += 1
            letter = text[i]
            for k, v in num_map.items():
                if v == letter:
                    tamil += k
                    break
            continue
        for k, v in braille_map.items():
            if v == letter:
                if k in tamil_vowels:
                    if i == 0 or text[i-1] == ' ':
                        tamil += k
                        break
                else:
                    tamil += k
                    break
    return tamil


def tamil_OCR(filename):
    im = PIL.Image.open("uploads/"+filename)
    reader = easyocr.Reader(['ta','en'])
    words = reader.readtext("uploads/"+filename)
    extract = ""
    for word in words:
        extract += word[1]
    return tamil_to_braille(extract)

# def main():
#     text = "காடுகள் எங்கள் உயிரினத்தை பாதுகாக்கும் முக்கியமான பெருமையுள்ளன. காட்டுகள் நம் சூழலில் அதிக பங்களிப்புக்கு காரணமாக இருக்கின்றன. காட்டுகள் பெரும்பாலும் அரசியல் கட்டளைகளை சார்ந்து உருவாக்கப்பட்டிருக்கும். ஆனால் காட்டுகள் மாறுபாடு, கடல் உயிரினங்களின் தேய்த்துவம் முதலியவற்றினால் குறைந்து வருகின்றன"
#     braille = tamil_to_braille(text)
#     print(braille)
#     print("\n")
#     tamil = braille_to_tamil(braille)
#     print(tamil)
#     print("\n")
    
#     extract = (tamil_OCR('testdata\CSKvsMI'))
#     print(extract)
#     print(tamil_to_braille(extract))

# if __name__ == "__main__":
#     main()
