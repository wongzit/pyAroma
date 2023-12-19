# py.Aroma 4
![](pyAroma_banner.png)

## Statement
py.**Aroma** is a multi-functional Python program for aromaticity analyses.
py.**Aroma** is free of charge for acdemic user, for other license term, please contact the developer.

Please refer to the [homepage](https://wongzit.github.io/program/pyaroma/) for more information.

## Running with Source Code

Please run `pyAroma_main.py` file in `/src` folder with Python 3 IDE. Other files including `config.ini` and `assets` folder should 
be put at same dictionary as `pyAroma_main.py` file.

## Download

Version 4.0.0, Build 3116.
- [macOS](https://drive.google.com/file/d/1dysLAgXqhUs0A0XIZUC9nrdccMttKVvq/view?usp=share_link)
- [Windows](https://drive.google.com/file/d/1kwrasGuiMpLjxnPaeUTuhIcRg8mvXYVp/view?usp=share_link)

Version 3.1.0, Build 3100.
- [macOS](https://drive.google.com/file/d/1cPFGJ_h85831Wuth6nwK0UUjat5VPlcx/view?usp=sharing)

Version 3.0.0, Build 2314.

- [Windows](https://drive.google.com/file/d/1QUojgzprZRvWLBtgcQ55pXqR8uX4vqRu/view?usp=share_link)
- [Linux](https://drive.google.com/drive/folders/12ukrOltMulc7Kz6ZV9--I7g9PDn8UeFL?usp=share_link)

## Update History

### v4.0.0, Build 3116.

1. Fixed the issue of HOMA interface not outputting results.
2. Fixed the problem of overlapping of HOMA values or program crashing when calculating HOMA for large cyclic and spherical molecules.
3. Ignored monocycles composed of more than 10 atoms.
4. Fixed the issue that unable to read *Gaussian* input files with custom basis sets.
5. Fixed the issue that unable to read .pdb files converted from .cif through *Mercury*.
6. Added the functionality to generate INICS input files.
7. Added the functionality to process INICS output files generated from INICS input files by **py.Aroma 4**.
8. Added the functionality to calculate BLA values.
9. Added the functionality to calculate NICS_ZZ for twisted/tilted rings and rings not in the XY plane.
10. Fixed the element symbol error: Ym → Tm.
11. Integrated the functionality of [*py.NMR*](https://github.io/wongzit/pyNMR).
12. Added some pop-up infomations.

### v3.1.0, Build 3100.
1. Now the program can recognize chordless monocycles.
2. Improved reliability for adding ghost atoms for distorted cycles.

### v3.0.0, Build 2314.
1. Fully re-wrote code with all new GUI, powered by PyQt6.
2. Added BLA, HOMA and POAV functions.
3. Combined [*CSIgen*](https://github.com/wongzit/CSIgen) module.
4. Added more functions for 2D and 3D NICS analyses.
5. Added 1D NICS scan function.
6. In 3D NICS module, user can also access 2D NICS module.

### v2.1.0, Build 2026.
1. Fixed the issue of scientific notation of Cartesian coordinates in *Gaussian* input files.

### v2.0.1, Build 1516.
1. Fixed a minor bug.

### v2.0.0, Build 1510.
1. A new graphical user interface (GUI) is available for **py.Aroma**.
2. HOMA calculation function was removed.
3. Improved sufficiency of 2D-NICS plotting.

### v1.0.0, Build 410.
1. Improved stability.
2. Typos are fixed in main program.
3. Perfoming test has been carried on seven platforms.

### v0.6.0, Build 409b.
1. [*HOMAcalc*](https://github.com/wongzit/HOMAcalc) module has been added into main program for HOMA calculation.
2. *This version is a beta release.*

### v0.3.0, Build 408b.
1. The basic functions of [*ICSSgen*](https://github.com/wongzit/ICSSgen), [*ICSScsv*](https://github.com/wongzit/ICSScsv), [*ICSSgen3D*](https://github.com/wongzit/ICSSgen3D), [*ICSScub3D*](https://github.com/wongzit/ICSScub3D) and [*NICSgen*](https://github.com/wongzit/NICSgen) are combined to **py.Aroma**. 
2. *This version is a beta release.*

## Citation

If **py.Aroma** if ultilized in your work, or the code is implied in your own code, please consider citing following contents:

- Yuki Miyazawa, Zhe Wang, Misaki Matsumoto, Sayaka Hatano, Ivana Antol, Eiichi Kayahara, Shigeru Yamago, Manabu Abe, *Journal of the American Chemical Society*, **2021**, *143*(*19*), 7426-7439.

- Zhe Wang, **py.Aroma 4**, https://wongzit.github.io/program/pyaroma (accessed *data*, *month*, *year*).
