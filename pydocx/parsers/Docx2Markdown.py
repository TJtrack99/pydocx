from __future__ import (
    absolute_import,
    print_function,
    unicode_literals,
)

from pydocx.DocxParser import DocxParser


class Docx2Markdown(DocxParser):
    def escape(self, text):
        return text

    def linebreak(self):
        return '\n'

    def paragraph(self, text):
        return text + '\n'

    def insertion(self, text, author, date):
        pass

    def bold(self, text):
        return '**' + text + '**'

    def italics(self, text):
        # TODO do we need a "pre" variable, so I can check for
        # *italics**italics* and turn it into *italicsitatlics*?
        return '*' + text + '*'

    def underline(self, text):
        return '***' + text + '***'

    def hyperlink(self, text, href):
        if text == '':
            return ''
        return '[' + text + '](' + href + ')'

    def strike(self, text):
        return '~~' + text + '~~'

    def heading(self, text, heading_value):
        #TODO check that this makes sense for deeper levels of headings too
        if heading_value == 1:
            return text + '\n==========\n'
        elif heading_value == 2:
            return text + '\n----------\n'
        else: 
            return '### ' + text

