# Constant lists, including atom color, atom radii,
# covalent radii and homa.
# A Module for py.Aroma
# By Dr. Zhe Wang @Ktoyo, 2022-02-06

import numpy as np
import os
import configparser

atom_colors = np.array([(229, 51, 255),
                        (220, 220, 220), (217, 255, 255), (204, 128, 255),
                        (194, 255, 0), (255, 181, 181), (144, 144, 144),
                        (48, 80, 248), (255, 13, 13), (144, 224, 80),
                        (179, 227, 245), (171, 92, 242), (138, 255, 0),
                        (191, 166, 166), (240, 200, 160), (255, 128, 0),
                        (255, 255, 48), (31, 240, 31), (128, 209, 227),
                        (143, 64, 212), (61, 225, 0), (230, 230, 230),
                        (191, 194, 199), (166, 166, 171), (138, 153, 199),
                        (156, 122, 199), (224, 102, 51), (240, 144, 160),
                        (80, 208, 80), (200, 128, 51), (125, 128, 176),
                        (194, 143, 143), (102, 143, 143), (189, 128, 227),
                        (225, 161, 0), (166, 41, 41), (92, 184, 209),
                        (112, 46, 176), (0, 255, 0), (148, 255, 255),
                        (148, 224, 224), (115, 194, 201), (84, 181, 181),
                        (59, 158, 158), (36, 143, 143), (10, 125, 140),
                        (0, 105, 133), (192, 192, 192), (255, 217, 143),
                        (166, 117, 115), (102, 128, 128), (158, 99, 181),
                        (212, 122, 0), (148, 0, 148), (66, 158, 176),
                        (87, 23, 143), (0, 201, 0), (112, 212, 255),
                        (255, 255, 199), (217, 225, 199), (199, 225, 199),
                        (163, 225, 199), (143, 225, 199), (97, 225, 199),
                        (69, 225, 199), (48, 225, 199), (31, 225, 199),
                        (0, 225, 156), (0, 230, 117), (0, 212, 82),
                        (0, 191, 56), (0, 171, 36), (77, 194, 255),
                        (77, 166, 255), (33, 148, 214), (38, 125, 171),
                        (38, 102, 150), (23, 84, 135), (208, 208, 224),
                        (255, 209, 35), (184, 184, 208), (166, 84, 77),
                        (87, 89, 97), (158, 79, 181), (171, 92, 0),
                        (117, 79, 69), (66, 130, 150), (66, 0, 102),
                        (0, 125, 0), (112, 171, 250), (0, 186, 255),
                        (0, 161, 255), (0, 143, 255), (0, 128, 255),
                        (0, 107, 255), (84, 92, 242), (120, 92, 227),
                        (138, 79, 227), (161, 54, 212), (179, 31, 212),
                        (179, 31, 186), (179, 13, 166), (189, 13, 135),
                        (199, 0, 102), (204, 0, 89), (209, 0, 79),
                        (217, 0, 69), (224, 0, 56), (230, 0, 46),
                        (235, 0, 38), (255, 0, 255), (255, 0, 255),
                        (255, 0, 255), (255, 0, 255), (255, 0, 255),
                        (255, 0, 255), (255, 0, 255), (255, 0, 255), (255, 0, 255)], dtype = np.float32) / 255.0

period_table = ['BQ', 'H', 'HE', 'LI', 'BE', 'B', 'C', 'N', 'O', 'F', 'NE', 'NA', 'MG', 'AL', 'SI', 'P', 'S', 'CL', 'AR', \
                    'K', 'CA', 'SC', 'TI', 'V', 'CR', 'MN', 'FE', 'CO', 'NI', 'CU', 'ZN', 'GA', 'GE', 'AS', 'SE', 'BR', 'KR', \
                    'RB', 'SR', 'Y', 'ZR', 'NB', 'MO', 'TC', 'RU', 'RH', 'PD', 'AG', 'CD', 'IN', 'SN', 'SB', 'TE', 'I', 'XE', \
                    'CS', 'BA', 'LA', 'CE', 'PR', 'ND', 'PM', 'SM', 'EU', 'GD', 'TB', 'DY', 'HO', 'ER', 'YM', 'YB', 'LU', 'HA', 'TA', \
                    'W', 'RE', 'OS', 'IR', 'PT', 'AU', 'HG', 'TL', 'PB', 'BI', 'PO', 'AT', 'RN', 'FR', 'RA', 'AC', 'TH', 'PA', 'U', \
                    'NP', 'PU', 'AM', 'CM', 'BK', 'CF', 'ES', 'FM', 'MD', 'NO', 'LR', 'RF', 'DB', 'SG', 'BH', 'HS', 'MT', 'DS', 'RG', \
                    'CN', 'NH', 'FL', 'MC', 'LV', 'TS', 'OG']

