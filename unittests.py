from mainmodules import ignorethis
import unittest
import os


class Test_Game(unittest.TestCase):

    """ignorethis tests"""
    def test_encrypt(self):
        self.assertEqual(ignorethis.encrypt("hello this is a test...", 'password'), [216, 198, 223, 223, 230, 143, 230, 204, 217,
                                                                                     212, 147, 220, 234, 143, 211, 132, 228, 198,
                                                                                     230, 231, 165, 157, 160])

        self.assertEqual(ignorethis.encrypt("!this is a line break\nblablablab", 'password'),[145, 213, 219, 220, 234, 143,
                                                                                              219, 215, 144, 194, 147, 223, 224,
                                                                                              221, 215, 132, 210, 211, 216, 212,
                                                                                              226, 121, 212, 208, 209, 195, 223,
                                                                                              212, 217, 219, 211, 198])

        self.assertEqual(ignorethis.encrypt("6-6-4%4", '5'), [107, 98, 107, 98, 105, 90, 105])

    def test_decrypt(self):

        self.assertEqual(ignorethis.decrypt([107, 98, 107, 98, 105, 90, 105], '5'), "6-6-4%4")
        self.assertRaises(ValueError, ignorethis.decrypt, [107, 98, 107, 98, 105, 90, 105], 't')
        self.assertRaises(ValueError, ignorethis.decrypt, [0], 't')

    def test_write_plaintext(self):
        self.assertEqual(ignorethis.write_plaintext(cyphertext='encrypted_articles/welcome.encrypted.txt', file_to_create='unittest.blob', key='5'), None)
        self.assertRaises(TypeError, ignorethis.write_plaintext, [0, 1, 2, 3, 4, 666], 'unittest.blob', 'RandomString')

    """
    CommandPrompt tests:  Need to find way to do this correctly. whenever class is instanceated, command line starts...
    tree function seems trivial, no seemingly good way to test it
    """

    def tearDown(self):
        try:
            os.remove("user/texts/unittest.blob")
        except:
            pass


if __name__ == '__main__':
    unittest.main()
