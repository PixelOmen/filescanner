from src.scanning import Scanner

testpath = r"C:\Users\eman\Projects\python\alulamoat"

scanner = Scanner()
scanner.setroot(testpath)
scanner.scan(excludedirs=["__pycache__"], dironly=False)
if scanner.results:
    print(len(scanner.results.dirs))