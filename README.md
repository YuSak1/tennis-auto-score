# tennis-auto-score

Tennis scoring app using speech recognition.

## Setting
Microphone settin is required to detect voice.

Windows

Follow "Step 2 : Enable Stereo Mixer" in below article.

https://shankhanilborthakur.medium.com/recording-system-audio-in-windows-10-using-pyaudio-1559f3e1b64f

## Run

```shell
python main.py
```

## Run
- Say "Play" to start a match.
- Say "1" or "2" to select who is serving first.
- Call the score after each point. e.g. 15-love, 40-30. Alternatively, you can say "1" or "2" for whoever won the point.
- Say "Game" if a game is won.
- Say "Cancel" to undo a call.

## Future work
### Scoring functions
- Tie-breaker
- Enable to select match format, e.g. 3-sets or 5-sets
- Web app for better visualization
