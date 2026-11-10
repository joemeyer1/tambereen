#!/usr/bin/env python3
# Copyright (c) 2026 Joseph Meyer. MIT License.

import os
import random

from typing import Optional

from src.utils import make_name_unique

import torch
torch.set_grad_enabled(False)


def make_maxpat(audio_model_name: str, latent_dim: Optional[int] = None, new_maxpat_name: Optional[str] = None) -> None:
    """Writes a new maxpatch, using the percussion max path as reference.
    
    If not passed explicitly, latent_dim and new_maxpat_name are inferred from audio_model_name.
    """

    if latent_dim is None:
        model_path = f"pretrained_model_checkpoints/audio_model_checkpoints/{audio_model_name}.ts"
        assert os.path.exists(model_path), f"Either latent dim must be passed explicitly, or model_path '{model_path}' must exist to infer latent dim"
        model = torch.jit.load(model_path).eval()
        latent_dim = model.encode(torch.zeros(1, 1, 1)).shape[1]
    
    if new_maxpat_name is None:
        new_maxpat_name = f'tambereen_interface_{audio_model_name}.maxpat'
    
    if os.path.exists(f'interfaces/{new_maxpat_name}'):
        new_maxpat_name = make_name_unique(new_maxpat_name)
    print(f"Creating new maxpat 'interfaces/{new_maxpat_name}'...")

    with open('interfaces/tambereen_interface_percussion.maxpat', 'r') as f_ref:
        ref_maxpat = f_ref.read()

    # update model name
    new_maxpat = ref_maxpat.replace("nn~ percussion decode", f"nn~ {audio_model_name} decode")

    # Update novelification ratio modes
    new_maxpat = new_maxpat.replace(' '.join([str(1)] * 4), ' '.join([str(1)] * latent_dim))  # percussion RAVE has 4 latent dims
    new_maxpat = new_maxpat.replace("1 0 0 0", '1 ' + ' '.join([str(0)] * (latent_dim - 1)))
    new_maxpat = new_maxpat.replace("0. 1. -1.2 0.4", ' '.join([str(random.randint(-1000, 1000) / 100) for _ in range(latent_dim)]))

    # update multislider sizes
    new_maxpat = new_maxpat.replace('"size" : 4,', f'"size" : {latent_dim},')

    # update output connections from unpacking embeddings
    new_maxpat = new_maxpat.replace("mc.list~ 1 2 3 4", "mc.list~ " + ' '.join([str(i) for i in range(1, latent_dim + 1)]))
    new_maxpat = new_maxpat.replace("mc.unpack~ 4", f"mc.unpack~ {latent_dim}")
    new_maxpat = new_maxpat.replace(
        '"numoutlets" : 4,\n\t\t\t\t\t"outlettype" : [ "signal", "signal", "signal", "signal"',
        f'"numoutlets" : {latent_dim},' + '\n\t\t\t\t\t"outlettype" : [ ' + ', '.join(['"signal"']*latent_dim),
    )

    # update input connections to decoder
    ixs = list(map(str, range(latent_dim)))
    ixs.reverse()
    ref_patchlines = ', \t\t\t{\n\t\t\t\t"patchline" : \t\t\t\t{\n\t\t\t\t\t"destination" : [ "obj-9", 3 ],\n\t\t\t\t\t"order" : 0,\n\t\t\t\t\t"source" : [ "obj-8", 3 ]\n\t\t\t\t}\n\n\t\t\t}\n, \t\t\t{\n\t\t\t\t"patchline" : \t\t\t\t{\n\t\t\t\t\t"destination" : [ "obj-9", 2 ],\n\t\t\t\t\t"source" : [ "obj-8", 2 ]\n\t\t\t\t}\n\n\t\t\t}\n, \t\t\t{\n\t\t\t\t"patchline" : \t\t\t\t{\n\t\t\t\t\t"destination" : [ "obj-9", 1 ],\n\t\t\t\t\t"source" : [ "obj-8", 1 ]\n\t\t\t\t}\n\n\t\t\t}\n, \t\t\t{\n\t\t\t\t"patchline" : \t\t\t\t{\n\t\t\t\t\t"destination" : [ "obj-9", 0 ],\n\t\t\t\t\t"source" : [ "obj-8", 0 ]\n\t\t\t\t}\n\n\t\t\t}'
    new_patchlines = ''.join([', \t\t\t{\n\t\t\t\t"patchline" : \t\t\t\t{\n\t\t\t\t\t"destination" : [ "obj-9", 3 ],\n\t\t\t\t\t"order" : 0,\n\t\t\t\t\t"source" : [ "obj-8", 3 ]\n\t\t\t\t}\n\n\t\t\t}\n'.replace('", 3 ]', f'", {i} ]') for i in ixs])
    new_maxpat = new_maxpat.replace(ref_patchlines, new_patchlines)

    with open(f'interfaces/{new_maxpat_name}', 'w') as f:
        f.write(new_maxpat)

