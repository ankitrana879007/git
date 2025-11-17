import pyaudio
import wave
from openai import OpenAI

client = OpenAI(api_key="your_api_key_here")

def record_audio():
    chunk = 1024
    sample_format = pyaudio.paInt16
    channels = 1
    rate = 16000
    seconds = 5
    filename = "voice.wav"

    p = pyaudio.PyAudio()
    stream = p.open(format=sample_format, channels=channels, rate=rate,
                    input=True, frames_per_buffer=chunk)

    print("Speak now...")

    frames = []
    for _ in range(0, int(rate / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(filename, "wb")
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(rate)
    wf.writeframes(b"".join(frames))
    wf.close()

    return filename


def speech_to_text():
    audio_file = record_audio()

    with open(audio_file, "rb") as f:
        transcript = client.audio.transcriptions.create(
            model="gpt-4o-mini-tts",
            file=f
        )
    
    return transcript.text
