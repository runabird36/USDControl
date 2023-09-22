
export HGWEAVER_USD_ROOT="$(cd "$(dirname "$0")" && pwd)/.."
export PYTHONPATH=$PYTHONPATH:$HGWEAVER_USD_ROOT/module
cp $HGWEAVER_USD_ROOT/shelves/* /home/$USERNAME/maya/2023/prefs/shelves/