import unittest
from index import caesar_cipher


class TestCaesarCipher(unittest.TestCase):
    def test_cipher(self):
        test_phrase = "Almost before we knew it, we had left the ground."
        expected_outputs = [
            (test_phrase, 0, "Almost before we knew it, we had left the ground."),
            (test_phrase, 26, "Almost before we knew it, we had left the ground."),
            (test_phrase, -26, "Almost before we knew it, we had left the ground."),
            (test_phrase, 1, "Bmnptu cfgpsf xf lofx ju, xf ibe mfgu uif hspvoe."),
            (test_phrase, 2, "Cnoquv dghqtg yg mpgy kv, yg jcf nghv vjg itqwpf."),
            (test_phrase, 30, "Epqswx fijsvi ai oria mx, ai leh pijx xli kvsyrh."),
            (test_phrase, -15, "Lwxzde mpqzcp hp vyph te, hp slo wpqe esp rczfyo."),
        ]

        for to_convert, shift, output in expected_outputs:
            self.assertEqual(caesar_cipher(to_convert, shift), output)

    def test_types(self):
        self.assertRaises(TypeError, caesar_cipher, 123, 3)
        self.assertRaises(TypeError, caesar_cipher, True, 3)
        self.assertRaises(TypeError, caesar_cipher, [], 3)
        self.assertRaises(TypeError, caesar_cipher, {}, 3)


if __name__ == "__main__":
    unittest.main()