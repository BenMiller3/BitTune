import Lexer
from Lexer import Lexer
import __main__
import __main__
import _bootlocale
import ast
import codecs
from codecs import IncrementalEncoder
from mock import patch
import unittest


class LexerTest(unittest.TestCase):
    def test_<listcomp>(self):
        self.assertEqual(
            __main__.<listcomp>(.0=<range_iterator object at 0x7f3003278d50>),
            [['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'D'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'C', 'R', 'R'], ['R', 'F', 'R', 'R'], ['R', 'C', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'B', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R']]
        )


    def test_colour_midpoints(self):
        self.assertEqual(
            Lexer.colour_midpoints(self=<__main__.Lexer object at 0x7f3004547550>),
            None
        )


    def test_colour_to_note(self):
        self.assertEqual(
            Lexer.colour_to_note(self=<__main__.Lexer object at 0x7f3004547550>,colour='violet'),
            'G'
        )


    def test_compose_song(self):
        self.assertEqual(
            Lexer.compose_song(self=<__main__.Lexer object at 0x7f3004547550>),
            [['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'D'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'C', 'R', 'R'], ['R', 'F', 'R', 'R'], ['R', 'C', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'B', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'R']]
        )


    def test_get_midpoints(self):
        self.assertEqual(
            Lexer.get_midpoints(self=<__main__.Lexer object at 0x7f3004547550>),
            [[387.0, 147.0, 'A'], [388.0, 147.0, 'A'], [389.0, 147.0, 'A'], [390.0, 147.0, 'A'], [392.0, 147.0, 'A'], [391.0, 147.0, 'A'], [398.0, 136.0, 'E'], [397.0, 136.0, 'E'], [397.0, 138.0, 'E'], [396.0, 139.0, 'E'], [396.0, 140.0, 'E'], [396.0, 141.0, 'E'], [396.0, 142.0, 'E'], [395.0, 142.0, 'E'], [395.0, 143.0, 'E'], [395.0, 144.0, 'E'], [395.0, 145.0, 'E'], [395.0, 146.0, 'E'], [394.0, 147.0, 'E'], [394.0, 146.0, 'E'], [405.0, 157.0, 'C'], [404.0, 157.0, 'C'], [403.0, 157.0, 'C'], [402.0, 158.0, 'C'], [400.0, 158.0, 'C'], [399.0, 158.0, 'C'], [398.0, 158.0, 'C'], [397.0, 158.0, 'C'], [395.0, 159.0, 'C'], [394.0, 159.0, 'C'], [392.0, 158.0, 'C'], [391.0, 158.0, 'C'], [386.0, 156.0, 'C'], [383.0, 154.0, 'C'], [382.0, 154.0, 'C'], [380.0, 153.0, 'C'], [380.0, 152.0, 'C'], [379.0, 152.0, 'C'], [378.0, 152.0, 'C'], [378.0, 151.0, 'C'], [378.0, 150.0, 'C'], [377.0, 149.0, 'C'], [377.0, 147.0, 'C'], [377.0, 146.0, 'C'], [375.0, 144.0, 'C'], [375.0, 143.0, 'C'], [375.0, 140.0, 'C'], [375.0, 139.0, 'C'], [375.0, 137.0, 'C'], [375.0, 136.0, 'C'], [375.0, 134.0, 'C'], [375.0, 133.0, 'C'], [376.0, 132.0, 'C'], [376.0, 131.0, 'C'], [376.0, 130.0, 'C'], [375.0, 130.0, 'C'], [388.0, 158.0, 'C'], [388.0, 157.0, 'C'], [389.0, 151.0, 'G'], [383.0, 149.0, 'F'], [582.0, 156.0, 'B'], [583.0, 155.0, 'B'], [31.0, 304.0, 'D']]
        )


    def test_main(self):
        self.assertEqual(
            __main__.main(),
            None
        )


    def test_remove_duplicates(self):
        self.assertEqual(
            Lexer.remove_duplicates(self=<__main__.Lexer object at 0x7f3004547550>),
            [[382, 392, 142, 152, 'red'], [383, 393, 142, 152, 'red'], [384, 394, 142, 152, 'red'], [385, 395, 142, 152, 'red'], [387, 397, 142, 152, 'red'], [386, 396, 142, 152, 'red'], [393, 403, 131, 141, 'blue'], [392, 402, 131, 141, 'blue'], [392, 402, 133, 143, 'blue'], [391, 401, 134, 144, 'blue'], [391, 401, 135, 145, 'blue'], [391, 401, 136, 146, 'blue'], [391, 401, 137, 147, 'blue'], [390, 400, 137, 147, 'blue'], [390, 400, 138, 148, 'blue'], [390, 400, 139, 149, 'blue'], [390, 400, 140, 150, 'blue'], [390, 400, 141, 151, 'blue'], [389, 399, 142, 152, 'blue'], [389, 399, 141, 151, 'blue'], [400, 410, 152, 162, 'yellow'], [399, 409, 152, 162, 'yellow'], [398, 408, 152, 162, 'yellow'], [397, 407, 153, 163, 'yellow'], [395, 405, 153, 163, 'yellow'], [394, 404, 153, 163, 'yellow'], [393, 403, 153, 163, 'yellow'], [392, 402, 153, 163, 'yellow'], [390, 400, 154, 164, 'yellow'], [389, 399, 154, 164, 'yellow'], [387, 397, 153, 163, 'yellow'], [386, 396, 153, 163, 'yellow'], [381, 391, 151, 161, 'yellow'], [378, 388, 149, 159, 'yellow'], [377, 387, 149, 159, 'yellow'], [375, 385, 148, 158, 'yellow'], [375, 385, 147, 157, 'yellow'], [374, 384, 147, 157, 'yellow'], [373, 383, 147, 157, 'yellow'], [373, 383, 146, 156, 'yellow'], [373, 383, 145, 155, 'yellow'], [372, 382, 144, 154, 'yellow'], [372, 382, 142, 152, 'yellow'], [372, 382, 141, 151, 'yellow'], [370, 380, 139, 149, 'yellow'], [370, 380, 138, 148, 'yellow'], [370, 380, 135, 145, 'yellow'], [370, 380, 134, 144, 'yellow'], [370, 380, 132, 142, 'yellow'], [370, 380, 131, 141, 'yellow'], [370, 380, 129, 139, 'yellow'], [370, 380, 128, 138, 'yellow'], [371, 381, 127, 137, 'yellow'], [371, 381, 126, 136, 'yellow'], [371, 381, 125, 135, 'yellow'], [370, 380, 125, 135, 'yellow'], [383, 393, 153, 163, 'yellow'], [383, 393, 152, 162, 'yellow'], [384, 394, 146, 156, 'violet'], [378, 388, 144, 154, 'indigo'], [577, 587, 151, 161, 'orange'], [578, 588, 150, 160, 'orange'], [26, 36, 299, 309, 'green']]
        )


    @patch.object(IncrementalEncoder, '__init__')
    @patch.object(_bootlocale, 'getpreferredencoding')
    def test_write_song_to_file(self, mock_getpreferredencoding, mock___init__):
        mock_getpreferredencoding.return_value = 'UTF-8'
        mock___init__.return_value = None
        self.assertEqual(
            Lexer.write_song_to_file(self=<__main__.Lexer object at 0x7f3004547550>,fileName='testOutput.txt'),
            None
        )


if __name__ == "__main__":
    unittest.main()
