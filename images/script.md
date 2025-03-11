find . -name '*.jpg' -exec basename {} \; | xargs -n1 -P8 -I{} convert -resize 40% "{}" "opt-{}"
