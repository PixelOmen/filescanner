
# FileScanner

## Overview

A library designed to recursively scan directories and collect information about files and subdirectories. It allows for the exclusion of specific directories from the scan and can operate in a directory-only mode.

## Installation

To use the FileScanner module, simply clone this repository and import it into your Python project.

```bash
git clone https://github.com/PixelOmen/filescanner.git
```

## Usage

### Importing the Module

```python
from pathlib import Path
from filescanner import Scanner
```

### Initializing the Scanner

Create an instance of the `Scanner` class. Optionally, you can enable directory printing to get real-time feedback on the directories being scanned.

```python
scanner = Scanner(printdir=True)
```

### Setting the Root Directory

Before starting a scan, you need to set the root directory from which the scan will begin.

```python
scanner.setroot("/path/to/your/directory")
```

### Performing a Scan

You can perform a scan with the option to exclude specific directories and to scan for directories only.

```python
# Scan all files and directories, excluding 'dir_to_exclude'
scanner.scan(excludedirs=["dir_to_exclude"])

# Scan directories only
scanner.scan(dironly=True)
```

### Accessing Scan Results

The scan results are stored in the `results` attribute of the `Scanner` instance. The results include lists of files and directories, as well as a dictionary mapping directories to their files.

```python
# List of scanned files
files = scanner.results.files

# List of scanned directories
dirs = scanner.results.dirs

# Dictionary of directories and their files
manifests = scanner.results.manifests
```

## Classes and Methods

### ScanResults

A dataclass that stores the results of the scan.

- `files`: List of scanned files.
- `dirs`: List of scanned directories.
- `manifests`: Dictionary mapping directories to their files.

### Scanner

The main class for performing directory scans.

#### Methods

- `setroot`: Sets the root directory for the scan.
- `scan`: Performs the scan with optional exclusion of directories and directory-only mode.
- `recursive_scan`: A static method that performs the recursive scan.

## Example

```python
from filescanner import Scanner

# Initialize the scanner
scanner = Scanner(printdir=True)

# Set the root directory
scanner.setroot("/path/to/your/directory")

# Perform the scan, excluding 'dir_to_exclude'
scanner.scan(excludedirs=["dir_to_exclude"])

# Access the results
print("Files:", scanner.results.files)
print("Directories:", scanner.results.dirs)
print("Manifests:", scanner.results.manifests)
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.
