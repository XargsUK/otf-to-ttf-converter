import os
import logging
from fontTools.ttLib import TTFont
from fontTools.ttLib.tables._c_m_a_p import CmapSubtable

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

otf_dir = '/otf'

ttf_dir = '/ttf'

os.makedirs(ttf_dir, exist_ok=True)

for filename in os.listdir(otf_dir):
    try:
        if filename.endswith('.otf'):
            ttf_filename = filename.replace('.otf', '.ttf')
            if os.path.exists(os.path.join(ttf_dir, ttf_filename)):
                logging.info(f'The font {ttf_filename} has already been converted.')
                continue

            font = TTFont(os.path.join(otf_dir, filename))

            for table in font['cmap'].tables:
                if isinstance(table, CmapSubtable):
                    table.cmap = {code: name for code, name in sorted(table.cmap.items(), key=lambda item: item[1])}

            font.save(os.path.join(ttf_dir, ttf_filename))

            logging.info(f'The font {ttf_filename} has been converted successfully.')
    except Exception as e:
        logging.error(f'An error occurred while converting the font {filename}: {e}')
