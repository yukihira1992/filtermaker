from io import StringIO

import filtermaker


class TestTextFilter:
    class LineWordCounter(filtermaker.TextFilter):
        def main(self, line):
            return len(line)

    def test_main(self):
        reader = StringIO(
            'Beautiful\n'
            'is\n'
            'better\n'
            'than\n'
            'ugly.\n'
        )
        writer = StringIO()
        line_word_counter = self.LineWordCounter(reader=reader, writer=writer)
        line_word_counter.run()

        expected = '9\n' \
                   '2\n' \
                   '6\n' \
                   '4\n' \
                   '5\n'

        assert writer.getvalue() == expected

    def test_main_with_default_io(self, monkeypatch):
        stdin = StringIO(
            'Beautiful\n'
            'is\n'
            'better\n'
            'than\n'
            'ugly.\n'
        )
        stdout = StringIO()
        monkeypatch.setattr('sys.stdin', stdin)
        monkeypatch.setattr('sys.stdout', stdout)

        line_word_counter = self.LineWordCounter()
        line_word_counter.run()

        expected = '9\n' \
                   '2\n' \
                   '6\n' \
                   '4\n' \
                   '5\n'

        assert stdout.getvalue() == expected
