import speech_recognition as sr
import subprocess

# Dictionary to store app paths
app_commands = {
    "spotify": "C:\\Users\\91834\\AppData\\Local\\Microsoft\\WindowsApps\\Spotify.exe",
    "microsoft store": "explorer.exe ms-windows-store://",
    "telegram": "C:\\Users\\91834\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe",
    "whatsapp": "C:\\Users\\91834\\AppData\\Local\\WhatsApp\\WhatsApp.exe",
    "notepad": "notepad.exe",
    "youtube": "explorer.exe http://youtube.com",
    "file explorer": "explorer.exe",
    "mysql": r"C:\Program Files\MySQL\MySQL Workbench 8.0 CE\MySQLWorkbench.exe",
    "word": r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE",
    "excel": r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE",
    "player": r"C:\KMPlayer\KMPlayer.exe",
    "edge": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "system information": r"%windir%\system32\msinfo32.exe",
    "powerpoint": r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE",
    "firefox": r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe",
    "vlc": r"C:\Program Files (x86)\VideoLAN\VLC\vlc.exe",
}

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
        return ""
    except sr.RequestError:
        print("Network error.")
        return ""

def open_application(app_name):
    """Open an application based on the provided app name."""
    if app_name in app_commands:
        print(f"Opening {app_name}...")
        subprocess.Popen(app_commands[app_name], shell=True)
    else:
        print(f"Sorry, I can't open {app_name}.")

def confirm_and_open_application(command):
    """Ask for user confirmation and open the application if confirmed."""
    app = ""
    for key in app_commands.keys():
        if key in command:
            app = key
            break

    if app:
        confirmation = input(f"Do you want to open {app}? Type 'yes' or 'no': ").strip().lower()
        if confirmation == "yes":
            open_application(app)
        else:
            print("Canceled.")
    else:
        print("No recognizable application in the command.")

def main():
    while True:  # Keep asking until the user says 'stop'
        print("Say an application name to open (e.g., 'Spotify', 'Microsoft Store', 'WhatsApp', 'Notepad', 'Telegram', 'YouTube', 'File Explorer', 'MySQL', 'Word', 'Excel', etc.) or say 'stop' to end.")
        command = recognize_speech()
        if command == "stop":
            print("Stopping the voice assistant.")
            break
        if command:
            confirm_and_open_application(command)

if __name__ == "__main__":
    main()
