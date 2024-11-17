"""Minimal working example to reproduce an error when the DataLoader keeps all the files open."""

import torch
from tqdm import tqdm


class Dset(torch.utils.data.Dataset):
    def __getitem__(self, idx):
        return torch.randint(255, size=(2, 20), dtype=int)

    def __len__(self):
        return 100_000


dloader = torch.utils.data.DataLoader(Dset(), batch_size=1, num_workers=8)
stats = []
for items in tqdm(dloader):
    for item in items:
        stats.append(item.numpy())  # will give you the error after ~20-90k batches
        # stats.append(item.numpy().copy())  # works without error
