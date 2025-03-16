import get_all_pieces
import merge
import remove_border

URL = 'https://olimp.miet.ru/ppo_it/api'

get_all_pieces.download_unique_pieces(URL)
merge.run()
remove_border.run()