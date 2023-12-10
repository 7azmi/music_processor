import librosa
import numpy as np
import simpleaudio as sa
import time
import threading

def map_note_to_key(frequency):
    # Mapping frequencies to piano key numbers
    if frequency is not None:
        piano_key = 12 * np.log2(frequency / 440.0) + 49
        keys = 'asdfghjkl;'
        return keys[int(piano_key - 21) % len(keys)] if 21 <= piano_key <= 108 else None
    return None

def process_wav_file(file_path):
    y, sr = librosa.load(file_path)
    # Using a harmonic percussive source separation to better detect pitches
    y_harmonic, y_percussive = librosa.effects.hpss(y)
    pitches, magnitudes = librosa.piptrack(y=y_harmonic, sr=sr)

    with open('output.txt', 'w') as output_file:
        for t in range(pitches.shape[1]):
            index = magnitudes[:, t].argmax()
            pitch = pitches[index, t]
            if pitch > 0:
                key = map_note_to_key(pitch)
                if key:
                    intensity = magnitudes[index, t]
                    output_file.write(f"{t}: {key}, {intensity}\n")

# Example usage


def read_data(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return [line.strip() for line in data]


#process_wav_file('8-bit Franz Liszt - Hungarian Rhapsody No.2.wav')
