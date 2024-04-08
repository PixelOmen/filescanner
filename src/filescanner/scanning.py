from pathlib import Path
from dataclasses import dataclass, field

@dataclass
class ScanResults:
    files: list[Path] = field(default_factory=list)
    dirs: list[Path] = field(default_factory=list)
    manifests: dict[Path, list[Path]] = field(default_factory=dict)

class Scanner:
    @staticmethod
    def recursive_scan(dir: Path, previousresults: ScanResults | None = None,
                        excludedirs: list[str] | None = None, dironly:bool=False, printdir: bool=False) -> ScanResults:
        
        scanresults = ScanResults() if previousresults is None else previousresults

        if excludedirs is not None and dir.name in excludedirs:
            return scanresults
        else:
            scanresults.dirs.append(dir)

        if printdir:
            print(f"Scanning: {dir}", flush=True)

        for item in dir.iterdir():
            if item.name[0] == ".":
                continue
            if item.is_file():
                if dironly:
                    continue
                scanresults.files.append(item)
                if scanresults.manifests.get(dir):
                    scanresults.manifests[dir].append(item)
                else:
                    scanresults.manifests[dir] = [item]
            else:
                Scanner.recursive_scan(item, scanresults, excludedirs, dironly, printdir)
        return scanresults

    def __init__(self, printdir: bool=False):
        self.rootdir: Path|None = None
        self.printdir = printdir
        self._reset()

    def _reset(self) -> None:
        self.results: ScanResults = ScanResults()

    def setroot(self, rootdir: str|Path) -> None:
        self._reset()
        self.rootdir = Path(rootdir)

    def scan(self, excludedirs: list[str] | None = None, dironly: bool=False) -> None:
        self._reset()
        if self.rootdir is None:
            raise AttributeError("No rootdir set in Scanner")
        self.results = Scanner.recursive_scan(self.rootdir, excludedirs=excludedirs, dironly=dironly, printdir=self.printdir)

