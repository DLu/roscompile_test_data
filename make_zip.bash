#!/bin/bash
zip -r test_data.zip . -x '*.git/*' '*.md' '.*' make_zip.bash
