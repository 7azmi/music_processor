import simpleaudio as sa
import threading
import time


def play_music(file_path):
    wave_obj = sa.WaveObject.from_wave_file(file_path)
    play_obj = wave_obj.play()
    return play_obj


def simulate_keystrokes(notes, play_obj):
    # Assuming 'notes' is a list of tuples (note, start_time)
    start_time = time.time()
    for note, note_start_time in notes:
        # Wait for the right time to 'press' the key
        time.sleep(max(0, note_start_time - (time.time() - start_time)))
        if not play_obj.is_playing():
            break
        print(f"Simulated keystroke for note: {note}")


def main():
    # Replace with the path to your music file
    music_file_path = '8-bit Franz Liszt - Hungarian Rhapsody No.2.wav'

    # Replace this with your sequence of notes and their start times
    notes = [('C', 0), ('E', 1), ('G', 2)]  # Example: [('Note', start_time_in_seconds), ...]

    play_obj = play_music(music_file_path)

    # Start the keystroke simulation in a separate thread
    threading.Thread(target=simulate_keystrokes, args=(notes, play_obj)).start()



main()
