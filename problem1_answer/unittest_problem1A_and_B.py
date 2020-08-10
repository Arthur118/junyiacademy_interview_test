import unittest
from problem1A import reverse_string
from problem1B import sentence_reverse


class Test(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string('junyiacademy'), 'ymedacaiynuj')
        self.assertEqual(reverse_string('ilovejunyi'), 'iynujevoli')
        self.assertEqual(reverse_string('mynameisarthur'), 'ruhtrasiemanym')

    def test_sentence_reverse(self):
        self.assertEqual(sentence_reverse('flipped class room is important'), 'deppilf ssalc moor si tnatropmi')
        self.assertEqual(sentence_reverse('i love junyiacademy'), 'i evol ymedacaiynuj')
        self.assertEqual(sentence_reverse('my name is arthur'), 'ym eman si ruhtra')


if __name__ == '__main__':
    unittest.main()
