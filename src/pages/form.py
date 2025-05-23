# modules
import flet
from flet import *
from functools import partial
import time

# Sidebar Class


class ModernNavBar(UserControl):
    def _init_(self):
        super()._init_()

# main function


def build(self):
    return Container(content=None)


# main function
def main(page: Page):
    # title
    page.title = 'Flet Modern Sidebar'

    # alignemnts
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'

    # add class to page
    page.add(
        Container(
            width=200,
            height=580,
            content=ModernNavBar()
        )

    )


page.update()
