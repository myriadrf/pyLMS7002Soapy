#!/usr/bin/env bash
sdcc --model-small --iram-size 256 --xram-size 2048 --code-size 8192 -c spi_asm.c
sdcc --model-small --iram-size 256 --xram-size 2048 --code-size 8192 -c spi.c
sdcc --model-small --iram-size 256 --xram-size 2048 --code-size 8192 -c main.c
sdcc --model-small --iram-size 256 --xram-size 2048 --code-size 8192 main.rel spi.rel spi_asm.rel -o main.ihx

packihx main.ihx > vna.hex

