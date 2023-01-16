import pathlib

if __name__ == '__main__':

    # Check if kraken is installed
    try:
        from kraken import blla, rpred
        from kraken.lib import vgsl, models
    except ImportError:
        print("Install kraken OCR engine to run this script: https://github.com/mittagessen/kraken#installation.")
        exit(1)
    
    # This packages are kraken dependencies
    import torch
    from PIL import Image

    # Set number of threads to 1 to avoid multithreading issues
    torch.set_num_threads(1)

    # Set paths
    cwd = pathlib.Path.cwd()
    seg_model_path = cwd / "numerica_sinologica_siku_seg_4p.mlmodel"
    rec_model_path = cwd / "numerica_sinologica_siku_kanripo_rec.mlmodel"
    img_path = cwd / "test" / "siku_1.png"

    # Check if all files exist
    assert seg_model_path.exists()
    assert rec_model_path.exists()
    assert img_path.exists()

    # Load image
    img = Image.open(img_path)

    # Load segmentation model and segment the image
    seg_model = vgsl.TorchVGSLModel.load_model(seg_model_path)
    baseline_seg = blla.segment(img, text_direction="vertical-rl", model=seg_model)

    # Load recognition model and iterate over the lines
    rec_model = models.load_any(rec_model_path)
    pred_it = rpred.rpred(rec_model, img, baseline_seg)
    for record in pred_it:
        print(record)

    print("Done!")