# Numerica Sinologica Siku HTR models

This repository contains automatic transcription models trained using the [kraken OCR engine](https://github.com/mittagessen/kraken) on images from the Wenyuange 文淵閣 Siku quanshu 四庫全書.

This work is part of an ongoing project by the Numerica Sinologica consortium to build open-source digital tools for pre-modern Chinese studies.

## Segmentation models

- `numerica_sinologica_siku_seg_4p` is trained to segment reduced-format facsimile (缩印本) where each image contains four pages of the original book.

- `numerica_sinologica_base_seg_1p` is a base model trained using color images with a 9:16 aspect ratio.


## Recognition models

- `numerica_sinologica_siku_kanripo_rec` is a transcription model trained with images from the Wenyuange siku quanshu and diplomatic transcriptions from the Kansekei repository. This model acheived 99.11% accuracy on an untouched test dataset.

- `numerica_sinologica_siku_standard_rec` was trained with the same dataset as `numerica_sinologica_siku_kanripo_rec` but using standardized transcriptions.

## Test

`python test/test_siku_models.py`

## Acknowledgement

We wish to thank kraken main developer, Benjamin Kiessling, as well as eScriptorium project directors, Daniel Stökl Ben Ezra and Peter Stokes, for their support.

This work received funding from the Centre Chine, Corée, Japon (UMR 8173), the Centre de recherche sur les civilisations de l'Asie orientale (UMR 8155), the Institut d'Asie orientale (UMR 5062), the Institut Universitaire de France, and from the Vietnamica project (ERC 833933).

## License

This work is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License. See [LICENSE](./LICENCE) for details.

## Citation
