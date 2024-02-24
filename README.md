# tennis-auto-score

Tennis scoring app using speech recognition.

## Setting
Device setting is required to detect voice with microphone.

Windows

Follow "Step 2 : Enable Stereo Mixer" in below article.

https://shankhanilborthakur.medium.com/recording-system-audio-in-windows-10-using-pyaudio-1559f3e1b64f

## Requirement
Currently, Dockerfile does not work, so install the packages manually.
```shell
apt-get install libasound-dev libportaudio2 libportaudiocpp0 portaudio19-dev -y
apt install espeak
pip install PyAudio
pip install SpeechRecognition
pip install pyttsx3
```

## Run

```shell
python main.py
```

## Run
- Say "Play" to start a match.
- Say "1" or "2" to select who is serving first.
- Call the score after each point. e.g. 15-love, 40-30. Alternatively, you can say "1" or "2" for whoever won the point.
- Say "Game" if a game is won.
- Say "Cancel" to undo a previous call.

## Future work
### Scoring features
- Tie-breaker
- Enable to select match format, e.g. 3-sets / 5-sets
- Web app for better visualization
