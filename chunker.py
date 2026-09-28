"""
Stage 2 of the pipeline: splitting documents into chunks.

⚠️ THIS IS THE FILE YOU CHANGE IN MILESTONE 3.

`split_documents` below is deliberately plain. It cuts every document into
fixed-size pieces with a fixed overlap and pays no attention to where sentences
or paragraphs end. It works, and it is not good.

On a corpus of short posts it may not cut anything at all: `campus_life` comes
out as 88 documents and 88 chunks, because almost nothing in it reaches 800
characters. That is the baseline, not a bug — Milestone 3 is where you decide
whether one post should stay one chunk.

Your job in Milestone 3 is to replace the *body* of `split_documents` with a
strategy that fits the documents you actually read in Milestone 1. Keep the
name and the shape of what it returns — the rest of the pipeline calls it, and
your README has to name the function that produced your chunks.

If you get stuck for 30 minutes, `fallback_split` is the original. Switch back
to it, write down what you saw, and move on. That's a real observation about
your pipeline, not giving up.
"""

import re
from dataclasses import dataclass

import config
from ingest import Document


@dataclass
class Chunk:
    """One piece of one document."""

    text: str
    source: str        # which file it came from
    index: int         # which chunk within that file, starting at 0
    produced_by: str   # the function that made it — cite this in your README

    @property
    def label(self) -> str:
        return f"{self.source}#{self.index}"


def fallback_split(
    documents: list[Document],
    chunk_size: int | None = None,
    overlap: int | None = None,
) -> list[Chunk]:
    """
    The starter's original chunker. Fixed-size character windows with overlap.

    Keep this function. Milestone 3's stop rule points back at it, and having
    something to compare your own strategy against is useful in unit 2.
    """
    chunk_size = chunk_size or config.CHUNK_SIZE
    overlap = overlap or config.CHUNK_OVERLAP

    if overlap >= chunk_size:
        raise ValueError("overlap has to be smaller than chunk_size")

    chunks: list[Chunk] = []
    for doc in documents:
        start = 0
        index = 0
        while start < len(doc.text):
            piece = doc.text[start : start + chunk_size].strip()
            if piece:
                chunks.append(
                    Chunk(
                        text=piece,
                        source=doc.source,
                        index=index,
                        produced_by="chunker.py::fallback_split",
                    )
                )
                index += 1
            start += chunk_size - overlap

    return chunks


def _extract_heading(text: str) -> str:
    """Return the first markdown or bold title inside a chunk, if present."""
    for line in text.splitlines():
        cleaned = line.strip()
        if not cleaned:
            continue
        if cleaned.startswith("#"):
            return re.sub(r"^#+\s*", "", cleaned).strip("*_`").lower()
        match = re.search(r"\*\*(.+?)\*\*", cleaned)
        if match:
            return match.group(1).strip().lower()
    return ""


def _titles_are_related(left: str, right: str) -> bool:
    """Treat nearby section titles as related when they share a topic keyword."""
    if not left or not right:
        return False
    left_norm = left.lower().strip()
    right_norm = right.lower().strip()
    if left_norm == right_norm:
        return True
    if left_norm in right_norm or right_norm in left_norm:
        return True

    stop_words = {
        "the", "and", "for", "with", "from", "into", "about", "your",
        "what", "when", "where", "how", "there", "around", "local",
    }
    left_words = {
        word for word in re.findall(r"[a-z]+", left_norm)
        if len(word) > 2 and word not in stop_words
    }
    right_words = {
        word for word in re.findall(r"[a-z]+", right_norm)
        if len(word) > 2 and word not in stop_words
    }
    if not left_words or not right_words:
        return False
    return bool(left_words & right_words)


def _split_sections(text: str) -> list[tuple[str, str]]:
    """Break a document into heading-led sections to preserve the document's shape."""
    sections: list[tuple[str, str]] = []
    title = ""
    body: list[str] = []

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            if title:
                body.append("")
            continue

        if re.match(r"^(#{1,6}\s+.+|\*\*.+?\*\*)$", line):
            if title or body:
                sections.append((title.strip(), "\n".join(body).strip()))
            title = re.sub(r"^#+\s*|\*\*|\*\*$", "", line).strip("*_`")
            body = []
            continue

        body.append(raw_line)

    if title or body:
        sections.append((title.strip(), "\n".join(body).strip()))

    return [section for section in sections if section[0] or section[1]]


def split_documents(documents: list[Document]) -> list[Chunk]:
    """
    Split documents into chunks without losing the structure of short posts or
    long sectioned guides.

    The behaviour is intentionally section-aware rather than fixed-width only:

      - Tiny posts stay whole; they are more useful as one chunk than half a
        thought.
      - Long posts still use the fallback window as a baseline so they break up
        before a document turns into one giant chunk.
      - Related section titles share their overlap, which keeps neighbouring
        material together when the next heading is part of the same topic.

    Keep the `produced_by` string set to "chunker.py::split_documents" so the
    README and outputs accurately name the generator.
    """
    chunks: list[Chunk] = []

    for doc in documents:
        if not doc.text or not doc.text.strip():
            continue

        if len(doc.text) <= config.CHUNK_SIZE:
            chunks.append(
                Chunk(
                    text=doc.text.strip(),
                    source=doc.source,
                    index=0,
                    produced_by="chunker.py::split_documents",
                )
            )
            continue

        sections = _split_sections(doc.text)
        merged_sections: list[str] = []
        index = 0

        while index < len(sections):
            title, body = sections[index]
            text = (f"## {title}\n{body}" if title else body).strip()

            if index + 1 < len(sections):
                next_title, next_body = sections[index + 1]
                next_text = (f"## {next_title}\n{next_body}" if next_title else next_body).strip()
                if _titles_are_related(title.lower(), next_title.lower()):
                    overlap = next_text[: config.CHUNK_OVERLAP].strip()
                    if overlap:
                        merged_sections.append((text + "\n\n" + overlap).strip())
                        index += 2
                        continue

            merged_sections.append(text)
            index += 1

        doc_index = 0
        for section_text in merged_sections:
            if len(section_text) <= config.CHUNK_SIZE:
                chunks.append(
                    Chunk(
                        text=section_text.strip(),
                        source=doc.source,
                        index=doc_index,
                        produced_by="chunker.py::split_documents",
                    )
                )
                doc_index += 1
                continue

            for chunk in fallback_split(
                [Document(doc.source, section_text)],
                chunk_size=config.CHUNK_SIZE,
                overlap=config.CHUNK_OVERLAP,
            ):
                chunks.append(
                    Chunk(
                        text=chunk.text,
                        source=doc.source,
                        index=doc_index,
                        produced_by="chunker.py::split_documents",
                    )
                )
                doc_index += 1

    return chunks


def describe(chunks: list[Chunk]) -> str:
    """A one-line summary, printed after indexing."""
    if not chunks:
        return "0 chunks"
    lengths = [len(c.text) for c in chunks]
    return (
        f"{len(chunks)} chunks, "
        f"{sum(lengths) // len(lengths)} characters on average "
        f"(shortest {min(lengths)}, longest {max(lengths)}), "
        f"produced by {chunks[0].produced_by}"
    )


if __name__ == "__main__":
    from ingest import load_documents

    chunks = split_documents(load_documents())
    print(describe(chunks))
