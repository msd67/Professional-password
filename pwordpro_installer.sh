#!/bin/bash

install() {
	if [[ ! -d "$libAdd/pwordpro" ]]; then
		mkdir "$libAdd/pwordpro"
	fi
	cp color_print.py dencryption.py hashmake.py pwordpro.py sqliteDrive.py useraccount.py UserInterface.py validation.py "$libAdd/pwordpro"
	chmod u+x pwordpro
	cp pwordpro "$binAdd"
}

localdir() {
	mkdir -p bin etc lib man share
}

libAdd="$HOME/.local/lib"
binAdd="$HOME/.local/bin"
# selected operatioin
slop=""

while getopts ":i:u" option; do
	case $option in
		i) slop="install";;
		u) slop="uninstall";;
		?)
			echo "The installation operation is performed by default"
			slop="install";;
	esac
done

echo "switches $@"
echo "slop= $slop"

if [[ "$slop" == "install" ]]; then
	echo "Installation process started"
	if [[ -d $libAdd ]]; then
		install
	else
		if [[ -d "$HOME/.local" ]]; then
			localdir
		else
			mkdir "$HOME/.local"
			localdir
		fi
		install
	fi
elif [[ "$slop" == "uninstall" ]]; then
	echo "Uninstallation process started"
	if [[ -d "$libAdd/pwordpro" ]]; then
		rm -rf "$libAdd/pwordpro"
	fi
	if [[ -f "$binAdd/pwordpro" ]]; then
		rm -f "$binAdd/pwordpro"
	fi
else
	echo "Unexpected problem ocurred"
fi

echo "The End of pwordpro_installer"
