from . import get_all_pieces
from . import merge
from . import remove_border
from . import get_coords

# import get_all_pieces
# import merge
# import remove_border
# import get_coords


def run(URL='https://olimp.miet.ru/ppo_it/api'):
    URL = URL.strip('/')
    get_all_pieces.download_unique_pieces(URL)
    merge.run()
    remove_border.run()

    get_coords.run(f'{URL}/coords')