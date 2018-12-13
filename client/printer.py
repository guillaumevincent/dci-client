# -*- coding: utf-8 -*-


class Printer(object):
    def __init__(self, head):
        self.head = head
        self.offset = 1
        self.char = {
            "top": "─",
            "top-mid": "┬",
            "top-left": "┌",
            "top-right": "┐",
            "bottom": "─",
            "bottom-mid": "┴",
            "bottom-left": "└",
            "bottom-right": "┘",
            "left": "│",
            "left-mid": "├",
            "mid": "─",
            "mid-mid": "┼",
            "right": "│",
            "right-mid": "┤",
            "middle": "│",
        }

    def draw_line(self, blocs, col_widths, new_line=True):
        result = ""
        result += blocs["left"]
        nb_cells = len(self.head)
        for i in range(nb_cells):
            result += blocs["offset"] * self.offset
            result += blocs["content"] * col_widths[i]
            result += blocs["offset"] * self.offset
            is_last_cell = i == nb_cells - 1
            if is_last_cell:
                result += blocs["right"]
            else:
                result += blocs["sep"]
        if new_line:
            result += "\n"
        return result

    def draw_top_line(self, col_widths):
        blocs = {
            "left": self.char["top-left"],
            "offset": self.char["top"],
            "content": self.char["top"],
            "sep": self.char["top-mid"],
            "right": self.char["top-right"],
        }
        return self.draw_line(blocs, col_widths)

    def draw_separator_line(self, col_widths):
        blocs = {
            "left": self.char["left-mid"],
            "offset": self.char["mid"],
            "content": self.char["mid"],
            "sep": self.char["mid-mid"],
            "right": self.char["right-mid"],
        }
        return self.draw_line(blocs, col_widths)

    def draw_bottom_line(self, col_widths):
        blocs = {
            "left": self.char["bottom-left"],
            "offset": self.char["bottom"],
            "content": self.char["bottom"],
            "sep": self.char["bottom-mid"],
            "right": self.char["bottom-right"],
        }
        return self.draw_line(blocs, col_widths, new_line=False)

    def draw_header(self, col_widths):
        result = ""
        result += self.draw_top_line(col_widths)
        result += self.draw_content(self.head, col_widths)
        result += self.draw_separator_line(col_widths)
        return result

    def draw_content(self, data, col_widths):
        result = ""
        result += self.char["left"]
        nb_cells = len(self.head)
        for i in range(nb_cells):
            content = str(data[i]) if data[i] else ""
            result += " " * self.offset
            result += content
            result += " " * (col_widths[i] - len(content))
            result += " " * self.offset
            is_last_cell = i == nb_cells - 1
            if is_last_cell:
                result += self.char["right"]
            else:
                result += self.char["middle"]
        result += "\n"
        return result

    def get_col_widths(self, data):
        col_widths = [len(c) for c in self.head]
        for d in data:
            for i, k in enumerate(self.head):
                content = str(d[k]) if d[k] else ""
                col_widths[i] = max(col_widths[i], len(content))
        return col_widths

    def to_string(self, data):
        result = ""
        col_widths = self.get_col_widths(data)
        result += self.draw_header(col_widths)
        for i, d in enumerate(data):
            columns = [d[k] for k in self.head]
            result += self.draw_content(columns, col_widths)
            is_last_row = i == len(data) - 1
            if is_last_row:
                result += self.draw_bottom_line(col_widths)
            else:
                result += self.draw_separator_line(col_widths)
        return result
