import wave

def em_audio(af, string, output):
    try:
        print("Please wait...")
        waveaudio = wave.open(af, mode='rb')
        frame_bytes = bytearray(list(waveaudio.readframes(waveaudio.getnframes())))
        string = string + int((len(frame_bytes)-(len(string)*8*8))/8) *'#'
        bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in string])))
        for i, bit in enumerate(bits):
            frame_bytes[i] = (frame_bytes[i] & 254) | bit
        frame_modified = bytes(frame_bytes)
        with wave.open(output, 'wb') as fd:
            fd.setparams(waveaudio.getparams())
            fd.writeframes(frame_modified)
        waveaudio.close()
        print("Done...")
    except Exception as e:
        print("Something went wrong:", e)

# Input values (audio file, secret message, output file)
audio_file_path = 'Demo.wav'  # Specify the path to your audio file
secret_message = 'Code RED!'  # Your secret message here
output_file_path = 'outpiut_audio_stego.wav'  # Specify the desired output path

# Call the function with the provided inputs
em_audio(audio_file_path, secret_message, output_file_path)
