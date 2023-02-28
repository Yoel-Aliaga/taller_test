from unittest import TestCase
from funciones import sumar 

class TestSumar(TestCase):
    def test_exito(self):
        resultado = sumar (5,4)
        #assert. nos da diferentes opciones de comparacion
        self.assertEqual(resultado,9)

    def test_fallo_primer_parametro(self):
        # resultado = sumar("a",5)
        with self.assertRaises(TypeError) as error:
            sumar('a',5)
        excepcion = error.exception

        self.assertEqual(excepcion.args[0],'Los parametros deben ser numericos')


    def test_fallo_segundo_parametro(self):
        # resultado = sumar("a",5)
        with self.assertRaises(TypeError) as error:
            sumar(5,'a')
        excepcion = error.exception

        self.assertEqual(excepcion.args[0],'Los parametros deben ser numericos')

    
    def test_fallo_ambos_parametro(self):
        # resultado = sumar("a",5)
        with self.assertRaises(TypeError) as error:
            sumar('a','e')
        excepcion = error.exception

        self.assertEqual(excepcion.args[0],'Los parametros deben ser numericos')    