atom_valence_radii = np.array([0, 230, 930, 680, 350, 830, 680, 680, 680, 640,
                               1120, 970, 1100, 1350, 1200, 750, 1020, 990,
                               1570, 1330, 990, 1440, 1470, 1330, 1350, 1350,
                               1340, 1330, 1500, 1520, 1450, 1220, 1170, 1210,
                               1220, 1210, 1910, 1470, 1120, 1780, 1560, 1480,
                               1470, 1350, 1400, 1450, 1500, 1590, 1690, 1630,
                               1460, 1460, 1470, 1400, 1980, 1670, 1340, 1870,
                               1830, 1820, 1810, 1800, 1800, 1990, 1790, 1760,
                               1750, 1740, 1730, 1720, 1940, 1720, 1570, 1430,
                               1370, 1350, 1370, 1320, 1500, 1500, 1700, 1550,
                               1540, 1540, 1680, 1700, 2400, 2000, 1900, 1880,
                               1790, 1610, 1580, 1550, 1530, 1510, 1500, 1500,
                               1500, 1500, 1500, 1500, 1500, 1500, 1600, 1600,
                               1600, 1600, 1600, 1600, 1600, 1600, 1600, 1600,
                               1600, 1600, 1600, 1600, 1600, 1600],
                              dtype = np.float32) / 1000.0

atom_radii = np.array(atom_valence_radii, copy = True) * 1.25
'''
# Load config.ini
config_file = configparser.ConfigParser()
config_file_path = os.path.join(os.path.dirname(__file__), 'config.ini')
config_file.read(config_file_path)

# Load homa from config.ini
homa_para = {
    'CC':[float(config_file.get('homa', 'cc').split(',')[0]), \
    float(config_file.get('homa', 'cc').split(',')[1])],
    'CN':[float(config_file.get('homa', 'cn').split(',')[0]), \
    float(config_file.get('homa', 'cn').split(',')[1])],
    'NC':[float(config_file.get('homa', 'cn').split(',')[0]), \
    float(config_file.get('homa', 'cn').split(',')[1])],
    'CO':[float(config_file.get('homa', 'co').split(',')[0]), \
    float(config_file.get('homa', 'co').split(',')[1])],
    'OC':[float(config_file.get('homa', 'co').split(',')[0]), \
    float(config_file.get('homa', 'co').split(',')[1])],
    'CP':[float(config_file.get('homa', 'cp').split(',')[0]), \
    float(config_file.get('homa', 'cp').split(',')[1])],
    'PC':[float(config_file.get('homa', 'cp').split(',')[0]), \
    float(config_file.get('homa', 'cp').split(',')[1])],
    'CS':[float(config_file.get('homa', 'cs').split(',')[0]), \
    float(config_file.get('homa', 'cs').split(',')[1])],
    'SC':[float(config_file.get('homa', 'cs').split(',')[0]), \
    float(config_file.get('homa', 'cs').split(',')[1])],
    'NN':[float(config_file.get('homa', 'nn').split(',')[0]), \
    float(config_file.get('homa', 'nn').split(',')[1])],
    'NO':[float(config_file.get('homa', 'no').split(',')[0]), \
    float(config_file.get('homa', 'no').split(',')[1])],
    'ON':[float(config_file.get('homa', 'no').split(',')[0]), \
    float(config_file.get('homa', 'no').split(',')[1])],
    'BN':[float(config_file.get('homa', 'bn').split(',')[0]), \
    float(config_file.get('homa', 'bn').split(',')[1])],
    'NB':[float(config_file.get('homa', 'bn').split(',')[0]), \
    float(config_file.get('homa', 'bn').split(',')[1])],
    'CSE':[float(config_file.get('homa', 'cse').split(',')[0]), \
    float(config_file.get('homa', 'cse').split(',')[1])],
    'SEC':[float(config_file.get('homa', 'cse').split(',')[0]), \
    float(config_file.get('homa', 'cse').split(',')[1])]
}
'''

mplCmap = [
    'viridis', 'plasma', 'inferno', 'magma', 'cividis',
    'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
    'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
    'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn',
    'binary', 'gist_yarg', 'gist_gray', 'gray', 'bone',
    'pink', 'spring', 'summer', 'autumn', 'winter', 'cool',
    'Wistia', 'hot', 'afmhot', 'gist_heat', 'copper',
    'PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu', 'RdYlBu',
    'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic',
    'twilight', 'twilight_shifted', 'hsv',
    'Pastel1', 'Pastel2', 'Paired', 'Accent', 'Dark2',
    'Set1', 'Set2', 'Set3', 'tab10', 'tab20', 'tab20b', 'tab20c',
    'flag', 'prism', 'ocean', 'gist_earth', 'terrain',
    'gist_stern', 'gnuplot', 'gnuplot2', 'CMRmap',
    'cubehelix', 'brg', 'gist_rainbow', 'rainbow', 'jet',
    'turbo', 'nipy_spectral', 'gist_ncar'

]

molColor = [
    'white', 'black', 'grey', 'red', 'darkred', 'orange', 'yellow', 'gold',
    'yellowgreen', 'green', 'darkgreen', 'skyblue', 'steelblue', 'navy', 'darkblue',
    'purple', 'violet', 'pink'
]