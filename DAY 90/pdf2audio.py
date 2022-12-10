import pyttsx3
import pdfplumber

P_D_F = "./test.pdf"

with pdfplumber.open(P_D_F)as pdf:
    content = ""
    speaker = pyttsx3.init()
    speaker.setProperty('rate', 130)
    voices = speaker.getProperty('voices')
    speaker.setProperty('voice', voices[1].id)
    for page in pdf.pages:
        text = page.extract_text()
        if text is not None:
            content += text
    mp3_name = input("Enter mp3 file name:\t")
    speaker.save_to_file(content, f"{mp3_name}.mp3")
    speaker.runAndWait()