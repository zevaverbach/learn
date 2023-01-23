#!/bin/sh

set -xe

clang -Wall -Wextra -glldb -o zed main.c
