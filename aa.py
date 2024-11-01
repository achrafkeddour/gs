# Install the TTS library from Coqui
!pip install TTS

from TTS.utils.synthesizer import Synthesizer

# Load a pre-trained model from Coqui TTS
synthesizer = Synthesizer.from_pretrained("tts_models/en/ljspeech/tacotron2-DDC")

# Generate audio for text with a synthetic voice (Note: does not clone voices directly)
text = "Hello AI, hello Python!"
wav = synthesizer.tts(text)
synthesizer.save_wav(wav, "output.wav")