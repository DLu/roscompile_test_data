#!/bin/bash
zip -r test_data.zip . -x '*.git/*' -x '*.md' make_zip.bash
