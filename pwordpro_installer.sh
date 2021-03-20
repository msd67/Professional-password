#!/bin/bash

install() {
	if [[ ! -d "$libAdd/pwordpro" ]]; then
		mkdir "$libAdd/pwordpro"
		echo "directory $libAdd/pwordpro created"
	fi
	cp color_print.py dencryption.py hashmake.py pwordpro.py sqliteDrive.py useraccount.py UserInterface.py validation.py "$libAdd/pwordpro"
	echo "lib files were copied"
	chmod u+x pwordpro
	cp pwordpro "$binAdd"
	echo "Execution file were copied"
}

localdir() {
	mkdir -p "$lclAdd/bin" "$lclAdd/etc" "$lclAdd/lib" "$lclAdd/man" "$lclAdd/share"
}

lclAdd="$HOME/.local"
libAdd="$HOME/.local/lib"
binAdd="$HOME/.local/bin"
dbAdd="$HOME/.local/etc/pwordpro"
# selected operatioin
slop=""

while getopts ":iu" option; do
	case $option in
		i) slop="install";;
		u) slop="uninstall";;
		?)
			echo "The installation operation is performed by default"
			slop="install";;
	esac
done

#echo "switches $@"
#echo "slop= $slop"

if [[ "$slop" == "install" ]]; then
	echo "Installation process started"
	if [[ -d $libAdd ]] && [[ -d $binAdd ]]; then
		install
	else
		if [[ -d "$HOME/.local" ]]; then
			localdir
		else
			echo "directory $HOME/.local created"
			mkdir "$HOME/.local"
			localdir
		fi
		install
	fi
	if [[ ! -d "$dbAdd" ]]; then
		mkdir -p "$dbAdd"
		echo "directory $dbAdd created"
	fi
elif [[ "$slop" == "uninstall" ]]; then
	echo "Uninstallation process started"
	if [[ -d "$libAdd/pwordpro" ]]; then
		rm -rf "$libAdd/pwordpro"
		echo "$libAdd/pwordpro removed"
	fi
	if [[ -f "$binAdd/pwordpro" ]]; then
		rm -f "$binAdd/pwordpro"
		echo "$binAdd/pwordpro removed"
	fi
	if [[ -d "$dbAdd" ]]; then
		echo -e "\nAre you sure you want to delete $dbAdd?"
		echo "The configs and DataBase located here!"
		read -p "Do you really want to do this [Y/N]? " ans
		if [[ "$ans" == "Y" ]] || [[ "$ans" == "y" ]]; then
			rm -r "$dbAdd"
		else
			echo "Configuration path could not be deleted"
		fi
	fi
else
	echo "Unexpected problem ocurred"
fi

echo "The End of pwordpro_installer"
