
## Minimal working example for a common problem with the pytorch DataLoader

When using the default pytorch dataloader, it uses file descriptors as memory handles.
See [here](https://pytorch.org/docs/main/multiprocessing.html#file-descriptor-file-descriptor) for details.

A problem occurs when the batch from the dataloader if at least some of the data in the batch is saved
(e.g., for debugging).
The file descriptors of all items will be kept open indefinitely, leading to the following error.
```
RuntimeError: unable to mmap 320 bytes from file <filename not specified>: Cannot allocate memory (12)
```
