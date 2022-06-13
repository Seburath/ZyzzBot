#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from unittest import TestCase

from .db import DBMan


class TestDBMan(TestCase):
    db = DBMan("Test")

    def test_trabajadores(self):
        self.assertEqual(self.db.get_trabajadores(), [])

        self.db.add_trabajador("t1")
        self.assertEqual(self.db.get_trabajadores(), [(1, "t1")])

        self.db.add_trabajador("t2")
        self.assertEqual(self.db.get_trabajadores(), [(1, "t1"), (2, "t2")])

        self.db.rm_trabajador(1)
        self.assertEqual(self.db.get_trabajadores(), [(2, "t2")])


"""
    def test_bodega(self):
        self.assertEqual(self.db.get_inventario(), {})
        self.assertEqual(self.db.get_last_bodega_id(), 0)
        self.assertEqual(self.db.get_from_bodega("parrillero blanco abierto"), 0)
        self.assertEqual(self.db.get_all_bodega_registers(), [])

        self.db.var_bodega("parrillero blanco abierto", "t1 t2 t3", 100)

        self.assertEqual(self.db.get_inventario(), {"parrillero blanco abierto": 100})
        self.assertEqual(self.db.get_last_bodega_id(), 1)
        self.assertEqual(self.db.get_from_bodega("parrillero blanco abierto"), 100)
        self.assertEqual(
            self.db.get_all_bodega_registers()[-1][0:3],
            (
                1,
                "parrillero blanco abierto",
                "t1 t2 t3",
            ),
        )

        self.db.var_bodega("parrillero blanco abierto", "t1 t2 t3", 100)

        self.assertEqual(self.db.get_inventario(), {"parrillero blanco abierto": 200})
        self.assertEqual(self.db.get_last_bodega_id(), 2)
        self.assertEqual(self.db.get_from_bodega("parrillero blanco abierto"), 200)
        self.assertEqual(
            self.db.get_all_bodega_registers()[-1][0:3],
            (
                2,
                "parrillero blanco abierto",
                "t1 t2 t3",
            ),
        )

        self.db.var_bodega("parrillero blanco abierto", "t1 t2 t3", -50)

        self.assertEqual(self.db.get_inventario(), {"parrillero blanco abierto": 150})
        self.assertEqual(self.db.get_last_bodega_id(), 3)
        self.assertEqual(self.db.get_from_bodega("parrillero blanco abierto"), 150)
        self.assertEqual(
            self.db.get_all_bodega_registers()[-1][0:3],
            (
                3,
                "parrillero blanco abierto",
                "t1 t2 t3",
            ),
        )

        self.db.var_bodega("parrillero blanco cerrado", "t1 t2 t3", 100)

        self.assertEqual(
            self.db.get_inventario(),
            {"parrillero blanco abierto": 150, "parrillero blanco cerrado": 100},
        )
        self.assertEqual(self.db.get_last_bodega_id(), 4)
        self.assertEqual(self.db.get_from_bodega("parrillero blanco abierto"), 150)
        self.assertEqual(self.db.get_from_bodega("parrillero blanco cerrado"), 100)
        self.assertEqual(len(self.db.get_all_bodega_registers()), 4)

        self.db.rm_var_bodega(1)

        self.assertEqual(
            self.db.get_inventario(),
            {"parrillero blanco abierto": 50, "parrillero blanco cerrado": 100},
        )
        self.assertEqual(self.db.get_last_bodega_id(), 5)
        self.assertEqual(self.db.get_from_bodega("parrillero blanco abierto"), 50)
        self.assertEqual(self.db.get_from_bodega("parrillero blanco cerrado"), 100)
        self.assertEqual(len(self.db.get_all_bodega_registers()), 5)

        self.db.make_fd(4)
        self.assertEqual(self.db.bodega_var_is_fd(4), True)

        self.db.unmake_fd(4)
        self.assertEqual(self.db.bodega_var_is_fd(4), False)

    def test_pagos(self):
        self.assertEqual(self.db.get_pagos("t1"), 0)
        self.assertEqual(self.db.get_all_pagos(), [])
        self.assertEqual(self.db.get_last_pago_id(), 0)

        self.db.var_pagos(100, "t1", "Estiba")

        self.assertEqual(self.db.get_pagos("t1"), 100)
        self.assertEqual(len(self.db.get_all_pagos()), 1)
        self.assertEqual(self.db.get_last_pago_id(), 1)

        self.db.var_pagos(100, "t1", "Estiba")

        self.assertEqual(self.db.get_pagos("t1"), 200)
        self.assertEqual(len(self.db.get_all_pagos()), 2)
        self.assertEqual(self.db.get_last_pago_id(), 2)

        self.db.rm_pago("Estiba", 1)

        self.assertEqual(self.db.get_pagos("t1"), 100)
        self.assertEqual(len(self.db.get_all_pagos()), 3)
        self.assertEqual(self.db.get_last_pago_id(), 3)

"""
