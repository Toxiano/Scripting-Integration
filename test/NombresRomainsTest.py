import unittest

import parameterized as parameterized

import ConvertisseurNombresRomains


class MyTestCase(unittest.TestCase):

    @parameterized.parameterized.expand([[1], [2], [3]])
    def test_unité(self, n):
        # ETANT DONNE un chiffre <n> entre 1 et 3
        # QUAND on le convertit en nombres romains
        result = ConvertisseurNombresRomains.convertir(n)

        # ALORS on obtient <n> fois 'I'
        attendu = 'I'*n
        self.assertEqual(attendu, result)

    def test_four(self):
        # ETANT DONNE le chiffre 4
        nombre = 4

        # QUAND on le convertit en nombres romains
        result = ConvertisseurNombresRomains.convertir(nombre)

        # ALORS on obtient 'IV'
        self.assertEqual('IV', result)

    def test_five(self):
        # ETANT DONNE le chiffre 5
        nombre = 5

        # QUAND on le convertit en nombres romains
        result = ConvertisseurNombresRomains.convertir(nombre)

        # ALORS on obtient 'V'
        self.assertEqual('V', result)

    def test_six(self):
        # ETANT DONNE le chiffre 6
        nombre = 6

        # QUAND on le convertit en nombres romains
        result = ConvertisseurNombresRomains.convertir(nombre)

        # ALORS on obtient 'VI'
        self.assertEqual('VI', result)

    def test_sept(self):
        # ETANT DONNE le chiffre 7
        nombre = 7

        # QUAND on le convertit en nombres romains
        result = ConvertisseurNombresRomains.convertir(nombre)

        # ALORS on obtient 'VII'
        self.assertEqual('VII', result)

    def test_huit(self):
        # ETANT DONNE le chiffre 8
        nombre = 8

        # QUAND on le convertit en nombres romains
        result = ConvertisseurNombresRomains.convertir(nombre)

        # ALORS on obtient 'VIII'
        self.assertEqual('VIII', result)


if __name__ == '__main__':
    unittest.main()