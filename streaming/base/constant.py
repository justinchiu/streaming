# Copyright 2022-2024 MosaicML Streaming authors
# SPDX-License-Identifier: Apache-2.0
import os

"""Constants."""
prefix = f"{os.getenv('STREAMING_PREFIX')}_" if os.getenv('STREAMING_PREFIX') is not None else ""

# Shared Memory names
LOCALS = f'{prefix}locals'
BARRIER = f'{prefix}barrier'
NEXT_EPOCH = f'{prefix}next_epoch'
CACHE_USAGE = f'{prefix}cache_usage'
SHARD_STATES = f'{prefix}shard_states'
SHARD_ACCESS_TIMES = f'{prefix}shard_access_times'
RESUME = f'{prefix}resume'
EPOCH_SHAPE = f'{prefix}epoch_shape'
EPOCH_DATA = f'{prefix}epoch_data'
SHM_TO_CLEAN = [
    LOCALS,
    BARRIER,
    NEXT_EPOCH,
    CACHE_USAGE,
    SHARD_STATES,
    SHARD_ACCESS_TIMES,
    RESUME,
    EPOCH_SHAPE,
    EPOCH_DATA,
]

# filelock names
BARRIER_FILELOCK = f'{prefix}barrier_filelock'
CACHE_FILELOCK = f'{prefix}cache_filelock'

# Time to wait, in seconds.
TICK = 0.007


