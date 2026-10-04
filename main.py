import PyPDF2
import edge_tts
import asyncio
import os


async def create_audio():

    book = open("OOP.pdf", "rb")
    pdfReader = PyPDF2.PdfReader(book)

    pages = len(pdfReader.pages)

    print("Total pages:", pages)

    # Har page ka audio create karo
    for num in range(pages):

        print(f"Creating audio for page {num + 1}/{pages}")

        page = pdfReader.pages[num]
        text = page.extract_text()

        if text and text.strip():

            filename = f"page_{num + 1}.mp3"

            communicate = edge_tts.Communicate(
                text.strip(),
                "en-US-AriaNeural",
                rate="+30%"
            )

            await communicate.save(filename)

    book.close()

    print("\nAll pages converted to audio.")
    print("Now opening audio...")


asyncio.run(create_audio())