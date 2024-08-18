from PyPDF2 import PdfWriter, PdfReader
from pathlib import Path
from PIL import Image
from typing import Generator
from utils.constants import RAW_DIR, NOTES_DIR, MEDIA_SUFFIXES


def _cropPDF(filePath: Path, outputDir: Path) -> None:
    """
    Crops a pdf file with path *filePath* and puts it with the same file name in the
    *outputDir*
    """
    if not filePath.is_file() or not outputDir.is_dir():
        return

    fileName = filePath.name
    outputFile = outputDir / fileName

    reader = PdfReader(filePath)
    page = reader.pages[0]

    # (x, y) dimensions:
    # page.cropbox.lower_left = (0, 0)
    # page.cropbox.upper_right = (612, 792)
    # page.cropbox.lower_left = (17, 642)
    # page.cropbox.upper_right = (200, 770)

    midPoint = (108, 707)
    recHeight = 70
    recWidth = 120
    # (16, 732)
    page.cropbox.lower_left = (
        abs(midPoint[0] - recWidth // 2),
        abs(midPoint[1] - recHeight // 2),
    )
    page.cropbox.upper_right = (
        abs(midPoint[0] + recWidth // 2),
        abs(midPoint[1] + recHeight // 2),
    )

    writer = PdfWriter()
    writer.add_page(page)

    with open(outputFile, "wb") as fd:
        writer.write(fd)


def _cropIMG(filePath: Path, outputDir: Path) -> None:
    """
    Crops a image file with path *filePath* and puts it with the same file name in the
    *outputDir*
    """
    if not filePath.is_file() or not outputDir.is_dir():
        return

    fileName = filePath.name
    outputFile = outputDir / fileName

    midPoint = (305, 245) # (x, y)
    recHeight = 230
    recWidth = 270

    # left, top, right, bottom
    area = (
        midPoint[0] - recWidth // 2,
        midPoint[1] - recHeight // 2,
        midPoint[0] + recWidth // 2,
        midPoint[1] + recHeight // 2,
    )
    img = Image.open(filePath)
    img.crop(area).save(outputFile)


def _getMusicNotesFromDir(inputDir: Path, outputDir: Path) -> None:
    outputDir.mkdir(parents=True, exist_ok=True)

    for file in inputDir.iterdir():
        if file.is_file():
            name = file.name.lower()
            for suffix in MEDIA_SUFFIXES:
                if name.endswith(suffix):
                    if suffix == ".pdf":
                        _cropPDF(file, outputDir)
                    else:
                        _cropIMG(file, outputDir)
                    break


def renameFiles(sourceDir: Path, origPat: str, newPat: str) -> None:
    for file in sourceDir.glob("*.pdf"):
        if file.is_file():
            new_name = file.name.replace(origPat, newPat)
            file.rename(file.parent / new_name)


def getFilesEndingWithSuffixes(sourceDir: Path, suffixes: list[str]) -> Generator[Path, None, None]:
    for file in sourceDir.iterdir():
        if file.is_file():
            name = file.name.lower()
            if any(name.endswith(suffix) for suffix in suffixes):
                yield file


def getMusicNotes():
    for child in RAW_DIR.iterdir():
        if child.is_dir:
            _getMusicNotesFromDir(child, NOTES_DIR / child.name)
