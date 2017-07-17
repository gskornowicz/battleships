echo "Building battleships"
pyinstaller --clean -F -n battleships ./main.py
echo "Check dist folder for binary file"
