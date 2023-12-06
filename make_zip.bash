#!/bin/bash
zip -r test_data.zip . -x '*.git/*' -x '.*' make_zip.bash
