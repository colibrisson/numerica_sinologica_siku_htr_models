import pathlib

import torch
from PIL import Image

from kraken import blla, rpred
from kraken.lib import vgsl, models

if __name__ == '__main__':

    torch.set_num_threads(1)

    cwd = pathlib.Path.cwd()
    seg_model_path = cwd / "numerica_sinologica_siku_seg_4p.mlmodel"
    rec_model_path = cwd / "numerica_sinologica_siku_kanripo_rec.mlmodel"
    img_path = cwd / "test" / "siku_1.png"

    assert seg_model_path.exists()
    assert rec_model_path.exists()
    assert img_path.exists()

    img = Image.open(img_path)

    seg_model = vgsl.TorchVGSLModel.load_model(seg_model_path)
    baseline_seg = blla.segment(img, text_direction="vertical-rl",model=seg_model)

    rec_model = models.load_any(rec_model_path)
    pred_it = rpred.rpred(rec_model, img, baseline_seg)
    for record in pred_it:
        print(record)

    print("Done!")