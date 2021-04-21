#!/usr/bin/env bash

if test -z "$1"; then
  echo "Missing root folder"
  exit 1
fi

myInputDir=$(pwd)

cd
cd bin

cat > myinput <<EOF
#!/usr/bin/env bash
MYINPUT_ROOT_PATH=$1 ${myInputDir}/main.py
EOF

chmod +x myinput

