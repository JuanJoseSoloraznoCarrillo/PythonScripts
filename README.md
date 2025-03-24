# Voltage Signal Simulation

## Overview

This project is a school exercise designed to help students learn the Python programming language by creating a class that simulates a voltage signal. The `VoltageSignal` class generates a voltage signal with optional noise and allows for plotting the signal using Matplotlib.

## Description

The `VoltageSignal` class provides methods to create and manipulate a voltage signal. The class includes properties for voltage, duration, rate, and noise, and it generates a signal based on these parameters. The signal can be plotted using the `plot` method.

### Features

- **VoltageSignal Class**: A class to simulate a voltage signal with optional noise.
- **Properties**: Voltage, Duration, Rate, Noise, and Data properties to get and set signal parameters.
- **Plotting**: A method to plot the generated voltage signal using Matplotlib.
- **Command-Line Interface**: A simple CLI to create and plot a voltage signal based on user input.

## How to Use

### Command-Line Usage

To use the script from the command line, run the following command:

```sh
python3 voltage_signal.py [voltage] [duration] [rate<opt>] [noise<opt>]