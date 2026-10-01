import unittest

from chunker import split_documents
from ingest import Document


class SplitDocumentsTests(unittest.TestCase):
    CHUNK_SIZE = 120
    CHUNK_OVERLAP = 30

    def test_split_documents_keeps_whole_short_post(self):
        doc = Document("short_post.txt", "A short post with no need to split.")

        chunks = split_documents(
            [doc], chunk_size=self.CHUNK_SIZE, overlap=self.CHUNK_OVERLAP
        )

        self.assertEqual(len(chunks), 1)
        self.assertEqual(chunks[0].text, doc.text)
        self.assertEqual(chunks[0].source, doc.source)
        self.assertEqual(chunks[0].produced_by, "chunker.py::split_documents")

    def test_split_documents_creates_partial_chunks_for_long_posts(self):
        text = ("This is a longer post. " * 30)

        chunks = split_documents(
            [Document("long_post.txt", text)],
            chunk_size=self.CHUNK_SIZE,
            overlap=self.CHUNK_OVERLAP,
        )

        self.assertGreater(len(chunks), 1)
        self.assertTrue(all(chunk.text.strip() for chunk in chunks))
        self.assertTrue(all(chunk.produced_by == "chunker.py::split_documents" for chunk in chunks))

    def test_split_documents_merges_related_sections(self):
        text = (
            "## Getting there\n"
            "The train runs every hour and reaches the station on time.\n\n"
            "## Getting around\n"
            "The local bus is regular and the river walk is easy to follow.\n\n"
            "## Eat and drink\n"
            "The market is lively and the riverside strip is affordable.\n"
        )

        chunks = split_documents(
            [Document("related_sections.txt", text)],
            chunk_size=self.CHUNK_SIZE,
            overlap=self.CHUNK_OVERLAP,
        )

        merged_text = "\n".join(chunk.text for chunk in chunks)
        self.assertIn("Getting there", merged_text)
        self.assertIn("Getting around", merged_text)
        self.assertTrue(any("Getting there" in chunk.text and "Getting around" in chunk.text for chunk in chunks))

    def test_split_documents_skips_empty_documents(self):
        chunks = split_documents([
            Document("empty.txt", ""),
            Document("real.txt", "A real post that should survive chunking."),
        ], chunk_size=self.CHUNK_SIZE, overlap=self.CHUNK_OVERLAP)

        self.assertTrue(all(chunk.text.strip() for chunk in chunks))
        self.assertTrue(all(chunk.produced_by == "chunker.py::split_documents" for chunk in chunks))
        self.assertEqual(len(chunks), 1)

    def test_split_documents_rejects_incorrect_chunks(self):
        text = ("This is a longer post. " * 30)

        chunks = split_documents(
            [Document("incorrect_chunk.txt", text)],
            chunk_size=self.CHUNK_SIZE,
            overlap=self.CHUNK_OVERLAP,
        )

        self.assertTrue(all(chunk.text.strip() for chunk in chunks))
        self.assertTrue(all(chunk.source for chunk in chunks))
        self.assertTrue(all(chunk.produced_by == "chunker.py::split_documents" for chunk in chunks))


if __name__ == "__main__":
    unittest.main()
