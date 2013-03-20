#!/usr/bin/env perl

$home=`echo -n ~`;

$WhereCmd=`pwd`

if(-d "$home/.gnome2/nautilus-scripts/")
{

 ` echo "$WhereCmd/GetLink.py  $UTILUS_SCRIPT_SELECTED_FILE_PATHS" > Send_to_Vdisk_template`  && `cp Send_to_Vdisk_template $home/.gnome2/nautilus-scripts/`
 
}
else{
	print "$home/.gnome2/nautilus-scripts/目录不存在!\n";
exit(2)

}

