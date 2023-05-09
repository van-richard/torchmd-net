import os
import torch as pt
from torch.utils import cpp_extension

src_dir = os.path.dirname(__file__)
sources = ['neighbors.cpp', 'neighbors_cpu.cpp'] + (['neighbors_cuda.cu', 'neighbors_cuda_cell.cu', 'backwards.cu'] if pt.cuda.is_available() else [])
sources = [os.path.join(src_dir, name) for name in sources]
cpp_extension.load(name='neighbors', sources=sources, is_python_module=False)

get_neighbor_pairs_brute = pt.ops.neighbors.get_neighbor_pairs_brute
get_neighbor_pairs_shared = pt.ops.neighbors.get_neighbor_pairs_shared
get_neighbor_pairs_cell = pt.ops.neighbors.get_neighbor_pairs_cell
