import simpleaudio as sa

def success():
    a = sa.WaveObject.from_wave_file("/Users/karthikrajatp/Desktop/filesystem/sounds/short-success.wav")
    a.play()

def warning():
    a = sa.WaveObject.from_wave_file("/Users/karthikrajatp/Desktop/filesystem/sounds/notify.wav")
    a.play()

def error():
    a = sa.WaveObject.from_wave_file("/Users/karthikrajatp/Desktop/filesystem/sounds/nvebeeps.wav")
    a.play()

