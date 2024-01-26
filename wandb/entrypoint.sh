#!/bin/bash
set -e

source .env

wandb login $WANDB_TOKEN

exec "$@"
