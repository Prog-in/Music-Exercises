from pathlib import Path


WINDOW_TITLE = "Music Exercises"
WINDOW_WIDTH = 720
WINDOW_HEIGHT = 480

MEDIA_DIR = Path(__file__).absolute().parent.parent.parent / "media"
RAW_DIR = MEDIA_DIR / "raw"
NOTES_DIR = MEDIA_DIR / "notes"

MEDIA_SUFFIXES = [".pdf", ".jpg", ".jpeg", ".png"]

C_MAJOR = ["C", "D", "E", "F", "G", "A", "B"]

CLEFS = {
    "TREBLE": {
        "notes": [""]
    },
    "BASS": {
        "notes": [
            "Fb1", "F1", "Fs1", "Gb1", "G1", "Gs1", "Ab1", "A1", "As1", 
            "Bb1", "B1", "Bs1", "Cb2", "C2", "Cs2", "Db2", "D2", "Ds2", 
            "Eb2", "E2", "Es2", "Fb2", "F2", "Fs2", "Gb2", "G2", "Gs2",
            "Ab2", "A2", "As2", "Bb2", "B2", "Bs2", "Cb3", "C3", "Cs3", 
            "Db3", "D3", "Ds3", "Eb3", "E3", "Es3", "Fb3", "F3", "Fs3", 
            "Gb3", "G3", "Gs3", "Ab3", "A3", "As3", "Bb3", "B3", "Bs3", 
            "Cb4", "C4", "Cs4", "Db4", "D4", "Ds4", "Eb4", "E4", "Es4",
            "Fb4", "F4", "Fs4", "Gb4", "G4", "Gs4", "Ab4", "A4", "As4", 
            "Bb4", "B4", "Bs4", "Cb5", "C5", "Cs5",
        ]
    }
}
