# build-test-issue
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
