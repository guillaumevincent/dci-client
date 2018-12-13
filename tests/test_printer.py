# -*- coding: utf-8 -*-

import unittest

from client.printer import Printer


class TestPrinter(unittest.TestCase):
    def test_printer_to_string(self):
        expected = [
            "┌──────────────────────────────────────┬───────────┬────────────────────┐",
            "│ id                                   │ name      │ email              │",
            "├──────────────────────────────────────┼───────────┼────────────────────┤",
            "│ 6018975a-dde7-4666-9436-b171c5a11dde │ Jonh Doe  │ jdoe@example.org   │",
            "├──────────────────────────────────────┼───────────┼────────────────────┤",
            "│ f05b3da7-701b-40bd-87e8-780693a07b13 │ Bob Dylan │ bdylan@example.org │",
            "└──────────────────────────────────────┴───────────┴────────────────────┘",
        ]
        printer = Printer(head=["id", "name", "email"])
        self.assertEqual(
            printer.to_string(
                [
                    {
                        "id": "6018975a-dde7-4666-9436-b171c5a11dde",
                        "name": "Jonh Doe",
                        "email": "jdoe@example.org",
                    },
                    {
                        "id": "f05b3da7-701b-40bd-87e8-780693a07b13",
                        "name": "Bob Dylan",
                        "email": "bdylan@example.org",
                    },
                ]
            ),
            "\n".join(expected),
        )

    def test_printer_to_string_None_value(self):
        expected = [
            "┌──────────────────────────────────────┬───────────┬──────────────────┐",
            "│ id                                   │ name      │ email            │",
            "├──────────────────────────────────────┼───────────┼──────────────────┤",
            "│ 6018975a-dde7-4666-9436-b171c5a11dde │ Jonh Doe  │ jdoe@example.org │",
            "├──────────────────────────────────────┼───────────┼──────────────────┤",
            "│ f05b3da7-701b-40bd-87e8-780693a07b13 │ Bob Dylan │                  │",
            "└──────────────────────────────────────┴───────────┴──────────────────┘",
        ]
        printer = Printer(head=["id", "name", "email"])
        self.assertEqual(
            printer.to_string(
                [
                    {
                        "id": "6018975a-dde7-4666-9436-b171c5a11dde",
                        "name": "Jonh Doe",
                        "email": "jdoe@example.org",
                    },
                    {
                        "id": "f05b3da7-701b-40bd-87e8-780693a07b13",
                        "name": "Bob Dylan",
                        "email": None,
                    },
                ]
            ),
            "\n".join(expected),
        )

    def test_printer_to_string_int_value(self):
        expected = [
            "┌──────────┬─────┐",
            "│ name     │ age │",
            "├──────────┼─────┤",
            "│ Jonh Doe │ 32  │",
            "└──────────┴─────┘",
        ]
        printer = Printer(head=["name", "age"])
        self.assertEqual(
            printer.to_string(
                [
                    {
                        "id": "6018975a-dde7-4666-9436-b171c5a11dde",
                        "name": "Jonh Doe",
                        "age": 32,
                    }
                ]
            ),
            "\n".join(expected),
        )
