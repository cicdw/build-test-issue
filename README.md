# build-test-issue

**SOLVED** via https://docs.pytest.org/en/latest/goodpractices.html, in particular:
> If you need to have test modules with the same name, you might add \_\_init\_\_.py files to your tests folder and subfolders, changing them to packages:

```
setup.py
mypkg/
    ...
tests/
    __init__.py
    foo/
        __init__.py
        test_view.py
    bar/
        __init__.py
        test_view.py
```

> Now pytest will load the modules as tests.foo.test_view and tests.bar.test_view, allowing you to have modules with the same name. But now this introduces a subtle problem: in order to load the test modules from the tests directory, pytest prepends the root of the repository to sys.path, which adds the side-effect that now mypkg is also importable. This is problematic if you are using a tool like tox to test your package in a virtual environment, because you want to test the installed version of your package, not the local code from the repository.

> In this situation, it is strongly suggested to use a src layout where application root package resides in a sub-directory of your root.

Minimal Reproducible Example of a build + test CI issue I'm trying to figure out

```bash
# environment setup and install
git clone https://github.com/cicdw/build-test-issue.git
cd build-test-issue
conda env create
source activate build-test
pip install -e . # install the "build_test" package

## run pytest
pytest # all tests pass

## run tox
tox # all tests pass

# NOTE: sys.path still retains a reference to our git repo directory
# when tests are run with tox!

## inspect the quality of the distribution
cd .tox/dist/
unzip build_test-0.0.0.zip
cd build_test-0.0.0
pytest # tests fail!

## remove tests/__init__.py
cd ../../../ # return to git repo
rm tests/__init__.py
pytest # tests pass
tox # tests fail!
```

Clearly, including a `MANIFEST.in` file (with the one line `include config.txt`) will prevent this; however, that is precisely the thing I want `tox` to detect and raise to me.
