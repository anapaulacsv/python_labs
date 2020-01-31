import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

import unittest
from financas.correntista import Correntista

from unittest.mock import Mock

class TestCorrentista(unittest.TestCase):
    def setUp(self):
        auditor = Mock()
        self.correntista = Correntista("Nome", "12345678901", 10.0, auditor)

    def test_atributos(self):
        self.assertEqual(self.correntista.nome(), "Nome")
        self.assertEqual(self.correntista.cpf(), "12345678901")
        self.assertEqual(self.correntista.saldo(), 10.0)

    def test_deposito(self):
        auditor = Mock()

        self.correntista.deposita( 10.0, auditor)
        self.assertEqual(self.correntista.saldo(), 20.0)
  
        auditor.auditar.assert_called_with(self.correntista.cpf(), 'Deposito', 10.0)
        
    def test_deposito_invalido(self):
        auditor = Mock()

        with self.assertRaises(ValueError):
            self.correntista.deposita(-10.0, auditor)
        with self.assertRaises(ValueError):
            self.correntista.deposita(0.0, auditor) 
        with self.assertRaises(TypeError):
            self.correntista.deposita('aa', auditor)   
        auditor.auditar.assert_not_called()   

    def test_saque(self):
        auditor = Mock()

        self.correntista.saque( 10.0, auditor)
        self.assertEqual(self.correntista.saldo(),0.0)

        auditor.auditar.assert_called_with(self.correntista.cpf(), 'Saque', 10.0)

    def test_saque_verifica_saldo(self):
        auditor = Mock()

        with self.assertRaises(ValueError):
            self.correntista.saque( 20.0, auditor)

    def test_saque_invalido(self):
        auditor = Mock()

        with self.assertRaises(ValueError):
            self.correntista.saque(-10.0, auditor)
        with self.assertRaises(ValueError):
            self.correntista.saque(0.0, auditor) 
        with self.assertRaises(TypeError):
            self.correntista.saque('aa', auditor)  

        auditor.auditar.assert_not_called() 

if __name__ == '__main__':
    unittest.main()        