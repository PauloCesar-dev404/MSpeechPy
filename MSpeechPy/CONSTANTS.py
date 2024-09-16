import os

DIR_LIB = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE = os.path.join(DIR_LIB, 'section', 'auth_config.json')
TK_USER_SECTION = os.path.join(DIR_LIB, 'section', 'tokens_updater')

FORMATS = {
    8000: 'riff-8khz-8bit-mono-mulaw',
    16000: 'riff-16khz-16bit-mono-pcm, audio-16khz-128kbitrate-mono-mp3',
    24000: 'riff-24khz-16bit-mono-pcm, audio-24khz-96kbitrate-mono-mp3',
    48000: 'riff-48khz-16bit-mono-pcm, audio-48khz-192kbitrate-mono-mp3'
}
