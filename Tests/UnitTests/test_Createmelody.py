import CreateMelody
from PlayMelody import playMelody
import __main__
import ast
from mock import patch
import os
import pysynth
import pysynth as ps
import sys
import unittest
import wave


class CreatemelodyTest(unittest.TestCase):
    @patch.object(pysynth, 'make_wav')
    def test_createMelody(self, mock_make_wav):
        mock_make_wav.return_value = None
        self.assertEqual(
            __main__.createMelody(song=(('a3', 4), ('b3', 4), ('c4', 4), ('d4', 4)),timing=4,outputSongFileName='testSong.wav'),
            None
        )


    def test_main(self):
        self.assertEqual(
            __main__.main(),
            None
        )


    def test_remove_dup(self):
        self.assertEqual(
            __main__.remove_dup(noteList=('a3', 4)),
            ['a3', 4]
        )


if __name__ == "__main__":
    unittest.main()
